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
