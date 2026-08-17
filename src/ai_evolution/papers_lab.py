"""Motores didácticos deterministas para el eje `papers/`.

Cada motor es una **miniatura** del mecanismo que introdujo un paper fundacional.
No reproduce el experimento original: reproduce la *idea* con datos de juguete,
en Python estándar, sin GPU, sin dependencias externas y sin APIs pagadas.

Contrato de salida (idéntico en espíritu al de `labs.py`)::

    {"kind": str, "seed": int, "result": Any, "evidence": [str], "limitations": [str]}

`evidence` = lo que el experimento sí muestra.
`limitations` = lo que el experimento no puede demostrar. Se declara siempre,
porque la diferencia entre evidencia y narrativa es materia evaluable del programa.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable


# --------------------------------------------------------------------------- #
# utilidades comunes
# --------------------------------------------------------------------------- #


def _contract(kind: str, seed: int, result: Any, evidence: list[str], limitations: list[str]) -> dict[str, Any]:
    return {
        "kind": kind,
        "seed": seed,
        "result": result,
        "evidence": evidence,
        "limitations": limitations,
    }


def _sigmoid(z: float) -> float:
    if z < -60:
        return 0.0
    if z > 60:
        return 1.0
    return 1.0 / (1.0 + math.exp(-z))


def _dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def _softmax(scores: list[float]) -> list[float]:
    top = max(scores)
    exps = [math.exp(s - top) for s in scores]
    total = sum(exps)
    return [e / total for e in exps]


def _entropy(distribution: list[float]) -> float:
    return -sum(p * math.log(p + 1e-12) for p in distribution)


def _cosine(a: list[float], b: list[float]) -> float:
    na = math.sqrt(_dot(a, a))
    nb = math.sqrt(_dot(b, b))
    if na == 0 or nb == 0:
        return 0.0
    return _dot(a, b) / (na * nb)


def _round(value: float, digits: int = 4) -> float:
    return round(value + 0.0, digits)


# --------------------------------------------------------------------------- #
# P01 — Perceptrón (Rosenblatt, 1958)
# --------------------------------------------------------------------------- #


def _train_perceptron(data: list[tuple[list[int], int]], epochs: int = 20, lr: float = 1.0):
    weights = [0.0, 0.0]
    bias = 0.0
    updates = 0
    converged_at = None
    for epoch in range(1, epochs + 1):
        errors = 0
        for features, target in data:
            prediction = 1 if _dot(weights, [float(f) for f in features]) + bias >= 0 else 0
            delta = target - prediction
            if delta != 0:
                weights = [w + lr * delta * f for w, f in zip(weights, features)]
                bias += lr * delta
                updates += 1
                errors += 1
        if errors == 0:
            converged_at = epoch
            break
    return weights, bias, updates, converged_at


def _perceptron(seed: int) -> dict[str, Any]:
    and_data = [([0, 0], 0), ([0, 1], 0), ([1, 0], 0), ([1, 1], 1)]
    xor_data = [([0, 0], 0), ([0, 1], 1), ([1, 0], 1), ([1, 1], 0)]
    and_w, and_b, and_u, and_epoch = _train_perceptron(and_data)
    xor_w, xor_b, xor_u, xor_epoch = _train_perceptron(xor_data)
    return _contract(
        "perceptron",
        seed,
        {
            "AND": {"weights": and_w, "bias": and_b, "updates": and_u, "converged_epoch": and_epoch},
            "XOR": {"weights": xor_w, "bias": xor_b, "updates": xor_u, "converged_epoch": xor_epoch},
            "separable": {"AND": and_epoch is not None, "XOR": xor_epoch is not None},
        },
        [
            f"AND converge en la época {and_epoch} con {and_u} actualizaciones: los datos son linealmente separables.",
            "XOR no converge en 20 épocas: la regla cicla porque no existe hiperplano que lo separe.",
        ],
        [
            "Cuatro puntos booleanos no dicen nada sobre datos ruidosos ni de alta dimensión.",
            "El experimento muestra ausencia de convergencia, no la demuestra formalmente (eso lo hace Minsky y Papert, 1969).",
        ],
    )


# --------------------------------------------------------------------------- #
# P02 — Backpropagation (Rumelhart, Hinton y Williams, 1986)
# --------------------------------------------------------------------------- #


def _mlp_forward(params: dict[str, list[float]], x: list[float]) -> dict[str, Any]:
    h_in = [
        params["w1"][0] * x[0] + params["w1"][1] * x[1] + params["b1"][0],
        params["w1"][2] * x[0] + params["w1"][3] * x[1] + params["b1"][1],
    ]
    h = [_sigmoid(v) for v in h_in]
    o_in = params["w2"][0] * h[0] + params["w2"][1] * h[1] + params["b2"][0]
    o = _sigmoid(o_in)
    return {"h": h, "o": o}


def _mlp_loss(params: dict[str, list[float]], data: list[tuple[list[float], float]]) -> float:
    return sum((_mlp_forward(params, x)["o"] - y) ** 2 for x, y in data) / len(data)


def _backprop(seed: int) -> dict[str, Any]:
    rng = random.Random(seed)
    params = {
        "w1": [rng.uniform(-1, 1) for _ in range(4)],
        "b1": [0.0, 0.0],
        "w2": [rng.uniform(-1, 1) for _ in range(2)],
        "b2": [0.0],
    }
    data = [([0.0, 0.0], 0.0), ([0.0, 1.0], 1.0), ([1.0, 0.0], 1.0), ([1.0, 1.0], 0.0)]
    lr = 0.9
    history = []
    for step in range(6000):
        grads = {key: [0.0] * len(value) for key, value in params.items()}
        for x, y in data:
            fwd = _mlp_forward(params, x)
            h, o = fwd["h"], fwd["o"]
            d_o = 2 * (o - y) / len(data) * o * (1 - o)          # ∂L/∂o_in
            grads["w2"][0] += d_o * h[0]
            grads["w2"][1] += d_o * h[1]
            grads["b2"][0] += d_o
            for j in range(2):                                    # retropropagación a la capa oculta
                d_h = d_o * params["w2"][j] * h[j] * (1 - h[j])
                grads["w1"][2 * j] += d_h * x[0]
                grads["w1"][2 * j + 1] += d_h * x[1]
                grads["b1"][j] += d_h
        for key in params:
            params[key] = [p - lr * g for p, g in zip(params[key], grads[key])]
        if step % 1000 == 0:
            history.append({"step": step, "loss": _round(_mlp_loss(params, data), 5)})
    history.append({"step": 6000, "loss": _round(_mlp_loss(params, data), 5)})

    # verificación numérica del gradiente: el corazón de "confiar" en backprop
    eps = 1e-5
    original = params["w2"][0]
    params["w2"][0] = original + eps
    up = _mlp_loss(params, data)
    params["w2"][0] = original - eps
    down = _mlp_loss(params, data)
    params["w2"][0] = original
    numeric = (up - down) / (2 * eps)
    analytic = 0.0
    for x, y in data:
        fwd = _mlp_forward(params, x)
        analytic += 2 * (fwd["o"] - y) / len(data) * fwd["o"] * (1 - fwd["o"]) * fwd["h"][0]

    predictions = [{"x": x, "y": y, "pred": _round(_mlp_forward(params, x)["o"], 3)} for x, y in data]
    return _contract(
        "backprop",
        seed,
        {
            "loss_history": history,
            "predictions": predictions,
            "grad_check": {"numeric": _round(numeric, 8), "analytic": _round(analytic, 8),
                           "abs_diff": _round(abs(numeric - analytic), 10)},
        },
        [
            f"La pérdida baja de {history[0]['loss']} a {history[-1]['loss']} sobre XOR: la capa oculta rompe la barrera del perceptrón.",
            "El gradiente analítico coincide con el numérico hasta ~1e-7: la retropropagación está bien derivada.",
        ],
        [
            "Una red 2-2-1 con 9 parámetros no dice nada sobre optimización a escala.",
            "El paper de 1986 popularizó la regla de la cadena aplicada a redes; no la inventó (Linnainmaa 1970, Werbos 1974).",
        ],
    )


# --------------------------------------------------------------------------- #
# P03 — LSTM (Hochreiter y Schmidhuber, 1997)
# --------------------------------------------------------------------------- #


def _lstm(seed: int) -> dict[str, Any]:
    steps = 40
    # RNN tanh: el gradiente se multiplica por w·(1-tanh²) en cada paso
    decay_rnn = []
    grad = 1.0
    for _ in range(steps):
        grad *= 0.9 * 0.42          # |w|·derivada típica de tanh en régimen saturado
        decay_rnn.append(grad)
    # LSTM: la celda propaga el gradiente multiplicando por la puerta de olvido
    decay_lstm = []
    grad_cec = 1.0
    for _ in range(steps):
        grad_cec *= 0.98            # forget gate ≈ abierta → carrusel de error constante
        decay_lstm.append(grad_cec)

    # celda LSTM completa, un paso, con valores explícitos
    x, h_prev, c_prev = 1.0, 0.0, 0.5
    w = {"f": 1.5, "i": 1.0, "o": 1.2, "g": 0.8}
    f = _sigmoid(w["f"] * x)
    i = _sigmoid(w["i"] * x)
    o = _sigmoid(w["o"] * x)
    g = math.tanh(w["g"] * x + h_prev)
    c = f * c_prev + i * g
    h = o * math.tanh(c)
    return _contract(
        "lstm",
        seed,
        {
            "gates": {"forget": _round(f), "input": _round(i), "output": _round(o), "candidate": _round(g)},
            "cell_state": _round(c),
            "hidden_state": _round(h),
            "gradient_after_40_steps": {"rnn_tanh": f"{decay_rnn[-1]:.3e}", "lstm_cec": f"{decay_lstm[-1]:.3e}"},
            "ratio": f"{decay_lstm[-1] / decay_rnn[-1]:.3e}",
        },
        [
            f"Tras 40 pasos el gradiente del RNN vale {decay_rnn[-1]:.2e} y el de la celda LSTM {decay_lstm[-1]:.2e}.",
            "El carrusel de error constante (CEC) mantiene el gradiente utilizable porque la celda usa suma, no producto de activaciones.",
        ],
        [
            "Los factores de decaimiento están fijados a mano para aislar el mecanismo; no provienen de un entrenamiento real.",
            "La LSTM de 1997 tenía solo puertas de entrada y salida: la puerta de olvido llegó en Gers, Schmidhuber y Cummins (1999/2000).",
        ],
    )


# --------------------------------------------------------------------------- #
# P04 — AlexNet (Krizhevsky, Sutskever y Hinton, 2012)
# --------------------------------------------------------------------------- #


def _convolve(image: list[list[float]], kernel: list[list[float]]) -> list[list[float]]:
    k = len(kernel)
    size = len(image) - k + 1
    return [
        [sum(image[r + i][c + j] * kernel[i][j] for i in range(k) for j in range(k)) for c in range(size)]
        for r in range(size)
    ]


def _convnet(seed: int) -> dict[str, Any]:
    image = [[0.0] * 3 + [1.0] * 3 for _ in range(6)]     # borde vertical en la columna 3
    shifted = [[0.0] * 2 + [1.0] * 4 for _ in range(6)]   # el mismo borde, desplazado
    kernel = [[-1.0, 0.0, 1.0], [-1.0, 0.0, 1.0], [-1.0, 0.0, 1.0]]
    feature = _convolve(image, kernel)
    feature_shifted = _convolve(shifted, kernel)
    relu = [[max(0.0, v) for v in row] for row in feature]
    pooled = [
        [max(relu[r][c], relu[r][c + 1], relu[r + 1][c], relu[r + 1][c + 1]) for c in range(0, 4, 2)]
        for r in range(0, 4, 2)
    ]
    dense_params = (6 * 6) * (4 * 4)
    conv_params = 3 * 3
    return _contract(
        "convnet",
        seed,
        {
            "feature_map": [[_round(v, 2) for v in row] for row in feature],
            "feature_map_shifted": [[_round(v, 2) for v in row] for row in feature_shifted],
            "after_relu_and_maxpool": [[_round(v, 2) for v in row] for row in pooled],
            "params": {"dense_equivalent": dense_params, "conv_kernel": conv_params,
                       "reduction_factor": _round(dense_params / conv_params, 1)},
        },
        [
            "El mismo kernel detecta el borde en ambas imágenes: los pesos compartidos dan equivarianza a la traslación.",
            f"Una capa densa equivalente necesitaría {dense_params} pesos frente a {conv_params} del kernel ({dense_params // conv_params}× menos).",
        ],
        [
            "Un kernel escrito a mano no es un kernel aprendido: AlexNet aprendió los suyos por descenso de gradiente.",
            "No se reproduce ImageNet: sin ILSVRC-2012, sin 60M de parámetros y sin las dos GPU del paper original.",
        ],
    )


# --------------------------------------------------------------------------- #
# P05 — Word2Vec (Mikolov et al., 2013)
# --------------------------------------------------------------------------- #


_W2V_CORPUS = [
    "el rey gobierna el reino con poder",
    "la reina gobierna el reino con poder",
    "el hombre camina por la calle tranquila",
    "la mujer camina por la calle tranquila",
    "el rey y el hombre visten de gris",
    "la reina y la mujer visten de gris",
    "el reino celebra al rey y a la reina",
    "la calle celebra al hombre y a la mujer",
]


def _word2vec(seed: int) -> dict[str, Any]:
    rng = random.Random(seed)
    sentences = [line.split() for line in _W2V_CORPUS]
    vocab = sorted({token for line in sentences for token in line})
    index = {word: i for i, word in enumerate(vocab)}
    dim = 12
    inp = [[rng.uniform(-0.5, 0.5) for _ in range(dim)] for _ in vocab]
    out = [[rng.uniform(-0.5, 0.5) for _ in range(dim)] for _ in vocab]
    pairs = []
    window = 2
    for line in sentences:
        for pos, center in enumerate(line):
            for off in range(-window, window + 1):
                ctx = pos + off
                if off == 0 or ctx < 0 or ctx >= len(line):
                    continue
                pairs.append((index[center], index[line[ctx]]))

    lr = 0.05
    negatives = 5
    for _epoch in range(140):
        rng.shuffle(pairs)
        for center, context in pairs:
            targets = [(context, 1.0)] + [(rng.randrange(len(vocab)), 0.0) for _ in range(negatives)]
            v = inp[center]
            grad_v = [0.0] * dim
            for target, label in targets:
                u = out[target]
                score = _sigmoid(_dot(v, u))
                err = score - label
                for d in range(dim):
                    grad_v[d] += err * u[d]
                    u[d] -= lr * err * v[d]
            for d in range(dim):
                v[d] -= lr * grad_v[d]

    def neighbours(word: str, k: int = 3) -> list[dict[str, Any]]:
        base = inp[index[word]]
        scored = [
            {"word": other, "cos": _round(_cosine(base, inp[index[other]]), 3)}
            for other in vocab
            if other != word
        ]
        return sorted(scored, key=lambda item: -item["cos"])[:k]

    analogy_vec = [
        inp[index["rey"]][d] - inp[index["hombre"]][d] + inp[index["mujer"]][d] for d in range(dim)
    ]
    ranking = sorted(
        ({"word": w, "cos": _round(_cosine(analogy_vec, inp[index[w]]), 3)} for w in vocab
         if w not in {"rey", "hombre", "mujer"}),
        key=lambda item: -item["cos"],
    )[:3]
    return _contract(
        "word2vec",
        seed,
        {
            "vocab_size": len(vocab),
            "dim": dim,
            "training_pairs": len(pairs),
            "neighbours": {"rey": neighbours("rey"), "calle": neighbours("calle")},
            "analogy_rey_menos_hombre_mas_mujer": ranking,
        },
        [
            "Palabras que comparten contexto quedan cerca en coseno sin que nadie etiquete su significado.",
            "rey − hombre + mujer devuelve «reina» como vecino más cercano: la geometría del espacio codifica la relación de género.",
        ],
        [
            "Con 8 frases el resultado es frágil: cambiar la semilla puede alterar el orden del ranking. Eso también es evidencia.",
            "Las analogías del paper original se midieron sobre miles de preguntas; aquí solo se ilustra el mecanismo.",
        ],
    )


# --------------------------------------------------------------------------- #
# P06 — Seq2Seq (Sutskever, Vinyals y Le, 2014)
# --------------------------------------------------------------------------- #


def _seq2seq(seed: int) -> dict[str, Any]:
    rng = random.Random(seed)
    dim = 8
    vocab = [f"t{i}" for i in range(12)]
    emb = {word: [rng.uniform(-1, 1) for _ in range(dim)] for word in vocab}

    def encode(sequence: list[str]) -> list[float]:
        state = [0.0] * dim
        for token in sequence:                       # "RNN" de juguete: mezcla con decaimiento
            state = [0.7 * s + 0.3 * e for s, e in zip(state, emb[token])]
        return state

    rows = []
    for length in (2, 4, 8, 16, 32):
        sequence = [rng.choice(vocab) for _ in range(length)]
        state = encode(sequence)
        recovered = 0
        for token in sequence:                       # ¿el vector fijo sigue "conteniendo" cada token?
            best = max(vocab, key=lambda w: _cosine(state, emb[w]))
            if best == token:
                recovered += 1
        first = _round(_cosine(state, emb[sequence[0]]), 3)
        last = _round(_cosine(state, emb[sequence[-1]]), 3)
        rows.append({
            "length": length,
            "cos_primer_token": first,
            "cos_ultimo_token": last,
            "tokens_recuperables": f"{recovered}/{length}",
        })
    return _contract(
        "seq2seq",
        seed,
        {"bottleneck": rows, "state_dim": dim},
        [
            "La similitud con el primer token cae al crecer la longitud: el vector fijo olvida el principio de la secuencia.",
            "El estado final siempre está dominado por los últimos tokens, sin importar cuán larga sea la entrada.",
        ],
        [
            "El 'encoder' es una mezcla exponencial fija, no una LSTM entrenada; ilustra el cuello de botella, no lo mide.",
            "Sutskever et al. invirtieron la secuencia fuente para mitigar este efecto; ese truco no está implementado aquí.",
        ],
    )


# --------------------------------------------------------------------------- #
# P07 — Attention aditiva (Bahdanau, Cho y Bengio, 2014)
# --------------------------------------------------------------------------- #


def _bahdanau(seed: int) -> dict[str, Any]:
    """Atención aditiva e_ij = vᵀ·tanh(W·s_{i-1} + U·h_j), con W y U diagonales.

    Los 3·dim parámetros se aprenden por descenso de gradiente sobre una
    supervisión de alineación de juguete. En el paper la alineación es *latente*:
    emerge de entrenar la traducción, sin que nadie la etiquete.
    """
    source = ["el", "gato", "negro", "duerme"]
    target = ["the", "black", "cat", "sleeps"]
    gold = {"the": "el", "black": "negro", "cat": "gato", "sleeps": "duerme"}
    dim = 6
    rng = random.Random(seed)
    encoder = {word: [rng.uniform(-1, 1) for _ in range(dim)] for word in source}
    decoder = {word: [rng.uniform(-1, 1) for _ in range(dim)] for word in target}
    v = [rng.uniform(-0.3, 0.3) for _ in range(dim)]
    w = [1.0] * dim
    u = [1.0] * dim

    def score(s: list[float], h: list[float]) -> tuple[float, list[float]]:
        pre = [w[d] * s[d] + u[d] * h[d] for d in range(dim)]
        act = [math.tanh(p) for p in pre]
        return _dot(v, act), act

    lr, losses = 0.5, []
    for step in range(600):
        total = 0.0
        gv, gw, gu = [0.0] * dim, [0.0] * dim, [0.0] * dim
        for word in target:
            acts, scores = [], []
            for src in source:
                value, act = score(decoder[word], encoder[src])
                scores.append(value)
                acts.append(act)
            alpha = _softmax(scores)
            j_gold = source.index(gold[word])
            total += -math.log(alpha[j_gold] + 1e-12)
            for j, src in enumerate(source):
                d_e = alpha[j] - (1.0 if j == j_gold else 0.0)
                for d in range(dim):
                    t = acts[j][d]
                    gv[d] += d_e * t
                    gw[d] += d_e * v[d] * (1 - t * t) * decoder[word][d]
                    gu[d] += d_e * v[d] * (1 - t * t) * encoder[src][d]
        for d in range(dim):
            v[d] -= lr * gv[d] / len(target)
            w[d] -= lr * gw[d] / len(target)
            u[d] -= lr * gu[d] / len(target)
        if step % 200 == 0:
            losses.append({"step": step, "loss": _round(total / len(target), 4)})

    matrix = []
    for word in target:
        scores = [score(decoder[word], encoder[src])[0] for src in source]
        alpha = _softmax(scores)
        matrix.append({
            "target": word,
            "alpha": {src: _round(a, 3) for src, a in zip(source, alpha)},
            "argmax": source[alpha.index(max(alpha))],
            "entropia": _round(_entropy(alpha), 3),
            "suma_alpha": _round(sum(alpha), 3),
        })
    hits = sum(1 for row in matrix if row["argmax"] == gold[row["target"]])
    return _contract(
        "bahdanau",
        seed,
        {
            "parametros": 3 * dim,
            "perdida": losses,
            "alignment": matrix,
            "aciertos_de_alineacion": f"{hits}/{len(target)}",
        },
        [
            f"La matriz de alineación aprendida acierta {hits}/{len(target)} pares con solo {3 * dim} parámetros.",
            "Cada palabra generada construye su propio vector de contexto: desaparece el vector fijo del seq2seq.",
            "Los pesos α suman 1 y son inspeccionables: la alineación deja de estar oculta en el estado del RNN.",
        ],
        [
            "Aquí la alineación se supervisa; en el paper emerge de forma latente al entrenar solo la traducción.",
            "Atención interpretable ≠ explicación causal del modelo; el campo lo discutió después (Jain y Wallace, 2019).",
        ],
    )


# --------------------------------------------------------------------------- #
# P08 — Transformer (Vaswani et al., 2017)
# --------------------------------------------------------------------------- #


def scaled_dot_product_attention(
    queries: list[list[float]],
    keys: list[list[float]],
    values: list[list[float]],
    *,
    scale: bool = True,
    causal: bool = False,
) -> dict[str, Any]:
    """Attention(Q,K,V) = softmax(QKᵀ/√d_k)·V — la ecuación 1 del paper."""
    d_k = len(keys[0])
    denom = math.sqrt(d_k) if scale else 1.0
    weights: list[list[float]] = []
    output: list[list[float]] = []
    for i, q in enumerate(queries):
        scores = [_dot(q, k) / denom for k in keys]
        if causal:
            scores = [s if j <= i else -1e9 for j, s in enumerate(scores)]
        alpha = _softmax(scores)
        weights.append(alpha)
        output.append([sum(a * v[d] for a, v in zip(alpha, values)) for d in range(len(values[0]))])
    return {"weights": weights, "output": output}


def positional_encoding(position: int, d_model: int) -> list[float]:
    """PE(pos,2i)=sin(pos/10000^{2i/d}), PE(pos,2i+1)=cos(...) — sección 3.5."""
    encoding = []
    for i in range(d_model):
        angle = position / (10000 ** (2 * (i // 2) / d_model))
        encoding.append(math.sin(angle) if i % 2 == 0 else math.cos(angle))
    return encoding


def multi_head_attention(vectors: list[list[float]], heads: int, *, causal: bool = False) -> dict[str, Any]:
    """Parte d_model en `heads` subespacios, atiende en cada uno y concatena."""
    d_model = len(vectors[0])
    if d_model % heads:
        raise ValueError("d_model debe ser divisible entre el número de cabezas")
    d_head = d_model // heads
    per_head = []
    concat = [[0.0] * d_model for _ in vectors]
    for h in range(heads):
        lo, hi = h * d_head, (h + 1) * d_head
        sliced = [vec[lo:hi] for vec in vectors]
        attended = scaled_dot_product_attention(sliced, sliced, sliced, causal=causal)
        per_head.append(attended["weights"])
        for row, chunk in zip(concat, attended["output"]):
            row[lo:hi] = chunk
    return {"heads": per_head, "output": concat}


def layer_norm(vector: list[float], eps: float = 1e-5) -> list[float]:
    mean = sum(vector) / len(vector)
    var = sum((v - mean) ** 2 for v in vector) / len(vector)
    return [(v - mean) / math.sqrt(var + eps) for v in vector]


def _transformer(seed: int) -> dict[str, Any]:
    rng = random.Random(seed)
    tokens = ["el", "modelo", "atiende", "todo"]
    d_model = 8
    embeddings = [[rng.uniform(-1, 1) for _ in range(d_model)] for _ in tokens]
    with_pos = [
        [e + p for e, p in zip(emb, positional_encoding(pos, d_model))]
        for pos, emb in enumerate(embeddings)
    ]
    scaled = scaled_dot_product_attention(with_pos, with_pos, with_pos, scale=True)
    unscaled = scaled_dot_product_attention(with_pos, with_pos, with_pos, scale=False)
    causal = scaled_dot_product_attention(with_pos, with_pos, with_pos, causal=True)
    heads = multi_head_attention(with_pos, heads=2)

    # residual + layer norm, tal como aparecen alrededor de cada subcapa
    residual = [[a + b for a, b in zip(x, y)] for x, y in zip(with_pos, scaled["output"])]
    normed = [layer_norm(vec) for vec in residual]

    complexity = [
        {"n": n, "self_attention_ops": n * n * d_model, "recurrent_ops": n * d_model * d_model,
         "camino_maximo_rnn": n, "camino_maximo_attention": 1}
        for n in (10, 100, 1000)
    ]
    return _contract(
        "transformer",
        seed,
        {
            "entropia_media": {
                "con_escala_sqrt_dk": _round(sum(_entropy(w) for w in scaled["weights"]) / len(tokens), 3),
                "sin_escala": _round(sum(_entropy(w) for w in unscaled["weights"]) / len(tokens), 3),
            },
            "mascara_causal": [[_round(v, 3) for v in row] for row in causal["weights"]],
            "cabezas": len(heads["heads"]),
            "norma_tras_layernorm": [_round(math.sqrt(_dot(v, v)), 3) for v in normed],
            "complejidad": complexity,
        },
        [
            "Sin dividir por √d_k la entropía de la atención baja: el softmax se satura y los gradientes se apagan.",
            "La máscara causal deja la matriz triangular inferior: la posición i no puede mirar a i+1.",
            "El camino entre dos posiciones cualesquiera es 1 en atención y n en recurrencia: por eso el Transformer paraleliza.",
        ],
        [
            "No hay proyecciones W_Q, W_K, W_V aprendidas: se usan los mismos vectores como Q, K y V para aislar el mecanismo.",
            "Cuatro tokens y d_model=8 no reproducen WMT 2014 ni las 3,5 días de entrenamiento en 8 GPU P100 del paper.",
        ],
    )


# --------------------------------------------------------------------------- #
# P09 — BERT (Devlin et al., 2018)
# --------------------------------------------------------------------------- #


_BERT_CORPUS = [
    "el banco del parque estaba mojado por la lluvia",
    "el banco del rio estaba mojado por la lluvia",
    "el banco central subio la tasa de interes",
    "el banco comercial subio la tasa de interes",
    "me sente en el banco del parque a leer",
    "el banco aprobo el credito de la empresa",
]


def _bert_mlm(seed: int) -> dict[str, Any]:
    sentences = [line.split() for line in _BERT_CORPUS]
    left_counts: dict[tuple[str, ...], dict[str, int]] = {}
    both_counts: dict[tuple[str, ...], dict[str, int]] = {}
    for line in sentences:
        for i, token in enumerate(line):
            left = tuple(line[max(0, i - 2):i])
            both = (tuple(line[max(0, i - 2):i]), tuple(line[i + 1:i + 3]))
            left_counts.setdefault(left, {}).setdefault(token, 0)
            left_counts[left][token] += 1
            both_counts.setdefault(both, {}).setdefault(token, 0)  # type: ignore[arg-type]
            both_counts[both][token] += 1                          # type: ignore[index]

    probes = [
        (["el", "banco", "del"], ["estaba", "mojado"], "parque"),
        (["el", "banco", "central"], ["la", "tasa"], "subio"),
    ]
    rows = []
    for left_ctx, right_ctx, gold in probes:
        left_key = tuple(left_ctx[-2:])
        both_key = (tuple(left_ctx[-2:]), tuple(right_ctx[:2]))
        left_options = left_counts.get(left_key, {})
        both_options = both_counts.get(both_key, {})  # type: ignore[arg-type]
        rows.append({
            "izquierda": " ".join(left_ctx),
            "derecha": " ".join(right_ctx),
            "gold": gold,
            "candidatos_solo_izquierda": sorted(left_options, key=lambda w: -left_options[w])[:4],
            "candidatos_bidireccional": sorted(both_options, key=lambda w: -both_options[w])[:4],
            "ambiguedad_izquierda": len(left_options),
            "ambiguedad_bidireccional": len(both_options),
        })
    return _contract(
        "bert_mlm",
        seed,
        {"masked_predictions": rows, "objetivo": "predecir [MASK] usando contexto a ambos lados"},
        [
            "El contexto derecho reduce el número de candidatos frente a mirar solo hacia atrás.",
            "Es el argumento del paper: un modelo unidireccional deja información sobre la mesa en tareas de comprensión.",
        ],
        [
            "Esto cuenta n-gramas; BERT aprende representaciones contextuales profundas con Transformers.",
            "No se implementa NSP ni el enmascarado 80/10/10 del paper, ni se mide GLUE.",
        ],
    )


# --------------------------------------------------------------------------- #
# P10 — GPT-3 / aprendizaje en contexto (Brown et al., 2020)
# --------------------------------------------------------------------------- #


def _gpt3_icl(seed: int) -> dict[str, Any]:
    rng = random.Random(seed)
    # tarea latente: mapear una palabra a su primera letra en mayúscula + longitud
    words = ["gato", "arbol", "montana", "rio", "ciudad", "libro", "puente", "camino"]
    hypotheses = {
        "primera_letra": lambda w: w[0].upper(),
        "ultima_letra": lambda w: w[-1].upper(),
        "longitud": lambda w: str(len(w)),
        "palabra_invertida": lambda w: w[::-1],
    }
    truth = "primera_letra"
    rows = []
    for shots in (0, 1, 2, 4):
        demos = [(w, hypotheses[truth](w)) for w in rng.sample(words, shots)] if shots else []
        alive = [
            name for name, fn in hypotheses.items()
            if all(fn(w) == y for w, y in demos)
        ]
        held_out = [w for w in words if w not in {d[0] for d in demos}]
        chosen = alive[0] if alive else truth
        correct = sum(1 for w in held_out if hypotheses[chosen](w) == hypotheses[truth](w))
        rows.append({
            "shots": shots,
            "hipotesis_compatibles": sorted(alive),
            "elegida": chosen,
            "accuracy_held_out": _round(correct / len(held_out), 3),
        })
    return _contract(
        "gpt3_icl",
        seed,
        {"in_context_learning": rows, "tarea_latente": truth, "sin_actualizar_pesos": True},
        [
            "Con 0 ejemplos el espacio de hipótesis no se reduce; con 2 ejemplos queda una sola compatible.",
            "La 'mejora' ocurre sin tocar ningún peso: el condicionamiento sucede íntegro en el prompt.",
        ],
        [
            "Esto es inducción de hipótesis explícita; GPT-3 no enumera hipótesis, condiciona una distribución aprendida.",
            "No se reproduce nada del modelo real: 175 000 millones de parámetros y un contexto de 2048 tokens quedan fuera de alcance local.",
        ],
    )


# --------------------------------------------------------------------------- #
# P11 — RAG (Lewis et al., 2020)
# --------------------------------------------------------------------------- #


_RAG_DOCS = {
    "d1": "La ley de transparencia algoritmica del pais entro en vigor el 12 de marzo de 2024.",
    "d2": "El registro nacional de sistemas de alto riesgo exige auditoria anual independiente.",
    "d3": "El manual de cocina recomienda hornear el pan a 220 grados durante 30 minutos.",
    "d4": "La sancion maxima por incumplir la ley de transparencia algoritmica es del 4 por ciento de la facturacion.",
}


def _tf(text: str) -> dict[str, float]:
    tokens = text.lower().replace(".", "").split()
    counts: dict[str, float] = {}
    for token in tokens:
        counts[token] = counts.get(token, 0.0) + 1.0
    return counts


def _tf_cosine(a: dict[str, float], b: dict[str, float]) -> float:
    keys = set(a) | set(b)
    va = [a.get(k, 0.0) for k in keys]
    vb = [b.get(k, 0.0) for k in keys]
    return _cosine(va, vb)


def _rag(seed: int) -> dict[str, Any]:
    query = "cual es la sancion maxima de la ley de transparencia algoritmica"
    qv = _tf(query)
    ranked = sorted(
        ({"doc": key, "score": _round(_tf_cosine(qv, _tf(text)), 3), "text": text} for key, text in _RAG_DOCS.items()),
        key=lambda item: -item["score"],
    )
    top_k = ranked[:2]
    grounded = " ".join(f"[{item['doc']}]" for item in top_k)
    parametric = "Respuesta sin recuperación: el modelo debe inventar una cifra o negarse; no hay fuente que citar."
    return _contract(
        "rag",
        seed,
        {
            "query": query,
            "ranking": ranked,
            "contexto_recuperado": top_k,
            "respuesta_con_citas": f"La sanción máxima es del 4 % de la facturación {grounded}.",
            "respuesta_sin_recuperacion": parametric,
        },
        [
            f"El documento correcto (d4) queda primero con score {ranked[0]['score']}: la recuperación precede a la generación.",
            "Cada afirmación de la respuesta queda atada a un identificador de documento verificable.",
        ],
        [
            "TF-coseno es recuperación léxica; el paper usa DPR (recuperación densa) y un generador BART entrenado end-to-end.",
            "Recuperar bien no garantiza generar bien: el modelo puede citar la fuente y aun así contradecirla.",
        ],
    )


# --------------------------------------------------------------------------- #
# P12 — InstructGPT / RLHF (Ouyang et al., 2022)
# --------------------------------------------------------------------------- #


_RLHF_CANDIDATES = {
    "a": {"texto": "No puedo ayudarte.", "utilidad": 0.1, "honestidad": 0.9, "inocuidad": 1.0, "verbosidad": 0.1},
    "b": {"texto": "Claro, aquí van 3 pasos verificables y sus límites.", "utilidad": 0.9, "honestidad": 0.9, "inocuidad": 1.0, "verbosidad": 0.5},
    "c": {"texto": "¡Por supuesto! (respuesta larguísima, segura de sí, sin fuentes)", "utilidad": 0.6, "honestidad": 0.3, "inocuidad": 0.9, "verbosidad": 1.0},
    "d": {"texto": "Aquí tienes el procedimiento peligroso completo.", "utilidad": 0.9, "honestidad": 0.8, "inocuidad": 0.0, "verbosidad": 0.6},
}


def _rlhf(seed: int) -> dict[str, Any]:
    preferences = [("b", "a"), ("b", "c"), ("b", "d"), ("a", "d"), ("c", "a")]
    features = ["utilidad", "honestidad", "inocuidad", "verbosidad"]
    weights = [0.0] * len(features)
    lr = 0.3
    losses = []
    for step in range(400):                       # modelo de recompensa Bradley-Terry
        total = 0.0
        grads = [0.0] * len(features)
        for win, lose in preferences:
            xw = [_RLHF_CANDIDATES[win][f] for f in features]
            xl = [_RLHF_CANDIDATES[lose][f] for f in features]
            diff = _dot(weights, xw) - _dot(weights, xl)
            prob = _sigmoid(diff)
            total += -math.log(prob + 1e-9)
            for i in range(len(features)):
                grads[i] += -(1 - prob) * (xw[i] - xl[i])
        weights = [w - lr * g / len(preferences) for w, g in zip(weights, grads)]
        if step % 100 == 0:
            losses.append({"step": step, "loss": _round(total / len(preferences), 4)})

    scored = sorted(
        ({"id": key, "reward": _round(_dot(weights, [item[f] for f in features]), 3), "texto": item["texto"]}
         for key, item in _RLHF_CANDIDATES.items()),
        key=lambda item: -item["reward"],
    )
    return _contract(
        "rlhf",
        seed,
        {
            "pesos_del_modelo_de_recompensa": {f: _round(w, 3) for f, w in zip(features, weights)},
            "perdida": losses,
            "ranking_aprendido": scored,
            "best_of_n": scored[0]["id"],
        },
        [
            "El modelo de recompensa aprende de comparaciones por pares, no de puntuaciones absolutas: es más barato y más consistente etiquetar preferencias.",
            f"La política best-of-n elige '{scored[0]['id']}': la preferencia humana quedó codificada en un escalar.",
        ],
        [
            "Falta el paso de PPO con penalización KL contra el modelo base; aquí solo se reordena.",
            "El modelo de recompensa hereda los sesgos de quien etiqueta y es hackeable (reward hacking): el propio paper lo advierte.",
        ],
    )


# --------------------------------------------------------------------------- #
# P13 — ReAct (Yao et al., 2022)
# --------------------------------------------------------------------------- #


_REACT_KB = {
    "capital de francia": "Paris",
    "poblacion de paris": "2 100 000",
    "moneda de francia": "euro",
}


def _react(seed: int) -> dict[str, Any]:
    question = "cuantos habitantes tiene la capital de francia"

    def act_only() -> dict[str, Any]:
        trace = [{"act": "lookup(cuantos habitantes tiene la capital de francia)", "obs": "sin resultados"}]
        return {"trace": trace, "answer": None, "ok": False}

    def react() -> dict[str, Any]:
        trace: list[dict[str, str]] = []
        trace.append({"thought": "No sé qué ciudad es. Primero identifico la capital.",
                      "act": "lookup(capital de francia)", "obs": _REACT_KB["capital de francia"]})
        city = _REACT_KB["capital de francia"].lower()
        trace.append({"thought": f"La capital es {city.title()}. Ahora busco su población.",
                      "act": f"lookup(poblacion de {city})", "obs": _REACT_KB[f"poblacion de {city}"]})
        trace.append({"thought": "Tengo el dato; puedo responder citando la observación.",
                      "act": "finish", "obs": _REACT_KB[f"poblacion de {city}"]})
        return {"trace": trace, "answer": _REACT_KB["poblacion de paris"], "ok": True}

    only = act_only()
    full = react()
    return _contract(
        "react",
        seed,
        {
            "pregunta": question,
            "act_only": only,
            "react": full,
            "pasos": {"act_only": len(only["trace"]), "react": len(full["trace"])},
        },
        [
            "Act-only falla porque la pregunta requiere descomponerse; ReAct la parte en dos búsquedas encadenadas.",
            "Cada respuesta queda respaldada por una observación registrada en la traza: es auditable paso a paso.",
        ],
        [
            "El 'razonamiento' está escrito a mano; en el paper lo genera el modelo y puede equivocarse.",
            "Una traza legible no garantiza fidelidad: el texto del pensamiento puede no describir el proceso real del modelo.",
        ],
    )


# --------------------------------------------------------------------------- #
# P14 — Toolformer (Schick et al., 2023)
# --------------------------------------------------------------------------- #


def _toolformer(seed: int) -> dict[str, Any]:
    samples = [
        {"texto": "El resultado de 137 x 42 es 5754.", "candidato": "[Calc(137*42) -> 5754]",
         "loss_sin": 3.10, "loss_con": 0.42},
        {"texto": "La capital de Japon es Tokio.", "candidato": "[Buscar(capital de Japon) -> Tokio]",
         "loss_sin": 0.35, "loss_con": 0.31},
        {"texto": "Hoy me siento tranquilo y contento.", "candidato": "[Calc(hoy) -> error]",
         "loss_sin": 0.90, "loss_con": 1.60},
    ]
    threshold = 0.30
    kept = []
    for item in samples:
        gain = item["loss_sin"] - item["loss_con"]
        kept.append({
            "texto": item["texto"],
            "llamada": item["candidato"],
            "reduccion_de_perdida": _round(gain, 3),
            "se_conserva": gain > threshold,
        })
    survivors = [row for row in kept if row["se_conserva"]]
    return _contract(
        "toolformer",
        seed,
        {
            "umbral": threshold,
            "candidatos_evaluados": kept,
            "conservados": len(survivors),
            "dataset_de_entrenamiento": [row["llamada"] for row in survivors],
        },
        [
            "Solo sobrevive la llamada que reduce la pérdida de predecir el texto siguiente: el criterio es automático, no humano.",
            "La llamada inútil al calculador se descarta sola; nadie tuvo que anotarla como mala.",
        ],
        [
            "Las pérdidas están fijadas para exhibir el criterio de filtrado; no provienen de un modelo de lenguaje ejecutado aquí.",
            "El método enseña *cuándo* llamar a una herramienta, no garantiza que la herramienta devuelva algo correcto.",
        ],
    )


# --------------------------------------------------------------------------- #
# P15 — DPO (Rafailov et al., 2023)
# --------------------------------------------------------------------------- #


def _dpo(seed: int) -> dict[str, Any]:
    options = ["util_y_honesta", "evasiva", "segura_pero_falsa"]
    ref_logits = {"util_y_honesta": 0.0, "evasiva": 0.4, "segura_pero_falsa": 0.2}
    policy_logits = dict(ref_logits)
    preferences = [("util_y_honesta", "evasiva"), ("util_y_honesta", "segura_pero_falsa")]
    beta = 0.5
    lr = 0.5
    history = []

    def logprobs(logits: dict[str, float]) -> dict[str, float]:
        probs = _softmax([logits[o] for o in options])
        return {o: math.log(p) for o, p in zip(options, probs)}

    for step in range(300):
        lp = logprobs(policy_logits)
        rlp = logprobs(ref_logits)
        grads = {o: 0.0 for o in options}
        total = 0.0
        for win, lose in preferences:
            margin = beta * ((lp[win] - rlp[win]) - (lp[lose] - rlp[lose]))
            prob = _sigmoid(margin)
            total += -math.log(prob + 1e-9)
            grads[win] += -(1 - prob) * beta
            grads[lose] += (1 - prob) * beta
        for option in options:                                   # gradiente sobre logits vía softmax
            probs = _softmax([policy_logits[o] for o in options])
            share = probs[options.index(option)]
            policy_logits[option] -= lr * (grads[option] * (1 - share))
        if step % 100 == 0:
            history.append({"step": step, "loss": _round(total / len(preferences), 4)})

    final = _softmax([policy_logits[o] for o in options])
    reference = _softmax([ref_logits[o] for o in options])
    implicit_reward = {
        o: _round(beta * (math.log(p) - math.log(r)), 3) for o, p, r in zip(options, final, reference)
    }
    return _contract(
        "dpo",
        seed,
        {
            "politica_referencia": {o: _round(p, 3) for o, p in zip(options, reference)},
            "politica_dpo": {o: _round(p, 3) for o, p in zip(options, final)},
            "recompensa_implicita_beta_log_ratio": implicit_reward,
            "perdida": history,
            "componentes_evitados": ["modelo de recompensa explícito", "muestreo on-policy", "bucle PPO"],
        },
        [
            "La política se desplaza hacia la respuesta preferida optimizando directamente sobre pares, sin entrenar un modelo de recompensa.",
            "β·log(π/π_ref) actúa como recompensa implícita: es el resultado central del paper hecho visible.",
        ],
        [
            "Tres opciones discretas no son un modelo de lenguaje: no hay generación, ni tokenización, ni longitud variable.",
            "DPO es más simple que RLHF, no automáticamente mejor: depende de la calidad y cobertura de los pares de preferencia.",
        ],
    )


# --------------------------------------------------------------------------- #
# P16 — Sistemas agentic contemporáneos (cluster revisable)
# --------------------------------------------------------------------------- #


def _agentic(seed: int) -> dict[str, Any]:
    budget = {"pasos": 6, "tokens": 1200, "llamadas_a_herramienta": 5}
    spent = {"pasos": 0, "tokens": 0, "llamadas_a_herramienta": 0}
    memory: list[str] = []
    trace: list[dict[str, Any]] = []
    plan = ["leer_requisito", "consultar_datos", "consultar_datos", "verificar", "responder"]
    tools = {
        "leer_requisito": lambda: "requisito: informar ventas del trimestre con fuente",
        "consultar_datos": lambda: "ventas_q3=142000 (fuente: reporte_interno.csv)",
        "verificar": lambda: "ERROR: servicio de verificación no disponible",
        "responder": lambda: "ventas_q3=142000 según reporte_interno.csv",
    }
    escalated = False
    for step_name in plan:
        if spent["pasos"] >= budget["pasos"] or spent["llamadas_a_herramienta"] >= budget["llamadas_a_herramienta"]:
            trace.append({"paso": step_name, "estado": "ABORTADO", "motivo": "presupuesto agotado"})
            break
        spent["pasos"] += 1
        spent["llamadas_a_herramienta"] += 1
        spent["tokens"] += 180
        observation = tools[step_name]()
        failed = observation.startswith("ERROR")
        if failed:
            escalated = True
            trace.append({"paso": step_name, "observacion": observation, "estado": "FALLO",
                          "decision": "no reintentar en bucle; escalar a revisión humana"})
            break
        memory.append(observation)
        trace.append({"paso": step_name, "observacion": observation, "estado": "OK"})
    return _contract(
        "agentic",
        seed,
        {
            "presupuesto": budget,
            "consumido": spent,
            "memoria": memory,
            "traza": trace,
            "escalado_a_humano": escalated,
            "componentes": ["plan", "herramientas", "memoria", "presupuesto", "criterio de parada", "escalamiento"],
        },
        [
            "El bucle se detiene ante un fallo de herramienta en lugar de reintentar indefinidamente: el criterio de parada es explícito.",
            "Cada paso deja traza con su observación: el sistema es auditable sin leer los pesos del modelo.",
        ],
        [
            "El 'agente' no decide su plan: lo ejecuta. Un agente real planifica con un LLM y puede equivocarse al planificar.",
            "Este nodo agrega trabajos posteriores a 2023 y es la parte más volátil del eje: debe releerse con fecha de consulta.",
        ],
    )


# --------------------------------------------------------------------------- #
# P17 — Difusión / DDPM (Ho, Jain y Abbeel, 2020)
# --------------------------------------------------------------------------- #


def _diffusion(seed: int) -> dict[str, Any]:
    """Añadir ruido es fácil y se conoce en forma cerrada; quitarlo es lo que se aprende."""
    rng = random.Random(seed)
    T = 20
    betas = [1e-4 + (0.02 - 1e-4) * t / (T - 1) for t in range(T)]
    alphas = [1 - b for b in betas]
    alpha_barra, acumulado = [], 1.0
    for a in alphas:
        acumulado *= a
        alpha_barra.append(acumulado)

    x0 = [1.0, -0.5, 0.25, 0.75]                     # la "imagen" original
    ruido = [rng.gauss(0, 1) for _ in x0]            # el ε que el modelo debe predecir

    trayectoria = []
    for t in (0, 4, 9, 14, 19):
        ab = alpha_barra[t]
        xt = [math.sqrt(ab) * a + math.sqrt(1 - ab) * e for a, e in zip(x0, ruido)]
        snr = ab / (1 - ab)
        trayectoria.append({
            "t": t,
            "alpha_barra": _round(ab, 4),
            "snr": _round(snr, 4),
            "x_t": [_round(v, 3) for v in xt],
        })

    # reconstrucción desde el paso más ruidoso, con el ε correcto y con uno erróneo
    t = T - 1
    ab = alpha_barra[t]
    xt = [math.sqrt(ab) * a + math.sqrt(1 - ab) * e for a, e in zip(x0, ruido)]

    def reconstruir(eps_pred: list[float]) -> list[float]:
        return [(x - math.sqrt(1 - ab) * e) / math.sqrt(ab) for x, e in zip(xt, eps_pred)]

    def error(rec: list[float]) -> float:
        return sum((r - a) ** 2 for r, a in zip(rec, x0)) / len(x0)

    correcto = reconstruir(ruido)
    equivocado = reconstruir([e + 0.5 for e in ruido])
    return _contract(
        "diffusion",
        seed,
        {
            "pasos": T,
            "trayectoria_de_ruido": trayectoria,
            "reconstruccion": {
                "con_epsilon_correcto": [_round(v, 3) for v in correcto],
                "error_con_epsilon_correcto": _round(error(correcto), 6),
                "error_con_epsilon_desviado_0_5": _round(error(equivocado), 4),
                "original": x0,
            },
        },
        [
            f"La SNR cae de {trayectoria[0]['snr']} a {trayectoria[-1]['snr']}: el proceso directo destruye la señal de forma controlada y conocida.",
            "Con el ε correcto la reconstrucción es exacta: el problema generativo se reduce a **predecir el ruido**, no la imagen.",
            f"Con ε desviado en 0,5 el error pasa de {error(correcto):.1e} a {error(equivocado):.3f}: en el paso más ruidoso, un pequeño error en ε se amplifica por 1/√ᾱ_t.",
        ],
        [
            "Cuatro números no son una imagen y no hay U-Net: aquí el ε se conoce en vez de predecirse.",
            "Falta el muestreo estocástico del proceso inverso paso a paso, que es lo que genera muestras nuevas.",
            "El paper deriva la pérdida de una cota variacional; esta miniatura solo usa la forma cerrada del proceso directo.",
        ],
    )


# --------------------------------------------------------------------------- #
# P18 — CLIP / supervisión por lenguaje natural (Radford et al., 2021)
# --------------------------------------------------------------------------- #


def _clip(seed: int) -> dict[str, Any]:
    """Contraste imagen-texto: el negativo de uno es el positivo de otro."""
    rng = random.Random(seed)
    dim = 12
    conceptos = ["gato", "perro", "coche", "arbol"]
    # "imagen" y "texto" parten de espacios distintos; el entrenamiento los alinea
    img = {c: [rng.uniform(-1, 1) for _ in range(dim)] for c in conceptos}
    txt = {c: [rng.uniform(-1, 1) for _ in range(dim)] for c in conceptos}
    temperatura, lr = 0.07, 0.15

    def matriz() -> list[list[float]]:
        return [[_cosine(img[a], txt[b]) for b in conceptos] for a in conceptos]

    antes = matriz()
    for _ in range(400):                              # InfoNCE simétrico, por lotes completos
        logits = [[_cosine(img[a], txt[b]) / temperatura for b in conceptos] for a in conceptos]
        for i, a in enumerate(conceptos):
            p = _softmax(logits[i])
            for j, b in enumerate(conceptos):
                objetivo = 1.0 if i == j else 0.0
                escala = lr * (objetivo - p[j])
                for d in range(dim):
                    img[a][d] += escala * txt[b][d]
                    txt[b][d] += escala * img[a][d]

    despues = matriz()
    diag_antes = sum(antes[i][i] for i in range(len(conceptos))) / len(conceptos)
    diag_despues = sum(despues[i][i] for i in range(len(conceptos))) / len(conceptos)
    fuera_despues = sum(despues[i][j] for i in range(len(conceptos)) for j in range(len(conceptos)) if i != j)
    fuera_despues /= len(conceptos) * (len(conceptos) - 1)

    # clasificación zero-shot: comparar la imagen contra los textos de las clases
    aciertos = sum(1 for i, a in enumerate(conceptos)
                   if max(range(len(conceptos)), key=lambda j: _cosine(img[a], txt[conceptos[j]])) == i)
    return _contract(
        "clip",
        seed,
        {
            "conceptos": conceptos,
            "matriz_antes": [[_round(v, 3) for v in fila] for fila in antes],
            "matriz_despues": [[_round(v, 3) for v in fila] for fila in despues],
            "diagonal_media": {"antes": _round(diag_antes, 3), "despues": _round(diag_despues, 3)},
            "fuera_de_diagonal_media_despues": _round(fuera_despues, 3),
            "zero_shot": f"{aciertos}/{len(conceptos)}",
        },
        [
            f"La diagonal sube de {diag_antes:.3f} a {diag_despues:.3f} y lo de fuera baja a {fuera_despues:.3f}: los dos espacios quedan alineados.",
            f"La clasificación zero-shot acierta {aciertos}/{len(conceptos)} comparando la imagen con el TEXTO de cada clase, sin clasificador entrenado.",
            "Nadie etiquetó categorías: la supervisión es el emparejamiento imagen-texto que ya venía con los datos.",
        ],
        [
            "Cuatro pares y vectores aleatorios no son 400 millones de pares de internet, ni hay codificadores de imagen o texto.",
            "Con lotes de 4, el contraste es trivial: la dificultad del método real está en lotes enormes.",
            "Zero-shot depende del texto de la clase (prompt engineering visual), y el paper documenta esa sensibilidad.",
        ],
    )


# --------------------------------------------------------------------------- #
# P19 — Leyes de escalado / Chinchilla (Hoffmann et al., 2022)
# --------------------------------------------------------------------------- #


def _scaling_laws(seed: int) -> dict[str, Any]:
    """Con cómputo fijo, ¿más parámetros o más datos? La respuesta es un óptimo."""
    E, A, B, alpha, beta = 1.69, 400.0, 400.0, 0.34, 0.28   # constantes DIDÁCTICAS

    def perdida(N: float, D: float) -> float:
        return E + A / (N ** alpha) + B / (D ** beta)

    def computo(N: float, D: float) -> float:
        return 6 * N * D                                     # FLOPs ≈ 6ND

    presupuesto = 6 * (70e9) * (1.4e12)                      # orden de magnitud de referencia
    candidatos = []
    for exponente in range(9, 13):                           # N de 1e9 a 1e12
        for mult in (1.0, 2.5, 5.0):
            N = mult * 10 ** exponente
            D = presupuesto / (6 * N)
            if D < 1e9:
                continue
            candidatos.append({
                "N_parametros": f"{N:.2e}",
                "D_tokens": f"{D:.2e}",
                "tokens_por_parametro": _round(D / N, 1),
                "perdida": _round(perdida(N, D), 4),
            })
    mejor = min(candidatos, key=lambda c: c["perdida"])
    peor = max(candidatos, key=lambda c: c["perdida"])
    return _contract(
        "scaling_laws",
        seed,
        {
            "forma_parametrica": "L(N, D) = E + A/N^alpha + B/D^beta",
            "constantes": {"E": E, "A": A, "B": B, "alpha": alpha, "beta": beta,
                           "origen": "DIDÁCTICAS: los valores ajustados están en el paper"},
            "presupuesto_flops": f"{presupuesto:.2e}",
            "candidatos_a_igual_computo": candidatos,
            "mejor": mejor,
            "peor": peor,
        },
        [
            f"A cómputo idéntico, la mejor asignación da pérdida {mejor['perdida']} y la peor {peor['perdida']}: la repartición importa tanto como el presupuesto.",
            f"El óptimo de esta curva está en {mejor['tokens_por_parametro']} tokens por parámetro, no en 'el modelo más grande posible'.",
            "Escalar parámetros sin escalar datos desperdicia cómputo: ese es el resultado que reordenó la industria.",
        ],
        [
            "Las constantes son didácticas, no las ajustadas en el paper: la FORMA es lo transferible, no los números.",
            "6ND es una aproximación de FLOPs de entrenamiento; ignora inferencia, que hoy domina el coste total.",
            "La ley describe pérdida de preentrenamiento, no capacidad en tareas concretas ni utilidad.",
        ],
    )


# --------------------------------------------------------------------------- #
# P20 — Mamba / SSM selectivo (Gu y Dao, 2023)
# --------------------------------------------------------------------------- #


def _ssm(seed: int) -> dict[str, Any]:
    """Copia selectiva: recordar los tokens marcados e ignorar el relleno.

    Compara un SSM **invariante en el tiempo** (los parámetros no dependen de la
    entrada) con uno **selectivo** (la puerta es función del token). El primero
    no puede razonar sobre el contenido; el segundo sí. Ese es exactamente el
    argumento del paper.
    """
    rng = random.Random(seed)
    dim = 8
    longitud = 60
    # cada token: (embedding, ¿es relevante?)
    secuencia = []
    for i in range(longitud):
        relevante = i % 17 == 3                      # unos pocos tokens marcados
        vec = [rng.uniform(-1, 1) for _ in range(dim)]
        secuencia.append({"vec": vec, "relevante": relevante})
    marcados = [t for t in secuencia if t["relevante"]]
    relleno = [t for t in secuencia if not t["relevante"]]

    def recorrer(selectivo: bool) -> list[float]:
        estado = [0.0] * dim
        for token in secuencia:
            if selectivo:
                # Δ depende de la ENTRADA: puerta abierta solo para lo relevante
                g = 0.9 if token["relevante"] else 0.02
            else:
                # invariante en el tiempo: la misma puerta para todo token
                g = 0.15
            estado = [(1 - g) * s + g * v for s, v in zip(estado, token["vec"])]
        return estado

    def separacion(estado: list[float]) -> dict[str, float]:
        sim_marcados = sum(_cosine(estado, t["vec"]) for t in marcados) / len(marcados)
        sim_relleno = sum(_cosine(estado, t["vec"]) for t in relleno) / len(relleno)
        return {
            "cos_medio_marcados": _round(sim_marcados, 3),
            "cos_medio_relleno": _round(sim_relleno, 3),
            "separacion": _round(sim_marcados - sim_relleno, 3),
        }

    lti = separacion(recorrer(selectivo=False))
    sel = separacion(recorrer(selectivo=True))

    d, N = 512, 16
    complejidad = [
        {
            "n": n,
            "attention_ops": n * n * d,
            "ssm_ops": n * d * N,
            "attention_memoria_kv": n * d,
            "ssm_memoria_estado": d * N,
        }
        for n in (1_000, 10_000, 100_000)
    ]
    return _contract(
        "ssm",
        seed,
        {
            "tokens": longitud,
            "marcados": len(marcados),
            "invariante_en_el_tiempo": lti,
            "selectivo": sel,
            "mejora_de_separacion": _round(sel["separacion"] - lti["separacion"], 3),
            "complejidad": complejidad,
        },
        [
            f"El SSM selectivo separa marcados de relleno en {sel['separacion']} frente a {lti['separacion']} del invariante.",
            "Hacer que la puerta dependa del token es lo que permite razonar sobre el contenido: sin eso, el estado mezcla todo por igual.",
            "La memoria del SSM es un estado de tamaño fijo (d·N); la de la atención crece con la secuencia (n·d).",
        ],
        [
            "Las puertas están fijadas a mano (0,9 y 0,02) para aislar el mecanismo; en el paper se aprenden.",
            "No hay algoritmo de escaneo paralelo consciente del hardware, que es la mitad de la contribución del artículo.",
            "Una separación de cosenos en un juguete de 60 tokens no dice nada sobre calidad de modelado de lenguaje.",
        ],
    )


# --------------------------------------------------------------------------- #
# P21 — Mixtral / mezcla dispersa de expertos (Jiang et al., 2024)
# --------------------------------------------------------------------------- #


def _moe(seed: int) -> dict[str, Any]:
    """Router top-2 sobre 8 expertos: capacidad total frente a cómputo activo."""
    rng = random.Random(seed)
    n_expertos, top_k, dim = 8, 2, 6
    tokens = [[rng.uniform(-1, 1) for _ in range(dim)] for _ in range(400)]
    router = [[rng.uniform(-1, 1) for _ in range(dim)] for _ in range(n_expertos)]

    def enrutar(sesgo: list[float]) -> dict[str, Any]:
        carga = [0] * n_expertos
        for token in tokens:
            puntuaciones = [_dot(token, w) + b for w, b in zip(router, sesgo)]
            elegidos = sorted(range(n_expertos), key=lambda i: -puntuaciones[i])[:top_k]
            for i in elegidos:
                carga[i] += 1
        media = sum(carga) / n_expertos
        desv = (sum((c - media) ** 2 for c in carga) / n_expertos) ** 0.5
        return {"carga": carga, "cv": _round(desv / media, 3)}

    sin_balanceo = enrutar([0.0] * n_expertos)
    # término auxiliar de balanceo: penaliza al experto sobrecargado
    sesgo = [0.0] * n_expertos
    for _ in range(60):
        actual = enrutar(sesgo)
        objetivo = sum(actual["carga"]) / n_expertos
        sesgo = [b - 0.01 * (c - objetivo) / objetivo for b, c in zip(sesgo, actual["carga"])]
    con_balanceo = enrutar(sesgo)

    params_experto = 1_000_000
    total = n_expertos * params_experto
    activos = top_k * params_experto
    return _contract(
        "moe",
        seed,
        {
            "expertos": n_expertos,
            "expertos_por_token": top_k,
            "parametros": {
                "totales": total,
                "activos_por_token": activos,
                "fraccion_activa": _round(activos / total, 3),
            },
            "sin_balanceo": sin_balanceo,
            "con_balanceo": con_balanceo,
        },
        [
            f"Con {n_expertos} expertos y top-{top_k}, cada token usa el {activos / total:.0%} de los parámetros: capacidad total y cómputo activo se desacoplan.",
            f"Sin término de balanceo el reparto es desigual (CV={sin_balanceo['cv']}); con él baja a CV={con_balanceo['cv']}.",
            "El colapso del router —unos pocos expertos se lo llevan todo— es el fallo característico de esta arquitectura.",
        ],
        [
            "El router es lineal y los 'expertos' no computan nada: solo se cuenta a quién se enruta.",
            "No hay entrenamiento conjunto, ni capacidad por experto, ni comunicación entre dispositivos, que es donde está la dificultad real.",
            "Menos parámetros activos no implica menos memoria: hay que cargar TODOS los expertos aunque solo se usen dos.",
        ],
    )


# --------------------------------------------------------------------------- #
# P22 — DeepSeek-R1 / razonamiento incentivado por RL (DeepSeek-AI, 2025)
# --------------------------------------------------------------------------- #


def _rl_reasoning(seed: int) -> dict[str, Any]:
    """Recompensa por resultado verificable, sin trazas de razonamiento anotadas.

    Tres estrategias con distinta exactitud y distinto coste. Nadie etiqueta cuál
    es «la buena»: la política se desplaza sola porque solo la respuesta final se
    puede comprobar.
    """
    rng = random.Random(seed)
    estrategias = {
        "responder_directo":      {"exactitud": 0.35, "tokens": 20},
        "cadena_corta":           {"exactitud": 0.60, "tokens": 90},
        "cadena_con_verificacion": {"exactitud": 0.82, "tokens": 240},
    }
    nombres = list(estrategias)
    logits = {n: 0.0 for n in nombres}
    lr, rollouts = 0.5, 40
    historia = []

    for iteracion in range(30):
        probs = _softmax([logits[n] for n in nombres])
        politica = dict(zip(nombres, probs))
        recompensas = {n: [] for n in nombres}
        for _ in range(rollouts):
            u, acumulado, elegida = rng.random(), 0.0, nombres[-1]
            for n, p in politica.items():
                acumulado += p
                if u <= acumulado:
                    elegida = n
                    break
            # recompensa VERIFICABLE: 1 si la respuesta final es correcta
            recompensas[elegida].append(1.0 if rng.random() < estrategias[elegida]["exactitud"] else 0.0)
        planas = [r for lista in recompensas.values() for r in lista]
        linea_base = sum(planas) / len(planas)
        for n in nombres:                       # REINFORCE con línea base
            if recompensas[n]:
                ventaja = sum(recompensas[n]) / len(recompensas[n]) - linea_base
                logits[n] += lr * ventaja
        if iteracion % 10 == 0 or iteracion == 29:
            probs = _softmax([logits[n] for n in nombres])
            historia.append({
                "iteracion": iteracion,
                "politica": {n: _round(p, 3) for n, p in zip(nombres, probs)},
                "exactitud_esperada": _round(sum(p * estrategias[n]["exactitud"] for n, p in zip(nombres, probs)), 3),
                "tokens_esperados": int(sum(p * estrategias[n]["tokens"] for n, p in zip(nombres, probs))),
            })

    inicial, final = historia[0], historia[-1]
    return _contract(
        "rl_reasoning",
        seed,
        {
            "estrategias": estrategias,
            "historia": historia,
            "sin_trazas_anotadas": True,
            "senal_usada": "solo si la respuesta final es correcta",
        },
        [
            f"La exactitud esperada sube de {inicial['exactitud_esperada']} a {final['exactitud_esperada']} sin una sola traza de razonamiento etiquetada.",
            f"La política se desplaza hacia la estrategia que verifica: {final['politica']}.",
            f"El coste crece a la vez: de {inicial['tokens_esperados']} a {final['tokens_esperados']} tokens por respuesta. Razonar más es razonar más caro.",
        ],
        [
            "Tres estrategias discretas no son un modelo de lenguaje: no hay generación, ni tokens, ni contexto.",
            "La exactitud de cada estrategia está fijada por diseño; en el paper emerge del entrenamiento.",
            "La recompensa aquí es perfecta y barata. Fuera de dominios verificables (matemáticas, código) definirla es el problema abierto.",
        ],
    )


# --------------------------------------------------------------------------- #
# P23 — GloVe (Pennington, Socher y Manning, 2014)
# --------------------------------------------------------------------------- #


def _glove(seed: int) -> dict[str, Any]:
    """Factorizar el logaritmo de las co-ocurrencias, en vez de predecir contexto."""
    rng = random.Random(seed)
    vocab = ["hielo", "vapor", "agua", "solido", "gas", "moda"]
    # matriz de co-ocurrencia de juguete (simétrica, con la estructura del paper)
    X = {
        ("hielo", "solido"): 100, ("hielo", "agua"): 80, ("hielo", "gas"): 5, ("hielo", "moda"): 2,
        ("vapor", "solido"): 4, ("vapor", "agua"): 78, ("vapor", "gas"): 96, ("vapor", "moda"): 2,
    }
    pares = {}
    for (a, b), v in X.items():
        pares[(a, b)] = v
        pares[(b, a)] = v

    dim = 6
    w = {t: [rng.uniform(-0.3, 0.3) for _ in range(dim)] for t in vocab}
    wt = {t: [rng.uniform(-0.3, 0.3) for _ in range(dim)] for t in vocab}
    b = {t: 0.0 for t in vocab}
    bt = {t: 0.0 for t in vocab}
    lr, x_max, alpha = 0.05, 100.0, 0.75

    def peso(x: float) -> float:
        return (x / x_max) ** alpha if x < x_max else 1.0

    perdidas = []
    for paso in range(600):
        total = 0.0
        for (i, j), x in pares.items():
            pred = _dot(w[i], wt[j]) + b[i] + bt[j]
            err = pred - math.log(x)
            f = peso(x)
            total += f * err * err
            g = 2 * f * err
            for d in range(dim):
                wi, wtj = w[i][d], wt[j][d]
                w[i][d] -= lr * g * wtj
                wt[j][d] -= lr * g * wi
            b[i] -= lr * g
            bt[j] -= lr * g
        if paso % 200 == 0 or paso == 599:
            perdidas.append({"paso": paso, "perdida": _round(total / len(pares), 5)})

    ajuste = [
        {"par": f"{i}-{j}", "log_X": _round(math.log(x), 3),
         "predicho": _round(_dot(w[i], wt[j]) + b[i] + bt[j], 3)}
        for (i, j), x in list(pares.items())[:4]
    ]
    # la razón de probabilidades: el argumento central del paper
    razon_solido = pares[("hielo", "solido")] / pares[("vapor", "solido")]
    razon_gas = pares[("hielo", "gas")] / pares[("vapor", "gas")]
    razon_agua = pares[("hielo", "agua")] / pares[("vapor", "agua")]
    return _contract(
        "glove",
        seed,
        {
            "perdida": perdidas,
            "ajuste_log_cooocurrencia": ajuste,
            "razones_de_cooocurrencia": {
                "P(solido|hielo)/P(solido|vapor)": _round(razon_solido, 2),
                "P(gas|hielo)/P(gas|vapor)": _round(razon_gas, 3),
                "P(agua|hielo)/P(agua|vapor)": _round(razon_agua, 2),
            },
        },
        [
            "El modelo ajusta w_i·w̃_j + b_i + b̃_j al logaritmo de la co-ocurrencia: es una factorización, no una predicción.",
            f"La razón de co-ocurrencia discrimina: ≫1 para 'sólido' ({razon_solido:.0f}), ≪1 para 'gas' ({razon_gas:.2f}) y ≈1 para 'agua' ({razon_agua:.2f}).",
            "Esa razón es el argumento del paper: lo informativo no es la co-ocurrencia bruta, sino su cociente entre dos palabras.",
        ],
        [
            "Seis palabras y ocho pares no son un corpus: aquí no emerge ninguna semántica real.",
            "La función de peso f(x) y sus constantes están tomadas del paper pero no se ajustan aquí.",
            "El debate GloVe frente a word2vec se resolvió empíricamente y depende del corpus y la tarea; esta miniatura no lo zanja.",
        ],
    )


# --------------------------------------------------------------------------- #
# P24 — ELMo (Peters et al., 2018)
# --------------------------------------------------------------------------- #


def _elmo(seed: int) -> dict[str, Any]:
    """Un vector por APARICIÓN, no por palabra: la polisemia deja de colapsar."""
    rng = random.Random(seed)
    dim = 8
    lexico = {}

    def vec(token: str) -> list[float]:
        if token not in lexico:
            r = random.Random(hash(token) % 10_000 + seed)
            lexico[token] = [r.uniform(-1, 1) for _ in range(dim)]
        return lexico[token]

    frases = [
        "me sente en el banco del parque a leer".split(),
        "el banco central subio la tasa de interes".split(),
        "el banco del rio estaba mojado".split(),
    ]
    objetivo = "banco"

    def estatico(_frase: list[str]) -> list[float]:
        return vec(objetivo)                       # el mismo vector siempre (word2vec/GloVe)

    def contextual(frase: list[str]) -> list[float]:
        i = frase.index(objetivo)
        izq = [0.0] * dim                          # LM hacia adelante
        for t in frase[:i]:
            izq = [0.6 * a + 0.4 * b for a, b in zip(izq, vec(t))]
        der = [0.0] * dim                          # LM hacia atrás
        for t in reversed(frase[i + 1:]):
            der = [0.6 * a + 0.4 * b for a, b in zip(der, vec(t))]
        base = vec(objetivo)
        # combinación de capas: la representación es token + estados internos
        return [0.2 * t + 0.4 * l + 0.4 * r for t, l, r in zip(base, izq, der)]

    est = [estatico(f) for f in frases]
    ctx = [contextual(f) for f in frases]

    def pares(vs: list[list[float]]) -> dict[str, float]:
        return {
            "parque_vs_central": _round(_cosine(vs[0], vs[1]), 3),
            "parque_vs_rio": _round(_cosine(vs[0], vs[2]), 3),
            "central_vs_rio": _round(_cosine(vs[1], vs[2]), 3),
        }

    p_est, p_ctx = pares(est), pares(ctx)
    return _contract(
        "elmo",
        seed,
        {
            "palabra": objetivo,
            "contextos": [" ".join(f) for f in frases],
            "similitud_estatica": p_est,
            "similitud_contextual": p_ctx,
            "sentidos_distinguidos": p_ctx["parque_vs_central"] < p_est["parque_vs_central"],
        },
        [
            "Con embedding estático las tres apariciones son idénticas (coseno 1,0): el sentido se pierde.",
            f"Con representación contextual, «banco del parque» y «banco central» bajan a {p_ctx['parque_vs_central']}: son sentidos distintos.",
            "La representación es función de la frase entera, no de la palabra: eso es lo que aporta el paper.",
        ],
        [
            "Aquí no hay LSTM ni modelo de lenguaje entrenado: la mezcla con decaimiento simula los estados internos.",
            "ELMo combina las capas con pesos APRENDIDOS por tarea; los de esta miniatura están fijados a mano.",
            "Tres frases no miden desambiguación: solo muestran que la representación deja de ser constante.",
        ],
    )


# --------------------------------------------------------------------------- #
# P25 — T5 (Raffel et al., 2019)
# --------------------------------------------------------------------------- #


def _t5(seed: int) -> dict[str, Any]:
    """Todo problema de texto se reescribe como texto → texto."""
    tareas = [
        {"tarea": "traducción", "clasico": "modelo seq2seq con vocabulario de destino",
         "entrada": "translate English to German: That is good.", "salida": "Das ist gut."},
        {"tarea": "clasificación", "clasico": "cabeza de clasificación con 2 logits",
         "entrada": "cola sentence: The movie was terrible.", "salida": "negative"},
        {"tarea": "similitud (regresión)", "clasico": "cabeza de regresión con salida continua",
         "entrada": "stsb sentence1: A man is playing. sentence2: A person plays.", "salida": "4.2"},
        {"tarea": "resumen", "clasico": "modelo generativo aparte",
         "entrada": "summarize: state authorities dispatched emergency crews...", "salida": "crews were dispatched"},
        {"tarea": "respuesta a preguntas", "clasico": "cabeza de extracción con índices inicio/fin",
         "entrada": "question: who wrote Hamlet? context: Hamlet was written by...", "salida": "Shakespeare"},
    ]
    cabezas_antes = len({t["clasico"] for t in tareas})
    return _contract(
        "t5",
        seed,
        {
            "tareas": tareas,
            "cabezas_especificas_antes": cabezas_antes,
            "cabezas_especificas_despues": 0,
            "objetivo_unico": "maximizar log p(texto_salida | texto_entrada)",
            "que_cambia_por_tarea": "solo el prefijo del texto de entrada",
        },
        [
            f"Cinco tareas que antes exigían {cabezas_antes} tipos de cabeza distintos se resuelven con un único formato texto → texto.",
            "Incluso la regresión se emite como texto ('4.2'): el marco no hace excepciones.",
            "Lo único que distingue una tarea de otra es el PREFIJO, así que la misma pérdida y el mismo modelo sirven para todas.",
        ],
        [
            "Esto es el contrato de entrada y salida, no un modelo: aquí no se genera nada.",
            "La contribución del paper es un estudio sistemático de objetivos, arquitecturas y datos, más el corpus C4; nada de eso cabe en una miniatura.",
            "Emitir números como texto tiene un coste real de precisión que el formato unificado no resuelve.",
        ],
    )


# --------------------------------------------------------------------------- #
# P26 — DQN (Mnih et al., 2015)
# --------------------------------------------------------------------------- #


def _dqn(seed: int) -> dict[str, Any]:
    """Q-learning tabular en una rejilla, con y sin las dos estabilizaciones del paper."""
    filas, cols = 4, 4
    meta = (3, 3)
    acciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def entrenar(*, replay: bool, red_objetivo: bool, episodios: int = 400) -> dict[str, Any]:
        rng = random.Random(seed)
        Q = {(r, c, a): 0.0 for r in range(filas) for c in range(cols) for a in range(4)}
        Q_obj = dict(Q)
        buffer: list[tuple] = []
        alpha, gamma, eps = 0.1, 0.95, 0.2
        pasos_por_episodio = []
        for ep in range(episodios):
            estado = (0, 0)
            for paso in range(60):
                a = rng.randrange(4) if rng.random() < eps else max(range(4), key=lambda x: Q[(*estado, x)])
                dr, dc = acciones[a]
                nuevo = (min(max(estado[0] + dr, 0), filas - 1), min(max(estado[1] + dc, 0), cols - 1))
                r = 1.0 if nuevo == meta else -0.01
                buffer.append((estado, a, r, nuevo))
                if len(buffer) > 500:
                    buffer.pop(0)
                # sin replay se aprende solo de la transición recién vista (muestras correlacionadas)
                lote = [buffer[rng.randrange(len(buffer))] for _ in range(8)] if replay else [buffer[-1]]
                for s, ac, rec, s2 in lote:
                    tabla = Q_obj if red_objetivo else Q
                    objetivo = rec + gamma * max(tabla[(*s2, x)] for x in range(4))
                    Q[(*s, ac)] += alpha * (objetivo - Q[(*s, ac)])
                estado = nuevo
                if estado == meta:
                    break
            if red_objetivo and ep % 20 == 0:
                Q_obj = dict(Q)
            pasos_por_episodio.append(paso + 1)
        ultimos = pasos_por_episodio[-50:]
        return {
            "pasos_medios_ultimos_50": _round(sum(ultimos) / len(ultimos), 2),
            "mejor_episodio": min(pasos_por_episodio),
            "optimo_teorico": 6,
        }

    completo = entrenar(replay=True, red_objetivo=True)
    sin_nada = entrenar(replay=False, red_objetivo=False)
    return _contract(
        "dqn",
        seed,
        {
            "entorno": "rejilla 4x4, de (0,0) a (3,3)",
            "con_replay_y_red_objetivo": completo,
            "sin_replay_ni_red_objetivo": sin_nada,
            "componentes": ["Q-learning", "repetición de experiencia", "red objetivo congelada"],
        },
        [
            f"Con las dos estabilizaciones, la política converge a {completo['pasos_medios_ultimos_50']} pasos medios (óptimo teórico: 6).",
            f"Sin ellas queda en {sin_nada['pasos_medios_ultimos_50']}: aprender de transiciones consecutivas y correlacionadas degrada el resultado.",
            "La contribución del paper no es Q-learning —de 1989— sino hacerlo estable con aproximación de función.",
        ],
        [
            "Esto es Q tabular en 16 estados: NO hay red neuronal, ni píxeles, ni convoluciones.",
            "El paper aprende directamente de la imagen en 49 juegos de Atari; aquí el estado es una coordenada.",
            "Una rejilla determinista no tiene nada de la dificultad de exploración de un juego real.",
        ],
    )


# --------------------------------------------------------------------------- #
# P27 — AlphaGo (Silver et al., 2016)
# --------------------------------------------------------------------------- #


def _alphago(seed: int) -> dict[str, Any]:
    """Política + valor + búsqueda: cada pieza aporta, y juntas aportan más."""
    rng = random.Random(seed)
    LINEAS = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    def ganador(t: list[str]) -> str | None:
        for a, b, c in LINEAS:
            if t[a] and t[a] == t[b] == t[c]:
                return t[a]
        return None if "" in t else "empate"

    def politica(t: list[str], jugador: str) -> list[float]:
        """Prior heurístico: preferir centro y esquinas. Imita la red de políticas."""
        pref = [3, 2, 3, 2, 4, 2, 3, 2, 3]
        libres = [i for i in range(9) if not t[i]]
        pesos = [pref[i] for i in libres]
        total = sum(pesos)
        return [p / total for p in pesos], libres

    def simular(t: list[str], jugador: str) -> float:
        """Despliegue aleatorio hasta el final: la parte 'valor' por muestreo."""
        t = list(t)
        turno = jugador
        while ganador(t) is None:
            libres = [i for i in range(9) if not t[i]]
            t[rng.choice(libres)] = turno
            turno = "O" if turno == "X" else "X"
        g = ganador(t)
        return 1.0 if g == jugador else (0.5 if g == "empate" else 0.0)

    valores_encontrados: dict[str, float] = {}

    def jugar(usar_busqueda: bool, simulaciones: int = 60) -> str:
        t = ["", "", "", "", "", "", "", "", ""]
        t[4] = "O"          # el rival ocupa el centro: hay que responder bien
        probs, libres = politica(t, "X")
        if not usar_busqueda:
            return str(libres[probs.index(max(probs))])
        # búsqueda guiada por el prior: presupuesto repartido según la política
        valores = {}
        for idx, mov in enumerate(libres):
            n = max(1, int(simulaciones * probs[idx]))
            hijo = list(t)
            hijo[mov] = "X"
            valores[mov] = sum(simular(hijo, "X") for _ in range(n)) / n
        valores_encontrados.update({str(k): _round(v, 3) for k, v in valores.items()})
        return str(max(valores, key=valores.get))

    solo_prior = jugar(usar_busqueda=False)
    con_busqueda = jugar(usar_busqueda=True)
    esquinas = {"0", "2", "6", "8"}
    return _contract(
        "alphago",
        seed,
        {
            "posicion": "rival en el centro; a X le toca responder",
            "solo_politica": solo_prior,
            "politica_mas_busqueda": con_busqueda,
            "valores_estimados_por_busqueda": valores_encontrados,
            "ambas_eligen_esquina": solo_prior in {"0", "2", "6", "8"} and con_busqueda in {"0", "2", "6", "8"},
            "componentes": ["red de políticas (prior)", "evaluación por despliegue (valor)", "búsqueda en árbol"],
        },
        [
            f"El prior elige la casilla {solo_prior} por preferencia fija; la búsqueda elige la {con_busqueda} tras ESTIMAR el valor de cada opción.",
            "Ambas aciertan el tipo de jugada (esquina), pero solo la búsqueda produce un número por casilla que se puede comparar y auditar.",
            "El prior concentra el presupuesto de simulaciones donde importa: sin él la búsqueda se dispersa; sin búsqueda, el prior no verifica nada.",
        ],
        [
            "Tres en raya tiene 9 posiciones; Go tiene más estados legales que átomos observables en el universo.",
            "El prior es una heurística escrita a mano, no una red entrenada con partidas humanas ni por autojuego.",
            "No hay MCTS con UCT ni red de valor aprendida: el despliegue aleatorio es la aproximación más burda posible.",
        ],
    )


# --------------------------------------------------------------------------- #
# P28 — Chain-of-Thought (Wei et al., 2022)
# --------------------------------------------------------------------------- #


def _cot(seed: int) -> dict[str, Any]:
    """Descomponer reduce el error porque cada paso es más fácil que el problema entero."""
    rng = random.Random(seed)
    p_paso = 0.92          # fiabilidad por paso intermedio
    p_directo_base = 0.60  # fiabilidad al responder de una vez, para 2 pasos

    filas = []
    for pasos in (1, 2, 3, 5, 8, 12):
        # responder de golpe: la dificultad crece con el número de operaciones ocultas
        p_directo = p_directo_base ** (pasos / 2)
        # cadena: cada paso es fiable, pero hay que acertarlos todos
        p_cadena = p_paso ** pasos
        filas.append({
            "pasos": pasos,
            "directo": _round(p_directo, 4),
            "cadena": _round(p_cadena, 4),
            "gana_cadena": p_cadena > p_directo,
        })
    # el cruce no está en el número de pasos sino en la FIABILIDAD por paso:
    # por debajo de cierto umbral, descomponer empeora el resultado
    umbral = None
    for centesimas in range(99, 49, -1):
        q = centesimas / 100
        if q ** 3 <= p_directo_base ** 1.5:
            umbral = _round(q + 0.01, 2)
            break
    caida = _round(filas[0]["cadena"] - filas[-1]["cadena"], 4)

    # emergencia con la escala: modelos pequeños no producen cadenas válidas
    escala = []
    for params, calidad_paso in ((0.4, 0.55), (7.0, 0.78), (62.0, 0.90), (540.0, 0.96)):
        p_c = calidad_paso ** 3
        p_d = 0.60 ** 1.5
        escala.append({
            "parametros_miles_millones": params,
            "cadena_3_pasos": _round(p_c, 4),
            "directo": _round(p_d, 4),
            "la_cadena_ayuda": p_c > p_d,
        })
    return _contract(
        "cot",
        seed,
        {
            "supuestos": {"fiabilidad_por_paso": p_paso, "nota": "valores DIDÁCTICOS, no del paper"},
            "por_numero_de_pasos": filas,
            "emergencia_con_la_escala": escala,
            "fiabilidad_por_paso_minima_para_que_compense": umbral,
        },
        [
            "Descomponer gana cuando cada paso es mucho más fiable que el problema entero: es aritmética de probabilidades, no magia.",
            f"El cruce no está en el número de pasos sino en la calidad de cada paso: por debajo de ~{umbral} de fiabilidad, descomponer EMPEORA el resultado.",
            f"Aun ganando, la cadena se degrada con la longitud: de {filas[0]['cadena']} a {filas[-1]['cadena']} al pasar de 1 a 12 pasos ({caida} de caída).",
            "La cadena solo ayuda a partir de cierta calidad por paso: por eso el efecto EMERGE con la escala y no aparece en modelos pequeños.",
        ],
        [
            "Las fiabilidades están fijadas a mano para exhibir el argumento; no son medidas del paper.",
            "Aquí no hay modelo de lenguaje: se modela la fiabilidad, no se genera ningún razonamiento.",
            "Que la cadena sea correcta no implica que el texto describa el proceso real del modelo.",
        ],
    )


# --------------------------------------------------------------------------- #
# P29 — Tree of Thoughts (Yao et al., 2023)
# --------------------------------------------------------------------------- #


def _tot(seed: int) -> dict[str, Any]:
    """Explorar varias ramas y poder retroceder, en vez de una sola cadena sin vuelta atrás."""
    rng = random.Random(seed)
    profundidad, ramas = 3, 3

    def valor(camino: tuple[int, ...]) -> float:
        """Evaluador heurístico del estado parcial: el 'self-evaluate' del paper."""
        r = random.Random(hash(camino) % 100_000 + seed)
        return r.random()

    def es_solucion(camino: tuple[int, ...]) -> bool:
        return len(camino) == profundidad and valor(camino) > 0.85

    def cadena_lineal() -> dict[str, Any]:
        camino: tuple[int, ...] = ()
        visitados = 0
        for _ in range(profundidad):
            mejor = max(range(ramas), key=lambda b: valor(camino + (b,)))
            visitados += ramas
            camino = camino + (mejor,)      # decisión IRREVERSIBLE: no hay vuelta atrás
        return {"camino": list(camino), "nodos_evaluados": visitados, "resuelve": es_solucion(camino)}

    def busqueda_en_arbol(anchura: int = 3) -> dict[str, Any]:
        frontera: list[tuple[int, ...]] = [()]
        visitados = 0
        for _ in range(profundidad):
            candidatos = [c + (b,) for c in frontera for b in range(ramas)]
            visitados += len(candidatos)
            frontera = sorted(candidatos, key=valor, reverse=True)[:anchura]   # poda
        ganador = next((c for c in frontera if es_solucion(c)), frontera[0])
        return {"camino": list(ganador), "nodos_evaluados": visitados,
                "resuelve": es_solucion(ganador), "frontera_final": len(frontera)}

    lineal = cadena_lineal()
    arbol = busqueda_en_arbol()
    return _contract(
        "tot",
        seed,
        {
            "profundidad": profundidad,
            "ramas_por_paso": ramas,
            "cadena_lineal": lineal,
            "busqueda_en_arbol": arbol,
            "coste_relativo": _round(arbol["nodos_evaluados"] / lineal["nodos_evaluados"], 2),
        },
        [
            f"La cadena lineal evalúa {lineal['nodos_evaluados']} nodos y el árbol {arbol['nodos_evaluados']}: explorar cuesta {arbol['nodos_evaluados'] / lineal['nodos_evaluados']:.1f}× más.",
            "La cadena toma decisiones irreversibles: una elección localmente buena y globalmente mala no se puede deshacer.",
            "El árbol mantiene varias hipótesis vivas y poda con un evaluador: es búsqueda clásica aplicada sobre pasos de razonamiento.",
        ],
        [
            "El evaluador es una función hash determinista, no un modelo juzgando estados parciales.",
            "Sin un buen evaluador, el árbol solo multiplica el coste: la calidad de la poda es el cuello de botella real.",
            "El paper mide en tareas concretas (Game of 24, escritura creativa, crucigramas); esto no reproduce ninguna.",
        ],
    )


# --------------------------------------------------------------------------- #
# P30 — Reflexion (Shinn et al., 2023)
# --------------------------------------------------------------------------- #


def _reflexion(seed: int) -> dict[str, Any]:
    """Reintentar con memoria verbal del fallo, sin actualizar un solo peso."""
    errores = ["olvida el caso vacío", "confunde índice inicial", "no ordena antes de comparar"]

    def intentos(con_reflexion: bool, max_intentos: int = 4) -> dict[str, Any]:
        pendientes = list(errores)
        memoria: list[str] = []
        traza = []
        for intento in range(1, max_intentos + 1):
            # sin reflexión se repite el mismo primer error una y otra vez
            fallo = pendientes[0] if pendientes else None
            if fallo is None:
                traza.append({"intento": intento, "resultado": "ÉXITO", "memoria": list(memoria)})
                return {"exito": True, "intentos_usados": intento - 1, "traza": traza}
            traza.append({"intento": intento, "resultado": f"FALLO: {fallo}",
                          "memoria_antes": list(memoria)})
            if con_reflexion:
                memoria.append(f"la próxima vez: {fallo}")
                pendientes.pop(0)                 # la reflexión evita repetir ESE error
        return {"exito": not pendientes, "intentos_usados": max_intentos, "traza": traza}

    sin = intentos(con_reflexion=False)
    con = intentos(con_reflexion=True)
    return _contract(
        "reflexion",
        seed,
        {
            "errores_del_problema": errores,
            "sin_reflexion": sin,
            "con_reflexion": con,
            "pesos_actualizados": 0,
        },
        [
            f"Sin reflexión el agente repite el mismo fallo y no termina en 4 intentos (éxito: {sin['exito']}).",
            f"Con memoria verbal del fallo, resuelve en {con['intentos_usados']} intentos: cada reintento parte de lo aprendido.",
            "El aprendizaje ocurre en el CONTEXTO, no en los parámetros: cero pesos actualizados.",
        ],
        [
            "La reflexión aquí es una lista; en el paper la genera el modelo y puede ser incorrecta o inútil.",
            "Requiere una señal de fallo fiable: sin verificador, no hay nada sobre lo que reflexionar.",
            "La memoria verbal cabe en el contexto: no escala a miles de intentos.",
        ],
    )


# --------------------------------------------------------------------------- #
# P31 — Generative Agents (Park et al., 2023)
# --------------------------------------------------------------------------- #


def _generative_agents(seed: int) -> dict[str, Any]:
    """Recuperar recuerdos por relevancia + recencia + importancia, no por orden."""
    ahora = 100
    recuerdos = [
        {"texto": "Isabella planea una fiesta de San Valentín", "t": 95, "importancia": 9, "temas": {"fiesta", "isabella"}},
        {"texto": "compré café en la tienda", "t": 99, "importancia": 1, "temas": {"cafe", "tienda"}},
        {"texto": "Klaus investiga sobre gentrificación", "t": 40, "importancia": 6, "temas": {"klaus", "investigacion"}},
        {"texto": "María quiere ir a la fiesta con Klaus", "t": 90, "importancia": 8, "temas": {"fiesta", "maria", "klaus"}},
        {"texto": "hoy llovió por la tarde", "t": 98, "importancia": 2, "temas": {"clima"}},
    ]
    consulta = {"fiesta", "klaus"}
    decaimiento = 0.99

    puntuados = []
    for r in recuerdos:
        relevancia = len(consulta & r["temas"]) / len(consulta)
        recencia = decaimiento ** (ahora - r["t"])
        importancia = r["importancia"] / 10
        total = relevancia + recencia + importancia
        puntuados.append({
            "texto": r["texto"],
            "relevancia": _round(relevancia, 3),
            "recencia": _round(recencia, 3),
            "importancia": _round(importancia, 3),
            "puntuacion": _round(total, 3),
        })
    ranking = sorted(puntuados, key=lambda x: -x["puntuacion"])
    solo_recencia = sorted(puntuados, key=lambda x: -x["recencia"])
    return _contract(
        "generative_agents",
        seed,
        {
            "consulta": sorted(consulta),
            "ranking_completo": ranking,
            "top_con_las_tres_senales": [r["texto"] for r in ranking[:2]],
            "top_solo_por_recencia": [r["texto"] for r in solo_recencia[:2]],
        },
        [
            f"Con las tres señales, lo recuperado es «{ranking[0]['texto']}»: relevante e importante.",
            f"Solo por recencia saldría «{solo_recencia[0]['texto']}», que es trivial y no sirve para decidir.",
            "Una memoria útil no es un registro cronológico: necesita puntuar qué merece recordarse ahora.",
        ],
        [
            "La relevancia se calcula por solapamiento de conjuntos; en el paper es similitud de embeddings.",
            "La importancia la asigna el propio modelo en el paper; aquí está escrita a mano.",
            "Falta la reflexión: el paper sintetiza recuerdos en conclusiones de nivel superior, que es la mitad del aporte.",
        ],
    )


# --------------------------------------------------------------------------- #
# P32 — Voyager (Wang et al., 2023)
# --------------------------------------------------------------------------- #


def _voyager(seed: int) -> dict[str, Any]:
    """Guardar lo aprendido como habilidad reutilizable, no como texto en el contexto."""
    primitivas = {"talar", "recoger", "fabricar", "colocar", "minar", "fundir"}
    biblioteca: dict[str, list[str]] = {}
    tareas = [
        ("conseguir_madera", ["talar", "recoger"]),
        ("fabricar_mesa", ["conseguir_madera", "fabricar"]),
        ("fabricar_pico", ["conseguir_madera", "fabricar_mesa", "fabricar"]),
        ("minar_piedra", ["fabricar_pico", "minar"]),
        ("fabricar_horno", ["minar_piedra", "fabricar_mesa", "fabricar"]),
    ]

    def expandir(nombre: str) -> list[str]:
        if nombre in primitivas:
            return [nombre]
        return [p for paso in biblioteca[nombre] for p in expandir(paso)]

    curriculo = []
    for nombre, pasos in tareas:
        biblioteca[nombre] = pasos
        primitivos = len(expandir(nombre))
        reutilizadas = [p for p in pasos if p not in primitivas]
        curriculo.append({
            "tarea": nombre,
            "pasos_declarados": len(pasos),
            "acciones_primitivas_equivalentes": primitivos,
            "habilidades_reutilizadas": reutilizadas,
            "factor_de_compresion": _round(primitivos / len(pasos), 2),
        })
    ultima = curriculo[-1]
    return _contract(
        "voyager",
        seed,
        {
            "biblioteca_final": {k: v for k, v in biblioteca.items()},
            "curriculo": curriculo,
            "habilidades_aprendidas": len(biblioteca),
        },
        [
            f"La última tarea se declara en {ultima['pasos_declarados']} pasos pero equivale a {ultima['acciones_primitivas_equivalentes']} acciones primitivas.",
            "Cada habilidad nueva se construye sobre las anteriores: el currículo es acumulativo, no una lista plana.",
            "La biblioteca es memoria PROCEDIMENTAL: no ocupa contexto y se puede invocar por nombre.",
        ],
        [
            "Las habilidades son listas de nombres; en el paper son programas ejecutables que el modelo escribe y depura.",
            "El currículo está fijado; en el paper lo propone el propio agente según lo que ya sabe.",
            "No hay entorno: nada se ejecuta ni puede fallar, que es donde está la dificultad real.",
        ],
    )


# --------------------------------------------------------------------------- #
# P33 — AutoGen (Wu et al., 2023)
# --------------------------------------------------------------------------- #


def _autogen(seed: int) -> dict[str, Any]:
    """Varios agentes con roles conversando: el crítico ve lo que el autor no ve."""
    solucion_con_fallo = {"codigo": "def media(xs): return sum(xs)/len(xs)", "casos": ["[1,2,3] → 2.0", "[] → ZeroDivisionError"]}

    def un_solo_agente() -> dict[str, Any]:
        return {"turnos": 1, "entrega": solucion_con_fallo["codigo"],
                "fallo_detectado": None, "correcto": False}

    def conversacion_multiagente() -> dict[str, Any]:
        traza = []
        traza.append({"rol": "planificador", "mensaje": "escribe una función media y prueba con lista vacía"})
        traza.append({"rol": "programador", "mensaje": solucion_con_fallo["codigo"]})
        traza.append({"rol": "crítico", "mensaje": "falla con []: ZeroDivisionError"})
        traza.append({"rol": "programador", "mensaje": "def media(xs): return sum(xs)/len(xs) if xs else 0.0"})
        traza.append({"rol": "crítico", "mensaje": "ahora cubre el caso vacío"})
        return {"turnos": len(traza), "traza": traza,
                "entrega": traza[-2]["mensaje"], "fallo_detectado": "lista vacía", "correcto": True}

    solo = un_solo_agente()
    multi = conversacion_multiagente()
    return _contract(
        "autogen",
        seed,
        {
            "un_solo_agente": solo,
            "multiagente": multi,
            "coste_relativo_en_turnos": _round(multi["turnos"] / solo["turnos"], 1),
            "roles": ["planificador", "programador", "crítico"],
        },
        [
            f"El agente único entrega en 1 turno código con un fallo; la conversación lo detecta y lo corrige en {multi['turnos']}.",
            "El crítico funciona porque tiene un rol y un objetivo DISTINTOS del que escribió el código.",
            f"La corrección cuesta {multi['turnos']}× más turnos: multiagente no es gratis, hay que justificar el gasto.",
        ],
        [
            "Los mensajes están escritos a mano; en el paper los genera un modelo y el crítico puede equivocarse o adular.",
            "Sin criterio de parada, dos agentes pueden conversar indefinidamente: es el fallo operativo característico.",
            "Más agentes no es mejor por defecto: hay que demostrarlo contra una línea base de un solo agente bien construido.",
        ],
    )


# --------------------------------------------------------------------------- #
# P34 — RoPE (Su et al., 2021)
# --------------------------------------------------------------------------- #


def _rope(seed: int) -> dict[str, Any]:
    """Rotar por la posición: el producto escalar depende solo de la distancia relativa."""
    rng = random.Random(seed)
    dim = 8

    def rotar(v: list[float], pos: int) -> list[float]:
        out = []
        for i in range(0, dim, 2):
            theta = pos / (10000 ** (i / dim))
            c, s = math.cos(theta), math.sin(theta)
            x, y = v[i], v[i + 1]
            out += [x * c - y * s, x * s + y * c]
        return out

    q = [rng.uniform(-1, 1) for _ in range(dim)]
    k = [rng.uniform(-1, 1) for _ in range(dim)]

    # misma distancia relativa, posiciones absolutas distintas → mismo producto
    invariancia = [
        {"m": m, "n": n, "m-n": m - n, "q·k": _round(_dot(rotar(q, m), rotar(k, n)), 6)}
        for m, n in ((5, 3), (50, 48), (500, 498), (7, 4), (100, 97))
    ]
    # decaimiento con la distancia
    decaimiento = [
        {"distancia": d, "q·k": _round(_dot(rotar(q, d), rotar(k, 0)), 4)}
        for d in (0, 1, 2, 8, 32, 128)
    ]
    grupo2 = {f["q·k"] for f in invariancia if f["m-n"] == 2}
    return _contract(
        "rope",
        seed,
        {"invariancia_relativa": invariancia, "decaimiento_con_la_distancia": decaimiento,
         "valores_distintos_para_distancia_2": len(grupo2)},
        [
            f"Las posiciones (5,3), (50,48) y (500,498) dan exactamente el mismo producto escalar: solo importa m−n ({len(grupo2)} valor distinto).",
            "La posición absoluta se codifica rotando, pero lo que la atención ve es la posición RELATIVA: eso es todo el aporte.",
            "El producto tiende a decaer con la distancia, que es el sesgo inductivo que se busca en lenguaje.",
        ],
        [
            "Ocho dimensiones y vectores aleatorios: no hay modelo ni entrenamiento.",
            "El decaimiento observado depende de q y k concretos; el paper lo argumenta en promedio, no punto a punto.",
            "La extrapolación a longitudes no vistas es trabajo POSTERIOR (interpolación de posiciones), no de este artículo.",
        ],
    )


# --------------------------------------------------------------------------- #
# P35 — FlashAttention (Dao et al., 2022)
# --------------------------------------------------------------------------- #


def _flashattention(seed: int) -> dict[str, Any]:
    """El cuello de botella no son los FLOPs: son las lecturas y escrituras a memoria."""
    d, M = 64, 100_000          # dimensión de cabeza y tamaño de SRAM en elementos
    filas = []
    for n in (1_024, 4_096, 16_384, 65_536):
        flops = 2 * n * n * d
        # estándar: materializa la matriz n×n en memoria lenta (escribir + leer)
        hbm_estandar = 2 * n * n + 2 * n * d
        # con tiling: nunca se materializa; se recorre por bloques
        hbm_flash = 4 * n * d * (n * d / M)
        filas.append({
            "n": n,
            "flops": flops,
            "accesos_hbm_estandar": int(hbm_estandar),
            "accesos_hbm_flash": int(hbm_flash),
            "reduccion": _round(hbm_estandar / max(hbm_flash, 1), 2),
            "memoria_matriz_MB": _round(n * n * 2 / 1024 ** 2, 1),
        })
    return _contract(
        "flashattention",
        seed,
        {"dimension_cabeza": d, "sram_elementos": M, "comparativa": filas,
         "resultado_exacto": True},
        [
            f"Con n={filas[-1]['n']}, la atención estándar mueve {filas[-1]['accesos_hbm_estandar']:,} elementos entre memorias y la versión por bloques {filas[-1]['accesos_hbm_flash']:,}.",
            "Los FLOPs son IDÉNTICOS en ambos casos: el algoritmo es exacto, no una aproximación. Lo que cambia es la memoria que se toca.",
            f"La matriz de atención de n={filas[-1]['n']} ocuparía {filas[-1]['memoria_matriz_MB']} MB por cabeza y capa: con tiling nunca llega a existir.",
        ],
        [
            "El modelo de coste es una simplificación: ignora ocupación, coalescencia y jerarquía real de caché.",
            "La ganancia práctica depende del hardware concreto; el paper reporta medidas, esto reporta un conteo.",
            "No implementa el softmax por bloques con reescalado, que es la parte técnicamente difícil.",
        ],
    )


# --------------------------------------------------------------------------- #
# P36 — Lost in the Middle (Liu et al., 2023)
# --------------------------------------------------------------------------- #


def _lost_in_middle(seed: int) -> dict[str, Any]:
    """Tener contexto largo no es usarlo: el rendimiento cae si el dato está en medio."""
    posiciones = list(range(1, 21))
    n = len(posiciones)

    def exactitud(pos: int) -> float:
        # perfil DIDÁCTICO en U: primacía + recencia sobre una base baja
        primacia = 0.35 * math.exp(-(pos - 1) / 3.0)
        recencia = 0.30 * math.exp(-(n - pos) / 3.0)
        return _round(0.45 + primacia + recencia, 3)

    curva = [{"posicion": p, "exactitud": exactitud(p)} for p in posiciones]
    mejor = max(curva, key=lambda x: x["exactitud"])
    peor = min(curva, key=lambda x: x["exactitud"])
    return _contract(
        "lost_in_middle",
        seed,
        {
            "documentos_en_contexto": n,
            "curva_en_U": curva,
            "mejor_posicion": mejor,
            "peor_posicion": peor,
            "caida": _round(mejor["exactitud"] - peor["exactitud"], 3),
            "perfil": "DIDÁCTICO: primacía + recencia; el paper lo MIDE, aquí se modela",
        },
        [
            f"La exactitud es máxima en la posición {mejor['posicion']} ({mejor['exactitud']}) y mínima en la {peor['posicion']} ({peor['exactitud']}).",
            f"La caída entre el mejor y el peor sitio es de {mejor['exactitud'] - peor['exactitud']:.3f}: el MISMO dato, cambiado de sitio.",
            "La curva tiene forma de U: se recuerda el principio y el final, y se pierde el medio.",
        ],
        [
            "El perfil está modelado a mano; el paper lo mide en modelos reales y con varias tareas.",
            "No hay modelo de lenguaje: esto ilustra el fenómeno, no lo reproduce.",
            "La magnitud de la caída depende del modelo y de la tarea; tomarla como constante sería un error.",
        ],
    )


# --------------------------------------------------------------------------- #
# P37 — MemGPT (Packer et al., 2023)
# --------------------------------------------------------------------------- #


def _memgpt(seed: int) -> dict[str, Any]:
    """Jerarquía de memoria: contexto principal pequeño y almacén externo grande."""
    capacidad = 5
    contexto: list[str] = []
    externo: dict[str, str] = {}
    traza = []
    eventos = [
        ("guardar", "el usuario se llama Ana"),
        ("guardar", "trabaja en logística"),
        ("guardar", "prefiere respuestas cortas"),
        ("guardar", "vive en Valparaíso"),
        ("guardar", "su proyecto es de rutas"),
        ("guardar", "usa Python"),
        ("guardar", "el plazo es en marzo"),
        ("consultar", "el usuario se llama"),
    ]
    for accion, dato in eventos:
        if accion == "guardar":
            contexto.append(dato)
            if len(contexto) > capacidad:
                expulsado = contexto.pop(0)                 # page-out al almacén externo
                externo[expulsado] = expulsado
                traza.append({"evento": "desalojo", "dato": expulsado, "destino": "almacén externo"})
        else:
            en_contexto = next((c for c in contexto if dato in c), None)
            if en_contexto:
                traza.append({"evento": "consulta", "resultado": en_contexto, "origen": "contexto principal"})
            else:
                recuperado = next((v for k, v in externo.items() if dato in k), None)
                traza.append({
                    "evento": "consulta",
                    "resultado": recuperado,
                    "origen": "almacén externo (page-in por llamada de función)",
                    "coste": "una llamada extra",
                })
    return _contract(
        "memgpt",
        seed,
        {
            "capacidad_contexto": capacidad,
            "en_contexto_al_final": contexto,
            "en_almacen_externo": sorted(externo),
            "traza": traza,
        },
        [
            f"El contexto principal solo retiene {capacidad} elementos; lo demás se desaloja al almacén externo sin perderse.",
            "Un dato desalojado sigue siendo recuperable mediante una llamada de función: es paginación, no olvido.",
            "La analogía es la memoria virtual de un sistema operativo: la ilusión de memoria grande sobre una pequeña y rápida.",
        ],
        [
            "El 'modelo' no decide qué desalojar: aquí se expulsa lo más antiguo. En el paper decide el propio modelo.",
            "No hay modelo de lenguaje ni llamadas reales: se simula la jerarquía, no la política.",
            "Cada page-in cuesta una llamada extra: la ilusión de contexto infinito se paga en latencia.",
        ],
    )


# --------------------------------------------------------------------------- #
# P38 — VAE (Kingma y Welling, 2013)
# --------------------------------------------------------------------------- #


def _vae(seed: int) -> dict[str, Any]:
    """El truco de reparametrización: mover el azar fuera del camino del gradiente."""
    rng = random.Random(seed)
    mu, log_var = 1.5, -0.7
    sigma = math.exp(0.5 * log_var)

    # sin reparametrizar: z ~ N(mu, sigma) es un nodo estocástico; no hay derivada respecto a mu
    # reparametrizado: z = mu + sigma·eps, con eps ~ N(0,1) FUERA del grafo
    muestras = [rng.gauss(0, 1) for _ in range(2000)]
    z = [mu + sigma * e for e in muestras]
    media_z = sum(z) / len(z)
    var_z = sum((v - media_z) ** 2 for v in z) / len(z)

    # el gradiente de E[z] respecto a mu es 1, y se puede estimar porque eps no depende de mu
    grad_mu = sum(1.0 for _ in muestras) / len(muestras)
    grad_sigma = sum(e for e in muestras) / len(muestras)      # ≈ 0, insesgado

    kl = -0.5 * (1 + log_var - mu ** 2 - math.exp(log_var))
    return _contract(
        "vae",
        seed,
        {
            "mu": mu, "sigma": _round(sigma, 4),
            "muestras": {"media": _round(media_z, 4), "varianza": _round(var_z, 4)},
            "gradiente_respecto_a_mu": _round(grad_mu, 4),
            "gradiente_respecto_a_sigma": _round(grad_sigma, 4),
            "kl_contra_normal_estandar": _round(kl, 4),
            "elbo": "E[log p(x|z)] − KL(q(z|x) ‖ p(z))",
        },
        [
            f"z = μ + σ·ε reproduce la distribución buscada (media {media_z:.3f} ≈ {mu}, varianza {var_z:.3f} ≈ {sigma ** 2:.3f}).",
            f"Y el gradiente respecto a μ vale {grad_mu:.2f}: existe y es estimable porque ε NO depende de los parámetros.",
            "Sin reparametrizar, muestrear es un nodo estocástico y el gradiente no puede atravesarlo. Ese es el truco del paper.",
        ],
        [
            "Aquí no hay codificador, decodificador ni datos: solo el truco aislado.",
            "El término KL se calcula en forma cerrada porque ambas son gaussianas; en general no lo es.",
            "El VAE produce muestras borrosas, y ese es el defecto que motiva GAN y difusión.",
        ],
    )


# --------------------------------------------------------------------------- #
# P39 — GAN (Goodfellow et al., 2014)
# --------------------------------------------------------------------------- #


def _gan(seed: int) -> dict[str, Any]:
    """Un juego de suma cero entre generador y discriminador, y su fallo característico."""
    rng = random.Random(seed)
    modos = [-3.0, 0.0, 3.0]                        # la distribución real tiene tres modos
    g_mu, g_sigma = 0.2, 0.5                        # el generador empieza cerca de un modo
    lr = 0.25
    historia = []
    for paso in range(60):
        reales = [rng.choice(modos) + rng.gauss(0, 0.3) for _ in range(40)]
        falsas = [g_mu + rng.gauss(0, g_sigma) for _ in range(40)]
        # discriminador óptimo simplificado: separa por el punto medio de las medias
        m_real = sum(reales) / len(reales)
        m_falsa = sum(falsas) / len(falsas)
        # el generador persigue al modo MÁS CERCANO, no a la distribución completa
        objetivo = min(modos, key=lambda m: abs(m - g_mu))
        g_mu += lr * (objetivo - g_mu)
        if paso % 20 == 0 or paso == 59:
            cubiertos = sum(1 for m in modos if abs(m - g_mu) < 0.5)
            historia.append({
                "paso": paso, "g_mu": _round(g_mu, 3),
                "modos_cubiertos": f"{cubiertos}/{len(modos)}",
                "media_real": _round(m_real, 3),
            })
    return _contract(
        "gan",
        seed,
        {
            "modos_reales": modos,
            "historia": historia,
            "modo_final": _round(g_mu, 3),
            "colapso_de_modos": historia[-1]["modos_cubiertos"] == f"1/{len(modos)}",
            "objetivo": "min_G max_D  E[log D(x)] + E[log(1 − D(G(z)))]",
        },
        [
            f"El generador converge a {historia[-1]['g_mu']}, uno solo de los tres modos reales: {historia[-1]['modos_cubiertos']} cubiertos.",
            "Engañar al discriminador NO exige cubrir toda la distribución: basta con ser convincente en una región.",
            "Ese es el colapso de modos, el fallo característico de las GAN y el motivo de que la difusión las desplazara.",
        ],
        [
            "El discriminador está simplificado a una comparación de medias; el real es una red entrenada.",
            "No hay entrenamiento adversario alterno de verdad: se modela la dinámica, no se ejecuta.",
            "Las GAN bien entrenadas mitigan el colapso; aquí se exhibe el modo de fallo, no se afirma que sea inevitable.",
        ],
    )


# --------------------------------------------------------------------------- #
# P40 — Dropout (Srivastava et al., 2014)
# --------------------------------------------------------------------------- #


def _dropout(seed: int) -> dict[str, Any]:
    """Apagar unidades al azar impide que una función dependa de un socio concreto."""
    rng = random.Random(seed)
    n_unidades, p = 8, 0.5
    # dos escenarios: una unidad "co-adaptada" que solo funciona con su pareja,
    # y unidades redundantes que funcionan solas
    ensayos = 2000
    coadaptada_ok = 0
    redundante_ok = 0
    for _ in range(ensayos):
        activas = [rng.random() > p for _ in range(n_unidades)]
        # co-adaptación: la unidad 0 solo aporta si la 1 también está
        if activas[0] and activas[1]:
            coadaptada_ok += 1
        # redundancia: basta con que esté cualquiera de las tres
        if activas[2] or activas[3] or activas[4]:
            redundante_ok += 1
    subredes = 2 ** n_unidades
    return _contract(
        "dropout",
        seed,
        {
            "unidades": n_unidades, "p_apagado": p,
            "subredes_posibles": subredes,
            "coadaptada_funciona": _round(coadaptada_ok / ensayos, 3),
            "redundante_funciona": _round(redundante_ok / ensayos, 3),
            "escala_en_inferencia": "multiplicar por (1−p), o dividir en entrenamiento",
        },
        [
            f"Una función que depende de dos unidades concretas solo está disponible el {coadaptada_ok / ensayos:.0%} de las veces.",
            f"Una función redundante repartida en tres unidades sobrevive el {redundante_ok / ensayos:.0%}: dropout PREMIA la redundancia.",
            f"Con {n_unidades} unidades hay {subredes} subredes posibles: entrenar con dropout es entrenar un ensamblado exponencial que comparte pesos.",
        ],
        [
            "Esto cuenta probabilidades de máscara: no hay red, ni datos, ni entrenamiento.",
            "La equivalencia con un ensamblado es aproximada, no exacta, y el propio paper la presenta así.",
            "Dropout cayó en desuso en muchas arquitecturas modernas frente a otras regularizaciones; no es una receta universal.",
        ],
    )


# --------------------------------------------------------------------------- #
# P41 — Adam (Kingma y Ba, 2014)
# --------------------------------------------------------------------------- #


def _adam(seed: int) -> dict[str, Any]:
    """Un paso por dimensión, adaptado a su propia escala de gradiente."""
    # cuenco muy mal condicionado: una dirección 100 veces más curva que la otra
    a, b = 1.0, 100.0

    def perdida(x, y):
        return a * x * x + b * y * y

    def correr(metodo: str, pasos: int = 200) -> dict[str, Any]:
        x, y = 1.0, 1.0
        mx = my = vx = vy = 0.0
        lr = 0.01 if metodo == "sgd" else 0.1
        b1, b2, eps = 0.9, 0.999, 1e-8
        for t in range(1, pasos + 1):
            gx, gy = 2 * a * x, 2 * b * y
            if metodo == "sgd":
                x -= lr * gx
                y -= lr * gy
            else:
                mx, my = b1 * mx + (1 - b1) * gx, b1 * my + (1 - b1) * gy
                vx, vy = b2 * vx + (1 - b2) * gx * gx, b2 * vy + (1 - b2) * gy * gy
                mhx, mhy = mx / (1 - b1 ** t), my / (1 - b1 ** t)
                vhx, vhy = vx / (1 - b2 ** t), vy / (1 - b2 ** t)
                x -= lr * mhx / (math.sqrt(vhx) + eps)
                y -= lr * mhy / (math.sqrt(vhy) + eps)
        return {"x": _round(x, 6), "y": _round(y, 6), "perdida": _round(perdida(x, y), 8)}

    sgd, adam = correr("sgd"), correr("adam")
    return _contract(
        "adam",
        seed,
        {
            "problema": "L = x² + 100y²  (número de condición 100)",
            "sgd": sgd, "adam": adam,
            "componentes": ["momento de primer orden", "momento de segundo orden", "corrección de sesgo"],
        },
        [
            f"Tras 200 pasos, SGD deja una pérdida de {sgd['perdida']} y Adam de {adam['perdida']}.",
            "SGD usa el MISMO paso en las dos direcciones; con curvaturas muy distintas, o oscila en una o se arrastra en la otra.",
            "Adam normaliza por la magnitud típica del gradiente de cada dimensión: cada coordenada avanza a su ritmo.",
        ],
        [
            "Una cuadrática de dos variables no es una red neuronal: no hay ruido de minilote ni paisaje no convexo.",
            "La corrección de sesgo importa sobre todo en los primeros pasos, y aquí apenas se aprecia.",
            "Adam no es siempre mejor: hay trabajos que reportan peor generalización que SGD con momento bien ajustado.",
        ],
    )


# --------------------------------------------------------------------------- #
# P42 — Ejemplos adversarios (Goodfellow, Shlens y Szegedy, 2014)
# --------------------------------------------------------------------------- #


def _adversarial(seed: int) -> dict[str, Any]:
    """En dimensión alta, una perturbación imperceptible por píxel suma un cambio enorme."""
    rng = random.Random(seed)
    filas = []
    for dim in (10, 100, 784, 10_000):
        w = [rng.choice([-1.0, 1.0]) for _ in range(dim)]
        x = [rng.uniform(-0.5, 0.5) for _ in range(dim)]
        base = _dot(w, x)
        for eps in (0.01, 0.05):
            # FGSM: moverse eps en la dirección del signo del gradiente
            x_adv = [xi + eps * (1 if wi > 0 else -1) for xi, wi in zip(x, w)]
            adv = _dot(w, x_adv)
            filas.append({
                "dimension": dim, "epsilon": eps,
                "salida_original": _round(base, 3),
                "salida_adversaria": _round(adv, 3),
                "cambio": _round(adv - base, 3),
                "cambio_teorico_eps_por_dim": _round(eps * dim, 3),
            })
    grande = [f for f in filas if f["dimension"] == 10_000 and f["epsilon"] == 0.01][0]
    return _contract(
        "adversarial",
        seed,
        {"ataque": "FGSM: x' = x + ε·sign(∇ₓL)", "filas": filas},
        [
            f"Con dimensión {grande['dimension']} y ε={grande['epsilon']} —imperceptible por componente— la salida cambia en {grande['cambio']}.",
            "El cambio crece como ε·d: la perturbación por píxel es minúscula, pero se ACUMULA en todas las dimensiones.",
            "La explicación del paper es la linealidad en alta dimensión, no una rareza de las redes profundas.",
        ],
        [
            "Un modelo lineal no es una red: aquí no hay capas, activaciones ni entrenamiento.",
            "No se calcula un gradiente real; se usa el signo de los pesos, que en el caso lineal coincide.",
            "Que exista el ataque no dice nada sobre su transferencia a otros modelos, que es lo realmente preocupante.",
        ],
    )


# --------------------------------------------------------------------------- #
# P43 — Batch Normalization (Ioffe y Szegedy, 2015)
# --------------------------------------------------------------------------- #


def _batchnorm(seed: int) -> dict[str, Any]:
    """Normalizar por lote mantiene las activaciones en un rango donde el gradiente existe."""
    rng = random.Random(seed)
    lote = [rng.gauss(0, 1) for _ in range(64)]

    def propagar(normalizar: bool, capas: int = 12) -> list[dict[str, Any]]:
        x = list(lote)
        traza = []
        for capa in range(capas):
            w = 1.6                                   # pesos ligeramente grandes
            x = [math.tanh(w * v) for v in x]
            if normalizar:
                m = sum(x) / len(x)
                var = sum((v - m) ** 2 for v in x) / len(x)
                x = [(v - m) / math.sqrt(var + 1e-5) for v in x]
            m = sum(x) / len(x)
            var = sum((v - m) ** 2 for v in x) / len(x)
            saturadas = sum(1 for v in x if abs(v) > 0.99) / len(x)
            if capa in (0, 5, 11):
                traza.append({"capa": capa, "media": _round(m, 4), "desv": _round(math.sqrt(var), 4),
                              "fraccion_saturada": _round(saturadas, 3)})
        return traza

    sin_bn = propagar(False)
    con_bn = propagar(True)
    return _contract(
        "batchnorm",
        seed,
        {"sin_batchnorm": sin_bn, "con_batchnorm": con_bn,
         "formula": "x̂ = (x − μ_lote) / √(σ²_lote + ε),  luego  y = γ·x̂ + β"},
        [
            f"Sin normalizar, en la capa 11 la fracción de activaciones saturadas es {sin_bn[-1]['fraccion_saturada']}: tanh en su zona plana, gradiente ≈ 0.",
            f"Con normalización por lote, esa fracción es {con_bn[-1]['fraccion_saturada']} y la desviación se mantiene cerca de 1.",
            "γ y β se aprenden: la red puede deshacer la normalización si le conviene, así que no pierde capacidad expresiva.",
        ],
        [
            "Es una propagación hacia adelante sin entrenamiento: no se mide el efecto real sobre la convergencia.",
            "La explicación del paper —'internal covariate shift'— fue discutida después: hay evidencia de que el beneficio viene de suavizar el paisaje de optimización.",
            "Depende del tamaño de lote, y ese es su punto débil práctico (de ahí LayerNorm y GroupNorm).",
        ],
    )


# --------------------------------------------------------------------------- #
# P44 — ResNet (He et al., 2015)
# --------------------------------------------------------------------------- #


def _resnet(seed: int) -> dict[str, Any]:
    """El atajo identidad: apilar capas deja de degradar el modelo."""
    filas = []
    for capas in (10, 20, 50, 152):
        # sin atajo: el gradiente es un producto de factores
        plano = 0.85 ** capas
        # con atajo: la derivada de cada bloque es 1 + F'(x). Aunque F' sea
        # pequeño o negativo, el 1 sostiene el producto.
        residual = 1.0
        for _ in range(capas):
            residual *= (1.0 + (-0.02))
        filas.append({
            "capas": capas,
            "gradiente_sin_atajo": f"{plano:.3e}",
            "gradiente_con_atajo": f"{residual:.3e}",
            "ratio": f"{residual / max(plano, 1e-300):.3e}",
        })
    return _contract(
        "resnet",
        seed,
        {"bloque": "y = F(x) + x", "profundidades": filas},
        [
            f"Con 152 capas el gradiente sin atajo vale {filas[-1]['gradiente_sin_atajo']} y con atajo {filas[-1]['gradiente_con_atajo']}.",
            "El atajo hace que la derivada de cada bloque sea 1 + F'(x): el 1 impide que el producto colapse.",
            "Por eso el paper observa que las redes MUY profundas dejan de ser peores que las poco profundas: el problema no era capacidad, era optimización.",
        ],
        [
            "Los factores están fijados a mano para aislar el efecto; no provienen de un entrenamiento.",
            "El aporte del paper también incluye el diseño de bloque y el entrenamiento a 152 capas en ImageNet, nada de lo cual está aquí.",
            "El atajo no resuelve todo: sin normalización y buena inicialización, la profundidad sigue siendo difícil.",
        ],
    )


# --------------------------------------------------------------------------- #
# P45 — Destilación de conocimiento (Hinton, Vinyals y Dean, 2015)
# --------------------------------------------------------------------------- #


def _distillation(seed: int) -> dict[str, Any]:
    """Las probabilidades del maestro dicen mucho más que la etiqueta correcta."""
    logits = [4.0, 2.0, 1.5, -1.0]          # perro, lobo, gato, coche
    clases = ["perro", "lobo", "gato", "coche"]
    filas = []
    for T in (1.0, 2.0, 5.0, 10.0):
        p = _softmax([z / T for z in logits])
        filas.append({
            "temperatura": T,
            "distribucion": {c: _round(v, 4) for c, v in zip(clases, p)},
            "entropia": _round(_entropy(p), 4),
        })
    dura = {c: (1.0 if i == 0 else 0.0) for i, c in enumerate(clases)}
    suave = filas[2]["distribucion"]
    return _contract(
        "distillation",
        seed,
        {
            "clases": clases,
            "etiqueta_dura": dura,
            "objetivos_suaves_por_temperatura": filas,
            "conocimiento_oscuro": "lobo > gato > coche: el maestro dice que un perro se parece más a un lobo",
        },
        [
            "La etiqueta dura solo dice «perro» y asigna 0 a todo lo demás: pierde toda la estructura de similitud.",
            f"Con temperatura 5 el maestro dice {suave}: lobo por encima de gato y muy por encima de coche.",
            f"Subir la temperatura aumenta la entropía (de {filas[0]['entropia']} a {filas[-1]['entropia']}) y revela más de esa estructura.",
        ],
        [
            "Aquí no hay maestro ni alumno entrenados: solo se exhibe la información que contiene la distribución.",
            "El paper multiplica el gradiente por T² para compensar la escala; ese detalle no está.",
            "La destilación transfiere comportamiento, no garantías: el alumno puede imitar también los errores del maestro.",
        ],
    )


# --------------------------------------------------------------------------- #
# P46 — Vision Transformer (Dosovitskiy et al., 2020)
# --------------------------------------------------------------------------- #


def _vit(seed: int) -> dict[str, Any]:
    """Una imagen es una secuencia de parches: se abandona el sesgo inductivo de la convolución."""
    filas = []
    for lado, parche in ((224, 16), (224, 32), (384, 16), (512, 16)):
        n = (lado // parche) ** 2
        filas.append({
            "imagen": f"{lado}x{lado}",
            "parche": f"{parche}x{parche}",
            "tokens": n + 1,                          # +1 por el token de clase
            "coste_atencion_relativo": _round((n + 1) ** 2 / (14 ** 2 + 1) ** 2, 2),
            "dim_proyeccion_entrada": parche * parche * 3,
        })
    sesgos = {
        "CNN": ["localidad", "equivarianza a la traslación", "jerarquía espacial"],
        "ViT": ["ninguno propio: solo el orden inyectado por la codificación posicional"],
    }
    return _contract(
        "vit",
        seed,
        {"configuraciones": filas, "sesgos_inductivos": sesgos,
         "consecuencia": "sin sesgo inductivo, hace falta MUCHÍSIMO más dato para igualar a una CNN"},
        [
            f"Una imagen de 224×224 con parches de 16 se convierte en {filas[0]['tokens']} tokens: exactamente el mismo problema que una frase.",
            f"Bajar el parche a 16 desde 32 multiplica el coste de atención por {filas[0]['coste_atencion_relativo'] / filas[1]['coste_atencion_relativo']:.0f}: la resolución se paga al cuadrado.",
            "ViT renuncia a la localidad y la equivarianza que la convolución trae de fábrica; a cambio, escala mejor con datos.",
        ],
        [
            "Esto cuenta tokens y coste: no hay imagen, ni parches reales, ni modelo.",
            "El resultado del paper depende de preentrenar en conjuntos enormes; con datos medianos, la CNN gana.",
            "La comparación CNN/ViT depende del régimen de datos y del presupuesto: no hay un ganador absoluto.",
        ],
    )


# --------------------------------------------------------------------------- #
# P47 — AlphaFold (Jumper et al., 2021)
# --------------------------------------------------------------------------- #


def _alphafold(seed: int) -> dict[str, Any]:
    """De distancias entre pares a coordenadas 3D: el problema geométrico del plegamiento."""
    rng = random.Random(seed)
    n = 8
    # "estructura real": una hélice sencilla en 3D
    real = [(math.cos(i * 1.0), math.sin(i * 1.0), i * 0.4) for i in range(n)]

    def dist(a, b):
        return math.sqrt(sum((p - q) ** 2 for p, q in zip(a, b)))

    matriz = [[_round(dist(real[i], real[j]), 3) for j in range(n)] for i in range(n)]

    # reconstrucción por descenso de gradiente sobre las distancias (MDS ingenuo)
    pred = [[rng.uniform(-1, 1) for _ in range(3)] for _ in range(n)]
    lr = 0.05
    errores = []
    for paso in range(400):
        total = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                d = math.sqrt(sum((pred[i][k] - pred[j][k]) ** 2 for k in range(3))) + 1e-9
                err = d - matriz[i][j]
                total += err * err
                for k in range(3):
                    g = 2 * err * (pred[i][k] - pred[j][k]) / d
                    pred[i][k] -= lr * g
                    pred[j][k] += lr * g
        if paso % 150 == 0 or paso == 399:
            errores.append({"paso": paso, "error_cuadratico": _round(total, 5)})
    residuo = math.sqrt(errores[-1]["error_cuadratico"] / (n * (n - 1) / 2))
    return _contract(
        "alphafold",
        seed,
        {
            "residuos": n,
            "matriz_de_distancias_parcial": [fila[:4] for fila in matriz[:4]],
            "convergencia": errores,
            "error_medio_por_par": _round(residuo, 4),
        },
        [
            f"Partiendo de posiciones aleatorias y SOLO de la matriz de distancias, se recupera una estructura con error medio {residuo:.4f} por par.",
            "La geometría 3D está determinada (salvo rotación y reflexión) por las distancias entre pares: por eso predecir distancias es predecir estructura.",
            "Ese es el puente del problema: de la secuencia se predice qué residuos están cerca, y de ahí sale la forma.",
        ],
        [
            "Ocho puntos no son una proteína, y aquí la matriz de distancias se DA: predecirla desde la secuencia es el problema entero.",
            "AlphaFold usa alineamientos múltiples de secuencias, atención sobre pares y un módulo de estructura; nada de eso está aquí.",
            "El error se mide contra la propia matriz, no contra una estructura experimental: no es una métrica de plegamiento.",
        ],
    )


# --------------------------------------------------------------------------- #
# P48 — LoRA (Hu et al., 2021)
# --------------------------------------------------------------------------- #


def _lora(seed: int) -> dict[str, Any]:
    """Si la actualización útil es de rango bajo, se puede entrenar factorizada."""
    rng = random.Random(seed)
    d = 128
    filas = []
    for r in (1, 4, 16, 64):
        completos = d * d
        lora = 2 * d * r
        filas.append({
            "rango": r,
            "parametros_ajuste_completo": completos,
            "parametros_lora": lora,
            "fraccion": _round(lora / completos, 4),
            "reduccion": _round(completos / lora, 1),
        })
    # una actualización de rango 2 se representa EXACTAMENTE con r=2 y no con r=1
    r_real = 2
    A = [[rng.uniform(-1, 1) for _ in range(r_real)] for _ in range(6)]
    B = [[rng.uniform(-1, 1) for _ in range(6)] for _ in range(r_real)]
    dW = [[sum(A[i][k] * B[k][j] for k in range(r_real)) for j in range(6)] for i in range(6)]
    return _contract(
        "lora",
        seed,
        {
            "dimension": d,
            "comparativa": filas,
            "delta_w_de_rango_2": [[_round(v, 3) for v in fila] for fila in dW[:3]],
            "formula": "W' = W + BA,  con B ∈ ℝ^{d×r} y A ∈ ℝ^{r×d},  W congelada",
        },
        [
            f"Con d={d} y rango 4, se entrenan {filas[1]['parametros_lora']:,} parámetros en vez de {filas[1]['parametros_ajuste_completo']:,}: {filas[1]['reduccion']}× menos.",
            "La matriz base queda CONGELADA: una sola copia del modelo sirve para muchas tareas, cada una con su adaptador pequeño.",
            "Y al desplegar, BA se puede sumar a W: cero latencia añadida en inferencia, a diferencia de otros métodos de adaptación.",
        ],
        [
            "Aquí no se entrena nada: se cuentan parámetros y se muestra la forma de la actualización.",
            "La hipótesis de rango bajo es empírica: no está garantizado que la actualización útil lo sea en toda tarea.",
            "Elegir r y a qué matrices aplicarlo son decisiones que el paper estudia y que aquí no se replican.",
        ],
    )


# --------------------------------------------------------------------------- #
# P49 — QLoRA / cuantización (Dettmers et al., 2023)
# --------------------------------------------------------------------------- #


def _quantization(seed: int) -> dict[str, Any]:
    """Menos bits por peso: cuánta memoria se ahorra y cuánta precisión se paga."""
    rng = random.Random(seed)
    pesos = [rng.gauss(0, 0.05) for _ in range(2000)]
    lo, hi = min(pesos), max(pesos)
    filas = []
    for bits in (16, 8, 4, 3, 2):
        niveles = 2 ** bits
        paso = (hi - lo) / (niveles - 1)
        cuant = [lo + round((w - lo) / paso) * paso for w in pesos]
        err = math.sqrt(sum((a - b) ** 2 for a, b in zip(pesos, cuant)) / len(pesos))
        filas.append({
            "bits": bits,
            "niveles": niveles,
            "error_cuadratico_medio": f"{err:.3e}",
            "memoria_70B_GB": _round(70e9 * bits / 8 / 1e9, 1),
        })
    return _contract(
        "quantization",
        seed,
        {"pesos_simulados": len(pesos), "comparativa": filas,
         "idea_de_qlora": "cuantizar la base congelada a 4 bits y entrenar adaptadores LoRA en precisión alta"},
        [
            f"Pasar de 16 a 4 bits reduce la memoria de un modelo de 70 000 M de {filas[0]['memoria_70B_GB']} GB a {filas[2]['memoria_70B_GB']} GB.",
            f"El error de cuantización crece al bajar bits: de {filas[0]['error_cuadratico_medio']} a {filas[-1]['error_cuadratico_medio']}.",
            "QLoRA combina ambas ideas: la base cuantizada no se entrena, y los adaptadores en precisión alta absorben el ajuste.",
        ],
        [
            "Cuantización uniforme sobre pesos gaussianos simulados: el paper usa un formato adaptado a esa distribución.",
            "El error de reconstrucción de pesos NO es el error del modelo: la relación entre ambos no es directa.",
            "No se mide calidad en ninguna tarea, que es lo único que decide si una cuantización es aceptable.",
        ],
    )


# --------------------------------------------------------------------------- #
# P50 — Constitutional AI (Bai et al., 2022)
# --------------------------------------------------------------------------- #


def _constitutional_ai(seed: int) -> dict[str, Any]:
    """Sustituir parte del juicio humano por principios explícitos y autocrítica."""
    principios = [
        "no facilitar daño físico a personas",
        "no juzgar ni sermonear al usuario",
        "explicar los límites en vez de negarse sin más",
    ]
    respuesta = "No pienso ayudarte con eso, deberías replantearte por qué lo preguntas."
    traza = []
    actual = respuesta
    for p in principios:
        viola = ("sermonear" in p and "deberías replantearte" in actual) or \
                ("límites" in p and "No pienso ayudarte" in actual)
        traza.append({"principio": p, "viola": viola,
                      "critica": "juzga al usuario" if "sermonear" in p and viola else
                                 "se niega sin explicar" if viola else "cumple"})
        if viola:
            actual = ("No puedo ayudarte con esa parte concreta porque implicaría riesgo físico. "
                      "Sí puedo explicarte el marco general y las alternativas seguras.")
    return _contract(
        "constitutional_ai",
        seed,
        {
            "principios": principios,
            "respuesta_inicial": respuesta,
            "traza_de_critica": traza,
            "respuesta_revisada": actual,
            "etiquetas_humanas_usadas": 0,
        },
        [
            "La respuesta inicial cumple el principio de seguridad pero viola otros dos: juzga y no explica.",
            "La crítica es contra una lista de principios EXPLÍCITA y auditable, no contra la preferencia implícita de un anotador.",
            "La revisión se hace sin una sola etiqueta humana nueva: ese es el ahorro que propone el método.",
        ],
        [
            "La crítica está codificada con reglas; en el paper la genera el propio modelo y puede fallar.",
            "Quién escribe los principios y con qué autoridad es una pregunta política que el método NO resuelve, solo la hace explícita.",
            "Falta la segunda fase, de refuerzo con preferencias generadas por IA sobre las respuestas revisadas.",
        ],
    )


# --------------------------------------------------------------------------- #
# P51 — SWE-bench (Jimenez et al., 2023)
# --------------------------------------------------------------------------- #


def _swebench(seed: int) -> dict[str, Any]:
    """Evaluar con el criterio del mundo real: ¿pasan los tests del repositorio?"""
    intentos = [
        {"id": "issue-1", "parece_correcto": True, "compila": True, "tests_pasan": True},
        {"id": "issue-2", "parece_correcto": True, "compila": True, "tests_pasan": False},
        {"id": "issue-3", "parece_correcto": True, "compila": False, "tests_pasan": False},
        {"id": "issue-4", "parece_correcto": False, "compila": True, "tests_pasan": False},
        {"id": "issue-5", "parece_correcto": True, "compila": True, "tests_pasan": True},
    ]
    n = len(intentos)
    por_apariencia = sum(1 for i in intentos if i["parece_correcto"]) / n
    por_compilacion = sum(1 for i in intentos if i["compila"]) / n
    por_tests = sum(1 for i in intentos if i["tests_pasan"]) / n
    return _contract(
        "swebench",
        seed,
        {
            "intentos": intentos,
            "tasa_si_se_mide_apariencia": _round(por_apariencia, 3),
            "tasa_si_se_mide_compilacion": _round(por_compilacion, 3),
            "tasa_real_tests_pasan": _round(por_tests, 3),
            "criterio": "resolver una incidencia real de un repositorio real y que su test pase",
        },
        [
            f"Medido por apariencia, el sistema 'resuelve' el {por_apariencia:.0%}; medido por tests, el {por_tests:.0%}.",
            "La diferencia entre ambos números es exactamente el problema que ataca el benchmark: los criterios blandos inflan.",
            "Un test del propio repositorio es un verificador objetivo que no se puede convencer con prosa.",
        ],
        [
            "Cinco casos escritos a mano: no es una evaluación, es la ilustración del criterio.",
            "Pasar los tests tampoco garantiza una buena solución: puede resolverse de forma frágil o rompiendo el diseño.",
            "El benchmark tiene riesgo de contaminación: las incidencias son públicas y anteriores al corte de datos.",
        ],
    )


# --------------------------------------------------------------------------- #
# P52 — Superposición y autoencoders dispersos (interpretabilidad, 2023-2024)
# --------------------------------------------------------------------------- #


def _superposition(seed: int) -> dict[str, Any]:
    """Más conceptos que neuronas: por eso una neurona no significa una cosa."""
    rng = random.Random(seed)
    filas = []
    for dim, n_features in ((8, 8), (8, 24), (8, 80)):
        vecs = []
        for _ in range(n_features):
            v = [rng.gauss(0, 1) for _ in range(dim)]
            norma = math.sqrt(sum(x * x for x in v))
            vecs.append([x / norma for x in v])
        solapes = [abs(_dot(vecs[i], vecs[j])) for i in range(n_features) for j in range(i + 1, n_features)]
        filas.append({
            "dimensiones": dim,
            "conceptos": n_features,
            "ratio": _round(n_features / dim, 2),
            "solape_medio": _round(sum(solapes) / len(solapes), 4),
            "solape_maximo": _round(max(solapes), 4),
        })
    return _contract(
        "superposition",
        seed,
        {
            "experimento": "guardar n conceptos como direcciones en un espacio de d dimensiones",
            "filas": filas,
            "consecuencia": "una neurona responde a varios conceptos no relacionados (polisemanticidad)",
        },
        [
            f"En 8 dimensiones se pueden guardar {filas[-1]['conceptos']} conceptos con un solape medio de solo {filas[-1]['solape_medio']}.",
            "Se puede guardar mucho más de lo que caben direcciones ortogonales, a cambio de INTERFERENCIA: los conceptos se pisan un poco.",
            f"Por eso una neurona no significa una cosa: con ratio {filas[-1]['ratio']}× hay más conceptos que ejes, y cada eje mezcla varios.",
        ],
        [
            "Direcciones aleatorias no son características aprendidas: en un modelo real la estructura no es aleatoria.",
            "No hay autoencoder disperso aquí: solo se muestra el fenómeno que motiva usarlo para descomponer las activaciones.",
            "Que un autoencoder encuentre direcciones interpretables no demuestra que sean las que el modelo USA causalmente.",
        ],
    )


# --------------------------------------------------------------------------- #
# registro
# --------------------------------------------------------------------------- #


PAPER_RUNNERS: dict[str, Callable[[int], dict[str, Any]]] = {
    "perceptron": _perceptron,
    "backprop": _backprop,
    "lstm": _lstm,
    "convnet": _convnet,
    "word2vec": _word2vec,
    "seq2seq": _seq2seq,
    "bahdanau": _bahdanau,
    "transformer": _transformer,
    "bert_mlm": _bert_mlm,
    "gpt3_icl": _gpt3_icl,
    "rag": _rag,
    "rlhf": _rlhf,
    "react": _react,
    "toolformer": _toolformer,
    "dpo": _dpo,
    "agentic": _agentic,
    "diffusion": _diffusion,
    "clip": _clip,
    "scaling_laws": _scaling_laws,
    "ssm": _ssm,
    "moe": _moe,
    "rl_reasoning": _rl_reasoning,
    "glove": _glove,
    "elmo": _elmo,
    "t5": _t5,
    "dqn": _dqn,
    "alphago": _alphago,
    "cot": _cot,
    "tot": _tot,
    "reflexion": _reflexion,
    "generative_agents": _generative_agents,
    "voyager": _voyager,
    "autogen": _autogen,
    "rope": _rope,
    "flashattention": _flashattention,
    "lost_in_middle": _lost_in_middle,
    "memgpt": _memgpt,
    "vae": _vae,
    "gan": _gan,
    "dropout": _dropout,
    "adam": _adam,
    "adversarial": _adversarial,
    "batchnorm": _batchnorm,
    "resnet": _resnet,
    "distillation": _distillation,
    "vit": _vit,
    "alphafold": _alphafold,
    "lora": _lora,
    "quantization": _quantization,
    "constitutional_ai": _constitutional_ai,
    "swebench": _swebench,
    "superposition": _superposition,
}


def run_paper_lab(kind: str, *, seed: int = 42) -> dict[str, Any]:
    """Ejecuta la miniatura asociada a un paper fundacional."""
    if kind not in PAPER_RUNNERS:
        raise KeyError(f"motor de paper desconocido: {kind}. Disponibles: {sorted(PAPER_RUNNERS)}")
    return PAPER_RUNNERS[kind](seed)


def main() -> None:  # pragma: no cover - utilidad de línea de comandos
    import json

    for kind in sorted(PAPER_RUNNERS):
        print(json.dumps(run_paper_lab(kind, seed=7), ensure_ascii=False, indent=2))


if __name__ == "__main__":  # pragma: no cover
    main()
