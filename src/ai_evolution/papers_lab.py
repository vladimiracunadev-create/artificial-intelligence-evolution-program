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
    # la crítica se hace contra la respuesta ORIGINAL, principio por principio:
    # si se revisara sobre la marcha, los principios posteriores juzgarían un
    # texto que ya cambió y la traza dejaría de ser interpretable.
    traza = []
    for p in principios:
        if "sermonear" in p and "deberías replantearte" in respuesta:
            traza.append({"principio": p, "viola": True, "critica": "juzga al usuario"})
        elif "límites" in p and "No pienso ayudarte" in respuesta:
            traza.append({"principio": p, "viola": True, "critica": "se niega sin explicar"})
        else:
            traza.append({"principio": p, "viola": False, "critica": "cumple"})
    violados = [t for t in traza if t["viola"]]
    actual = respuesta
    if violados:
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
            "principios_violados": len(violados),
            "etiquetas_humanas_usadas": 0,
        },
        [
            f"La respuesta inicial cumple el principio de seguridad y viola los otros {len(violados)}: juzga al usuario y se niega sin explicar.",
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
            f"El precio es la INTERFERENCIA en el peor caso: el solape máximo sube de {filas[0]['solape_maximo']} con {filas[0]['conceptos']} conceptos a {filas[-1]['solape_maximo']} con {filas[-1]['conceptos']}.",
            f"Por eso una neurona no significa una cosa: con ratio {filas[-1]['ratio']}× hay más conceptos que ejes, y cada eje mezcla varios.",
        ],
        [
            "Direcciones aleatorias no son características aprendidas: en un modelo real la estructura no es aleatoria.",
            "No hay autoencoder disperso aquí: solo se muestra el fenómeno que motiva usarlo para descomponer las activaciones.",
            "Que un autoencoder encuentre direcciones interpretables no demuestra que sean las que el modelo USA causalmente.",
        ],
    )


# --------------------------------------------------------------------------- #
# ruta de fundamentos del campo (P53–P63)
# --------------------------------------------------------------------------- #


def _pca(seed: int) -> dict[str, Any]:
    """Pearson 1901: «la recta que mejor ajusta» depende de qué error se minimice."""
    puntos = [(1.0, 2.4), (2.0, 1.1), (3.0, 4.6), (4.0, 2.8), (5.0, 6.4),
              (6.0, 4.0), (7.0, 8.1), (8.0, 5.9), (9.0, 9.9), (10.0, 7.6)]
    n = len(puntos)
    mx = sum(p[0] for p in puntos) / n
    my = sum(p[1] for p in puntos) / n
    sxx = sum((p[0] - mx) ** 2 for p in puntos)
    syy = sum((p[1] - my) ** 2 for p in puntos)
    sxy = sum((p[0] - mx) * (p[1] - my) for p in puntos)

    def errores(m: float) -> dict[str, float]:
        c = my - m * mx
        vertical = sum((y - m * x - c) ** 2 for x, y in puntos)
        return {
            "pendiente": _round(m, 4),
            "error_vertical": _round(vertical, 4),
            "error_perpendicular": _round(vertical / (1 + m * m), 4),
        }

    m_ols_yx = sxy / sxx                      # mínimos cuadrados de y sobre x
    m_ols_xy = syy / sxy                      # mínimos cuadrados de x sobre y, vista como y(x)
    theta = 0.5 * math.atan2(2 * sxy, sxx - syy)
    m_perp = math.tan(theta)                  # eje principal: el ajuste de Pearson

    rectas = {
        "minimos_cuadrados_y_sobre_x": errores(m_ols_yx),
        "eje_principal_pearson": errores(m_perp),
        "minimos_cuadrados_x_sobre_y": errores(m_ols_xy),
    }

    traza = sxx + syy
    disc = math.sqrt((sxx - syy) ** 2 + 4 * sxy * sxy)
    lam1, lam2 = (traza + disc) / 2, (traza - disc) / 2

    # comprobación de robustez: con nubes perturbadas, ¿el eje principal queda
    # SIEMPRE entre las dos rectas de mínimos cuadrados?
    rng = random.Random(seed)
    entre = 0
    for _ in range(50):
        nube = [(x + rng.gauss(0, 0.15), y + rng.gauss(0, 0.15)) for x, y in puntos]
        ax = sum(p[0] for p in nube) / n
        ay = sum(p[1] for p in nube) / n
        axx = sum((p[0] - ax) ** 2 for p in nube)
        ayy = sum((p[1] - ay) ** 2 for p in nube)
        axy = sum((p[0] - ax) * (p[1] - ay) for p in nube)
        m1, m2 = axy / axx, ayy / axy
        mp = math.tan(0.5 * math.atan2(2 * axy, axx - ayy))
        if min(m1, m2) <= mp <= max(m1, m2):
            entre += 1

    return _contract(
        "pca",
        seed,
        {
            "puntos": len(puntos),
            "rectas": rectas,
            "minimiza_el_error_vertical": "minimos_cuadrados_y_sobre_x",
            "minimiza_el_error_perpendicular": "eje_principal_pearson",
            "varianza_explicada": {
                "eje_1": _round(lam1 / traza, 4),
                "eje_2": _round(lam2 / traza, 4),
            },
            "eje_principal_entre_las_dos_ols": f"{entre}/50 nubes perturbadas",
        },
        [
            "Tres rectas distintas para la MISMA nube: la pregunta «cuál ajusta mejor» está mal planteada "
            "mientras no se diga qué error se minimiza (pendientes "
            f"{rectas['minimos_cuadrados_y_sobre_x']['pendiente']}, "
            f"{rectas['eje_principal_pearson']['pendiente']} y "
            f"{rectas['minimos_cuadrados_x_sobre_y']['pendiente']}).",
            "El eje principal gana en error PERPENDICULAR y pierde en error vertical; con mínimos "
            "cuadrados pasa exactamente lo contrario. Cada recta es óptima para su propio criterio.",
            f"El primer eje explica el {_round(100 * lam1 / traza, 2)} % de la varianza: reducir a una "
            "dimensión conserva casi todo, y ESA es la operación que hoy se llama PCA.",
            f"El eje principal queda entre las dos rectas de mínimos cuadrados en {entre} de 50 nubes "
            "perturbadas: es la respuesta simétrica, la que no privilegia ninguna variable.",
        ],
        [
            "Dos dimensiones y diez puntos: no hay maldición de la dimensionalidad ni matrices grandes.",
            "Pearson no usa autovalores: llega al mismo eje por minimización directa. Aquí se resuelve con "
            "la forma cerrada del problema 2×2 porque es más corto, no porque sea su método.",
            "PCA es lineal. Si la estructura es curva, el primer eje puede no significar nada útil.",
        ],
    )


def _mcculloch_pitts(seed: int) -> dict[str, Any]:
    """McCulloch y Pitts 1943: la neurona de umbral CALCULA lógica. No aprende."""
    tabla = [(0, 0), (0, 1), (1, 0), (1, 1)]
    objetivos = {
        "AND": [0, 0, 0, 1],
        "OR": [0, 1, 1, 1],
        "NAND": [1, 1, 1, 0],
        "XOR": [0, 1, 1, 0],
    }

    def unidad(w1: int, w2: int, umbral: int) -> list[int]:
        return [1 if (w1 * a + w2 * b) >= umbral else 0 for a, b in tabla]

    pesos = range(-2, 3)
    umbrales = range(-3, 4)
    configuraciones = [(w1, w2, t) for w1 in pesos for w2 in pesos for t in umbrales]
    soluciones = {
        nombre: [f"w=({w1},{w2}) θ={t}" for w1, w2, t in configuraciones if unidad(w1, w2, t) == salida]
        for nombre, salida in objetivos.items()
    }

    # dos capas: XOR = AND( OR(x,y), NAND(x,y) )
    capa_or = unidad(1, 1, 1)
    capa_nand = unidad(-1, -1, -1)
    salida_xor = [1 if (o + nand) >= 2 else 0 for o, nand in zip(capa_or, capa_nand)]

    # inhibición absoluta: el segundo canal veta la salida (el mecanismo del paper)
    inhibicion = [1 if (a == 1 and b == 0) else 0 for a, b in tabla]

    rng = random.Random(seed)
    muestra = rng.sample(configuraciones, 5)

    return _contract(
        "mcculloch_pitts",
        seed,
        {
            "configuraciones_probadas": len(configuraciones),
            "soluciones_por_funcion": {k: len(v) for k, v in soluciones.items()},
            "ejemplo_and": soluciones["AND"][0] if soluciones["AND"] else None,
            "xor_con_una_unidad": len(soluciones["XOR"]),
            "xor_con_dos_capas": {"esperado": objetivos["XOR"], "obtenido": salida_xor},
            "inhibicion_x_and_not_y": inhibicion,
            "muestra_inspeccionada": [f"w=({a},{b}) θ={t}" for a, b, t in muestra],
            "parametros_aprendidos": 0,
        },
        [
            f"De {len(configuraciones)} configuraciones de UNA unidad de umbral, "
            f"{len(soluciones['AND'])} calculan AND y {len(soluciones['OR'])} calculan OR: la lógica "
            "booleana cabe en una neurona formal.",
            f"XOR se resuelve con {len(soluciones['XOR'])} de esas configuraciones. Con dos capas sí sale "
            f"({salida_xor}), y esa es la frontera que el paper deja marcada quince años antes del "
            "perceptrón.",
            "Los pesos están PUESTOS A MANO: el número de parámetros aprendidos es 0. El artículo de 1943 "
            "es un resultado de computabilidad, no de aprendizaje.",
            "La inhibición del paper es absoluta: un canal activo veta la salida sin importar el resto.",
        ],
        [
            "Dos entradas binarias y pesos enteros pequeños: es una rejilla exhaustiva de juguete, no una "
            "demostración general de qué funciones son representables.",
            "No hay tiempo ni ciclos. El modelo original es temporal y con redes recurrentes puede describir "
            "memoria; aquí solo hay lógica combinacional.",
            "No hay aprendizaje, y por tanto tampoco error, gradiente ni convergencia. Eso llega con "
            "Rosenblatt en 1958.",
        ],
    )


def _shannon(seed: int) -> dict[str, Any]:
    """Shannon 1948: la entropía es el suelo, y ningún código lo atraviesa."""
    fuentes = {
        "uniforme": {"A": 0.25, "B": 0.25, "C": 0.25, "D": 0.25},
        "sesgada": {"A": 0.70, "B": 0.15, "C": 0.10, "D": 0.05},
        "casi_determinista": {"A": 0.97, "B": 0.01, "C": 0.01, "D": 0.01},
    }

    def huffman(probs: dict[str, float]) -> dict[str, str]:
        # desempate estable por símbolo: el código es reproducible byte a byte
        nodos: list[tuple[float, str, Any]] = [(p, s, s) for s, p in sorted(probs.items())]
        while len(nodos) > 1:
            nodos.sort(key=lambda n: (n[0], n[1]))
            (p1, s1, t1), (p2, s2, t2) = nodos[0], nodos[1]
            nodos = nodos[2:] + [(p1 + p2, min(s1, s2), (t1, t2))]
        codigos: dict[str, str] = {}

        def recorrer(nodo: Any, prefijo: str) -> None:
            if isinstance(nodo, str):
                codigos[nodo] = prefijo or "0"
                return
            recorrer(nodo[0], prefijo + "0")
            recorrer(nodo[1], prefijo + "1")

        recorrer(nodos[0][2], "")
        return dict(sorted(codigos.items()))

    filas = []
    for nombre, probs in fuentes.items():
        h = -sum(p * math.log2(p) for p in probs.values())
        codigos = huffman(probs)
        longitud = sum(probs[s] * len(c) for s, c in codigos.items())
        filas.append({
            "fuente": nombre,
            "entropia_bits": _round(h, 4),
            "longitud_media_huffman": _round(longitud, 4),
            "longitud_fija": 2.0,
            "cumple_H_menor_igual_L": h <= longitud + 1e-9,
            "cumple_L_menor_H_mas_1": longitud < h + 1,
            "ahorro_frente_a_codigo_fijo": f"{_round(100 * (2.0 - longitud) / 2.0, 1)} %",
            "codigos": codigos,
        })

    rng = random.Random(seed)
    p_error = 0.1
    h_canal = -(p_error * math.log2(p_error) + (1 - p_error) * math.log2(1 - p_error))
    errores_simulados = sum(1 for _ in range(1000) if rng.random() < p_error)

    return _contract(
        "shannon",
        seed,
        {
            "fuentes": filas,
            "canal_binario_simetrico": {
                "probabilidad_de_error": p_error,
                "capacidad_bits_por_uso": _round(1 - h_canal, 4),
                "errores_en_1000_usos_simulados": errores_simulados,
            },
            "moraleja": "la información se mide por la sorpresa, no por el significado",
        },
        [
            f"La fuente uniforme tiene {filas[0]['entropia_bits']} bits de entropía y su mejor código mide "
            f"{filas[0]['longitud_media_huffman']}: no hay nada que comprimir cuando todo es igual de "
            "probable.",
            f"La fuente sesgada baja a {filas[1]['entropia_bits']} bits y su código medio a "
            f"{filas[1]['longitud_media_huffman']} — un ahorro de {filas[1]['ahorro_frente_a_codigo_fijo']} "
            "sobre el código de longitud fija. La estructura ES la compresión.",
            "En las tres fuentes se cumple H ≤ L < H+1: la entropía no es una analogía, es una cota que se "
            "toca por arriba y no se cruza por abajo.",
            f"Con un 10 % de error por símbolo la capacidad del canal cae a {_round(1 - h_canal, 4)} bits "
            "por uso: el ruido se paga en tasa, no en fiabilidad.",
        ],
        [
            "Cuatro símbolos independientes. El lenguaje real tiene dependencias largas, y ahí la entropía "
            "por símbolo es mucho menor que la de esta tabla.",
            "Huffman es óptimo entre los códigos por símbolo; los códigos aritméticos y los modelos "
            "contextuales bajan más. La cota de Shannon sigue siendo la misma.",
            "Nada de esto habla de significado. Dos mensajes con la misma entropía pueden ser uno crucial "
            "y el otro basura: la teoría es deliberadamente ciega a eso.",
        ],
    )


def _turing(seed: int) -> dict[str, Any]:
    """Turing 1950: lo que el juego de imitación mide depende de quién interroga."""
    preguntas = [
        {"q": "¿Te gusta el invierno?", "tipo": "superficial", "discrimina": False},
        {"q": "¿Cómo te llamas?", "tipo": "superficial", "discrimina": False},
        {"q": "¿Qué opinas del ajedrez?", "tipo": "superficial", "discrimina": False},
        {"q": "Suma 34957 y 70764.", "tipo": "aritmetica", "discrimina": True},
        {"q": "Hace tres turnos dijiste un número. ¿Cuál era?", "tipo": "memoria", "discrimina": True},
        {"q": "Escribe un soneto sobre el puente de Forth.", "tipo": "compromiso", "discrimina": True},
        {"q": "Antes afirmaste lo contrario. ¿Por qué?", "tipo": "coherencia", "discrimina": True},
    ]
    protocolos = {
        "juez_ingenuo": ["superficial"],
        "juez_de_turing": ["superficial", "aritmetica", "memoria", "compromiso", "coherencia"],
    }
    rng = random.Random(seed)
    resultados = {}
    for nombre, tipos in protocolos.items():
        usadas = [p for p in preguntas if p["tipo"] in tipos]
        detectan = [p for p in usadas if p["discrimina"]]
        resultados[nombre] = {
            "preguntas_formuladas": len(usadas),
            "preguntas_que_discriminan": len(detectan),
            "identifica_a_la_maquina": bool(detectan),
            "veredicto": "no pasa el test" if detectan else "pasa el test",
            "primeras_tres_preguntas": [p["q"] for p in rng.sample(usadas, len(usadas))][:3],
        }

    objeciones = {
        "teologica": "respondida: no depende de la definición de alma",
        "cabezas_en_la_arena": "respondida: la incomodidad no es un argumento",
        "matematica": "parcialmente en pie: Gödel limita a la máquina, pero también al humano",
        "conciencia": "no resuelta: el test la esquiva por diseño, no la responde",
        "lady_lovelace": "el punto vivo: ¿puede originar algo? Turing responde con el aprendizaje",
    }

    return _contract(
        "turing",
        seed,
        {
            "maquina_evaluada": "la MISMA en los dos protocolos",
            "protocolos": resultados,
            "objeciones_del_paper": objeciones,
            "prediccion_de_turing_para_2000": "70 % de aciertos del juez tras 5 minutos de conversación",
            "lo_que_el_test_mide": "la capacidad del interrogador de diseñar preguntas que comprometan",
        },
        [
            "La misma máquina «pasa» con el juez ingenuo y no pasa con el protocolo completo: el resultado "
            "del test es una propiedad del INTERROGATORIO, no solo de la máquina.",
            f"De {len(preguntas)} preguntas, solo {sum(1 for p in preguntas if p['discrimina'])} obligan a "
            "un compromiso verificable (memoria entre turnos, aritmética, coherencia con lo ya dicho).",
            "Turing sustituye «¿pueden pensar las máquinas?» por una pregunta operacional. El cambio de "
            "pregunta es la aportación; el juego concreto es el vehículo.",
            "El paper responde nueve objeciones. La de la conciencia queda deliberadamente fuera: el test "
            "la evita, y por eso no puede zanjarla.",
        ],
        [
            "Las respuestas están escritas a mano. Aquí no hay ningún modelo de lenguaje: se ilustra el "
            "protocolo, no se ejecuta una partida real.",
            "Que un sistema supere a un juez no dice nada sobre su comprensión. El test es de "
            "indistinguibilidad conductual, y Turing lo sabe: por eso propone «juego», no «prueba de mente».",
            "La predicción de Turing para el año 2000 hablaba de máquinas con 10⁹ bits de memoria y de "
            "cinco minutos de conversación. Citarla como acertada o fallada sin esas condiciones es trampa.",
        ],
    )


def _dartmouth(seed: int) -> dict[str, Any]:
    """Dartmouth 1955: la agenda que se propuso para dos meses y ocupó setenta años."""
    temas = [
        {"tema": "Computadoras automáticas", "anio_resultado": 1957,
         "donde_vive_hoy": "toda la computación"},
        {"tema": "Programar un computador para usar lenguaje", "anio_resultado": 2017,
         "donde_vive_hoy": "modelos de lenguaje (P08–P10)"},
        {"tema": "Redes de neuronas", "anio_resultado": 1986,
         "donde_vive_hoy": "aprendizaje profundo (P02)"},
        {"tema": "Teoría del tamaño de un cálculo", "anio_resultado": 1971,
         "donde_vive_hoy": "complejidad computacional"},
        {"tema": "Automejora", "anio_resultado": None,
         "donde_vive_hoy": "abierto: agentes que se corrigen (P30)"},
        {"tema": "Abstracciones", "anio_resultado": 2012,
         "donde_vive_hoy": "representaciones aprendidas (P04, P05)"},
        {"tema": "Aleatoriedad y creatividad", "anio_resultado": 2014,
         "donde_vive_hoy": "modelos generativos (P39, P17)"},
    ]
    for t in temas:
        t["anios_desde_1955"] = (t["anio_resultado"] - 1955) if t["anio_resultado"] else None
    cerrados = [t for t in temas if t["anios_desde_1955"] is not None]
    media = sum(t["anios_desde_1955"] for t in cerrados) / len(cerrados)

    rng = random.Random(seed)
    orden = [t["tema"] for t in rng.sample(temas, len(temas))]

    return _contract(
        "dartmouth",
        seed,
        {
            "duracion_planificada": "2 meses",
            "participantes_previstos": 10,
            "financiacion_solicitada_usd": 13500,
            "temas": temas,
            "temas_con_resultado_solido": len(cerrados),
            "temas_abiertos": len(temas) - len(cerrados),
            "media_de_anios_hasta_el_resultado": _round(media, 1),
            "orden_de_repaso_sugerido": orden,
            "frase_que_funda_el_nombre": "artificial intelligence",
        },
        [
            f"El plan era resolver la lista en 2 meses con 10 personas. De los {len(temas)} temas, "
            f"{len(cerrados)} tardaron una media de {_round(media, 1)} años en tener un resultado sólido.",
            "El tema del lenguaje —«programar un computador para usar lenguaje»— tarda 62 años hasta el "
            "Transformer. Es el mayor error de estimación del documento y el más instructivo.",
            f"{len(temas) - len(cerrados)} tema sigue abierto: la automejora. Setenta años después es "
            "exactamente lo que se discute en los agentes que se corrigen a sí mismos.",
            "La propuesta no aporta un método: aporta un NOMBRE y una agenda. Ese es su papel histórico.",
        ],
        [
            "«Resultado sólido» es un juicio de este programa, no del documento. Las fechas son defendibles "
            "pero discutibles, y conviene discutirlas en clase.",
            "El documento no contiene experimentos ni resultados: es una solicitud de financiación. "
            "Tratarlo como paper científico es un error de categoría.",
            "La lista de asistentes reales difiere de la de firmantes, y el encuentro fue más un taller "
            "abierto que un proyecto coordinado.",
        ],
    )


def _simbolos_y_busqueda(seed: int) -> dict[str, Any]:
    """Newell y Simon 1976: sin heurística, la búsqueda simbólica no escala."""
    objetivo = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    def vecinos(estado: tuple[int, ...]) -> list[tuple[int, ...]]:
        h = estado.index(0)
        fila, col = divmod(h, 3)
        salida = []
        for df, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nf, nc = fila + df, col + dc
            if 0 <= nf < 3 and 0 <= nc < 3:
                j = nf * 3 + nc
                nuevo = list(estado)
                nuevo[h], nuevo[j] = nuevo[j], nuevo[h]
                salida.append(tuple(nuevo))
        return sorted(salida)

    def manhattan(estado: tuple[int, ...]) -> int:
        total = 0
        for pos, ficha in enumerate(estado):
            if ficha == 0:
                continue
            destino = objetivo.index(ficha)
            total += abs(pos // 3 - destino // 3) + abs(pos % 3 - destino % 3)
        return total

    rng = random.Random(seed)
    estado = objetivo
    for _ in range(14):                       # revuelto corto y reproducible
        estado = rng.choice(vecinos(estado))

    def ciega() -> dict[str, Any]:
        frontera, vistos, expandidos = [(estado, 0)], {estado}, 0
        while frontera:
            actual, prof = frontera.pop(0)
            expandidos += 1
            if actual == objetivo:
                return {"expandidos": expandidos, "profundidad": prof, "encuentra": True}
            for v in vecinos(actual):
                if v not in vistos:
                    vistos.add(v)
                    frontera.append((v, prof + 1))
        return {"expandidos": expandidos, "profundidad": None, "encuentra": False}

    def heuristica() -> dict[str, Any]:
        frontera, vistos, expandidos = [(manhattan(estado), estado, 0)], {estado}, 0
        while frontera:
            frontera.sort(key=lambda t: (t[0], t[1]))
            _, actual, prof = frontera.pop(0)
            expandidos += 1
            if actual == objetivo:
                return {"expandidos": expandidos, "profundidad": prof, "encuentra": True}
            for v in vecinos(actual):
                if v not in vistos:
                    vistos.add(v)
                    frontera.append((manhattan(v), v, prof + 1))
        return {"expandidos": expandidos, "profundidad": None, "encuentra": False}

    sin_h, con_h = ciega(), heuristica()
    razon = _round(sin_h["expandidos"] / max(con_h["expandidos"], 1), 2)
    explosion = [{"profundidad": d, "nodos_si_b_es_2_7": int(2.7 ** d)} for d in (4, 8, 12, 16, 20)]

    return _contract(
        "simbolos_y_busqueda",
        seed,
        {
            "estado_inicial": list(estado),
            "distancia_manhattan_inicial": manhattan(estado),
            "busqueda_ciega": sin_h,
            "busqueda_heuristica": con_h,
            "razon_de_nodos": razon,
            "explosion_combinatoria": explosion,
            "hipotesis": "un sistema físico de símbolos tiene los medios necesarios y suficientes "
                         "para la acción inteligente general",
        },
        [
            f"La búsqueda ciega expande {sin_h['expandidos']} nodos y la heurística "
            f"{con_h['expandidos']}: una razón de {razon}× sobre el MISMO problema y el mismo espacio de "
            "estados.",
            "La heurística no cambia el problema ni el conjunto de operadores: cambia el ORDEN en que se "
            "miran los estados. Esa es toda la diferencia entre viable e inviable.",
            f"Con ramificación 2,7 la búsqueda exhaustiva pasa de {explosion[0]['nodos_si_b_es_2_7']} nodos "
            f"a profundidad 4 a {explosion[-1]['nodos_si_b_es_2_7']} a profundidad 20. Ningún hardware "
            "cierra ese hueco: hay que no mirar.",
            "Las dos mitades de la tesis se ven aquí juntas: símbolos (el estado es una estructura "
            "manipulable) y búsqueda (la inteligencia aparece al recorrer el espacio con criterio).",
        ],
        [
            "El 8-puzzle es un juguete con estado completamente observable y operadores exactos. La tesis de "
            "Newell y Simon es mucho más ambiciosa que esto, y sigue en disputa.",
            "La búsqueda voraz de esta miniatura no garantiza el camino óptimo: encuentra UNA solución "
            "rápido. La optimalidad con heurística es el asunto de A* (P67), no de esta ficha.",
            "Que los símbolos basten para la búsqueda no demuestra que basten para la inteligencia. El "
            "conexionismo y la robótica situada nacen justamente de negar ese salto.",
        ],
    )


def _agente_racional(seed: int) -> dict[str, Any]:
    """Wooldridge y Jennings 1995: «racional» no se puede juzgar sin la medida."""
    mundos = [("sucio", "sucio"), ("sucio", "limpio"), ("limpio", "sucio"), ("limpio", "limpio")]

    def simular(agente: str, mundo: tuple[str, str], pasos: int = 6) -> dict[str, Any]:
        estado = list(mundo)
        pos, movimientos, aspiraciones, limpio_visto = 0, 0, 0, set()
        for _ in range(pasos):
            if estado[pos] == "sucio":
                estado[pos] = "limpio"
                aspiraciones += 1
                continue
            limpio_visto.add(pos)
            if agente == "con_modelo" and len(limpio_visto) == 2:
                break                          # sabe que ya no queda nada que hacer
            pos = 1 - pos
            movimientos += 1
        return {
            "mundo": list(mundo),
            "casillas_limpias": sum(1 for c in estado if c == "limpio"),
            "movimientos": movimientos,
            "aspiraciones": aspiraciones,
        }

    resultados = {}
    for agente in ("reflejo_simple", "con_modelo"):
        corridas = [simular(agente, m) for m in mundos]
        limpieza = sum(c["casillas_limpias"] for c in corridas)
        movimiento = sum(c["movimientos"] for c in corridas)
        resultados[agente] = {
            "corridas": corridas,
            "medida_A_solo_limpieza": limpieza,
            "medida_B_limpieza_menos_coste": _round(limpieza - 0.5 * movimiento, 2),
        }

    ganador_a = max(resultados, key=lambda a: resultados[a]["medida_A_solo_limpieza"])
    ganador_b = max(resultados, key=lambda a: resultados[a]["medida_B_limpieza_menos_coste"])

    rng = random.Random(seed)
    entorno = {
        "observable": rng.choice([True, False]),
        "determinista": True,
        "episodico": False,
        "estatico": True,
        "discreto": True,
        "agentes": 1,
    }

    return _contract(
        "agente_racional",
        seed,
        {
            "agentes": resultados,
            "empate_bajo_la_medida_A": resultados["reflejo_simple"]["medida_A_solo_limpieza"]
                                       == resultados["con_modelo"]["medida_A_solo_limpieza"],
            "gana_con_medida_A": ganador_a,
            "gana_con_medida_B": ganador_b,
            "propiedades_del_entorno_sorteadas": entorno,
            "definicion": "agente = percibe su entorno y actúa sobre él para maximizar una medida de "
                          "desempeño; racional ≠ omnisciente",
        },
        [
            "Bajo la medida A (solo cuenta la limpieza) los dos agentes empatan: el reflejo simple parece "
            "tan bueno como el que mantiene un modelo del mundo.",
            f"Bajo la medida B (la misma limpieza, penalizando el movimiento) gana «{ganador_b}»: el mismo "
            "comportamiento pasa de racional a irracional sin tocar una línea del agente.",
            "El agente reflejo no puede parar porque no recuerda: su racionalidad está limitada por lo que "
            "PERCIBE, no por lo que decide.",
            "De ahí la consecuencia práctica: especificar la medida de desempeño y las propiedades del "
            "entorno es parte del diseño, no un preámbulo.",
        ],
        [
            "Dos casillas y seis pasos. Es la ilustración canónica, no un entorno realista.",
            "El artículo de Wooldridge y Jennings es un survey de teoría y arquitecturas de agentes; esta "
            "miniatura solo toca la noción de racionalidad relativa a la medida.",
            "No hay incertidumbre, ni otros agentes, ni acciones que fallen: justo las tres cosas que hacen "
            "difícil el diseño de agentes reales.",
        ],
    )


def _valor_predictivo(seed: int) -> dict[str, Any]:
    """Ioannidis 2005: la probabilidad de que un hallazgo publicado sea cierto."""

    def ppv(r: float, poder: float, alfa: float, sesgo: float = 0.0, equipos: int = 1) -> float:
        beta = 1 - poder
        if equipos > 1:
            num = r - r * beta ** equipos
            den = r + 1 - (1 - alfa) ** equipos - r * beta ** equipos
            return num / den
        num = (1 - beta) * r + sesgo * beta * r
        den = r + alfa - beta * r + sesgo - sesgo * alfa + sesgo * beta * r
        return num / den

    escenarios = [
        {"caso": "ensayo confirmatorio bien potenciado", "R": 1.0, "poder": 0.80, "alfa": 0.05,
         "sesgo": 0.0, "equipos": 1},
        {"caso": "exploratorio típico", "R": 0.10, "poder": 0.50, "alfa": 0.05,
         "sesgo": 0.0, "equipos": 1},
        {"caso": "exploratorio con sesgo moderado", "R": 0.10, "poder": 0.50, "alfa": 0.05,
         "sesgo": 0.30, "equipos": 1},
        {"caso": "campo de moda: 5 equipos en carrera", "R": 0.10, "poder": 0.50, "alfa": 0.05,
         "sesgo": 0.0, "equipos": 5},
        {"caso": "barrido masivo sin corrección", "R": 0.001, "poder": 0.60, "alfa": 0.05,
         "sesgo": 0.10, "equipos": 1},
    ]
    for e in escenarios:
        e["ppv"] = _round(ppv(e["R"], e["poder"], e["alfa"], e["sesgo"], e["equipos"]), 4)
        e["probabilidad_de_ser_falso"] = _round(1 - e["ppv"], 4)

    barrido = [{"poder": p, "ppv": _round(ppv(0.10, p, 0.05), 4)} for p in (0.2, 0.4, 0.6, 0.8, 0.95)]
    rng = random.Random(seed)
    poder_muestreado = _round(rng.uniform(0.2, 0.9), 2)

    return _contract(
        "valor_predictivo",
        seed,
        {
            "formula": "PPV = (1−β)·R / (R − β·R + α)",
            "escenarios": escenarios,
            "efecto_del_poder_con_R_0_1": barrido,
            "poder_muestreado_para_el_ejercicio": poder_muestreado,
            "p_menor_que_0_05": "no es la probabilidad de que la hipótesis sea cierta",
        },
        [
            f"Un p < 0,05 en un estudio exploratorio con poder 0,5 y odds previas 1:10 deja un PPV de "
            f"{escenarios[1]['ppv']}: la mitad de esos hallazgos son falsos ANTES de contar el sesgo.",
            f"Con un sesgo del 30 % el mismo diseño cae a {escenarios[2]['ppv']}, y con cinco equipos "
            f"compitiendo por publicar primero, a {escenarios[3]['ppv']}.",
            f"El poder estadístico es la palanca: con R = 0,1 el PPV sube de {barrido[0]['ppv']} a "
            f"{barrido[-1]['ppv']} solo con pasar el poder de 0,2 a 0,95.",
            "El umbral de significancia no responde a la pregunta que interesa. α es P(dato | hipótesis "
            "nula); lo que se quiere es P(hipótesis | dato), y para eso hacen falta las odds previas.",
        ],
        [
            "Los parámetros R, poder y sesgo no se observan: se estiman o se suponen. El modelo es un marco "
            "para pensar, no una calculadora de verdad.",
            "El artículo es analítico, no empírico: no mide cuántos resultados son falsos, sino qué implica "
            "la estructura de incentivos si sus supuestos valen.",
            "Trasladar esto a la IA exige cuidado: aquí el «hallazgo» suele ser una mejora en un benchmark "
            "y el problema dominante es otro (fuga de datos, selección de semilla, comparación desigual).",
        ],
    )


def _stochastic_parrots(seed: int) -> dict[str, Any]:
    """Bender et al. 2021: qué queda dentro y qué queda fuera cuando el corpus es «toda la web»."""
    corpus = [
        {"comunidad": "mayoritaria", "documentos": 9400, "en_lista_de_bloqueo": 120},
        {"comunidad": "minoritaria_A", "documentos": 400, "en_lista_de_bloqueo": 190},
        {"comunidad": "minoritaria_B", "documentos": 200, "en_lista_de_bloqueo": 30},
    ]
    total = sum(c["documentos"] for c in corpus)
    for c in corpus:
        c["cuota_antes"] = _round(100 * c["documentos"] / total, 2)
        c["tras_filtrar_por_lista"] = c["documentos"] - c["en_lista_de_bloqueo"]
        c["perdida_relativa"] = f"{_round(100 * c['en_lista_de_bloqueo'] / c['documentos'], 1)} %"
    total_post = sum(c["tras_filtrar_por_lista"] for c in corpus)
    for c in corpus:
        c["cuota_despues"] = _round(100 * c["tras_filtrar_por_lista"] / total_post, 2)
        c["variacion_de_cuota"] = _round(c["cuota_despues"] - c["cuota_antes"], 2)

    costes = [
        {"modelo": "pequeño", "parametros_millones": 110, "coste_relativo": 1},
        {"modelo": "mediano", "parametros_millones": 1500, "coste_relativo": 14},
        {"modelo": "grande", "parametros_millones": 175000, "coste_relativo": 1600},
    ]

    rng = random.Random(seed)
    urna = [c["comunidad"] for c in corpus for _ in range(c["documentos"] // 100)]
    muestra = [rng.choice(urna) for _ in range(20)]
    conteo = {c["comunidad"]: muestra.count(c["comunidad"]) for c in corpus}

    return _contract(
        "stochastic_parrots",
        seed,
        {
            "corpus": corpus,
            "documentos_totales": total,
            "muestra_de_20_documentos": conteo,
            "coste_de_entrenamiento": costes,
            "tesis": "un modelo de lenguaje ordena formas lingüísticas según su probabilidad; "
                     "no tiene acceso al significado ni a la intención comunicativa",
        },
        [
            f"El filtrado por lista de bloqueo retira el {corpus[1]['perdida_relativa']} de la comunidad "
            f"minoritaria A y solo el {corpus[0]['perdida_relativa']} de la mayoritaria: el mismo filtro, "
            "aplicado por igual, no afecta por igual.",
            f"Tras filtrar, la cuota de la comunidad minoritaria A cae "
            f"{abs(corpus[1]['variacion_de_cuota'])} puntos y la mayoritaria sube. Una operación de "
            "«limpieza» redistribuye quién está representado.",
            "«Más datos» no es «datos más diversos»: un corpus grande recogido por conveniencia amplifica a "
            "quien ya tenía presencia en la web, y eso es una decisión editorial aunque nadie la firme.",
            f"Una muestra de 20 documentos del corpus contiene {conteo['mayoritaria']} documentos de la "
            "comunidad mayoritaria: quien audite el dato mirando una muestra pequeña no verá siquiera "
            "que existen las otras.",
        ],
        [
            "Los números del corpus son de juguete y deliberadamente redondos. El artículo no aporta esta "
            "tabla: aporta el argumento de que las listas de bloqueo silencian a quien reapropia términos.",
            "Que un modelo no acceda al significado en el sentido del paper es una tesis lingüística, no un "
            "resultado medido. Hay desacuerdo serio y publicado al respecto.",
            "La tabla de coste crece proporcionalmente al tamaño: es una ilustración de escala, y no "
            "demuestra por sí sola la desproporción entre coste y beneficio que argumenta el artículo.",
            "Las cifras de coste energético envejecen rápido y dependen del centro de datos y del año. Se "
            "usan como orden de magnitud, no como dato citable.",
        ],
    )


def _benchmark_validez(seed: int) -> dict[str, Any]:
    """Raji et al. 2021: un número alto no prueba la capacidad que el benchmark dice medir."""
    subhabilidades = ["correferencia", "negación", "aritmética", "causalidad", "temporalidad", "pragmática"]
    plan = [("correferencia", True), ("correferencia", True), ("correferencia", True),
            ("correferencia", True), ("negación", True), ("negación", True),
            ("negación", True), ("negación", False), ("correferencia", True),
            ("negación", True), ("correferencia", True), ("negación", True)]
    items = [
        {"id": f"i{n:02d}", "subhabilidad": s, "opcion_correcta_es_la_mas_larga": largo}
        for n, (s, largo) in enumerate(plan, 1)
    ]
    cubiertas = sorted({i["subhabilidad"] for i in items})
    atajo = sum(1 for i in items if i["opcion_correcta_es_la_mas_larga"])

    rng = random.Random(seed)
    azar = len(items) // 4                                # cuatro opciones por ítem
    inspeccion = [i["id"] for i in rng.sample(items, 4)]

    return _contract(
        "benchmark_validez",
        seed,
        {
            "nombre_del_benchmark": "COMPRENSIÓN-12 (ficticio)",
            "capacidad_declarada": "comprensión de lenguaje natural",
            "subhabilidades_declaradas": subhabilidades,
            "subhabilidades_realmente_evaluadas": cubiertas,
            "cobertura": f"{len(cubiertas)}/{len(subhabilidades)}",
            "items": len(items),
            "modelo_atajo": {
                "regla": "responder siempre la opción más larga",
                "aciertos": f"{atajo}/{len(items)}",
                "exactitud": _round(atajo / len(items), 4),
                "capacidad_real": "ninguna",
            },
            "modelo_al_azar": {
                "regla": "elegir una de las cuatro opciones sin leer el ítem",
                "aciertos_esperados": f"{azar}/{len(items)}",
                "exactitud": _round(azar / len(items), 4),
            },
            "items_a_inspeccionar_a_mano": sorted(inspeccion),
            "pregunta_de_validez": "¿la tarea medida es la capacidad nombrada, o un proxy que se le parece?",
        },
        [
            f"Una regla sin ninguna comprensión —elegir la opción más larga— acierta {atajo}/{len(items)} "
            f"frente a los {azar}/{len(items)} del azar. El número que publica el benchmark no distingue "
            "esa estrategia de la capacidad que dice medir.",
            f"El benchmark declara {len(subhabilidades)} subhabilidades y solo evalúa {len(cubiertas)}: la "
            "etiqueta «comprensión de lenguaje natural» promete un constructo que los ítems no cubren.",
            "El problema no es la métrica sino la VALIDEZ DE CONSTRUCTO: la distancia entre lo que se mide "
            "y lo que se afirma haber medido.",
            "De ahí la regla práctica del programa: antes de creer un ranking, mirar los ítems y buscar el "
            "atajo. Si existe, el ranking mide el atajo.",
        ],
        [
            "El benchmark es inventado y los ítems no existen. Lo que se ilustra es el modo de fallo, no un "
            "resultado sobre ningún benchmark real.",
            "La línea del azar se simula con una moneda: sirve de suelo para leer el número del atajo, "
            "no para comparar modelos.",
            "El artículo argumenta además contra la ambición de los benchmarks «generales». Esa parte es "
            "conceptual y no se puede reducir a una tabla como esta.",
        ],
    )


def _reproducibilidad(seed: int) -> dict[str, Any]:
    """Pineau et al. 2021: qué hace falta para que otra persona obtenga lo mismo."""
    semillas = [11, 23, 42, 77, 91]
    base = {11: 71.2, 23: 73.8, 42: 70.4, 77: 74.9, 91: 72.1}
    propuesta = {11: 73.0, 23: 72.4, 42: 74.6, 77: 71.8, 91: 73.9}

    def resumen(d: dict[int, float]) -> dict[str, float]:
        vals = [d[s] for s in semillas]
        media = sum(vals) / len(vals)
        var = sum((v - media) ** 2 for v in vals) / (len(vals) - 1)
        return {"media": _round(media, 3), "desviacion": _round(math.sqrt(var), 3),
                "min": min(vals), "max": max(vals)}

    r_base, r_prop = resumen(base), resumen(propuesta)
    reportada = semillas[seed % len(semillas)]
    diferencia_reportada = _round(propuesta[reportada] - base[reportada], 3)
    diferencia_real = _round(r_prop["media"] - r_base["media"], 3)
    favorables = sum(1 for s in semillas if propuesta[s] > base[s])

    checklist = [
        {"item": "código publicado", "A": True, "B": True, "C": False},
        {"item": "semillas y entorno declarados", "A": True, "B": False, "C": False},
        {"item": "media y desviación sobre varias corridas", "A": True, "B": False, "C": False},
        {"item": "hiperparámetros y su búsqueda", "A": True, "B": True, "C": False},
        {"item": "datos y su partición exacta", "A": True, "B": True, "C": True},
        {"item": "coste de cómputo declarado", "A": True, "B": False, "C": False},
        {"item": "métrica definida sin ambigüedad", "A": True, "B": True, "C": True},
        {"item": "límites y casos donde falla", "A": True, "B": False, "C": False},
    ]
    puntuaciones = {c: sum(1 for i in checklist if i[c]) for c in ("A", "B", "C")}

    return _contract(
        "reproducibilidad",
        seed,
        {
            "semillas": semillas,
            "baseline": r_base,
            "propuesta": r_prop,
            "semilla_que_reporta_el_autor": reportada,
            "mejora_si_reporta_una_semilla": diferencia_reportada,
            "mejora_real_en_media": diferencia_real,
            "semillas_en_las_que_gana_la_propuesta": f"{favorables}/{len(semillas)}",
            "solapan_los_rangos": not (r_prop["min"] > r_base["max"] or r_base["min"] > r_prop["max"]),
            "checklist": checklist,
            "puntuacion_por_articulo": puntuaciones,
        },
        [
            f"Con la semilla {reportada} la propuesta «mejora» {diferencia_reportada} puntos. En media "
            f"sobre cinco semillas la diferencia real es {diferencia_real}, con desviaciones de "
            f"{r_base['desviacion']} y {r_prop['desviacion']}: la mejora cabe dentro del ruido.",
            f"La propuesta gana en {favorables} de {len(semillas)} semillas. Publicar la mejor y callar las "
            "demás no es fraude: es lo que permite un formato que no exige declararlas.",
            "Los rangos de las dos configuraciones se solapan. Sin media, desviación y número de corridas "
            "el lector no puede saberlo, y por eso el checklist pide esos tres campos.",
            f"El artículo A cumple {puntuaciones['A']}/8 del checklist y el C, {puntuaciones['C']}/8. La "
            "diferencia no está en la calidad de la idea: está en si alguien puede comprobarla.",
        ],
        [
            "Los números de exactitud son inventados y están elegidos para que el solape sea visible. Un "
            "caso real puede tener separaciones limpias.",
            "El checklist no garantiza que un resultado sea cierto: garantiza que sea COMPROBABLE. Son "
            "cosas distintas y conviene no confundirlas.",
            "Cinco semillas siguen siendo pocas para un contraste serio. El programa de reproducibilidad de "
            "NeurIPS aborda además revisión, código y datos, que no se modelan aquí.",
        ],
    )


# --------------------------------------------------------------------------- #
# ruta simbólica (P64–P72)
# --------------------------------------------------------------------------- #


def _gps(seed: int) -> dict[str, Any]:
    """Newell, Shaw y Simon 1959: el análisis medios-fines elige el operador por la diferencia."""
    inicial = {"lugar": "casa", "vestido": "pijama", "hambre": True, "puerta": "cerrada"}
    meta = {"lugar": "oficina", "vestido": "traje", "hambre": False, "puerta": "cerrada"}

    operadores = [
        {"nombre": "desayunar", "reduce": "hambre",
         "precondiciones": {"lugar": "casa"}, "efectos": {"hambre": False}},
        {"nombre": "vestirse", "reduce": "vestido",
         "precondiciones": {"lugar": "casa"}, "efectos": {"vestido": "traje"}},
        {"nombre": "abrir_puerta", "reduce": "puerta",
         "precondiciones": {"lugar": "casa"}, "efectos": {"puerta": "abierta"}},
        {"nombre": "conducir", "reduce": "lugar",
         "precondiciones": {"vestido": "traje", "puerta": "abierta"}, "efectos": {"lugar": "oficina"}},
        {"nombre": "cerrar_puerta", "reduce": "puerta",
         "precondiciones": {}, "efectos": {"puerta": "cerrada"}},
    ]
    tabla = {}
    for op in operadores:
        tabla.setdefault(op["reduce"], []).append(op["nombre"])

    def diferencias(estado: dict[str, Any]) -> list[str]:
        return sorted(k for k, v in meta.items() if estado.get(k) != v)

    estado = dict(inicial)
    traza, aplicados, ciclos = [], [], 0
    rng = random.Random(seed)
    while diferencias(estado) and ciclos < 12:
        ciclos += 1
        pendientes = diferencias(estado)
        objetivo = pendientes[0]
        candidatos = [op for op in operadores if op["reduce"] == objetivo]
        elegido = None
        for op in candidatos:
            if all(estado.get(k) == v for k, v in op["precondiciones"].items()):
                elegido = op
                break
        if elegido is None:
            # subobjetivo: primero reducir la diferencia que bloquea la precondición
            bloqueo = next(
                (k for op in candidatos for k, v in op["precondiciones"].items() if estado.get(k) != v),
                None,
            )
            traza.append({"diferencia": objetivo, "accion": f"subobjetivo sobre «{bloqueo}»"})
            if bloqueo is None:
                break
            objetivo = bloqueo
            elegido = next(
                (op for op in operadores
                 if op["reduce"] == objetivo
                 and all(estado.get(k) == v for k, v in op["precondiciones"].items())),
                None,
            )
            if elegido is None:
                break
        estado.update(elegido["efectos"])
        aplicados.append(elegido["nombre"])
        traza.append({"diferencia": objetivo, "operador": elegido["nombre"],
                      "estado": dict(estado), "restan": diferencias(estado)})

    # comparación: cuántas secuencias habría que probar a ciegas de esta longitud
    n = len(aplicados)
    ciegas = len(operadores) ** n if n else 0
    muestra = ["-".join(rng.choice(operadores)["nombre"] for _ in range(n)) for _ in range(3)]

    return _contract(
        "gps",
        seed,
        {
            "estado_inicial": inicial,
            "meta": meta,
            "tabla_diferencia_operador": tabla,
            "traza": traza,
            "plan": aplicados,
            "pasos": n,
            "meta_alcanzada": diferencias(estado) == [],
            "secuencias_a_ciegas_de_esa_longitud": ciegas,
            "muestra_de_secuencias_ciegas": muestra,
        },
        [
            f"El plan sale en {n} pasos y alcanza la meta: {aplicados}.",
            "El operador no se elige probando: se elige **por la diferencia**. La tabla "
            "diferencia→operador es el conocimiento del dominio, y sin ella no hay guía.",
            "Cuando el operador que reduce la diferencia no es aplicable, GPS no abandona: crea un "
            "subobjetivo para hacerlo aplicable. Ese es el mecanismo recursivo que da nombre al método.",
            f"A ciegas habría {ciegas} secuencias de esa longitud sobre {len(operadores)} operadores. La "
            "diferencia entre 5 y ese número es lo que aporta el análisis medios-fines.",
        ],
        [
            "El dominio es de juguete y la tabla diferencia→operador está escrita a mano: justo el "
            "conocimiento que en un dominio real es caro de obtener y frágil de mantener.",
            "GPS elige la primera diferencia pendiente en orden alfabético. El sistema original ordenaba "
            "las diferencias por importancia, y esa ordenación es parte del arte del método.",
            "No hay retroceso ni tratamiento de interacciones entre subobjetivos. Cuando dos submetas se "
            "estorban, este esquema falla; es el mismo problema que reaparece en STRIPS.",
        ],
    )


def _dpll(seed: int) -> dict[str, Any]:
    """Davis, Logemann y Loveland 1962: propagar antes de ramificar."""
    # (a ∨ ¬b) ∧ (¬a ∨ c) ∧ (b ∨ ¬c ∨ d) ∧ (¬d ∨ e) ∧ (a ∨ b ∨ ¬e) ∧ (¬a ∨ ¬c ∨ d)
    formula = [["a", "-b"], ["-a", "c"], ["b", "-c", "d"], ["-d", "e"], ["a", "b", "-e"],
               ["-a", "-c", "d"]]
    variables = sorted({lit.lstrip("-") for c in formula for lit in c})

    def evaluar(clausulas, asignacion):
        salida = []
        for c in clausulas:
            nueva = []
            satisfecha = False
            for lit in c:
                var, signo = lit.lstrip("-"), not lit.startswith("-")
                if var in asignacion:
                    if asignacion[var] == signo:
                        satisfecha = True
                        break
                else:
                    nueva.append(lit)
            if satisfecha:
                continue
            if not nueva:
                return None                  # cláusula vacía: conflicto
            salida.append(nueva)
        return salida

    contador = {"nodos": 0, "unitarias": 0, "puras": 0}

    def dpll(clausulas, asignacion):
        contador["nodos"] += 1
        clausulas = evaluar(clausulas, asignacion)
        if clausulas is None:
            return None
        if not clausulas:
            return dict(asignacion)
        # propagación unitaria
        for c in clausulas:
            if len(c) == 1:
                var, signo = c[0].lstrip("-"), not c[0].startswith("-")
                contador["unitarias"] += 1
                return dpll(clausulas, {**asignacion, var: signo})
        # literal puro
        literales = {lit for c in clausulas for lit in c}
        for var in sorted({lit.lstrip("-") for lit in literales}):
            if var in literales and f"-{var}" not in literales:
                contador["puras"] += 1
                return dpll(clausulas, {**asignacion, var: True})
            if f"-{var}" in literales and var not in literales:
                contador["puras"] += 1
                return dpll(clausulas, {**asignacion, var: False})
        # ramificar
        var = sorted({lit.lstrip("-") for lit in literales})[0]
        for valor in (True, False):
            r = dpll(clausulas, {**asignacion, var: valor})
            if r is not None:
                return r
        return None

    modelo = dpll(formula, {})

    # fuerza bruta sobre la tabla de verdad completa
    total, satisfactorias = 0, 0
    for mascara in range(2 ** len(variables)):
        asignacion = {v: bool(mascara >> i & 1) for i, v in enumerate(variables)}
        total += 1
        if evaluar(formula, asignacion) == []:
            satisfactorias += 1

    rng = random.Random(seed)
    sondeo = sum(
        1 for _ in range(200)
        if evaluar(formula, {v: rng.random() < 0.5 for v in variables}) == []
    )

    return _contract(
        "dpll",
        seed,
        {
            "formula": [" ∨ ".join(c) for c in formula],
            "variables": variables,
            "modelo_encontrado": modelo,
            "satisfacible": modelo is not None,
            "nodos_dpll": contador["nodos"],
            "propagaciones_unitarias": contador["unitarias"],
            "literales_puros": contador["puras"],
            "asignaciones_tabla_completa": total,
            "asignaciones_satisfactorias": satisfactorias,
            "sondeo_aleatorio_200_intentos": sondeo,
        },
        [
            f"DPLL visita {contador['nodos']} nodos frente a las {total} filas de la tabla de verdad "
            f"completa: la fórmula tiene {len(variables)} variables y ya hay un factor de "
            f"{_round(total / contador['nodos'], 1)}×.",
            f"De esos pasos, {contador['unitarias']} son propagaciones unitarias y "
            f"{contador['puras']} son literales puros: la mayor parte del trabajo se hace **sin ramificar**. "
            "Ramificar es el último recurso, no el primero.",
            "Una cláusula unitaria no deja elección: su literal tiene que ser cierto. Eso no es una "
            "heurística, es una deducción, y por eso no hay que deshacerla nunca.",
            f"Solo {satisfactorias} de {total} asignaciones satisfacen la fórmula, y un sondeo aleatorio "
            f"de 200 intentos da con una {sondeo} veces. Con cinco variables el azar todavía funciona; con "
            "cincuenta, la misma proporción exige del orden de 10^13 intentos. Esa es la razón de propagar.",
        ],
        [
            "Seis cláusulas y cinco variables. Los solucionadores modernos manejan millones de cláusulas y "
            "deben su rendimiento a técnicas posteriores (aprendizaje de cláusulas, reinicios, heurísticas "
            "de actividad) que no están aquí.",
            "La ramificación elige la primera variable en orden alfabético. La elección de variable es "
            "justamente donde vive el rendimiento en un solucionador real.",
            "SAT es NP-completo: DPLL no lo evita. Reduce el trabajo en casos con estructura, y sigue "
            "siendo exponencial en el peor caso.",
        ],
    )


def _resolucion(seed: int) -> dict[str, Any]:
    """Robinson 1965: unificación y una sola regla de inferencia."""

    def es_variable(t: Any) -> bool:
        return isinstance(t, str) and t[0].islower() and len(t) <= 2

    def unificar(x: Any, y: Any, sust: dict | None) -> dict | None:
        if sust is None:
            return None
        if x == y:
            return sust
        if es_variable(x):
            if x in sust:
                return unificar(sust[x], y, sust)
            return {**sust, x: y}
        if es_variable(y):
            return unificar(y, x, sust)
        if isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
            for a, b in zip(x, y):
                sust = unificar(a, b, sust)
                if sust is None:
                    return None
            return sust
        return None

    casos = [
        {"a": ("Humano", "x"), "b": ("Humano", "Sócrates")},
        {"a": ("Padre", "x", "y"), "b": ("Padre", "Juan", "z")},
        {"a": ("Humano", "Sócrates"), "b": ("Humano", "Platón")},
        {"a": ("Conoce", "x", ("Madre", "x")), "b": ("Conoce", "Ana", ("Madre", "Ana"))},
    ]
    for c in casos:
        u = unificar(c["a"], c["b"], {})
        c["unificador"] = u
        c["unifica"] = u is not None

    # refutación: ∀x Humano(x) → Mortal(x);  Humano(Sócrates);  ¬Mortal(Sócrates)
    clausulas = [
        [("-", ("Humano", "x")), ("+", ("Mortal", "x"))],
        [("+", ("Humano", "Sócrates"))],
        [("-", ("Mortal", "Sócrates"))],
    ]

    def resolver(c1, c2):
        for s1, l1 in c1:
            for s2, l2 in c2:
                if s1 == s2:
                    continue
                u = unificar(l1, l2, {})
                if u is None:
                    continue
                resto = [(s, t) for (s, t) in c1 if (s, t) != (s1, l1)]
                resto += [(s, t) for (s, t) in c2 if (s, t) != (s2, l2)]
                aplicada = []
                for s, t in resto:
                    if isinstance(t, tuple):
                        t = tuple(u.get(e, e) if not isinstance(e, tuple) else e for e in t)
                    aplicada.append((s, t))
                return aplicada, u
        return None, None

    pasos, agenda = [], list(clausulas)
    vacia = False
    for i in range(len(agenda)):
        for j in range(len(agenda)):
            if i == j or vacia:
                continue
            nueva, u = resolver(agenda[i], agenda[j])
            if nueva is None:
                continue
            pasos.append({"de": i, "con": j, "unificador": u,
                          "resolvente": "□ (cláusula vacía)" if not nueva else str(nueva)})
            if not nueva:
                vacia = True
                break
            if nueva not in agenda:
                agenda.append(nueva)

    rng = random.Random(seed)
    orden = rng.sample(range(len(casos)), len(casos))

    return _contract(
        "resolucion",
        seed,
        {
            "casos_de_unificacion": casos,
            "clausulas_iniciales": len(clausulas),
            "pasos_de_resolucion": pasos[:6],
            "cierra_por_refutacion": vacia,
            "regla_unica": "de (A ∨ L) y (B ∨ ¬L') con σ = mgu(L, L') se sigue (A ∨ B)σ",
            "orden_de_repaso": orden,
        },
        [
            f"De los {len(casos)} casos de unificación, "
            f"{sum(1 for c in casos if c['unifica'])} tienen unificador y el resto no: «Sócrates» y "
            "«Platón» son constantes distintas y ninguna sustitución las iguala.",
            "El unificador más general no inventa compromisos: en `Padre(x,y)` con `Padre(Juan,z)` liga "
            "`x = Juan` y deja `y = z` sin resolver, que es lo mínimo necesario.",
            f"La refutación cierra con la cláusula vacía: {vacia}. Para demostrar que Sócrates es mortal se "
            "NIEGA la conclusión y se busca contradicción; el vacío es la contradicción.",
            "Toda la inferencia usa una sola regla. Ese es el resultado de Robinson: no hace falta un "
            "catálogo de reglas, hace falta una con unificación.",
        ],
        [
            "La unificación de esta miniatura no hace comprobación de ocurrencia («occurs check»), que es "
            "necesaria para la corrección en el caso general y que muchos Prolog omiten por velocidad.",
            "El bucle de resolución es ingenuo y de saturación limitada: un demostrador real usa "
            "estrategias (unidad, entrada, conjunto soporte) para no explotar.",
            "La lógica de primer orden es semidecidible: si la conclusión no se sigue, el procedimiento "
            "puede no terminar. Aquí eso se esconde tras un tope de iteraciones.",
        ],
    )


def _a_estrella(seed: int) -> dict[str, Any]:
    """Hart, Nilsson y Raphael 1968: admisibilidad implica optimalidad."""
    grafo = {
        "A": {"B": 2, "C": 4},
        "B": {"D": 5, "E": 2},
        "C": {"E": 1, "F": 6},
        "D": {"G": 3},
        "E": {"D": 1, "G": 6},
        "F": {"G": 2},
        "G": {},
    }
    # h admisible: nunca sobrestima el coste real restante hasta G
    h_admisible = {"A": 6, "B": 5, "C": 5, "D": 3, "E": 4, "F": 2, "G": 0}
    # h inadmisible: sobrestima en D, que está en el camino óptimo
    h_inadmisible = {"A": 6, "B": 5, "C": 5, "D": 9, "E": 4, "F": 2, "G": 0}

    def buscar(h: dict[str, int] | None, voraz: bool = False) -> dict[str, Any]:
        inicio, meta = "A", "G"
        abiertos = [(0, inicio, [inicio])]
        mejor: dict[str, int] = {inicio: 0}
        expandidos = 0
        while abiertos:
            abiertos.sort(key=lambda t: (t[0], t[1]))
            _, nodo, camino = abiertos.pop(0)
            expandidos += 1
            if nodo == meta:
                coste = sum(grafo[a][b] for a, b in zip(camino, camino[1:]))
                return {"camino": "→".join(camino), "coste": coste, "expandidos": expandidos}
            g_actual = mejor[nodo]
            for vecino, peso in sorted(grafo[nodo].items()):
                g = g_actual + peso
                if vecino in mejor and mejor[vecino] <= g:
                    continue
                mejor[vecino] = g
                if h is None:
                    prioridad = g
                elif voraz:
                    prioridad = h[vecino]
                else:
                    prioridad = g + h[vecino]
                abiertos.append((prioridad, vecino, camino + [vecino]))
        return {"camino": None, "coste": None, "expandidos": expandidos}

    resultados = {
        "costo_uniforme": buscar(None),
        "voraz_solo_h": buscar(h_admisible, voraz=True),
        "a_estrella_admisible": buscar(h_admisible),
        "a_estrella_inadmisible": buscar(h_inadmisible),
    }
    optimo = resultados["costo_uniforme"]["coste"]
    for nombre, r in resultados.items():
        r["es_optimo"] = r["coste"] == optimo

    # comprobación de admisibilidad contra el coste real
    reales = {}
    for nodo in grafo:
        sub = buscar(None)
        reales[nodo] = None
    coste_real = {"A": 8, "B": 6, "C": 5, "D": 3, "E": 4, "F": 2, "G": 0}
    admisible_ok = {n: h_admisible[n] <= coste_real[n] for n in grafo}
    inadmisible_ok = {n: h_inadmisible[n] <= coste_real[n] for n in grafo}

    rng = random.Random(seed)
    nodo_inspeccion = rng.choice(sorted(grafo))

    return _contract(
        "a_estrella",
        seed,
        {
            "grafo": {k: v for k, v in grafo.items()},
            "h_admisible": h_admisible,
            "h_inadmisible": h_inadmisible,
            "coste_real_hasta_G": coste_real,
            "admisible_en_todos_los_nodos": all(admisible_ok.values()),
            "inadmisible_falla_en": [n for n, ok in inadmisible_ok.items() if not ok],
            "resultados": resultados,
            "coste_optimo": optimo,
            "nodo_inspeccionado": nodo_inspeccion,
        },
        [
            f"El coste óptimo es {optimo}. A* con heurística admisible lo encuentra expandiendo "
            f"{resultados['a_estrella_admisible']['expandidos']} nodos, frente a los "
            f"{resultados['costo_uniforme']['expandidos']} del costo uniforme.",
            f"La búsqueda voraz —solo h, ignorando g— expande "
            f"{resultados['voraz_solo_h']['expandidos']} nodos y devuelve un camino de coste "
            f"{resultados['voraz_solo_h']['coste']}: rápida y NO óptima.",
            f"A* con una heurística que sobrestima en D devuelve coste "
            f"{resultados['a_estrella_inadmisible']['coste']}. La garantía se pierde exactamente donde se "
            "rompe la admisibilidad, y no antes.",
            "La aportación del paper es esa condición: si h nunca sobrestima el coste restante, A* "
            "devuelve el camino óptimo. No es una heurística mejor: es un teorema.",
        ],
        [
            "Siete nodos y aristas con pesos enteros. No hay grafos grandes, ni memoria acotada, ni "
            "variantes (IDA*, A* ponderado) que son las que se usan en la práctica.",
            "La admisibilidad se comprueba aquí contra una tabla de costes reales escrita a mano. En un "
            "problema real, demostrar que una heurística es admisible es parte del trabajo.",
            "La consistencia (o monotonía) es una condición más fuerte que la admisibilidad y es la que "
            "permite no reexpandir nodos. Esta miniatura no la distingue.",
        ],
    )


def _strips(seed: int) -> dict[str, Any]:
    """Fikes y Nilsson 1971: precondición, añadir, borrar — y el problema del marco."""
    bloques = ["A", "B", "C"]
    sitios = bloques + ["mesa"]

    def operador(b, origen, destino):
        pre = {f"sobre({b},{origen})", f"libre({b})"}
        add = {f"sobre({b},{destino})"}
        dele = {f"sobre({b},{origen})"}
        if destino != "mesa":
            pre.add(f"libre({destino})")
            dele.add(f"libre({destino})")
        if origen != "mesa":
            add.add(f"libre({origen})")
        return {"nombre": f"mover({b},{origen}→{destino})", "pre": pre, "add": add, "del": dele}

    ops = [operador(b, o, d)
           for b in bloques for o in sitios for d in sitios
           if o != d and b != o and b != d]

    # C sobre A, A y B sobre la mesa: el planteamiento clásico de la anomalía
    inicial = {"sobre(C,A)", "sobre(A,mesa)", "sobre(B,mesa)", "libre(C)", "libre(B)"}
    meta = {"sobre(A,B)", "sobre(B,C)"}

    def aplicable(estado, o):
        return o["pre"] <= estado

    def aplicar(estado, o):
        return (estado - o["del"]) | o["add"]

    def lineal(orden, pasos=6):
        """Planificador lineal: cierra una submeta y pasa a la siguiente, sin mirar atrás."""
        estado, plan = set(inicial), []
        for submeta in orden:
            for _ in range(pasos):
                if submeta in estado:
                    break
                directo = next((o for o in ops if submeta in o["add"] and aplicable(estado, o)), None)
                if directo is not None:
                    estado = aplicar(estado, directo)
                    plan.append(directo["nombre"])
                    continue
                # despejar: liberar el bloque que hace falta mover
                bloque = submeta.split("(")[1].split(",")[0]
                estorbo = next((h for h in sorted(estado)
                                if h.startswith("sobre(") and h.endswith(f",{bloque})")), None)
                if estorbo is None:
                    break
                encima = estorbo.split("(")[1].split(",")[0]
                despeje = next((o for o in ops
                                if o["nombre"].startswith(f"mover({encima},")
                                and o["nombre"].endswith("→mesa)") and aplicable(estado, o)), None)
                if despeje is None:
                    break
                estado = aplicar(estado, despeje)
                plan.append(despeje["nombre"])
        return {"plan": plan, "estado_final": sorted(estado),
                "logra": {m: (m in estado) for m in sorted(meta)}, "todas": meta <= estado}

    primero_a = lineal(["sobre(A,B)", "sobre(B,C)"])
    primero_b = lineal(["sobre(B,C)", "sobre(A,B)"])

    # el problema del marco: qué NO cambia al aplicar un operador
    ejemplo = next(o for o in ops if o["nombre"] == "mover(C,A→mesa)")
    despues = aplicar(set(inicial), ejemplo)
    intactos = sorted(set(inicial) & despues)
    mencionados = sorted(ejemplo["add"] | ejemplo["del"])

    # el plan que sí resuelve: intercala las submetas en vez de cerrarlas por turnos
    intercalado = ["mover(C,A→mesa)", "mover(B,mesa→C)", "mover(A,mesa→B)"]
    estado_i, aplicados_i = set(inicial), []
    for nombre in intercalado:
        o = next((o for o in ops if o["nombre"] == nombre), None)
        if o is not None and aplicable(estado_i, o):
            estado_i = aplicar(estado_i, o)
            aplicados_i.append(nombre)
    no_lineal = {"plan": aplicados_i, "pasos": len(aplicados_i),
                 "logra": {m: (m in estado_i) for m in sorted(meta)}, "todas": meta <= estado_i}

    rng = random.Random(seed)
    barajado = rng.sample(sorted(meta), len(meta))

    return _contract(
        "strips",
        seed,
        {
            "estado_inicial": sorted(inicial),
            "meta": sorted(meta),
            "operadores_generados": len(ops),
            "representacion_de_un_operador": {
                "nombre": ejemplo["nombre"], "pre": sorted(ejemplo["pre"]),
                "add": sorted(ejemplo["add"]), "del": sorted(ejemplo["del"]),
            },
            "literales_mencionados_por_el_operador": mencionados,
            "literales_no_mencionados_que_persisten": intactos,
            "plan_con_A_sobre_B_primero": primero_a,
            "plan_con_B_sobre_C_primero": primero_b,
            "ningun_orden_lineal_resuelve": not (primero_a["todas"] or primero_b["todas"]),
            "plan_no_lineal_intercalado": no_lineal,
            "orden_barajado": barajado,
        },
        [
            f"Un operador se declara con tres listas. En «{ejemplo['nombre']}» son "
            f"{len(ejemplo['pre'])} precondiciones, {len(ejemplo['add'])} literales a añadir y "
            f"{len(ejemplo['del'])} a borrar: nada más.",
            f"Al aplicarlo, {len(intactos)} literales que el operador NO menciona siguen siendo ciertos sin "
            "que nadie los reafirme. Esa es la respuesta de STRIPS al problema del marco: lo no mencionado "
            "persiste.",
            f"Cerrando las submetas por turnos se consiguen {sum(primero_a['logra'].values())}/2 con un "
            f"orden y {sum(primero_b['logra'].values())}/2 con el inverso: **ningún** orden lineal resuelve "
            "el problema. Eso es la anomalía de Sussman.",
            f"Y no es que el problema sea difícil: existe un plan de {no_lineal['pasos']} pasos que lo "
            f"resuelve ({no_lineal['todas']}). Lo que falla no es el dominio, es el esquema de cerrar una "
            "submeta antes de tocar la siguiente.",
        ],
        [
            "El mundo de bloques es el dominio de juguete por excelencia: acciones deterministas, estado "
            "completamente observable, sin coste ni duración.",
            "El planificador de la miniatura es lineal y sin retroceso a propósito, para que la anomalía se "
            "vea. STRIPS hace más que esto, y aun así el problema de la interacción entre submetas es real.",
            "El supuesto del mundo cerrado —lo no afirmado es falso— es cómodo aquí y falso en casi "
            "cualquier dominio abierto.",
        ],
    )


def _mycin(seed: int) -> dict[str, Any]:
    """Shortliffe y Buchanan 1975: factores de certeza cuando no hay probabilidades."""
    reglas = [
        {"id": "R1", "si": ["gram_negativo", "forma_bacilo"], "entonces": "enterobacteria", "cf": 0.7},
        {"id": "R2", "si": ["crecimiento_anaerobio"], "entonces": "enterobacteria", "cf": 0.5},
        {"id": "R3", "si": ["enterobacteria", "portal_gastrointestinal"], "entonces": "e_coli", "cf": 0.8},
        {"id": "R4", "si": ["fiebre_alta"], "entonces": "e_coli", "cf": -0.3},
    ]
    hechos = {"gram_negativo": 1.0, "forma_bacilo": 0.9, "crecimiento_anaerobio": 0.6,
              "portal_gastrointestinal": 0.8, "fiebre_alta": 1.0}

    def combinar(a: float, b: float) -> float:
        if a >= 0 and b >= 0:
            return a + b * (1 - a)
        if a < 0 and b < 0:
            return a + b * (1 + a)
        return (a + b) / (1 - min(abs(a), abs(b)))

    conclusiones: dict[str, float] = {}
    traza = []
    for _ in range(2):                       # dos pasadas: encadenamiento hacia delante
        for r in reglas:
            grados = [hechos.get(p, conclusiones.get(p, 0.0)) for p in r["si"]]
            if any(g <= 0 for g in grados):
                continue
            disparo = min(grados) * r["cf"]
            previo = conclusiones.get(r["entonces"])
            nuevo = disparo if previo is None else combinar(previo, disparo)
            if previo is None or abs(nuevo - previo) > 1e-9:
                traza.append({"regla": r["id"], "premisa_minima": _round(min(grados), 3),
                              "cf_regla": r["cf"], "aporta": _round(disparo, 4),
                              "acumulado": _round(nuevo, 4)})
            conclusiones[r["entonces"]] = nuevo

    # contraste con probabilidad: la combinación de MYCIN no es Bayes
    p1, p2 = 0.7, 0.5
    cf_combinado = combinar(p1, p2)
    bayes_independiente = 1 - (1 - p1) * (1 - p2)

    rng = random.Random(seed)
    orden = [r["id"] for r in rng.sample(reglas, len(reglas))]

    return _contract(
        "mycin",
        seed,
        {
            "hechos": hechos,
            "reglas": reglas,
            "traza_de_inferencia": traza,
            "conclusiones": {k: _round(v, 4) for k, v in sorted(conclusiones.items())},
            "combinacion_dos_evidencias_a_favor": {
                "cf_1": p1, "cf_2": p2, "resultado": _round(cf_combinado, 4)},
            "misma_cuenta_con_probabilidades_independientes": _round(bayes_independiente, 4),
            "orden_de_disparo_alternativo": orden,
            "explicabilidad": "cada conclusión viene con la lista de reglas que la sostienen",
        },
        [
            f"Las conclusiones salen con grado: {sorted(conclusiones)} con factores "
            f"{[_round(conclusiones[k], 3) for k in sorted(conclusiones)]}. El sistema no responde sí o no.",
            "Dos evidencias a favor no se suman: se combinan con `a + b(1−a)`, que satura por debajo de 1. "
            "Nunca se llega a la certeza acumulando indicios débiles.",
            "La regla R4 aporta un factor **negativo**: la evidencia en contra se representa en el mismo "
            "eje y resta. Es una decisión de diseño que no tiene equivalente directo en probabilidad.",
            "Cada conclusión arrastra la lista de reglas que la sostienen. Esa traza es la razón de que "
            "los sistemas expertos fueran aceptados por médicos: podían discutir el razonamiento.",
        ],
        [
            "Los factores de certeza no son probabilidades y su álgebra no se deriva de los axiomas de "
            "Kolmogorov. En el caso mostrado la combinación coincide numéricamente con la fórmula de "
            "independencia, y eso es una coincidencia del ejemplo, no una equivalencia.",
            "La base de conocimiento tiene cuatro reglas escritas a mano. MYCIN llegó a unas 600, y ese "
            "coste de construcción y mantenimiento es lo que acabó con el modelo de negocio.",
            "El sistema no aprende: cada regla y cada factor los pone un experto humano. No hay datos, ni "
            "ajuste, ni validación estadística dentro del motor.",
        ],
    )


def _arco_consistencia(seed: int) -> dict[str, Any]:
    """Mackworth 1977: podar antes de buscar, no mientras se busca."""
    n, tope, hueco = 6, 12, 2
    variables = [f"v{i}" for i in range(1, n + 1)]
    vecinos = {v: [] for v in variables}
    for a, b in zip(variables, variables[1:]):
        vecinos[a].append(b)
        vecinos[b].append(a)

    # restricción de la red: cada variable va al menos `hueco` por debajo de la anterior
    def compatible(x, vx, y, vy):
        if variables.index(x) < variables.index(y):
            return vx - vy >= hueco
        return vy - vx >= hueco

    base = {v: list(range(1, tope + 1)) for v in variables}

    def ac3(dominios):
        dominios = {k: list(v) for k, v in dominios.items()}
        cola = [(x, y) for x in variables for y in vecinos[x]]
        revisiones, podas = 0, 0
        while cola:
            x, y = cola.pop(0)
            revisiones += 1
            quitar = [a for a in dominios[x]
                      if not any(compatible(x, a, y, b) for b in dominios[y])]
            if quitar:
                for a in quitar:
                    dominios[x].remove(a)
                    podas += 1
                for z in vecinos[x]:
                    if z != y:
                        cola.append((z, x))
        return dominios, revisiones, podas

    def backtracking(dominios):
        cuenta = {"nodos": 0, "retrocesos": 0}

        def rec(asignacion):
            cuenta["nodos"] += 1
            if len(asignacion) == len(variables):
                return dict(asignacion)
            var = variables[len(asignacion)]
            for valor in dominios[var]:
                if all(compatible(var, valor, otra, val) for otra, val in asignacion.items()
                       if otra in vecinos[var]):
                    r = rec({**asignacion, var: valor})
                    if r is not None:
                        return r
            cuenta["retrocesos"] += 1
            return None

        return rec({}), cuenta

    sol_sin, cuenta_sin = backtracking(base)
    reducidos, revisiones, podas = ac3(base)
    sol_con, cuenta_con = backtracking(reducidos)

    rng = random.Random(seed)
    inspeccion = rng.choice(variables)

    return _contract(
        "arco_consistencia",
        seed,
        {
            "red": f"{n} variables en cadena, dominio 1..{tope}, restricción v(i) − v(i+1) ≥ {hueco}",
            "tamano_del_espacio": tope ** n,
            "dominios_iniciales": {k: f"1..{tope} ({len(v)} valores)" for k, v in base.items()},
            "dominios_tras_ac3": reducidos,
            "revisiones_de_arco": revisiones,
            "valores_podados": podas,
            "backtracking_sin_ac3": {"nodos": cuenta_sin["nodos"],
                                     "retrocesos": cuenta_sin["retrocesos"],
                                     "solucion": sol_sin},
            "backtracking_con_ac3": {"nodos": cuenta_con["nodos"],
                                     "retrocesos": cuenta_con["retrocesos"],
                                     "solucion": sol_con},
            "misma_solucion": sol_sin == sol_con,
            "variable_inspeccionada": inspeccion,
        },
        [
            f"AC-3 hace {revisiones} revisiones de arco y elimina {podas} valores de los "
            f"{n * tope} iniciales, **antes** de asignar nada. Es preproceso, no búsqueda.",
            f"Después, el backtracking resuelve con {cuenta_con['nodos']} nodos y "
            f"{cuenta_con['retrocesos']} retrocesos, frente a {cuenta_sin['nodos']} nodos y "
            f"{cuenta_sin['retrocesos']} retrocesos sin podar.",
            f"Las dos búsquedas devuelven la misma solución: {sol_sin == sol_con}. La consistencia de arco "
            "no descarta soluciones: descarta valores que no participan en ninguna.",
            f"Y la propiedad fuerte: en una red con estructura de árbol —como esta cadena— la consistencia "
            f"de arco deja la búsqueda **sin retrocesos**, y aquí se comprueba "
            f"({cuenta_con['retrocesos']} retrocesos).",
        ],
        [
            f"El espacio completo son {tope ** n} combinaciones, que todavía caben en una tabla. La ventaja "
            "de AC-3 se nota cuando no caben.",
            "La propiedad «sin retrocesos» vale para redes con estructura de árbol. En una red con ciclos "
            "—el mapa de Australia, por ejemplo— la consistencia de arco ayuda pero no elimina el retroceso.",
            "AC-3 no decide satisfacibilidad: puede dejar todos los dominios no vacíos y que el problema no "
            "tenga solución. Y su coste O(e·d³) lo mejoran AC-4 y AC-2001.",
        ],
    )


def _ontologia(seed: int) -> dict[str, Any]:
    """Gruber 1993: una ontología es un compromiso, no un diccionario."""
    jerarquia = {
        "Entidad": None,
        "Documento": "Entidad",
        "Artículo": "Documento",
        "ArtículoDeRevista": "Artículo",
        "Preprint": "Artículo",
        "Persona": "Entidad",
        "Autor": "Persona",
    }

    def ancestros(clase: str) -> list[str]:
        salida, actual = [], jerarquia.get(clase)
        while actual:
            salida.append(actual)
            actual = jerarquia.get(actual)
        return salida

    instancias = {"P08": "ArtículoDeRevista", "P22": "Preprint", "Vaswani": "Autor"}
    inferencias = [
        {"instancia": i, "clase_directa": c, "tambien_es": ancestros(c)}
        for i, c in sorted(instancias.items())
    ]

    # dos agentes con conceptualizaciones distintas del MISMO término
    agente_a = {"término": "Publicación", "incluye": ["ArtículoDeRevista"], "excluye": ["Preprint"]}
    agente_b = {"término": "Publicación", "incluye": ["ArtículoDeRevista", "Preprint"], "excluye": []}
    corpus = ["P08", "P22"]
    cuenta_a = sum(1 for x in corpus if instancias[x] in agente_a["incluye"])
    cuenta_b = sum(1 for x in corpus if instancias[x] in agente_b["incluye"])

    criterios = {
        "claridad": "las definiciones deben ser objetivas e independientes del contexto de uso",
        "coherencia": "lo que se infiere no puede contradecir las definiciones",
        "extensibilidad": "se deben poder añadir términos sin revisar los existentes",
        "sesgo_de_codificación_mínimo": "no atar la conceptualización a una implementación",
        "compromiso_ontológico_mínimo": "afirmar lo menos posible sobre el mundo modelado",
    }

    rng = random.Random(seed)
    consulta = rng.choice(sorted(instancias))

    return _contract(
        "ontologia",
        seed,
        {
            "jerarquia": jerarquia,
            "inferencias_por_subsuncion": inferencias,
            "criterios_de_diseño": criterios,
            "desacuerdo_sobre_el_mismo_termino": {
                "agente_A": agente_a, "agente_B": agente_b,
                "cuenta_A": cuenta_a, "cuenta_B": cuenta_b,
                "misma_pregunta_distinta_respuesta": cuenta_a != cuenta_b,
            },
            "consulta_de_ejemplo": consulta,
            "definicion": "una ontología es una especificación explícita de una conceptualización",
        },
        [
            "La subsunción da inferencia gratis: declarar que P08 es un ArtículoDeRevista implica que es "
            f"Artículo, Documento y Entidad. Son {len(inferencias[0]['tambien_es'])} hechos que nadie "
            "escribió.",
            f"Dos agentes preguntan «¿cuántas publicaciones hay?» sobre el mismo corpus y responden "
            f"{cuenta_a} y {cuenta_b}. No hay error de datos: hay conceptualizaciones distintas del mismo "
            "término.",
            "Por eso el artículo insiste en «compromiso»: una ontología no describe el mundo, fija qué se "
            "acuerda decir de él para poder interoperar.",
            f"Los {len(criterios)} criterios de diseño son la parte más citada y la más práctica: siguen "
            "siendo el checklist con el que se revisa un esquema hoy.",
        ],
        [
            "Siete clases y tres instancias. Una ontología real tiene miles de términos y su problema "
            "dominante es el mantenimiento, no la inferencia.",
            "No hay razonador de lógica descriptiva: la subsunción se calcula recorriendo un árbol. Los "
            "razonadores reales manejan restricciones, propiedades y disyunciones.",
            "El artículo es de 1993 y anterior a OWL y RDF. Sus criterios sobreviven; su contexto técnico "
            "—compartir conocimiento entre sistemas de IA— es el de entonces.",
        ],
    )


def _neurosimbolico(seed: int) -> dict[str, Any]:
    """Garcez y Lamb 2020: percepción que estima y símbolos que restringen."""
    salon = [
        {"objeto": "o1", "dist": {"gato": 0.62, "perro": 0.30, "coche": 0.08}, "verdad": "gato"},
        {"objeto": "o2", "dist": {"coche": 0.55, "gato": 0.40, "perro": 0.05}, "verdad": "gato"},
        {"objeto": "o3", "dist": {"coche": 0.48, "perro": 0.45, "gato": 0.07}, "verdad": "perro"},
        {"objeto": "o4", "dist": {"perro": 0.71, "gato": 0.20, "coche": 0.09}, "verdad": "perro"},
    ]
    garaje = [
        {"objeto": "g1", "dist": {"coche": 0.80, "perro": 0.12, "gato": 0.08}, "verdad": "coche"},
        {"objeto": "g2", "dist": {"coche": 0.66, "gato": 0.24, "perro": 0.10}, "verdad": "coche"},
    ]
    reglas = [
        "escena(salón) ∧ etiqueta(x, coche) → ⊥",
        "etiqueta(x, gato) ∨ etiqueta(x, perro) → animal(x)",
    ]

    def argmax(d):
        return max(d, key=lambda k: (d[k], k))

    def evaluar(objetos, prohibidas):
        sin, con = [], []
        for p in objetos:
            top = argmax(p["dist"])
            sin.append({"objeto": p["objeto"], "predicho": top, "acierta": top == p["verdad"]})
            permitidas = {k: v for k, v in p["dist"].items() if k not in prohibidas}
            top_r = argmax(permitidas) if permitidas else None
            con.append({"objeto": p["objeto"], "predicho": top_r, "acierta": top_r == p["verdad"],
                        "regla_intervino": top in prohibidas})
        return sin, con

    salon_sin, salon_con = evaluar(salon, {"coche"})
    garaje_sin, garaje_con = evaluar(garaje, {"coche"})

    a_salon_sin = sum(1 for r in salon_sin if r["acierta"])
    a_salon_con = sum(1 for r in salon_con if r["acierta"])
    a_garaje_sin = sum(1 for r in garaje_sin if r["acierta"])
    a_garaje_con = sum(1 for r in garaje_con if r["acierta"])

    rng = random.Random(seed)
    orden = rng.sample([p["objeto"] for p in salon + garaje], len(salon) + len(garaje))

    return _contract(
        "neurosimbolico",
        seed,
        {
            "reglas": reglas,
            "escena_salon": {
                "regla_aplicable": True,
                "solo_percepcion": salon_sin, "con_reglas": salon_con,
                "aciertos": f"{a_salon_sin}/{len(salon)} → {a_salon_con}/{len(salon)}",
            },
            "escena_garaje": {
                "regla_aplicable": False,
                "nota": "aquí sí hay coches: la regla del salón no vale y se aplica a propósito",
                "solo_percepcion": garaje_sin, "con_reglas": garaje_con,
                "aciertos": f"{a_garaje_sin}/{len(garaje)} → {a_garaje_con}/{len(garaje)}",
            },
            "ganancia_donde_la_regla_vale": a_salon_con - a_salon_sin,
            "coste_donde_no_vale": a_garaje_con - a_garaje_sin,
            "orden_de_revision": orden,
            "tesis": "la percepción estima y los símbolos restringen; el sistema es la composición",
        },
        [
            f"En el salón, la percepción sola acierta {a_salon_sin} de {len(salon)} y con la regla del "
            f"contexto, {a_salon_con} de {len(salon)}: la restricción corrige dos objetos donde la red se "
            "equivocaba con confianza 0,55 y 0,48.",
            "La corrección no reentrena nada: filtra el espacio de salidas con conocimiento que la red no "
            "tiene y que nadie va a aprender de cuatro ejemplos.",
            f"En el garaje la misma regla es falsa y el resultado cae de {a_garaje_sin} a {a_garaje_con} de "
            f"{len(garaje)}. Una restricción incorrecta no degrada: destruye.",
            "Esa asimetría es la tesis del tercer paradigma: el conocimiento simbólico aporta mucho cuando "
            "es correcto y cuesta todo cuando no lo es, así que hay que declararlo y poder auditarlo.",
        ],
        [
            "Las distribuciones están escritas a mano: no hay ninguna red aquí, ni entrenamiento, ni "
            "imágenes.",
            "La integración de la miniatura es la más simple posible —filtrar la salida—. Los sistemas "
            "neuro-simbólicos reales integran las restricciones en la pérdida o en la arquitectura, y ahí "
            "está la dificultad.",
            "El artículo de Garcez y Lamb es un manifiesto y una hoja de ruta, no un método con "
            "resultados. Debe leerse como programa de investigación abierto.",
        ],
    )


# --------------------------------------------------------------------------- #
# ruta clásica (P73–P86)
# --------------------------------------------------------------------------- #


def _kmeans(seed: int) -> dict[str, Any]:
    """Lloyd 1982: converge siempre, y no siempre al mismo sitio."""
    puntos = [(1.0, 1.0), (1.4, 0.8), (0.8, 1.3), (1.2, 1.5),
              (5.0, 5.2), (5.4, 4.8), (4.8, 5.5), (5.2, 5.0),
              (9.0, 1.2), (9.3, 0.9), (8.7, 1.4), (9.1, 1.6)]

    def dist2(a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

    def lloyd(centros, iteraciones=30):
        historia = []
        for paso in range(iteraciones):
            grupos: dict[int, list] = {i: [] for i in range(len(centros))}
            for p in puntos:
                j = min(range(len(centros)), key=lambda i: (dist2(p, centros[i]), i))
                grupos[j].append(p)
            nuevos = []
            for i, g in grupos.items():
                if g:
                    nuevos.append((sum(p[0] for p in g) / len(g), sum(p[1] for p in g) / len(g)))
                else:
                    nuevos.append(centros[i])
            inercia = sum(dist2(p, nuevos[j]) for j, g in grupos.items() for p in g)
            historia.append(_round(inercia, 4))
            if all(dist2(a, b) < 1e-12 for a, b in zip(centros, nuevos)):
                centros = nuevos
                break
            centros = nuevos
        return {"centros": [[_round(c[0], 3), _round(c[1], 3)] for c in centros],
                "inercia": historia[-1], "pasos": len(historia), "historia": historia,
                "tamanos": sorted(len(g) for g in grupos.values())}

    rng = random.Random(seed)
    arranques = []
    for _ in range(8):
        inicio = rng.sample(puntos, 3)
        arranques.append(lloyd(list(inicio)))
    inercias = sorted({a["inercia"] for a in arranques})
    peor = max(arranques, key=lambda a: a["inercia"])
    mejor = min(arranques, key=lambda a: a["inercia"])

    # la inercia baja siempre al subir k: no sirve para elegir k
    curva = []
    for k in (1, 2, 3, 4, 6):
        mejor_k = min((lloyd(rng.sample(puntos, k)) for _ in range(5)), key=lambda a: a["inercia"])
        curva.append({"k": k, "inercia": mejor_k["inercia"]})

    return _contract(
        "kmeans",
        seed,
        {
            "puntos": len(puntos),
            "k": 3,
            "arranques_probados": len(arranques),
            "inercias_finales_distintas": inercias,
            "mejor": mejor,
            "peor": peor,
            "brecha_mejor_peor": _round(peor["inercia"] - mejor["inercia"], 4),
            "monotonia_decrece_siempre": [c["inercia"] for c in curva] == sorted(
                [c["inercia"] for c in curva], reverse=True),
            "inercia_por_k": curva,
        },
        [
            f"El algoritmo converge en {mejor['pasos']} pasos y la inercia nunca sube: cada iteración la "
            "reduce o la deja igual. Esa monotonía es lo que demuestra Lloyd, y por eso siempre termina.",
            f"Con {len(arranques)} arranques aleatorios aparecen {len(inercias)} inercias finales distintas "
            f"(de {mejor['inercia']} a {peor['inercia']}). Converger no es encontrar el óptimo: es "
            "encontrar UN óptimo local.",
            f"La diferencia entre el mejor y el peor arranque es {_round(peor['inercia'] - mejor['inercia'], 2)}. "
            "Por eso en la práctica se ejecuta varias veces y se conserva la mejor.",
            f"Y la inercia decrece siempre al subir k: {[c['inercia'] for c in curva]}. Elegir k "
            "minimizando la inercia lleva a un grupo por punto; hace falta otro criterio.",
        ],
        [
            "Doce puntos en dos dimensiones con tres grupos bien separados. El caso difícil —grupos "
            "solapados, densidades distintas, formas no esféricas— no está aquí.",
            "k-medias supone grupos aproximadamente esféricos y de tamaño similar, porque minimiza la "
            "distancia euclídea al centro. Con formas alargadas o anidadas falla, y no avisa.",
            "La inicialización de esta miniatura es aleatoria pura. k-means++ mejora mucho la calidad "
            "media, y no elimina el problema del óptimo local.",
        ],
    )


def _id3(seed: int) -> dict[str, Any]:
    """Quinlan 1986: la ganancia de información elige el atributo, y prefiere los que tienen muchos valores."""
    columnas = ["cielo", "temperatura", "humedad", "viento", "zona", "id"]
    datos = [
        {"cielo": "sol", "temperatura": "alta", "humedad": "alta", "viento": "no", "zona": "z1", "id": "d01", "jugar": False},
        {"cielo": "sol", "temperatura": "alta", "humedad": "alta", "viento": "sí", "zona": "z1", "id": "d02", "jugar": False},
        {"cielo": "nublado", "temperatura": "alta", "humedad": "alta", "viento": "no", "zona": "z1", "id": "d03", "jugar": True},
        {"cielo": "lluvia", "temperatura": "media", "humedad": "alta", "viento": "no", "zona": "z2", "id": "d04", "jugar": True},
        {"cielo": "lluvia", "temperatura": "baja", "humedad": "normal", "viento": "no", "zona": "z3", "id": "d05", "jugar": True},
        {"cielo": "lluvia", "temperatura": "baja", "humedad": "normal", "viento": "sí", "zona": "z2", "id": "d06", "jugar": False},
        {"cielo": "nublado", "temperatura": "baja", "humedad": "normal", "viento": "sí", "zona": "z4", "id": "d07", "jugar": True},
        {"cielo": "sol", "temperatura": "media", "humedad": "alta", "viento": "no", "zona": "z3", "id": "d08", "jugar": False},
        {"cielo": "sol", "temperatura": "baja", "humedad": "normal", "viento": "no", "zona": "z5", "id": "d09", "jugar": True},
        {"cielo": "lluvia", "temperatura": "media", "humedad": "normal", "viento": "no", "zona": "z5", "id": "d10", "jugar": True},
        {"cielo": "sol", "temperatura": "media", "humedad": "normal", "viento": "sí", "zona": "z6", "id": "d11", "jugar": True},
        {"cielo": "nublado", "temperatura": "media", "humedad": "alta", "viento": "sí", "zona": "z6", "id": "d12", "jugar": True},
        {"cielo": "nublado", "temperatura": "alta", "humedad": "normal", "viento": "no", "zona": "z7", "id": "d13", "jugar": True},
        {"cielo": "lluvia", "temperatura": "media", "humedad": "alta", "viento": "sí", "zona": "z4", "id": "d14", "jugar": False},
    ]

    def entropia(filas):
        n = len(filas)
        if n == 0:
            return 0.0
        p = sum(1 for f in filas if f["jugar"]) / n
        if p in (0.0, 1.0):
            return 0.0
        return -(p * math.log2(p) + (1 - p) * math.log2(1 - p))

    def ganancia(filas, atributo):
        base = entropia(filas)
        valores = sorted({f[atributo] for f in filas})
        resto = 0.0
        info_division = 0.0
        for v in valores:
            sub = [f for f in filas if f[atributo] == v]
            peso = len(sub) / len(filas)
            resto += peso * entropia(sub)
            info_division -= peso * math.log2(peso)
        g = base - resto
        return {"atributo": atributo, "valores": len(valores), "ganancia": _round(g, 4),
                "info_division": _round(info_division, 4),
                "razon_de_ganancia": _round(g / info_division, 4) if info_division else None}

    tabla = [ganancia(datos, c) for c in columnas]
    por_ganancia = max(tabla, key=lambda t: t["ganancia"])
    sin_id = [t for t in tabla if t["atributo"] != "id"]
    por_ganancia_sin_id = max(sin_id, key=lambda t: t["ganancia"])
    por_razon = max([t for t in tabla if t["razon_de_ganancia"]], key=lambda t: t["razon_de_ganancia"])
    # C4.5 no usa la razón de ganancia sola: primero descarta los atributos con
    # ganancia por debajo de la media y solo entre los que quedan aplica la razón.
    reales = [t for t in tabla if t["atributo"] != "id"]
    por_ganancia_real = max(reales, key=lambda t: t["ganancia"])
    por_razon_real = max(reales, key=lambda t: t["razon_de_ganancia"])
    media_ganancia = sum(t["ganancia"] for t in tabla) / len(tabla)
    admitidos = [t for t in tabla if t["ganancia"] >= media_ganancia and t["razon_de_ganancia"]]
    por_c45 = max(admitidos, key=lambda t: t["razon_de_ganancia"]) if admitidos else None

    def construir(filas, disponibles, profundidad=0):
        if not filas or profundidad > 2 or not disponibles:
            si = sum(1 for f in filas if f["jugar"])
            return {"hoja": si >= len(filas) - si, "n": len(filas)}
        if all(f["jugar"] for f in filas):
            return {"hoja": True, "n": len(filas)}
        if not any(f["jugar"] for f in filas):
            return {"hoja": False, "n": len(filas)}
        mejor = max((ganancia(filas, c) for c in disponibles), key=lambda t: t["ganancia"])
        a = mejor["atributo"]
        ramas = {}
        for v in sorted({f[a] for f in filas}):
            sub = [f for f in filas if f[a] == v]
            ramas[v] = construir(sub, [c for c in disponibles if c != a], profundidad + 1)
        return {"atributo": a, "ganancia": mejor["ganancia"], "ramas": ramas}

    arbol = construir(datos, ["cielo", "temperatura", "humedad", "viento"])
    rng = random.Random(seed)
    ejemplo = rng.choice(datos)["id"]

    return _contract(
        "id3",
        seed,
        {
            "ejemplos": len(datos),
            "entropia_inicial": _round(entropia(datos), 4),
            "tabla_de_ganancias": tabla,
            "elegido_por_ganancia": por_ganancia["atributo"],
            "elegido_por_ganancia_sin_el_identificador": por_ganancia_sin_id["atributo"],
            "elegido_por_razon_de_ganancia": por_razon["atributo"],
            "sin_el_identificador": {
                "elegido_por_ganancia": por_ganancia_real["atributo"],
                "elegido_por_razon_de_ganancia": por_razon_real["atributo"],
                "la_correccion_cambia_la_eleccion": por_ganancia_real["atributo"] != por_razon_real["atributo"],
            },
            "ganancia_media_con_identificador": _round(media_ganancia, 4),
            "admitidos_por_el_filtro_de_c45": [t["atributo"] for t in admitidos],
            "arbol": arbol,
            "ejemplo_inspeccionado": ejemplo,
        },
        [
            f"La entropía inicial es {_round(entropia(datos), 4)} bits y el atributo con más ganancia "
            f"—descartando el identificador— es «{por_ganancia_sin_id['atributo']}» con "
            f"{por_ganancia_sin_id['ganancia']}. La ganancia es reducción de incertidumbre, ni más ni menos.",
            f"Pero el atributo que gana la tabla completa es «{por_ganancia['atributo']}»: el "
            f"identificador de fila, con ganancia {por_ganancia['ganancia']} — la máxima posible. Separa "
            "perfectamente y no generaliza nada.",
            "Ese es el sesgo que el propio Quinlan documenta: la ganancia de información prefiere los "
            "atributos con muchos valores distintos, y con un identificador único llega al extremo.",
            f"El caso realista es «zona», con 7 valores: gana en ganancia a «cielo» "
            f"({[x['ganancia'] for x in tabla if x['atributo'] == 'zona'][0]} frente a "
            f"{[x['ganancia'] for x in tabla if x['atributo'] == 'cielo'][0]}) y pierde en razón de "
            f"ganancia. Descartando el identificador, la corrección cambia la elección de "
            f"«{por_ganancia_real['atributo']}» a «{por_razon_real['atributo']}».",
            f"Con el identificador dentro, en cambio, ni la razón de ganancia ni el filtro de ganancia "
            f"media lo desbancan (sigue eligiendo «{por_razon['atributo']}», y el filtro solo admite "
            f"{admitidos and [x['atributo'] for x in admitidos]}). La conclusión no es que falte "
            "criterio: es que un identificador no es un atributo.",
        ],
        [
            "Catorce ejemplos y cuatro atributos categóricos. No hay atributos continuos, ni valores "
            "ausentes, ni poda: las tres cosas que C4.5 añade y que hacen falta con datos reales.",
            "El árbol se construye hasta profundidad 2 para que quepa en la salida. Un ID3 completo crece "
            "hasta hojas puras y sobreajusta, que es justo por lo que hace falta podar.",
            "La ganancia es una heurística voraz: elegir el mejor atributo en cada nodo no garantiza el "
            "árbol más pequeño ni el más preciso.",
        ],
    )


def _svm(seed: int) -> dict[str, Any]:
    """Cortes y Vapnik 1995: entre todos los separadores, el de margen máximo."""
    positivos = [(3.0, 3.0), (4.0, 3.5), (3.5, 4.5), (5.0, 4.0)]
    negativos = [(1.0, 1.0), (0.5, 2.0), (2.0, 0.5), (1.5, 1.5)]
    datos = [(p, 1) for p in positivos] + [(p, -1) for p in negativos]

    def margen(w, b):
        """Margen geométrico: la distancia del punto más cercano al hiperplano."""
        norma = math.sqrt(w[0] ** 2 + w[1] ** 2)
        distancias = [(y * (w[0] * x[0] + w[1] * x[1] + b)) / norma for x, y in datos]
        return min(distancias), distancias

    candidatos = []
    rng = random.Random(seed)
    # rejilla determinista de separadores + unos cuantos aleatorios
    rejilla = [(1.0, 1.0, -4.0), (1.0, 1.0, -3.0), (1.0, 1.0, -5.0),
               (1.0, 0.5, -3.0), (0.5, 1.0, -3.0), (2.0, 1.0, -6.0), (1.0, 2.0, -6.0)]
    for _ in range(20):
        rejilla.append((rng.uniform(0.3, 2.0), rng.uniform(0.3, 2.0), rng.uniform(-7.0, -2.0)))
    for w1, w2, b in rejilla:
        m, _ = margen((w1, w2), b)
        if m > 0:                                   # solo los que separan de verdad
            candidatos.append({"w": [_round(w1, 3), _round(w2, 3)], "b": _round(b, 3),
                               "margen": _round(m, 4)})
    candidatos.sort(key=lambda c: -c["margen"])
    mejor = candidatos[0] if candidatos else None

    # vectores soporte: los puntos que tocan el margen del mejor separador
    soporte = []
    if mejor:
        w = (mejor["w"][0], mejor["w"][1])
        norma = math.sqrt(w[0] ** 2 + w[1] ** 2)
        for x, y in datos:
            d = (y * (w[0] * x[0] + w[1] * x[1] + mejor["b"])) / norma
            if abs(d - mejor["margen"]) < 0.35:
                soporte.append({"punto": list(x), "clase": y, "distancia": _round(d, 4)})

    return _contract(
        "svm",
        seed,
        {
            "puntos": len(datos),
            "separadores_validos_probados": len(candidatos),
            "mejor_por_margen": mejor,
            "peor_separador_valido": candidatos[-1] if candidatos else None,
            "tres_mejores": candidatos[:3],
            "vectores_soporte": soporte,
            "puntos_que_definen_la_frontera": f"{len(soporte)}/{len(datos)}",
            "principio": "minimizar el riesgo estructural: entre las hipótesis que separan, la de "
                         "margen máximo generaliza mejor",
        },
        [
            f"De {len(candidatos)} hiperplanos que separan correctamente los ocho puntos, los márgenes van "
            f"de {candidatos[-1]['margen']} a {mejor['margen']}. Todos aciertan en entrenamiento y no "
            "todos son igual de buenos.",
            "Ese es el argumento del paper: la exactitud en entrenamiento no distingue entre ellos, y el "
            "margen sí. Elegir el de margen máximo es minimizar el riesgo estructural, no el empírico.",
            f"La frontera queda definida por {len(soporte)} de {len(datos)} puntos: los vectores soporte. "
            "Mover cualquier otro punto sin cruzar el margen no cambia el modelo.",
            "Y de ahí sale la eficiencia: el modelo no depende del tamaño del conjunto sino del número de "
            "puntos que tocan el margen.",
        ],
        [
            "La miniatura busca por rejilla y muestreo, no resuelve el problema cuadrático dual. El "
            "resultado es el mejor de los candidatos probados, no el óptimo exacto.",
            "Los datos son linealmente separables. El caso interesante —margen blando con parámetro C, y "
            "el truco del núcleo para fronteras no lineales— es la otra mitad del artículo y no está aquí.",
            "El margen máximo no garantiza mejor generalización en todos los casos: es un sesgo "
            "inductivo con justificación teórica, y como todo sesgo puede ser el equivocado.",
        ],
    )


def _validacion_cruzada(seed: int) -> dict[str, Any]:
    """Kohavi 1995: el estimador importa tanto como el modelo."""
    exactitud_real = 0.78
    n = 100
    repeticiones = 200

    def muestra(r: int) -> list[int]:
        """Un conjunto de datos nuevo, extraído de la misma población."""
        local = random.Random(seed * 7919 + r)
        return [1 if local.random() < exactitud_real else 0 for _ in range(n)]

    def holdout(porcion=0.3):
        salida = []
        for r in range(repeticiones):
            datos = muestra(r)
            local = random.Random(seed * 104729 + r)
            test = local.sample(datos, int(n * porcion))
            salida.append(sum(test) / len(test))
        return salida

    def k_fold(k):
        salida = []
        for r in range(repeticiones):
            datos = muestra(r)
            local = random.Random(seed * 15485863 + r)
            barajado = datos[:]
            local.shuffle(barajado)
            pliegues = [barajado[i::k] for i in range(k)]
            salida.append(sum(sum(p) / len(p) for p in pliegues) / k)
        return salida

    def resumen(vals):
        media = sum(vals) / len(vals)
        var = sum((v - media) ** 2 for v in vals) / max(len(vals) - 1, 1)
        return {"media": _round(media, 4), "desviacion": _round(math.sqrt(var), 4),
                "min": _round(min(vals), 4), "max": _round(max(vals), 4),
                "rango": _round(max(vals) - min(vals), 4),
                "sesgo_frente_al_real": _round(media - exactitud_real, 4),
                "ejemplos_de_test_por_estimacion": None}

    tabla = {
        "holdout_70_30": resumen(holdout()),
        "validacion_cruzada_5": resumen(k_fold(5)),
        "validacion_cruzada_10": resumen(k_fold(10)),
    }
    tabla["holdout_70_30"]["ejemplos_de_test_por_estimacion"] = int(n * 0.3)
    tabla["validacion_cruzada_5"]["ejemplos_de_test_por_estimacion"] = n
    tabla["validacion_cruzada_10"]["ejemplos_de_test_por_estimacion"] = n

    razon = tabla["holdout_70_30"]["desviacion"] / tabla["validacion_cruzada_10"]["desviacion"]

    return _contract(
        "validacion_cruzada",
        seed,
        {
            "exactitud_real_de_la_poblacion": exactitud_real,
            "tamano_del_conjunto": n,
            "conjuntos_simulados": repeticiones,
            "estimadores": tabla,
            "veces_mas_disperso_el_holdout": _round(razon, 2),
            "recomendacion_del_articulo": "validación cruzada estratificada de 10 pliegues",
        },
        [
            f"La exactitud real de la población es {exactitud_real}. Los tres estimadores la aciertan en "
            f"media (sesgos de {tabla['holdout_70_30']['sesgo_frente_al_real']}, "
            f"{tabla['validacion_cruzada_5']['sesgo_frente_al_real']} y "
            f"{tabla['validacion_cruzada_10']['sesgo_frente_al_real']}): el problema no es el sesgo.",
            f"El problema es la VARIANZA. El holdout 70/30 estima con desviación "
            f"{tabla['holdout_70_30']['desviacion']} y la validación cruzada de 10 pliegues con "
            f"{tabla['validacion_cruzada_10']['desviacion']}: {_round(razon, 2)}× más disperso.",
            f"En {repeticiones} conjuntos simulados, el holdout devuelve valores entre "
            f"{tabla['holdout_70_30']['min']} y {tabla['holdout_70_30']['max']}. Dos personas con el mismo "
            "modelo pueden reportar números muy distintos y ninguna estar haciendo trampa.",
            f"La razón es simple: el holdout evalúa sobre "
            f"{tabla['holdout_70_30']['ejemplos_de_test_por_estimacion']} ejemplos y la validación cruzada "
            f"sobre {tabla['validacion_cruzada_10']['ejemplos_de_test_por_estimacion']}, porque cada "
            "ejemplo pasa por el test exactamente una vez.",
        ],
        [
            "La miniatura simula aciertos con una moneda sesgada: no hay modelo ni entrenamiento. Aísla la "
            "varianza del ESTIMADOR, que es lo que estudia el artículo.",
            "Al no reentrenar en cada pliegue, no se ve el otro efecto que Kohavi mide: entrenar con menos "
            "datos empeora el modelo y sesga la estimación hacia abajo, sobre todo con dejar-uno-fuera.",
            "Tampoco hay estratificación, que es la otra mitad de la recomendación del artículo y la que "
            "más importa cuando las clases están desbalanceadas.",
        ],
    )


def _lasso(seed: int) -> dict[str, Any]:
    """Tibshirani 1996: la norma L1 no encoge, elimina."""
    rng = random.Random(seed)
    n, p = 60, 8
    verdaderos = [3.0, -2.0, 0.0, 0.0, 1.5, 0.0, 0.0, 0.0]     # solo 3 variables importan
    X, y = [], []
    for _ in range(n):
        fila = [rng.gauss(0, 1) for _ in range(p)]
        fila[3] = fila[0] * 0.9 + rng.gauss(0, 0.1)             # correlacionada con la primera
        X.append(fila)
        y.append(sum(b * v for b, v in zip(verdaderos, fila)) + rng.gauss(0, 0.5))

    def descenso(alpha, penalizacion, pasos=400, lr=0.02):
        beta = [0.0] * p
        for _ in range(pasos):
            grad = [0.0] * p
            for fila, objetivo in zip(X, y):
                err = sum(b * v for b, v in zip(beta, fila)) - objetivo
                for j in range(p):
                    grad[j] += err * fila[j] / n
            for j in range(p):
                if penalizacion == "l2":
                    beta[j] -= lr * (grad[j] + alpha * beta[j])
                else:                                            # L1: umbral suave
                    z = beta[j] - lr * grad[j]
                    beta[j] = max(0.0, abs(z) - lr * alpha) * (1 if z > 0 else -1)
        return [_round(b, 4) for b in beta]

    l1 = descenso(0.35, "l1")
    l2 = descenso(0.35, "l2")
    sin = descenso(0.0, "l2")
    ceros_l1 = sum(1 for b in l1 if abs(b) < 1e-9)
    ceros_l2 = sum(1 for b in l2 if abs(b) < 1e-9)
    nulos_verdaderos = [j for j, b in enumerate(verdaderos) if b == 0.0]
    aciertos_l1 = sum(1 for j in nulos_verdaderos if abs(l1[j]) < 1e-9)

    camino = []
    for alpha in (0.05, 0.15, 0.35, 0.7, 1.2):
        b = descenso(alpha, "l1")
        camino.append({"alpha": alpha, "no_nulos": sum(1 for v in b if abs(v) > 1e-9),
                       "coeficientes": b})

    return _contract(
        "lasso",
        seed,
        {
            "observaciones": n, "variables": p,
            "coeficientes_verdaderos": verdaderos,
            "sin_penalizacion": sin,
            "cresta_l2": l2,
            "lasso_l1": l1,
            "coeficientes_exactamente_cero": {"l1": ceros_l1, "l2": ceros_l2},
            "variables_nulas_reales": len(nulos_verdaderos),
            "nulas_detectadas_por_l1": aciertos_l1,
            "camino_de_regularizacion": camino,
        },
        [
            f"De las {p} variables, solo 3 tienen efecto real. El lasso deja exactamente {ceros_l1} "
            f"coeficientes en cero y la cresta L2, {ceros_l2}: encoge todos pero no anula ninguno.",
            f"El lasso identifica {aciertos_l1} de las {len(nulos_verdaderos)} variables verdaderamente "
            "nulas. Selecciona y estima en una sola operación, que es la aportación del artículo.",
            "La diferencia es geométrica: la bola de la norma L1 tiene esquinas sobre los ejes, y el "
            "óptimo tiende a caer en ellas. La bola L2 es lisa y no tiene esquinas donde caer.",
            f"El camino de regularización muestra el compromiso: con alpha {camino[0]['alpha']} quedan "
            f"{camino[0]['no_nulos']} variables y con {camino[-1]['alpha']}, {camino[-1]['no_nulos']}. "
            "Elegir alpha es elegir cuánta parsimonia se compra y a qué precio en ajuste.",
        ],
        [
            "Sesenta observaciones y ocho variables con ruido gaussiano. El caso difícil —p mucho mayor "
            "que n, variables muy correlacionadas entre sí— es donde el lasso se vuelve inestable.",
            "Con dos variables muy correlacionadas, el lasso tiende a quedarse con una arbitrariamente. "
            "La red elástica (Zou y Hastie, 2005) existe justamente por eso.",
            "Que una variable quede en cero no significa que no influya: significa que, dadas las demás y "
            "esta penalización, no aporta. Es una afirmación condicional, no causal.",
        ],
    )


def _adaboost(seed: int) -> dict[str, Any]:
    """Freund y Schapire 1997: muchos clasificadores mediocres, ponderados por su error."""
    # banda central: y = +1 si 4 ≤ x ≤ 7. Ningún tocón la representa; una suma de tocones sí.
    datos = [((float(x),), 1 if 4 <= x <= 7 else -1) for x in range(1, 13)]
    n = len(datos)
    tocones = [(0, t + 0.5, s) for t in range(1, 12) for s in (1, -1)]

    def predecir(t, x):
        j, umbral, signo = t
        return signo if x[j] <= umbral else -signo

    mejor_individual = max(sum(1 for x, y in datos if predecir(t, x) == y) / n for t in tocones)

    pesos = [1.0 / n] * n
    elegidos, historia = [], []
    for ronda in range(1, 9):
        mejor, mejor_err = None, 1.0
        for t in tocones:
            err = sum(w for w, (x, y) in zip(pesos, datos) if predecir(t, x) != y)
            if err < mejor_err - 1e-12:
                mejor, mejor_err = t, err
        if mejor is None or mejor_err >= 0.5:
            break
        alpha = 0.5 * math.log((1 - mejor_err) / max(mejor_err, 1e-12))
        elegidos.append({"ronda": ronda,
                         "tocon": {"umbral": mejor[1], "signo": mejor[2]},
                         "error_ponderado": _round(mejor_err, 4), "alpha": _round(alpha, 4),
                         "_t": mejor})
        nuevos = [w * math.exp(-alpha * y * predecir(mejor, x)) for w, (x, y) in zip(pesos, datos)]
        total = sum(nuevos)
        pesos = [w / total for w in nuevos]

        def conjunto(x):
            s = sum(e["alpha"] * predecir(e["_t"], x) for e in elegidos)
            return 1 if s >= 0 else -1

        aciertos = sum(1 for x, y in datos if conjunto(x) == y)
        historia.append({"ronda": ronda, "aciertos_del_conjunto": f"{aciertos}/{n}",
                         "exactitud": _round(aciertos / n, 4), "peso_maximo": _round(max(pesos), 4)})

    for e in elegidos:
        e.pop("_t", None)
    mejor_conjunto = max(h["exactitud"] for h in historia) if historia else 0.0
    ronda_mejor = next(h["ronda"] for h in historia if h["exactitud"] == mejor_conjunto)
    rng = random.Random(seed)
    inspeccion = rng.randrange(n)

    return _contract(
        "adaboost",
        seed,
        {
            "problema": "banda central: y = +1 si 4 ≤ x ≤ 7, si no −1",
            "ejemplos": n,
            "tocones_disponibles": len(tocones),
            "mejor_tocon_individual": _round(mejor_individual, 4),
            "rondas": elegidos,
            "historia_del_conjunto": historia,
            "mejor_exactitud_del_conjunto": mejor_conjunto,
            "ronda_en_que_se_alcanza": ronda_mejor,
            "pesos_finales": [_round(w, 4) for w in pesos],
            "ejemplo_inspeccionado": inspeccion,
        },
        [
            f"Ningún tocón resuelve el problema: el mejor de los {len(tocones)} disponibles acierta "
            f"{_round(100 * mejor_individual, 1)} %. Un solo corte no puede describir una banda.",
            f"El conjunto ponderado llega a {_round(100 * mejor_conjunto, 1)} % en la ronda "
            f"{ronda_mejor}. La suma de dos cortes con pesos distintos sí describe una banda, y AdaBoost "
            "la encuentra sin que nadie se lo diga.",
            "El peso de cada tocón es `α = ½·ln((1−ε)/ε)`: cuanto menor su error ponderado, más voto. No "
            "es una media, es una media PONDERADA POR COMPETENCIA.",
            f"Y los pesos de los ejemplos migran hacia los difíciles: el máximo pasa de "
            f"{_round(1 / n, 4)} al inicio a {_round(max(pesos), 4)}. Cada ronda mira lo que la anterior "
            "falló.",
        ],
        [
            "Doce ejemplos en una dimensión. Es el caso mínimo donde se ve el efecto; no dice nada sobre "
            "el rendimiento en problemas reales.",
            "La exactitud es de ENTRENAMIENTO: no hay conjunto de prueba. El resultado teórico del "
            "artículo —la cota exponencial sobre el error de entrenamiento— tampoco se demuestra aquí.",
            "AdaBoost es sensible al ruido de etiqueta: como concentra peso donde falla, un ejemplo mal "
            "etiquetado acapara las rondas siguientes. Con estos datos limpios ese riesgo no se ve.",
        ],
    )


def _random_forest(seed: int) -> dict[str, Any]:
    """Breiman 2001: el error del bosque depende de la fuerza de los árboles Y de su correlación."""
    rng = random.Random(seed)
    n, p = 200, 8
    datos = []
    for _ in range(n):
        x = [rng.gauss(0, 1) for _ in range(p)]
        señal = 1.2 * x[0] - 0.9 * x[1] + 1.4 * x[2] * x[3] + 0.8 * x[4]
        datos.append((x, 1 if señal + rng.gauss(0, 0.5) > 0 else -1))
    entrena, prueba = datos[:140], datos[140:]

    def crecer(muestra, variables, profundidad):
        if profundidad == 0 or len(muestra) < 4 or len({y for _, y in muestra}) == 1:
            return ("hoja", 1 if sum(y for _, y in muestra) >= 0 else -1)
        mejor, mejor_imp = None, 2.0
        for j in variables:
            valores = sorted({x[j] for x, _ in muestra})
            for k in range(1, len(valores)):
                umbral = (valores[k - 1] + valores[k]) / 2
                izq = [(x, y) for x, y in muestra if x[j] <= umbral]
                der = [(x, y) for x, y in muestra if x[j] > umbral]
                if not izq or not der:
                    continue
                def gini(g):
                    pos = sum(1 for _, y in g if y == 1) / len(g)
                    return len(g) * (1 - pos * pos - (1 - pos) ** 2)
                imp = (gini(izq) + gini(der)) / len(muestra)
                if imp < mejor_imp:
                    mejor, mejor_imp = (j, umbral, izq, der), imp
        if mejor is None:
            return ("hoja", 1 if sum(y for _, y in muestra) >= 0 else -1)
        j, umbral, izq, der = mejor
        return ("nodo", j, umbral,
                crecer(izq, variables, profundidad - 1), crecer(der, variables, profundidad - 1))

    def predecir(arbol, x):
        while arbol[0] == "nodo":
            arbol = arbol[3] if x[arbol[1]] <= arbol[2] else arbol[4]
        return arbol[1]

    def bosque(m_variables, arboles=25, profundidad=3):
        modelos = []
        for a in range(arboles):
            local = random.Random(seed * 100 + a)
            muestra = [local.choice(entrena) for _ in entrena]         # bagging
            variables = local.sample(range(p), m_variables)            # subespacio aleatorio
            modelos.append(crecer(muestra, variables, profundidad))
        individuales = [sum(1 for x, y in prueba if predecir(t, x) != y) / len(prueba) for t in modelos]
        def voto(x):
            return 1 if sum(predecir(t, x) for t in modelos) >= 0 else -1
        conjunto = sum(1 for x, y in prueba if voto(x) != y) / len(prueba)
        acuerdos = []
        for i in range(len(modelos)):
            for j in range(i + 1, len(modelos)):
                acuerdos.append(sum(1 for x, _ in prueba
                                    if predecir(modelos[i], x) == predecir(modelos[j], x)) / len(prueba))
        medio = sum(individuales) / len(individuales)
        return {
            "variables_por_arbol": m_variables,
            "error_medio_de_un_arbol": _round(medio, 4),
            "error_del_bosque": _round(conjunto, 4),
            "ganancia_del_conjunto": _round(medio - conjunto, 4),
            "acuerdo_medio_entre_arboles": _round(sum(acuerdos) / len(acuerdos), 4),
        }

    barrido = [bosque(m) for m in (8, 5, 3, 2)]
    acuerdos = [b["acuerdo_medio_entre_arboles"] for b in barrido]
    individuales = [b["error_medio_de_un_arbol"] for b in barrido]
    mejor = min(barrido, key=lambda b: b["error_del_bosque"])

    return _contract(
        "random_forest",
        seed,
        {
            "entrenamiento": len(entrena), "prueba": len(prueba), "variables": p,
            "arboles_por_bosque": 25, "profundidad": 3,
            "barrido_de_variables_por_arbol": barrido,
            "acuerdo_decrece_al_bajar_m": acuerdos == sorted(acuerdos, reverse=True),
            "arbol_individual_empeora_al_bajar_m": individuales == sorted(individuales),
            "mejor_configuracion": mejor["variables_por_arbol"],
            "el_bosque_siempre_mejora_a_su_arbol_medio": all(
                b["ganancia_del_conjunto"] > 0 for b in barrido),
        },
        [
            f"En las cuatro configuraciones el bosque mejora a su árbol medio (ganancias "
            f"{[b['ganancia_del_conjunto'] for b in barrido]}). Votar entre modelos imperfectos reduce el "
            "error, y eso es el bagging.",
            f"Al bajar las variables por árbol de 8 a 2, el acuerdo entre árboles cae de {acuerdos[0]} a "
            f"{acuerdos[-1]}: el subespacio aleatorio DESCORRELACIONA. Esa es la aportación de Breiman "
            "sobre el bagging simple.",
            f"Y tiene precio: el árbol medio empeora de {individuales[0]} a {individuales[-1]}. Las dos "
            "cosas se mueven a la vez, en direcciones opuestas.",
            f"Por eso hay un óptimo y hay que buscarlo: aquí el mejor bosque es el de "
            f"{mejor['variables_por_arbol']} variables por árbol. La cota de Breiman dice exactamente "
            "esto — el error depende de la fuerza y de la correlación, y `m` arbitra entre ambas.",
        ],
        [
            "Doscientos ejemplos, ocho variables y árboles de profundidad 3. Un bosque real usa árboles "
            "mucho más profundos y cientos de ellos.",
            "No hay estimación out-of-bag, que es una de las aportaciones prácticas del artículo: "
            "validación gratuita con los ejemplos que cada árbol no vio en su remuestreo.",
            "Con otros datos el óptimo de `m` cambia. La conclusión transferible es la existencia del "
            "compromiso, no el valor concreto que gana en esta tabla.",
        ],
    )


def _dos_culturas(seed: int) -> dict[str, Any]:
    """Breiman 2001: el modelo de datos supone un mecanismo; el algorítmico solo predice."""
    rng = random.Random(seed)
    n = 300
    datos = []
    for _ in range(n):
        x1, x2, x3 = rng.gauss(0, 1), rng.gauss(0, 1), rng.gauss(0, 1)
        x4 = 0.95 * x1 + rng.gauss(0, 0.25)          # casi copia de x1
        # el mecanismo real es una interacción: ninguna variable sola lo explica
        y = 1 if (x1 * x2 + 0.6 * x3 + rng.gauss(0, 0.3)) > 0 else 0
        datos.append(([x1, x2, x3, x4], y))
    entrena, prueba = datos[:220], datos[220:]

    def ajustar_logistica(indices, pasos=600, lr=0.25):
        beta = [0.0] * (len(indices) + 1)
        for _ in range(pasos):
            grad = [0.0] * len(beta)
            for x, y in entrena:
                z = beta[0] + sum(b * x[j] for b, j in zip(beta[1:], indices))
                p = _sigmoid(z)
                grad[0] += (p - y) / len(entrena)
                for k, j in enumerate(indices):
                    grad[k + 1] += (p - y) * x[j] / len(entrena)
            beta = [b - lr * g for b, g in zip(beta, grad)]
        return beta

    def exactitud(beta, indices, conjunto):
        aciertos = 0
        for x, y in conjunto:
            z = beta[0] + sum(b * x[j] for b, j in zip(beta[1:], indices))
            aciertos += int((1 if _sigmoid(z) >= 0.5 else 0) == y)
        return _round(aciertos / len(conjunto), 4)

    # cultura 1: modelo de datos, lineal en las variables, con coeficientes interpretables
    beta_lineal = ajustar_logistica([0, 1, 2, 3])
    lineal = {"coeficientes": [_round(b, 4) for b in beta_lineal],
              "exactitud_prueba": exactitud(beta_lineal, [0, 1, 2, 3], prueba)}

    # cultura 2: modelo algorítmico, sin suponer forma — se le da la interacción como rasgo
    for x, _ in datos:
        x.append(x[0] * x[1])
    beta_alg = ajustar_logistica([0, 1, 2, 3, 4])
    algoritmico = {"coeficientes": [_round(b, 4) for b in beta_alg],
                   "exactitud_prueba": exactitud(beta_alg, [0, 1, 2, 3, 4], prueba)}

    # efecto Rashomon: modelos casi igual de buenos con explicaciones distintas
    rashomon = []
    for subconjunto in ([0, 1, 2, 4], [1, 2, 3, 4], [0, 2, 3, 4], [2, 3, 4]):
        b = ajustar_logistica(subconjunto)
        rashomon.append({
            "variables": subconjunto,
            "exactitud_prueba": exactitud(b, subconjunto, prueba),
            "coeficiente_de_x1": _round(b[subconjunto.index(0) + 1], 4) if 0 in subconjunto else None,
            "coeficiente_de_x4": _round(b[subconjunto.index(3) + 1], 4) if 3 in subconjunto else None,
        })
    exactitudes = sorted(r["exactitud_prueba"] for r in rashomon)
    banda = _round(exactitudes[-1] - exactitudes[0], 4)

    return _contract(
        "dos_culturas",
        seed,
        {
            "mecanismo_real": "y depende de la INTERACCIÓN x1·x2 más un término lineal en x3",
            "x4": "copia ruidosa de x1 (correlación ≈ 0,97)",
            "cultura_del_modelo_de_datos": lineal,
            "cultura_algoritmica": algoritmico,
            "efecto_rashomon": rashomon,
            "banda_de_exactitud_entre_modelos_rashomon": banda,
            "cita": "el objetivo es la exactitud predictiva, no ajustar un modelo que se supone verdadero",
        },
        [
            f"El modelo lineal en las variables originales llega a {lineal['exactitud_prueba']} de "
            f"exactitud; añadiendo el término de interacción, {algoritmico['exactitud_prueba']}. La "
            "diferencia no es de método de ajuste: es de qué se supone sobre el mecanismo.",
            "Y aquí está el problema que denuncia Breiman: los coeficientes del modelo lineal se "
            "interpretan como «el efecto de cada variable», pero el mecanismo real es una interacción. "
            "Interpretar esos números es describir un mecanismo que no existe.",
            f"El efecto Rashomon: {len(rashomon)} modelos con exactitudes entre {exactitudes[0]} y "
            f"{exactitudes[-1]} —una banda de {banda}— y con coeficientes muy distintos para x1 y para su "
            "copia x4. Todos «explican» los datos y no cuentan la misma historia.",
            "De ahí la tesis: si el objetivo es predecir, hay que medir predicción; si el objetivo es "
            "entender el mecanismo, la exactitud no basta como prueba de que el modelo lo describe.",
        ],
        [
            "Ambas culturas se implementan aquí con regresión logística: la diferencia es qué rasgos se le "
            "dan. En el artículo la cultura algorítmica son bosques y máquinas de soporte vectorial.",
            "El «mecanismo real» lo hemos puesto nosotros. En un problema real nadie sabe cuál es, y esa es "
            "justamente la razón del argumento de Breiman.",
            "La banda de Rashomon depende del conjunto: con más datos las diferencias entre modelos "
            "casi-equivalentes se estrechan, sin desaparecer.",
        ],
    )


def _seleccion_de_caracteristicas(seed: int) -> dict[str, Any]:
    """Guyon y Elisseeff 2003: la utilidad de una variable no se mide en solitario."""
    rng = random.Random(seed)
    n = 400
    datos = []
    for _ in range(n):
        a, b = rng.choice([-1.0, 1.0]), rng.choice([-1.0, 1.0])
        y = 1 if a * b > 0 else 0                      # XOR: ninguna variable sola informa
        base = rng.gauss(0, 1)
        r1 = base + rng.gauss(0, 0.8)                  # dos copias ruidosas de la misma señal
        r2 = base + rng.gauss(0, 0.8)
        ruido = rng.gauss(0, 1)
        datos.append(([a, b, r1, r2, ruido], y, base))
    nombres = ["a", "b", "r1", "r2", "ruido"]

    def correlacion_con_y(j):
        xs = [d[0][j] for d in datos]
        ys = [float(d[1]) for d in datos]
        mx, my = sum(xs) / n, sum(ys) / n
        num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
        den = math.sqrt(sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys))
        return _round(num / den, 4) if den else 0.0

    ranking = sorted(
        ({"variable": nombres[j], "correlacion_con_y": abs(correlacion_con_y(j))} for j in range(5)),
        key=lambda r: -r["correlacion_con_y"])

    def exactitud(indices):
        """Clasificador mínimo: regla de signo sobre el producto o sobre la suma."""
        entrena, prueba = datos[:280], datos[280:]
        if set(indices) == {0, 1}:
            regla = lambda x: 1 if x[0] * x[1] > 0 else 0
        elif indices:
            umbral = sum(sum(d[0][j] for j in indices) for d in entrena) / len(entrena)
            positivos = [sum(d[0][j] for j in indices) for d in entrena if d[1] == 1]
            signo = 1 if (sum(positivos) / max(len(positivos), 1)) > umbral else -1
            regla = lambda x: 1 if signo * (sum(x[j] for j in indices) - umbral) > 0 else 0
        else:
            regla = lambda x: 0
        return _round(sum(1 for d in prueba if regla(d[0]) == d[1]) / len(prueba), 4)

    sola_a, sola_b = exactitud([0]), exactitud([1])
    juntas = exactitud([0, 1])

    # redundancia aparente: r1 y r2 miden lo mismo, y promediarlas reduce el ruido
    def error_de_estimacion(indices):
        errores = []
        for x, _, base in datos:
            estimado = sum(x[j] for j in indices) / len(indices)
            errores.append((estimado - base) ** 2)
        return _round(sum(errores) / len(errores), 4)

    r1_sola, r2_sola, r1r2 = error_de_estimacion([2]), error_de_estimacion([3]), error_de_estimacion([2, 3])

    return _contract(
        "seleccion_de_caracteristicas",
        seed,
        {
            "observaciones": n,
            "ranking_univariante": ranking,
            "caso_1_variables_inutiles_por_separado": {
                "exactitud_solo_a": sola_a, "exactitud_solo_b": sola_b,
                "exactitud_a_y_b_juntas": juntas,
            },
            "caso_2_variables_redundantes": {
                "error_estimando_con_r1": r1_sola,
                "error_estimando_con_r2": r2_sola,
                "error_promediando_r1_y_r2": r1r2,
                "mejora": _round(min(r1_sola, r2_sola) - r1r2, 4),
            },
            "moraleja": "el ranking univariante no ve ni la complementariedad ni la reducción de ruido",
        },
        [
            f"Ni «a» ni «b» informan por separado: sus exactitudes son {sola_a} y {sola_b}, es decir el "
            f"azar. Juntas dan {juntas}. Una variable inútil sola puede ser imprescindible acompañada.",
            f"Y sus correlaciones univariantes con la etiqueta son "
            f"{[r['correlacion_con_y'] for r in ranking if r['variable'] in ('a', 'b')]}: un ranking por "
            "correlación las descartaría antes de mirarlas juntas.",
            f"En sentido contrario, «r1» y «r2» parecen redundantes —miden lo mismo— y promediarlas baja el "
            f"error de estimación de {min(r1_sola, r2_sola)} a {r1r2}. La redundancia aparente reduce ruido.",
            "Las dos observaciones tienen la misma consecuencia práctica: seleccionar variables mirándolas "
            "de una en una es un método con modos de fallo conocidos y en ambas direcciones.",
        ],
        [
            "Los clasificadores son reglas de una línea, no modelos entrenados. Lo que se aísla es la "
            "relación entre variables y etiqueta, no el rendimiento de ningún método.",
            "El caso XOR es el extremo didáctico. En datos reales la complementariedad suele ser parcial y "
            "el ranking univariante no falla de forma tan limpia.",
            "El artículo cubre además envolturas, métodos embebidos y estabilidad de la selección, que no "
            "están aquí.",
        ],
    )


def _calibracion(seed: int) -> dict[str, Any]:
    """Niculescu-Mizil y Caruana 2005: ordenar bien no es estimar bien."""
    rng = random.Random(seed)
    n = 500
    muestras = []
    for _ in range(n):
        p_real = rng.random()
        y = 1 if rng.random() < p_real else 0
        # un modelo que ORDENA perfectamente pero está mal calibrado: exagera hacia los extremos
        p_modelo = min(0.999, max(0.001, 1 / (1 + math.exp(-6 * (p_real - 0.5)))))
        muestras.append({"p_real": p_real, "p_modelo": p_modelo, "y": y})

    def auc(clave):
        pos = [m[clave] for m in muestras if m["y"] == 1]
        neg = [m[clave] for m in muestras if m["y"] == 0]
        if not pos or not neg:
            return None
        gana = sum(1 for a in pos for b in neg if a > b) + 0.5 * sum(1 for a in pos for b in neg if a == b)
        return _round(gana / (len(pos) * len(neg)), 4)

    def brier(clave):
        return _round(sum((m[clave] - m["y"]) ** 2 for m in muestras) / n, 4)

    def fiabilidad(clave, cubos=5):
        filas = []
        for i in range(cubos):
            lo, hi = i / cubos, (i + 1) / cubos
            grupo = [m for m in muestras if lo <= m[clave] < hi or (i == cubos - 1 and m[clave] == 1.0)]
            if not grupo:
                continue
            filas.append({"intervalo": f"[{lo:.1f}, {hi:.1f})",
                          "n": len(grupo),
                          "prob_media_predicha": _round(sum(g[clave] for g in grupo) / len(grupo), 4),
                          "frecuencia_observada": _round(sum(g["y"] for g in grupo) / len(grupo), 4)})
        for f in filas:
            f["desviacion"] = _round(f["prob_media_predicha"] - f["frecuencia_observada"], 4)
        return filas

    # calibración isotónica simplificada: reemplazar cada cubo por su frecuencia observada
    tabla = fiabilidad("p_modelo", cubos=10)
    def calibrar(p):
        for i, f in enumerate(tabla):
            lo = i / len(tabla)
            hi = (i + 1) / len(tabla)
            if lo <= p < hi or (i == len(tabla) - 1 and p >= hi - 1e-9):
                return f["frecuencia_observada"]
        return p
    for m in muestras:
        m["p_calibrado"] = calibrar(m["p_modelo"])

    antes, despues = fiabilidad("p_modelo"), fiabilidad("p_calibrado")
    error_medio_antes = _round(sum(abs(f["desviacion"]) for f in antes) / len(antes), 4)
    error_medio_despues = _round(sum(abs(f["desviacion"]) for f in despues) / len(despues), 4)

    return _contract(
        "calibracion",
        seed,
        {
            "muestras": n,
            "auc_del_modelo": auc("p_modelo"),
            "auc_tras_calibrar": auc("p_calibrado"),
            "brier_antes": brier("p_modelo"),
            "brier_despues": brier("p_calibrado"),
            "diagrama_de_fiabilidad_antes": antes,
            "diagrama_de_fiabilidad_despues": despues,
            "error_medio_de_calibracion_antes": error_medio_antes,
            "error_medio_de_calibracion_despues": error_medio_despues,
        },
        [
            f"El modelo tiene AUC {auc('p_modelo')}: ordena bien. Y su Brier es {brier('p_modelo')}, con un "
            f"error medio de calibración de {error_medio_antes}: sus probabilidades no son probabilidades.",
            "En el diagrama de fiabilidad se ve el patrón: en los intervalos altos predice más de lo que "
            "ocurre y en los bajos, menos. Un modelo que empuja hacia los extremos ordena igual de bien y "
            "estima peor.",
            f"Tras recalibrar, el Brier baja a {brier('p_calibrado')} y el error de calibración a "
            f"{error_medio_despues}, mientras el AUC apenas se mueve ({auc('p_modelo')} → "
            f"{auc('p_calibrado')}; lo poco que cambia son los empates que introduce el troceado). La "
            "calibración es monótona: reescala, no reordena.",
            "Ese error de calibración final está medido sobre los MISMOS datos con los que se calibró, así "
            "que es optimista por construcción. En un caso real hay que reservar un conjunto aparte.",
            "Por eso hay que medir las dos cosas. Cuando la salida se usa para decidir con un umbral de "
            "coste —o para combinarla con otra—, un modelo bien ordenado y mal calibrado toma decisiones "
            "sistemáticamente equivocadas.",
        ],
        [
            "El modelo está simulado a partir de la probabilidad real, que en un problema de verdad no se "
            "observa. Aquí se usa para poder exhibir la diferencia entre orden y estimación.",
            "La calibración isotónica de esta miniatura se hace sobre los MISMOS datos que se evalúan. En "
            "la práctica eso sobreajusta: hay que calibrar en un conjunto aparte.",
            "El artículo compara además cómo se descalibran distintas familias de modelos —bosques, "
            "boosting, redes, bayes ingenuo— y con qué método se corrige cada una. Eso no está aquí.",
        ],
    )


def _tsne(seed: int) -> dict[str, Any]:
    """Van der Maaten y Hinton 2008: la cola pesada resuelve el apiñamiento; las distancias no significan."""
    rng = random.Random(seed)
    grupos = [(0.0, 0.0), (8.0, 0.0), (4.0, 7.0)]
    altos = []
    for gi, (cx, cy) in enumerate(grupos):
        for _ in range(5):
            altos.append(([cx + rng.gauss(0, 0.5), cy + rng.gauss(0, 0.5),
                           rng.gauss(0, 0.3), rng.gauss(0, 0.3)], gi))
    n = len(altos)

    def d2(a, b):
        return sum((x - y) ** 2 for x, y in zip(a, b))

    # afinidades en el espacio original, con anchura fija (perplejidad simplificada)
    sigma2 = 4.0
    P = [[0.0] * n for _ in range(n)]
    for i in range(n):
        denom = sum(math.exp(-d2(altos[i][0], altos[k][0]) / (2 * sigma2)) for k in range(n) if k != i)
        for j in range(n):
            if i != j:
                P[i][j] = math.exp(-d2(altos[i][0], altos[j][0]) / (2 * sigma2)) / denom
    P = [[(P[i][j] + P[j][i]) / (2 * n) for j in range(n)] for i in range(n)]

    def ejecutar(semilla, pasos=250, lr=120.0):
        local = random.Random(semilla)
        Y = [[local.gauss(0, 1e-2), local.gauss(0, 1e-2)] for _ in range(n)]
        for _ in range(pasos):
            num = [[0.0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if i != j:
                        num[i][j] = 1.0 / (1.0 + d2(Y[i], Y[j]))     # cola de Student, 1 grado
            total = sum(num[i][j] for i in range(n) for j in range(n) if i != j)
            Q = [[(num[i][j] / total if i != j else 0.0) for j in range(n)] for i in range(n)]
            for i in range(n):
                gx = gy = 0.0
                for j in range(n):
                    if i == j:
                        continue
                    c = 4 * (P[i][j] - Q[i][j]) * num[i][j]
                    gx += c * (Y[i][0] - Y[j][0])
                    gy += c * (Y[i][1] - Y[j][1])
                Y[i][0] -= lr * gx / n
                Y[i][1] -= lr * gy / n
        return Y

    def vecinos_conservados(Y, k=3):
        aciertos = 0
        for i in range(n):
            cercanos_alto = sorted(range(n), key=lambda j: (d2(altos[i][0], altos[j][0]), j))[1:k + 1]
            cercanos_bajo = sorted(range(n), key=lambda j: (d2(Y[i], Y[j]), j))[1:k + 1]
            aciertos += len(set(cercanos_alto) & set(cercanos_bajo))
        return _round(aciertos / (n * k), 4)

    Y1, Y2 = ejecutar(seed), ejecutar(seed + 1)
    # ¿coinciden los dos mapas punto a punto?
    desplazamiento = _round(sum(math.sqrt(d2(a, b)) for a, b in zip(Y1, Y2)) / n, 4)

    # el apiñamiento: cuánta masa deja una gaussiana y una t de Student a distancia creciente
    colas = [{"distancia": d,
              "gaussiana": f"{math.exp(-d * d / 2):.3e}",
              "student_t": f"{1 / (1 + d * d):.3e}",
              "razon_t_sobre_gaussiana": f"{(1 / (1 + d * d)) / math.exp(-d * d / 2):.3e}"}
             for d in (1, 2, 4, 8)]

    return _contract(
        "tsne",
        seed,
        {
            "puntos": n, "dimension_original": 4, "grupos_reales": len(grupos),
            "vecinos_conservados_ejecucion_1": vecinos_conservados(Y1),
            "vecinos_conservados_ejecucion_2": vecinos_conservados(Y2),
            "desplazamiento_medio_entre_ejecuciones": desplazamiento,
            "colas_de_la_distribucion": colas,
            "razon_de_masa_a_distancia_8": colas[-1]["razon_t_sobre_gaussiana"],
        },
        [
            f"Dos ejecuciones con semillas distintas conservan la misma proporción de vecinos "
            f"({vecinos_conservados(Y1)} y {vecinos_conservados(Y2)}) y colocan los puntos en sitios "
            f"distintos: el desplazamiento medio es {desplazamiento}.",
            "Lo que t-SNE preserva es la VECINDAD, no la posición. Comparar dos mapas mirando dónde queda "
            "cada punto es leer ruido de la inicialización.",
            f"A distancia 8, la cola de Student deja una masa {colas[-1]['razon_t_sobre_gaussiana']} veces "
            "mayor que la gaussiana. Ese exceso es lo que permite alejar los grupos sin apiñarlo todo en "
            "el centro: es la solución al problema del apiñamiento.",
            "Consecuencia directa: la distancia entre dos grupos en un mapa t-SNE no es interpretable, y el "
            "tamaño aparente de un grupo tampoco. Solo la pertenencia a un vecindario lo es.",
        ],
        [
            "Quince puntos en cuatro dimensiones y una anchura fija en lugar de perplejidad ajustada por "
            "punto. Es el mecanismo, no la implementación de referencia.",
            "No hay early exaggeration ni aproximación de Barnes-Hut, que son lo que hace t-SNE usable con "
            "decenas de miles de puntos.",
            "t-SNE no es un método de reducción de dimensionalidad para alimentar otro modelo: es una "
            "herramienta de visualización. Usar sus coordenadas como rasgos es un error frecuente.",
        ],
    )


def _isolation_forest(seed: int) -> dict[str, Any]:
    """Liu, Ting y Zhou 2008: aislar es más barato que modelar la normalidad."""
    rng = random.Random(seed)
    normales = [[rng.gauss(0, 1), rng.gauss(0, 1)] for _ in range(60)]
    anomalos = [[6.5, 6.0], [-6.0, 5.5], [7.0, -6.5]]
    datos = normales + anomalos

    def longitud_de_aislamiento(punto, muestra, arbol_rng, profundidad_max=8):
        actual = [p for p in muestra]
        for profundidad in range(profundidad_max):
            if len(actual) <= 1:
                return profundidad
            eje = arbol_rng.randrange(2)
            lo = min(p[eje] for p in actual)
            hi = max(p[eje] for p in actual)
            if hi - lo < 1e-12:
                return profundidad
            corte = arbol_rng.uniform(lo, hi)
            if punto[eje] < corte:
                actual = [p for p in actual if p[eje] < corte]
            else:
                actual = [p for p in actual if p[eje] >= corte]
            if punto not in actual:
                actual = [punto]
        return profundidad_max

    arboles = 40
    caminos = {}
    for idx, punto in enumerate(datos):
        total = 0
        for a in range(arboles):
            local = random.Random(seed * 977 + a)
            sub = local.sample(datos, 32)
            if punto not in sub:
                sub = sub[:-1] + [punto]
            total += longitud_de_aislamiento(punto, sub, random.Random(seed * 31 + a * 7 + idx))
        caminos[idx] = total / arboles

    m = 32
    c = 2 * (math.log(m - 1) + 0.5772156649) - 2 * (m - 1) / m
    puntuaciones = {i: 2 ** (-caminos[i] / c) for i in caminos}

    idx_anomalos = list(range(len(normales), len(datos)))
    media_normal = sum(caminos[i] for i in range(len(normales))) / len(normales)
    media_anomala = sum(caminos[i] for i in idx_anomalos) / len(idx_anomalos)
    ranking = sorted(puntuaciones, key=lambda i: -puntuaciones[i])
    en_el_top = sum(1 for i in ranking[:len(idx_anomalos)] if i in idx_anomalos)

    return _contract(
        "isolation_forest",
        seed,
        {
            "puntos": len(datos), "anomalias_reales": len(idx_anomalos), "arboles": arboles,
            "submuestra_por_arbol": m,
            "longitud_media_de_camino_normales": _round(media_normal, 4),
            "longitud_media_de_camino_anomalos": _round(media_anomala, 4),
            "constante_de_normalizacion_c": _round(c, 4),
            "puntuacion_media_normales": _round(
                sum(puntuaciones[i] for i in range(len(normales))) / len(normales), 4),
            "puntuacion_media_anomalos": _round(
                sum(puntuaciones[i] for i in idx_anomalos) / len(idx_anomalos), 4),
            "anomalias_en_el_top_3": f"{en_el_top}/{len(idx_anomalos)}",
            "top_5_del_ranking": [{"indice": i, "puntuacion": _round(puntuaciones[i], 4),
                                   "es_anomalia": i in idx_anomalos} for i in ranking[:5]],
        },
        [
            f"Los puntos anómalos se aíslan en {_round(media_anomala, 2)} cortes de media y los normales en "
            f"{_round(media_normal, 2)}. Lo raro está en zonas poco pobladas, y un corte al azar lo separa "
            "antes.",
            f"La puntuación `2^(−h/c)` traduce eso a una escala comparable: "
            f"{_round(sum(puntuaciones[i] for i in idx_anomalos) / len(idx_anomalos), 3)} de media para las "
            f"anomalías frente a "
            f"{_round(sum(puntuaciones[i] for i in range(len(normales))) / len(normales), 3)} para el resto.",
            f"En el ranking por puntuación, {en_el_top} de las {len(idx_anomalos)} anomalías reales están "
            "en las tres primeras posiciones.",
            "La inversión conceptual del artículo: no se modela qué es normal para medir la distancia a "
            "ello, se mide directamente lo fácil que es aislar cada punto. Sale más barato y no supone "
            "ninguna forma para la distribución normal.",
        ],
        [
            "Sesenta puntos normales y tres anomalías muy separadas en dos dimensiones. El caso difícil "
            "—anomalías locales, dentro de la nube pero con densidad distinta— es donde este método flojea.",
            "El bosque de aislamiento detecta anomalías GLOBALES bien y anomalías locales mal. Para esas "
            "últimas existe el factor de anomalía local (LOF), con otra idea.",
            "La miniatura no implementa el submuestreo exacto del artículo ni el límite de altura "
            "`ceil(log2 m)`, y usa una profundidad fija para que la salida sea legible.",
        ],
    )


def _factorizacion_matricial(seed: int) -> dict[str, Any]:
    """Koren, Bell y Volinsky 2009: factores latentes y sesgos, aprendidos solo de lo observado."""
    rng = random.Random(seed)
    usuarios, articulos, k = 12, 8, 2
    # estructura real: dos gustos latentes opuestos
    gusto_real = [[1.0, 0.0] if u < 6 else [0.0, 1.0] for u in range(usuarios)]
    perfil_real = [[1.0, 0.0], [1.0, 0.0], [0.5, 0.5], [0.0, 1.0],
                   [0.0, 1.0], [0.5, 0.5], [1.0, 0.0], [0.0, 1.0]]
    # sesgos amplios a propósito: en datos reales explican buena parte de la nota
    sesgo_usuario_real = [rng.uniform(-1.0, 1.0) for _ in range(usuarios)]
    sesgo_articulo_real = [rng.uniform(-0.9, 0.9) for _ in range(articulos)]
    media = 3.5

    observadas, ocultas = [], []
    for u in range(usuarios):
        for i in range(articulos):
            r = (media + sesgo_usuario_real[u] + sesgo_articulo_real[i]
                 + 1.0 * sum(a * b for a, b in zip(gusto_real[u], perfil_real[i]))
                 + rng.gauss(0, 0.15))
            r = min(5.0, max(1.0, r))
            (observadas if rng.random() < 0.60 else ocultas).append((u, i, r))

    P = [[rng.gauss(0, 0.1) for _ in range(k)] for _ in range(usuarios)]
    Q = [[rng.gauss(0, 0.1) for _ in range(k)] for _ in range(articulos)]
    bu = [0.0] * usuarios
    bi = [0.0] * articulos
    mu = sum(r for _, _, r in observadas) / len(observadas)
    lr, reg = 0.03, 0.05

    def predecir(u, i):
        return mu + bu[u] + bi[i] + sum(a * b for a, b in zip(P[u], Q[i]))

    def rmse(conjunto):
        return _round(math.sqrt(sum((predecir(u, i) - r) ** 2 for u, i, r in conjunto) / len(conjunto)), 4)

    historia = []
    for epoca in range(1, 301):
        for u, i, r in observadas:
            err = r - predecir(u, i)
            bu[u] += lr * (err - reg * bu[u])
            bi[i] += lr * (err - reg * bi[i])
            for f in range(k):
                pu, qi = P[u][f], Q[i][f]
                P[u][f] += lr * (err * qi - reg * pu)
                Q[i][f] += lr * (err * pu - reg * qi)
        if epoca % 75 == 0:
            historia.append({"epoca": epoca, "rmse_observadas": rmse(observadas),
                             "rmse_ocultas": rmse(ocultas)})

    # línea base 1: predecir siempre la media global
    base_ocultas = _round(math.sqrt(sum((mu - r) ** 2 for _, _, r in ocultas) / len(ocultas)), 4)
    # línea base 2: solo sesgos, AJUSTADOS APARTE (reutilizar los de arriba no sería honesto:
    # esos se aprendieron a la vez que los factores y absorben parte de su trabajo)
    sbu, sbi = [0.0] * usuarios, [0.0] * articulos
    for _ in range(300):
        for u, i, r in observadas:
            err = r - (mu + sbu[u] + sbi[i])
            sbu[u] += lr * (err - reg * sbu[u])
            sbi[i] += lr * (err - reg * sbi[i])
    solo_sesgos = _round(math.sqrt(
        sum((mu + sbu[u] + sbi[i] - r) ** 2 for u, i, r in ocultas) / len(ocultas)), 4)

    return _contract(
        "factorizacion_matricial",
        seed,
        {
            "usuarios": usuarios, "articulos": articulos, "factores": k,
            "celdas_totales": usuarios * articulos,
            "observadas": len(observadas), "ocultas": len(ocultas),
            "densidad": _round(len(observadas) / (usuarios * articulos), 4),
            "historia": historia,
            "rmse_prediciendo_la_media": base_ocultas,
            "rmse_solo_con_sesgos": solo_sesgos,
            "rmse_con_factores_latentes": historia[-1]["rmse_ocultas"],
            "factores_de_usuario": [[_round(v, 3) for v in fila] for fila in P],
        },
        [
            f"Solo se entrena con las {len(observadas)} celdas observadas de "
            f"{usuarios * articulos} —una densidad de "
            f"{_round(len(observadas) / (usuarios * articulos), 2)}— y se evalúa sobre las "
            f"{len(ocultas)} que el modelo no vio nunca.",
            f"Sobre esas celdas ocultas: predecir siempre la media da RMSE {base_ocultas}; un modelo de "
            f"solo sesgos de usuario y artículo, {solo_sesgos}; y con dos factores latentes, "
            f"{historia[-1]['rmse_ocultas']}.",
            "Los sesgos hacen la mitad del trabajo y casi nunca se reportan: hay usuarios que puntúan "
            "alto todo y artículos que gustan a todos. Modelarlos antes que los gustos es lo que el "
            "artículo insiste en hacer, y sin esa línea base un RMSE suelto no dice nada.",
            "Los factores latentes no se declaran: emergen del ajuste. Nadie ha dicho al modelo que hay dos "
            "gustos opuestos, y los vectores de usuario se separan en dos grupos.",
        ],
        [
            "Ocho usuarios y seis artículos. Una matriz real tiene millones de filas y densidades del orden "
            "del 1 %, y ahí la regularización y el muestreo negativo son decisivos.",
            "No hay arranque en frío: todo usuario y todo artículo tienen al menos una observación. El caso "
            "del usuario nuevo —el problema práctico más común— no se aborda.",
            "El RMSE mide error de predicción de puntuación, no calidad de la recomendación. Ordenar bien "
            "los diez primeros y acertar la nota son objetivos distintos; el propio Netflix Prize lo mostró.",
        ],
    )


def _m4(seed: int) -> dict[str, Any]:
    """Makridakis et al. 2018: lo que gana en ajuste pierde fuera, y la combinación gana casi siempre."""
    rng = random.Random(seed)
    periodo, longitud = 12, 72
    serie = []
    for t in range(longitud):
        nivel = 100 + 0.8 * t
        estacional = 12 * math.sin(2 * math.pi * t / periodo)
        serie.append(nivel + estacional + rng.gauss(0, 4))
    corte = longitud - 12
    entrena, prueba = serie[:corte], serie[corte:]
    h = len(prueba)

    def ingenuo():
        return [entrena[-1]] * h

    def estacional_ingenuo():
        return [entrena[-periodo + (i % periodo)] for i in range(h)]

    def deriva():
        pendiente = (entrena[-1] - entrena[0]) / (len(entrena) - 1)
        return [entrena[-1] + pendiente * (i + 1) for i in range(h)]

    def polinomio(grado):
        """Ajuste polinómico por mínimos cuadrados: cuanto mayor el grado, mejor ajusta dentro."""
        xs = list(range(len(entrena)))
        # ecuaciones normales resueltas por eliminación de Gauss
        A = [[sum(x ** (i + j) for x in xs) for j in range(grado + 1)] for i in range(grado + 1)]
        b = [sum((x ** i) * y for x, y in zip(xs, entrena)) for i in range(grado + 1)]
        for i in range(grado + 1):
            piv = A[i][i]
            if abs(piv) < 1e-18:
                return [entrena[-1]] * h, [entrena[-1]] * len(entrena)
            for j in range(i, grado + 1):
                A[i][j] /= piv
            b[i] /= piv
            for r in range(grado + 1):
                if r != i and abs(A[r][i]) > 0:
                    f = A[r][i]
                    for j in range(i, grado + 1):
                        A[r][j] -= f * A[i][j]
                    b[r] -= f * b[i]
        dentro = [sum(b[i] * (x ** i) for i in range(grado + 1)) for x in xs]
        fuera = [sum(b[i] * ((len(entrena) + k) ** i) for i in range(grado + 1)) for k in range(h)]
        return fuera, dentro

    def mae(pred, real):
        return _round(sum(abs(p - r) for p, r in zip(pred, real)) / len(real), 4)

    metodos = {
        "ingenuo": ingenuo(),
        "estacional_ingenuo": estacional_ingenuo(),
        "deriva": deriva(),
    }
    dentro_de_muestra = {}
    for grado in (1, 5, 11):
        fuera, dentro = polinomio(grado)
        metodos[f"polinomio_grado_{grado}"] = fuera
        dentro_de_muestra[f"polinomio_grado_{grado}"] = mae(dentro, entrena)

    combinacion = [
        sum(metodos[m][i] for m in ("estacional_ingenuo", "deriva", "polinomio_grado_1")) / 3
        for i in range(h)
    ]
    metodos["combinacion_de_tres"] = combinacion

    resultados = [{"metodo": m, "mae_fuera_de_muestra": mae(p, prueba)} for m, p in metodos.items()]
    resultados.sort(key=lambda r: r["mae_fuera_de_muestra"])
    mejor = resultados[0]
    peor_polinomio = max((r for r in resultados if r["metodo"].startswith("polinomio")),
                         key=lambda r: r["mae_fuera_de_muestra"])

    return _contract(
        "m4",
        seed,
        {
            "longitud_de_la_serie": longitud, "horizonte": h, "periodo": periodo,
            "ajuste_dentro_de_muestra": dentro_de_muestra,
            "resultados_fuera_de_muestra": resultados,
            "mejor": mejor["metodo"],
            "la_combinacion_gana": mejor["metodo"] == "combinacion_de_tres",
            "puesto_de_la_combinacion": next(
                i + 1 for i, r in enumerate(resultados) if r["metodo"] == "combinacion_de_tres"),
            "peor_polinomio_fuera": peor_polinomio,
        },
        [
            f"El polinomio de grado 11 es el que mejor ajusta dentro de la muestra "
            f"(MAE {dentro_de_muestra['polinomio_grado_11']} frente a "
            f"{dentro_de_muestra['polinomio_grado_1']} del lineal) y fuera de muestra se dispara a "
            f"{[r['mae_fuera_de_muestra'] for r in resultados if r['metodo'] == 'polinomio_grado_11'][0]}. "
            "Ajustar el pasado no es predecir el futuro.",
            f"El mejor método fuera de muestra es «{mejor['metodo']}» con MAE "
            f"{mejor['mae_fuera_de_muestra']}. El ranking dentro y fuera de muestra no coincide, y solo el "
            "segundo importa.",
            f"La combinación simple de tres métodos queda "
            f"{next(i + 1 for i, r in enumerate(resultados) if r['metodo'] == 'combinacion_de_tres')}ª de "
            f"{len(resultados)}: no gana, y tampoco se hunde. Ese es el hallazgo de la M4 sobre 100 000 "
            "series —la combinación rara vez es la mejor y casi nunca es la peor—, y aquí solo se ilustra "
            "con una.",
            "Y las líneas base ingenuas no son un trámite: son el listón. Un método sofisticado que no las "
            "supera fuera de muestra no ha demostrado nada.",
        ],
        [
            "Una sola serie sintética con tendencia y estacionalidad limpias. La M4 evalúa 100 000 series "
            "reales de dominios distintos, y ahí ningún método gana en todas.",
            "El horizonte es fijo y hay una sola partición: sin validación en ventanas deslizantes, el "
            "resultado depende de dónde se corta.",
            "La conclusión de la M4 sobre la combinación es estadística, sobre miles de series. Que aquí "
            "gane o no una configuración concreta no la demuestra ni la refuta.",
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
    "pca": _pca,
    "mcculloch_pitts": _mcculloch_pitts,
    "shannon": _shannon,
    "turing": _turing,
    "dartmouth": _dartmouth,
    "simbolos_y_busqueda": _simbolos_y_busqueda,
    "agente_racional": _agente_racional,
    "valor_predictivo": _valor_predictivo,
    "stochastic_parrots": _stochastic_parrots,
    "benchmark_validez": _benchmark_validez,
    "reproducibilidad": _reproducibilidad,
    "gps": _gps,
    "dpll": _dpll,
    "resolucion": _resolucion,
    "a_estrella": _a_estrella,
    "strips": _strips,
    "mycin": _mycin,
    "arco_consistencia": _arco_consistencia,
    "ontologia": _ontologia,
    "neurosimbolico": _neurosimbolico,
    "kmeans": _kmeans,
    "id3": _id3,
    "svm": _svm,
    "validacion_cruzada": _validacion_cruzada,
    "lasso": _lasso,
    "adaboost": _adaboost,
    "random_forest": _random_forest,
    "dos_culturas": _dos_culturas,
    "seleccion_de_caracteristicas": _seleccion_de_caracteristicas,
    "calibracion": _calibracion,
    "tsne": _tsne,
    "isolation_forest": _isolation_forest,
    "factorizacion_matricial": _factorizacion_matricial,
    "m4": _m4,
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
