"""Generador del eje `papers/`.

Fuente de verdad: `papers/catalog/papers.json` + las especificaciones de notebook
de este archivo. A partir de ahí se derivan, de forma reproducible:

* `papers/catalog/PAPERS_INDEX.md`
* `notebooks/papers/*.ipynb`  (52 papers + 8 miniaturas del Transformer)
* `instructor/papers/*.md`, `student/papers/*.md`, `assessments/papers/*.md`
* `papers/manifest.json` con SHA-256 de cada artefacto

Uso::

    python scripts/generate_papers.py            # genera todo
    python scripts/generate_papers.py --check    # falla si algo quedó desactualizado
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ai_evolution.papers import (  # noqa: E402
    FICHA_SECTIONS,
    NOTEBOOK_SECTIONS,
    load_papers,
    sha256_of,
)

BOOTSTRAP = """import json
import pathlib
import sys

ROOT = pathlib.Path.cwd()
while not (ROOT / "pyproject.toml").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent
sys.path.insert(0, str(ROOT / "src"))

from ai_evolution.papers_lab import run_paper_lab


def show(value):
    print(json.dumps(value, ensure_ascii=False, indent=2))
"""


# --------------------------------------------------------------------------- #
# especificaciones de notebook (secciones 4 a 16 del contrato)
# --------------------------------------------------------------------------- #

SPECS: dict[str, dict[str, Any]] = {
    "P01_perceptron": {
        "intuicion": (
            "Una recta que separa dos grupos de puntos. El aprendizaje consiste en empujar la recta "
            "cada vez que un punto queda del lado equivocado. Nada más. Si los grupos se pueden "
            "separar con una recta, el empujón termina; si no, el empujón nunca termina."
        ),
        "concepto": (
            "`ŷ = 1 si w·x + b ≥ 0, si no 0`. Regla de corrección: `w ← w + η(y − ŷ)x`, `b ← b + η(y − ŷ)`.\n\n"
            "Solo se corrige ante error: si acierta, no toca nada. El teorema de Novikoff (1962) acota "
            "el número de correcciones por `(R/γ)²` cuando existe un margen `γ > 0`."
        ),
        "codigo_md": "Veinte líneas bastan para el algoritmo de 1958. Lo que importa es la línea del `if`: sin error, no hay aprendizaje.",
        "codigo": (
            "def perceptron(data, epochs=20, lr=1.0):\n"
            "    w, b, historial = [0.0, 0.0], 0.0, []\n"
            "    for epoca in range(1, epochs + 1):\n"
            "        errores = 0\n"
            "        for x, y in data:\n"
            "            z = w[0] * x[0] + w[1] * x[1] + b\n"
            "            pred = 1 if z >= 0 else 0\n"
            "            if pred != y:                      # <-- solo se aprende del error\n"
            "                w = [wi + lr * (y - pred) * xi for wi, xi in zip(w, x)]\n"
            "                b += lr * (y - pred)\n"
            "                errores += 1\n"
            "        historial.append({'epoca': epoca, 'errores': errores, 'w': list(w), 'b': b})\n"
            "        if errores == 0:\n"
            "            return {'converge': True, 'epocas': epoca, 'w': w, 'b': b, 'historial': historial}\n"
            "    return {'converge': False, 'epocas': epochs, 'w': w, 'b': b, 'historial': historial[-3:]}\n"
            "\n"
            "AND = [([0, 0], 0), ([0, 1], 0), ([1, 0], 0), ([1, 1], 1)]\n"
            "XOR = [([0, 0], 0), ([0, 1], 1), ([1, 0], 1), ([1, 1], 0)]\n"
            "show(perceptron(AND))"
        ),
        "prediccion": (
            "Antes de ejecutar la celda siguiente, escribe tu respuesta:\n\n"
            "1. ¿En cuántas épocas converge AND?\n"
            "2. ¿Qué crees que hará XOR: converger en más épocas, o no converger nunca?\n"
            "3. Si XOR no converge, ¿los pesos se quedan quietos o siguen cambiando?"
        ),
        "experimento": (
            "resultado_and = perceptron(AND)\n"
            "resultado_xor = perceptron(XOR)\n"
            "print('AND converge:', resultado_and['converge'], '· épocas:', resultado_and['epocas'])\n"
            "print('XOR converge:', resultado_xor['converge'], '· épocas:', resultado_xor['epocas'])\n"
            "print('XOR, últimas 3 épocas:')\n"
            "show(resultado_xor['historial'])"
        ),
        "salida": (
            "AND converge y deja de moverse: `errores = 0`. XOR nunca llega a `errores = 0` y sus pesos "
            "siguen oscilando en las últimas épocas. **La oscilación es el dato**: no es que el algoritmo "
            "aprenda lento, es que no existe solución que buscar."
        ),
        "comentario": (
            "Esto separa dos ideas que los principiantes mezclan: *no converger por falta de épocas* "
            "(problema de presupuesto) y *no converger porque la clase de hipótesis no contiene la solución* "
            "(problema de capacidad representacional). Aumentar `epochs` a un millón no cambia el segundo caso."
        ),
        "antipatron_md": "Anti-patrón clásico: concluir «el modelo aprende» mirando solo el último `w` sin comprobar si el error llegó a cero.",
        "antipatron": (
            "malo = perceptron(XOR, epochs=200)\n"
            "print('pesos finales:', malo['w'], malo['b'])\n"
            "print('conclusión apresurada: «ya está entrenado, tengo pesos»')"
        ),
        "correccion_md": "La corrección es reportar siempre el criterio de parada junto con los pesos.",
        "correccion": (
            "def reportar(resultado, nombre):\n"
            "    estado = 'CONVERGIÓ' if resultado['converge'] else 'NO CONVERGIÓ (tope de épocas)'\n"
            "    print(f\"{nombre}: {estado} · w={resultado['w']} b={resultado['b']}\")\n"
            "\n"
            "reportar(perceptron(AND), 'AND')\n"
            "reportar(perceptron(XOR, epochs=200), 'XOR')"
        ),
        "desafio_guiado_md": (
            "Añade la característica `x₃ = x₁·x₂` a XOR y vuelve a entrenar. ¿Se vuelve separable? "
            "Este es exactamente el truco que las capas ocultas aprenderán solas en P02."
        ),
        "desafio_guiado": (
            "XOR3 = [([x[0], x[1], x[0] * x[1]], y) for x, y in XOR]\n"
            "\n"
            "def perceptron3(data, epochs=20, lr=1.0):\n"
            "    w, b = [0.0, 0.0, 0.0], 0.0\n"
            "    for epoca in range(1, epochs + 1):\n"
            "        errores = 0\n"
            "        for x, y in data:\n"
            "            pred = 1 if sum(wi * xi for wi, xi in zip(w, x)) + b >= 0 else 0\n"
            "            if pred != y:\n"
            "                w = [wi + lr * (y - pred) * xi for wi, xi in zip(w, x)]\n"
            "                b += lr * (y - pred)\n"
            "                errores += 1\n"
            "        if errores == 0:\n"
            "            return {'converge': True, 'epocas': epoca, 'w': w, 'b': b}\n"
            "    return {'converge': False, 'epocas': epochs, 'w': w, 'b': b}\n"
            "\n"
            "show(perceptron3(XOR3))"
        ),
        "desafio_autonomo": (
            "Genera dos nubes de puntos gaussianas con distintos grados de solapamiento y mide cuántas "
            "correcciones necesita el perceptrón en función del margen. Contrasta tu curva empírica con "
            "la cota `(R/γ)²`. Documenta la semilla y el criterio de parada."
        ),
        "evidencia": (
            "Guarda: (a) el número de épocas de AND, (b) la evidencia de no convergencia de XOR, "
            "(c) el resultado de XOR con la característica `x₁·x₂`, y (d) una frase tuya distinguiendo "
            "«no converge todavía» de «no puede converger»."
        ),
        "cierre": (
            "El perceptrón demostró que una máquina puede ajustar su propio comportamiento a partir de "
            "ejemplos. También demostró, sin quererlo, dónde estaba el techo: la frontera es lineal."
        ),
    },
    "P02_backpropagation": {
        "intuicion": (
            "Si el resultado final está mal, ¿de quién es la culpa? Backpropagation reparte la culpa "
            "hacia atrás: cada peso recibe una porción del error proporcional a cuánto influyó en él. "
            "No es magia, es la regla de la cadena del cálculo aplicada con orden."
        ),
        "concepto": (
            "Para una red `x → h = σ(W₁x + b₁) → o = σ(W₂h + b₂)` y pérdida `L = (o − y)²`:\n\n"
            "```text\n"
            "∂L/∂o_in = 2(o − y)·σ'(o_in)               con σ'(z) = σ(z)(1 − σ(z))\n"
            "∂L/∂W₂   = ∂L/∂o_in · h\n"
            "∂L/∂h_in = ∂L/∂o_in · W₂ · σ'(h_in)        ← aquí «viaja» el error hacia atrás\n"
            "∂L/∂W₁   = ∂L/∂h_in · x\n"
            "```"
        ),
        "codigo_md": "El motor del programa implementa esta derivación a mano, sin autograd, para que se vea cada término.",
        "codigo": (
            "resultado = run_paper_lab('backprop', seed=7)\n"
            "show(resultado['result']['loss_history'])\n"
            "show(resultado['result']['predictions'])"
        ),
        "prediccion": (
            "1. ¿Bajará la pérdida de forma monótona o habrá una meseta al principio?\n"
            "2. Con 2 neuronas ocultas, ¿podrá resolver XOR o hará falta más capacidad?\n"
            "3. ¿Cuánto esperas que difiera el gradiente analítico del numérico: 1e-2, 1e-5 o 1e-10?"
        ),
        "experimento": (
            "for semilla in (1, 7, 42):\n"
            "    r = run_paper_lab('backprop', seed=semilla)['result']\n"
            "    print(f\"semilla {semilla:>2} · pérdida inicial {r['loss_history'][0]['loss']:.5f} \"\n"
            "          f\"· final {r['loss_history'][-1]['loss']:.5f} \"\n"
            "          f\"· |analítico − numérico| = {r['grad_check']['abs_diff']}\")"
        ),
        "salida": (
            "La verificación numérica del gradiente es la parte más importante de la salida. "
            "`|analítico − numérico| ≈ 1e-8` significa que la derivación es correcta. Si diera `1e-2`, "
            "el entrenamiento podría *parecer* funcionar y estar optimizando otra cosa."
        ),
        "comentario": (
            "La meseta inicial es real: con pesos pequeños las sigmoides están en su zona lineal y la "
            "señal de gradiente es débil. Ese mismo fenómeno, multiplicado por muchas capas, es el "
            "gradiente desvaneciente que P03 tendrá que resolver."
        ),
        "antipatron_md": "Anti-patrón: confiar en un gradiente escrito a mano sin verificarlo. Aquí se compara contra una derivada numérica *mal calculada* (diferencia hacia adelante con ε enorme).",
        "antipatron": (
            "eps_malo = 1e-1                      # ε demasiado grande: mide una secante, no una tangente\n"
            "def f(x):\n"
            "    return (x - 3) ** 2\n"
            "\n"
            "aprox = (f(2.0 + eps_malo) - f(2.0)) / eps_malo\n"
            "print('derivada numérica con ε=1e-1 :', aprox, ' (analítica: -2.0)')"
        ),
        "correccion_md": "La corrección: diferencia **centrada** y un ε intermedio. Muy grande mide otra cosa; muy pequeño se come la precisión de punto flotante.",
        "correccion": (
            "for eps in (1e-1, 1e-3, 1e-5, 1e-9, 1e-12):\n"
            "    centrada = (f(2.0 + eps) - f(2.0 - eps)) / (2 * eps)\n"
            "    print(f'ε={eps:<8} → {centrada:+.10f}  error={abs(centrada + 2.0):.2e}')"
        ),
        "desafio_guiado_md": "Comprueba que el error del gradiente sube si aumentas la tasa de aprendizaje hasta desestabilizar el entrenamiento.",
        "desafio_guiado": (
            "r = run_paper_lab('backprop', seed=3)['result']\n"
            "print('pérdida final:', r['loss_history'][-1]['loss'])\n"
            "print('predicciones (XOR espera 0,1,1,0):')\n"
            "for fila in r['predictions']:\n"
            "    print(' ', fila['x'], '→', fila['pred'], ' (objetivo', fila['y'], ')')"
        ),
        "desafio_autonomo": (
            "Reescribe la red con 1 sola neurona oculta y comprueba que ya no resuelve XOR. Después, "
            "sustituye la sigmoide por ReLU y observa qué cambia en la meseta inicial. Documenta ambas "
            "curvas de pérdida y explica la diferencia en términos de gradiente."
        ),
        "evidencia": (
            "Guarda la curva de pérdida, la comprobación numérica del gradiente y una explicación de por "
            "qué una red de 9 parámetros resuelve lo que el perceptrón no podía."
        ),
        "cierre": (
            "Con backpropagation, las capas ocultas dejan de ser un misterio: se pueden entrenar. "
            "El problema siguiente aparece al apilar muchas capas —o muchos pasos de tiempo— y ver que "
            "el gradiente se apaga en el camino."
        ),
    },
    "P03_lstm": {
        "intuicion": (
            "Una cinta transportadora que atraviesa el tiempo sin ser tocada, y tres compuertas que "
            "deciden qué se sube, qué se baja y qué se mira. El truco no son las compuertas: es que la "
            "cinta se actualiza **sumando**, no multiplicando."
        ),
        "concepto": (
            "```text\n"
            "f = σ(W_f·[h, x])   olvido      c = f ⊙ c_prev + i ⊙ g     ← suma, no producto encadenado\n"
            "i = σ(W_i·[h, x])   entrada     h = o ⊙ tanh(c)\n"
            "o = σ(W_o·[h, x])   salida\n"
            "g = tanh(W_g·[h, x]) candidato\n"
            "```\n\n"
            "En un RNN clásico el gradiente se multiplica por `W·tanh'` en cada paso: si ese factor es "
            "0,4, en 40 pasos queda `0,4⁴⁰ ≈ 1e-16`. En la celda, `∂c_t/∂c_{t-1} = f ≈ 1`."
        ),
        "codigo_md": "El motor calcula ambos decaimientos y una pasada completa de la celda con valores explícitos.",
        "codigo": (
            "r = run_paper_lab('lstm', seed=7)['result']\n"
            "show(r['gates'])\n"
            "show(r['gradient_after_40_steps'])"
        ),
        "prediccion": (
            "1. Tras 40 pasos, ¿cuántos órdenes de magnitud separan el gradiente del RNN del de la celda?\n"
            "2. Si la puerta de olvido valiera 0,5 en lugar de ~1, ¿la celda seguiría preservando el gradiente?\n"
            "3. ¿Qué puerta controla lo que el resto de la red *ve*, sin borrar lo que la celda *recuerda*?"
        ),
        "experimento": (
            "import math\n"
            "\n"
            "for f in (1.00, 0.98, 0.90, 0.50):\n"
            "    grad = 1.0\n"
            "    for _ in range(40):\n"
            "        grad *= f\n"
            "    print(f'puerta de olvido={f:.2f} → gradiente tras 40 pasos = {grad:.3e}')"
        ),
        "salida": (
            "Con `f = 1,00` el gradiente se conserva exacto (carrusel de error constante). Con `f = 0,50` "
            "la celda vuelve a desvanecerse: **la LSTM no elimina el problema, lo pone bajo control de una "
            "puerta aprendida**. Esa distinción es la respuesta correcta en un examen."
        ),
        "comentario": (
            "Ojo con el anacronismo: el paper de 1997 tenía puertas de entrada y salida. La puerta de "
            "olvido —la que acabas de manipular— la añadieron Gers, Schmidhuber y Cummins en 1999/2000. "
            "Atribuirla al paper original es un error frecuente en resúmenes de internet."
        ),
        "antipatron_md": "Anti-patrón: explicar la LSTM diciendo «resuelve el gradiente desvaneciente» sin condición alguna.",
        "antipatron": (
            "afirmacion = 'La LSTM resuelve el gradiente desvaneciente.'\n"
            "print(afirmacion)\n"
            "print('→ falso como enunciado absoluto: acabas de ver f=0.50 desvanecerse igual.')"
        ),
        "correccion_md": "Enunciado correcto, con su condición explícita:",
        "correccion": (
            "correcto = ('La LSTM MITIGA el gradiente desvaneciente cuando la puerta de olvido '\n"
            "            'aprende a mantenerse cerca de 1 en el intervalo que hay que recordar.')\n"
            "print(correcto)"
        ),
        "desafio_guiado_md": "¿A partir de qué valor de `f` el gradiente cae por debajo de 1e-3 en 40 pasos? Búscalo numéricamente.",
        "desafio_guiado": (
            "umbral = 1e-3\n"
            "f = 1.0\n"
            "while f > 0:\n"
            "    if f ** 40 < umbral:\n"
            "        break\n"
            "    f -= 0.005\n"
            "print(f'la puerta debe mantenerse por encima de f≈{f + 0.005:.3f} para conservar 1e-3 en 40 pasos')"
        ),
        "desafio_autonomo": (
            "Implementa la tarea de «copia con retardo»: la red debe repetir un símbolo visto T pasos "
            "antes. Mide la precisión con un RNN tanh y con una celda LSTM para T = 5, 20 y 100. "
            "Reporta la semilla y el número de parámetros de cada modelo."
        ),
        "evidencia": (
            "Guarda la tabla de decaimiento por valor de puerta, el umbral que encontraste y el enunciado "
            "corregido sobre qué resuelve y qué no resuelve la LSTM."
        ),
        "cierre": (
            "Ya se pueden modelar secuencias largas. Falta que la entrada y la salida puedan tener "
            "longitudes distintas, que es lo que exige traducir."
        ),
    },
    "P04_alexnet": {
        "intuicion": (
            "Un detector de bordes no debería tener que reaprenderse en cada esquina de la imagen. "
            "La convolución aplica el mismo detector en todas partes: menos parámetros, y la posición "
            "deja de importar."
        ),
        "concepto": (
            "```text\n"
            "(I * K)[r, c] = Σᵢ Σⱼ I[r+i, c+j] · K[i, j]      convolución (correlación cruzada)\n"
            "ReLU(z) = max(0, z)                              no satura para z > 0\n"
            "maxpool                                          invarianza local a pequeños desplazamientos\n"
            "```\n\n"
            "Un kernel 3×3 tiene 9 parámetros y se reutiliza en toda la imagen. La capa densa equivalente "
            "necesitaría un peso por cada par (píxel de entrada, píxel de salida)."
        ),
        "codigo_md": "El motor convoluciona la misma imagen y una versión desplazada, y compara el conteo de parámetros.",
        "codigo": (
            "r = run_paper_lab('convnet', seed=7)['result']\n"
            "print('mapa de activación (borde en el centro):')\n"
            "for fila in r['feature_map']:\n"
            "    print(' ', fila)\n"
            "print('\\nla misma imagen desplazada:')\n"
            "for fila in r['feature_map_shifted']:\n"
            "    print(' ', fila)\n"
            "show(r['params'])"
        ),
        "prediccion": (
            "1. Si desplazo el borde una columna a la izquierda, ¿el pico de activación se desplaza o desaparece?\n"
            "2. ¿Cuántas veces menos parámetros usa el kernel frente a la capa densa equivalente?\n"
            "3. Tras ReLU y max-pool, ¿queda información de *dónde* estaba el borde?"
        ),
        "experimento": (
            "def convolucionar(imagen, kernel):\n"
            "    k = len(kernel)\n"
            "    n = len(imagen) - k + 1\n"
            "    return [[sum(imagen[r+i][c+j] * kernel[i][j] for i in range(k) for j in range(k))\n"
            "             for c in range(n)] for r in range(n)]\n"
            "\n"
            "vertical = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]\n"
            "horizontal = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]\n"
            "imagen = [[0.0] * 3 + [1.0] * 3 for _ in range(6)]     # borde VERTICAL\n"
            "\n"
            "print('kernel vertical  →', convolucionar(imagen, vertical)[0])\n"
            "print('kernel horizontal→', convolucionar(imagen, horizontal)[0])"
        ),
        "salida": (
            "El kernel vertical responde con `3.0` justo en el borde; el horizontal responde `0.0` en todas "
            "partes. **Un filtro solo ve aquello para lo que está sintonizado**: por eso una capa tiene "
            "muchos filtros distintos, y por eso AlexNet aprendió los suyos en lugar de escribirlos."
        ),
        "comentario": (
            "Lo que AlexNet aportó no fue la convolución (LeNet, 1998) sino la combinación que la hizo "
            "escalar: profundidad, ReLU, dropout, aumento de datos, dos GPU y un dataset del tamaño de "
            "ImageNet. Ninguna pieza sola explica el resultado."
        ),
        "antipatron_md": "Anti-patrón: presentar el resultado de AlexNet como «la CNN es mejor» sin nombrar el dataset ni el protocolo de evaluación.",
        "antipatron": (
            "print('«Las CNN son mejores que los métodos clásicos» ← afirmación sin contexto')\n"
            "print('¿mejores en qué tarea, con qué datos, con qué métrica, contra qué línea base?')"
        ),
        "correccion_md": "Un claim verificable nombra tarea, dataset, métrica, línea base y condiciones de cómputo.",
        "correccion": (
            "claim = {\n"
            "    'tarea': 'clasificación de imágenes en 1000 categorías',\n"
            "    'dataset': 'ILSVRC-2012 (subconjunto de ImageNet)',\n"
            "    'metrica': 'error top-5 en el conjunto de test',\n"
            "    'linea_base': 'mejor sistema del certamen basado en descriptores diseñados a mano',\n"
            "    'computo': '2 GPU, entrenamiento de varios días (ver sección 5 del paper)',\n"
            "    'verificar_en': 'tabla de resultados del paper original',\n"
            "}\n"
            "show(claim)"
        ),
        "desafio_guiado_md": "Comprueba la equivarianza: convoluciona la imagen desplazada y verifica que el pico se mueve la misma cantidad.",
        "desafio_guiado": (
            "desplazada = [[0.0] * 2 + [1.0] * 4 for _ in range(6)]\n"
            "original_fila = convolucionar(imagen, vertical)[0]\n"
            "desplazada_fila = convolucionar(desplazada, vertical)[0]\n"
            "print('original :', original_fila, '→ pico en índice', original_fila.index(max(original_fila)))\n"
            "print('desplazada:', desplazada_fila, '→ pico en índice', desplazada_fila.index(max(desplazada_fila)))"
        ),
        "desafio_autonomo": (
            "Toma un dataset pequeño y público de imágenes en escala de grises. Compara una red densa y "
            "una convolucional con un número de parámetros comparable. Reporta accuracy, número de "
            "parámetros y tiempo de entrenamiento, y evalúa también con las imágenes desplazadas 2 píxeles."
        ),
        "evidencia": (
            "Guarda los dos mapas de activación, el conteo comparado de parámetros y el claim reescrito "
            "con tarea, dataset, métrica y línea base."
        ),
        "cierre": (
            "La visión aprendió a extraer sus propias características. El lenguaje seguía representando "
            "las palabras como identificadores sin relación entre sí."
        ),
    },
    "P05_word2vec": {
        "intuicion": (
            "Dime con quién apareces y te diré qué significas. Si «rey» y «reina» aparecen rodeadas de "
            "las mismas palabras, sus vectores acabarán apuntando en direcciones parecidas — sin que "
            "nadie escriba jamás una definición."
        ),
        "concepto": (
            "Skip-gram maximiza `log σ(v_c·u_o)` para pares (centro, contexto) reales y "
            "`log σ(−v_c·u_k)` para `k` pares negativos muestreados al azar.\n\n"
            "El resultado es un espacio donde `coseno(a, b)` mide similitud distribucional y donde "
            "ciertas relaciones aparecen como desplazamientos aproximadamente constantes."
        ),
        "codigo_md": "El motor entrena skip-gram con muestreo negativo sobre un corpus de 8 frases, en Python puro.",
        "codigo": (
            "r = run_paper_lab('word2vec', seed=7)['result']\n"
            "print('vocabulario:', r['vocab_size'], '· dimensión:', r['dim'], '· pares:', r['training_pairs'])\n"
            "show(r['neighbours'])"
        ),
        "prediccion": (
            "1. ¿Quién estará más cerca de «rey»: «reina», «hombre» o «reino»?\n"
            "2. ¿El resultado de `rey − hombre + mujer` será estable al cambiar la semilla?\n"
            "3. Con solo 8 frases, ¿qué parte del resultado es señal y qué parte es ruido?"
        ),
        "experimento": (
            "for semilla in (1, 7, 42):\n"
            "    r = run_paper_lab('word2vec', seed=semilla)['result']\n"
            "    top = r['analogy_rey_menos_hombre_mas_mujer']\n"
            "    print(f\"semilla {semilla:>2} → 1º {top[0]['word']} ({top[0]['cos']}) · \"\n"
            "          f\"2º {top[1]['word']} ({top[1]['cos']})\")"
        ),
        "salida": (
            "«reina» sale primera en las tres semillas, con un coseno muy por encima del segundo lugar. "
            "Que el **primer** puesto sea estable y el **segundo** cambie es la lectura honesta: la señal "
            "fuerte se sostiene, la cola es ruido de un corpus diminuto."
        ),
        "comentario": (
            "La aritmética de analogías se popularizó como si el espacio codificara conceptos limpios. "
            "Trabajos posteriores mostraron que el resultado depende del protocolo (por ejemplo, de "
            "excluir del ranking las tres palabras de la consulta, como hace este código)."
        ),
        "antipatron_md": "Anti-patrón: evaluar la analogía **sin excluir** las palabras de la consulta. El vecino más cercano acaba siendo la propia palabra de partida.",
        "antipatron": (
            "print('Si no excluyes rey/hombre/mujer del ranking, «rey» suele ganar por su propio peso.')\n"
            "print('El resultado parecería trivialmente correcto o trivialmente absurdo, según el caso.')\n"
            "print('El protocolo de evaluación es parte del resultado, no un detalle de implementación.')"
        ),
        "correccion_md": "El código del motor ya aplica la exclusión. Aquí se hace explícito el criterio:",
        "correccion": (
            "protocolo = {\n"
            "    'consulta': 'rey - hombre + mujer',\n"
            "    'excluidas_del_ranking': ['rey', 'hombre', 'mujer'],\n"
            "    'metrica': 'coseno',\n"
            "    'corpus': '8 frases (juguete)',\n"
            "    'semillas_probadas': [1, 7, 42],\n"
            "}\n"
            "show(protocolo)"
        ),
        "desafio_guiado_md": "Comprueba si «calle» y «reino» quedan lejos entre sí: son las dos «familias» semánticas del corpus.",
        "desafio_guiado": (
            "r = run_paper_lab('word2vec', seed=7)['result']\n"
            "show(r['neighbours']['calle'])"
        ),
        "desafio_autonomo": (
            "Entrena embeddings sobre un corpus público en español de al menos 1 millón de palabras. "
            "Construye tu propio conjunto de 30 analogías y reporta accuracy top-1 y top-5, con la "
            "distribución de frecuencias de las palabras implicadas. Comenta el sesgo que encuentres."
        ),
        "evidencia": (
            "Guarda la tabla de vecinos, el resultado de la analogía en tres semillas y una frase sobre "
            "qué parte del resultado consideras evidencia y qué parte artefacto del corpus."
        ),
        "cierre": (
            "Las palabras ya tienen geometría. Falta que un modelo produzca *secuencias* completas a "
            "partir de otras secuencias."
        ),
    },
    "P06_seq2seq": {
        "intuicion": (
            "Leer una frase entera, cerrar los ojos, y escribir la traducción solo de memoria. Funciona "
            "con frases cortas. Con un párrafo, cuando llegas al final ya no recuerdas cómo empezaba."
        ),
        "concepto": (
            "```text\n"
            "c = encoder(x₁…x_n)                    un único vector de tamaño fijo\n"
            "p(y₁…y_m) = Π_t p(y_t | y_<t, c)       el decodificador solo ve c\n"
            "```\n\n"
            "Toda la información de la entrada tiene que caber en `c`. La capacidad de `c` no crece con "
            "la longitud de la frase: ahí está el cuello de botella."
        ),
        "codigo_md": "El motor codifica secuencias de longitud creciente en un vector fijo y mide cuánto sobrevive del principio.",
        "codigo": (
            "r = run_paper_lab('seq2seq', seed=7)['result']\n"
            "print('dimensión del vector de contexto:', r['state_dim'])\n"
            "for fila in r['bottleneck']:\n"
            "    print(f\"n={fila['length']:>2} · cos(primer token)={fila['cos_primer_token']:+.3f} \"\n"
            "          f\"· cos(último)={fila['cos_ultimo_token']:+.3f} · recuperables={fila['tokens_recuperables']}\")"
        ),
        "prediccion": (
            "1. ¿Cómo evolucionará el coseno con el primer token al pasar de n=2 a n=32?\n"
            "2. ¿Y el coseno con el último token?\n"
            "3. Si inviertes la secuencia de entrada, ¿a qué extremo beneficias?"
        ),
        "experimento": (
            "for fila in r['bottleneck']:\n"
            "    brecha = fila['cos_ultimo_token'] - fila['cos_primer_token']\n"
            "    print(f\"n={fila['length']:>2} · brecha último−primero = {brecha:+.3f}\")"
        ),
        "salida": (
            "La brecha crece con la longitud: el vector fijo está dominado por lo último que leyó. Este es "
            "exactamente el motivo por el que Sutskever et al. invirtieron la secuencia fuente — así el "
            "principio de la frase de entrada queda *cerca* del principio de la de salida."
        ),
        "comentario": (
            "Invertir la entrada es un parche brillante y honesto: no elimina el cuello de botella, "
            "reordena qué información se pierde. El siguiente paper eliminará la premisa entera."
        ),
        "antipatron_md": "Anti-patrón: culpar al tamaño del modelo («faltan parámetros») cuando el problema es estructural.",
        "antipatron": (
            "print('Diagnóstico incorrecto: «sube la dimensión del estado y se arregla».')\n"
            "print('Duplicar la dimensión retrasa el problema; no cambia que la capacidad sea CONSTANTE')\n"
            "print('mientras la longitud de la entrada es VARIABLE.')"
        ),
        "correccion_md": "Diagnóstico correcto: capacidad constante frente a información creciente.",
        "correccion": (
            "diagnostico = {\n"
            "    'sintoma': 'la calidad cae al crecer la longitud de la entrada',\n"
            "    'causa_estructural': 'la entrada se comprime en un vector de tamaño fijo',\n"
            "    'parche_del_paper': 'invertir la secuencia fuente',\n"
            "    'solucion_de_fondo': 'dejar que el decodificador consulte TODOS los estados (P07)',\n"
            "}\n"
            "show(diagnostico)"
        ),
        "desafio_guiado_md": "Sube `state_dim` mentalmente: ¿a partir de qué longitud volvería a fallar? Compruébalo con una versión propia del codificador.",
        "desafio_guiado": (
            "def codificar(tokens, dim, decaimiento=0.7):\n"
            "    estado = [0.0] * dim\n"
            "    for i, t in enumerate(tokens):\n"
            "        vec = [((i * 7 + d * 3) % 11) / 11 for d in range(dim)]\n"
            "        estado = [decaimiento * s + (1 - decaimiento) * v for s, v in zip(estado, vec)]\n"
            "    return estado\n"
            "\n"
            "for n in (4, 16, 64):\n"
            "    estado = codificar(list(range(n)), dim=8)\n"
            "    print(f'n={n:>2} → norma del estado {sum(x*x for x in estado) ** 0.5:.4f}')"
        ),
        "desafio_autonomo": (
            "Implementa un seq2seq de juguete para invertir cadenas de longitud variable. Mide la "
            "exactitud por longitud (2, 4, 8, 16) con y sin inversión de la entrada. Reporta la curva."
        ),
        "evidencia": (
            "Guarda la tabla de cosenos por longitud, la brecha primero-último y el diagnóstico "
            "distinguiendo causa estructural de parche."
        ),
        "cierre": (
            "El cuello de botella tiene nombre y medida. La solución no será un vector más grande, sino "
            "dejar de comprimir."
        ),
    },
    "P07_attention_bahdanau": {
        "intuicion": (
            "En vez de memorizar la frase entera y cerrar los ojos, el traductor deja el texto original "
            "sobre la mesa y, para cada palabra que escribe, vuelve a mirar la parte que le hace falta."
        ),
        "concepto": (
            "```text\n"
            "e_ij = vᵀ·tanh(W·s_{i−1} + U·h_j)      puntuación de compatibilidad (aditiva)\n"
            "α_ij = softmax_j(e_ij)                  pesos que suman 1\n"
            "c_i  = Σ_j α_ij · h_j                   vector de contexto DISTINTO en cada paso i\n"
            "```\n\n"
            "El cuello de botella desaparece: `c_i` se recalcula en cada paso a partir de todos los "
            "estados del codificador."
        ),
        "codigo_md": "El motor aprende los 18 parámetros de la atención aditiva por descenso de gradiente y muestra la matriz α.",
        "codigo": (
            "r = run_paper_lab('bahdanau', seed=7)['result']\n"
            "print('parámetros:', r['parametros'], '· aciertos:', r['aciertos_de_alineacion'])\n"
            "for fila in r['alignment']:\n"
            "    print(f\"{fila['target']:<8} → {fila['argmax']:<8} α={fila['alpha']} H={fila['entropia']}\")"
        ),
        "prediccion": (
            "1. ¿Sumarán exactamente 1 los pesos α de cada fila? ¿Por qué?\n"
            "2. ¿Será la entropía alta (atención repartida) o baja (atención concentrada) tras entrenar?\n"
            "3. Si la atención acierta la alineación, ¿demuestra eso que el modelo «entiende» la frase?"
        ),
        "experimento": (
            "for semilla in (1, 7, 42):\n"
            "    r = run_paper_lab('bahdanau', seed=semilla)['result']\n"
            "    entropias = [f['entropia'] for f in r['alignment']]\n"
            "    print(f\"semilla {semilla:>2} · aciertos {r['aciertos_de_alineacion']} \"\n"
            "          f\"· entropía media {sum(entropias)/len(entropias):.3f} \"\n"
            "          f\"· pérdida final {r['perdida'][-1]['loss']}\")"
        ),
        "salida": (
            "La entropía baja (cerca de 0) significa que α se concentra casi todo en una posición: la "
            "alineación es nítida. `suma_alpha = 1.0` en cada fila confirma que softmax produce una "
            "distribución de probabilidad sobre las posiciones de entrada."
        ),
        "comentario": (
            "Aquí la alineación está supervisada para que el mecanismo se vea. En el paper **nadie etiqueta "
            "la alineación**: emerge al entrenar solo la traducción. Esa es la parte notable, y conviene "
            "no atribuir a este notebook un mérito que corresponde al paper."
        ),
        "antipatron_md": "Anti-patrón: leer la matriz de atención como una explicación causal («el modelo se fijó en X porque X importa»).",
        "antipatron": (
            "print('Afirmación tentadora: «α muestra en qué se fijó el modelo, luego explica su decisión».')\n"
            "print('Jain y Wallace (2019) mostraron que se pueden construir distribuciones de atención')\n"
            "print('muy distintas que producen la MISMA salida. Correlación ≠ explicación.')"
        ),
        "correccion_md": "Enunciado defendible sobre lo que la atención sí aporta:",
        "correccion": (
            "defendible = [\n"
            "    'α es un peso de mezcla, verificable y que suma 1',\n"
            "    'α elimina el cuello de botella del vector fijo (eso sí es causal en la arquitectura)',\n"
            "    'α es una PISTA de interpretación, no una explicación del proceso interno',\n"
            "]\n"
            "for linea in defendible:\n"
            "    print('-', linea)"
        ),
        "desafio_guiado_md": "Comprueba qué ocurre si eliminas el softmax y usas los scores crudos como pesos.",
        "desafio_guiado": (
            "scores = [2.0, 1.0, 0.5, -3.0]\n"
            "suma_cruda = sum(scores)\n"
            "print('pesos crudos normalizados:', [round(s / suma_cruda, 3) for s in scores])\n"
            "print('→ hay pesos NEGATIVOS y la suma se rompe si los scores suman ~0')\n"
            "import math\n"
            "exp = [math.exp(s) for s in scores]\n"
            "print('softmax                  :', [round(e / sum(exp), 3) for e in exp])"
        ),
        "desafio_autonomo": (
            "Entrena atención aditiva sin supervisión de alineación: solo con la pérdida de predecir el "
            "token siguiente en un corpus paralelo de juguete. Comprueba si la alineación emerge sola y "
            "reporta cuántos ejemplos hicieron falta."
        ),
        "evidencia": (
            "Guarda la matriz α, la entropía por fila y tu enunciado sobre qué se puede y qué no se puede "
            "concluir de esa matriz."
        ),
        "cierre": (
            "Si la atención resuelve el acceso a toda la entrada… ¿para qué sigue haciendo falta la "
            "recurrencia? Esa pregunta es el título del paper siguiente."
        ),
    },
    "P08_transformer": {
        "intuicion": (
            "Cada palabra pregunta al resto de la frase «¿quién de vosotros me importa?», recibe una "
            "respuesta ponderada y se actualiza. Todas las palabras lo hacen **a la vez**, no en fila. "
            "Ahí está la paralelización, y ahí está el salto de escala."
        ),
        "concepto": (
            "```text\n"
            "Attention(Q, K, V) = softmax(QKᵀ / √d_k) · V\n"
            "MultiHead(X) = Concat(head₁ … head_h)·W^O,  head_i = Attention(XW_i^Q, XW_i^K, XW_i^V)\n"
            "PE(pos, 2i) = sin(pos/10000^{2i/d}),  PE(pos, 2i+1) = cos(pos/10000^{2i/d})\n"
            "sublayer(x) = LayerNorm(x + Sublayer(x))\n"
            "```\n\n"
            "`√d_k` no es cosmética: sin ella el producto escalar crece con la dimensión, el softmax se "
            "satura y el gradiente se apaga."
        ),
        "codigo_md": "El motor implementa la ecuación 1 completa: escala, máscara causal, multi-cabeza, codificación posicional y residual + layer norm.",
        "codigo": (
            "r = run_paper_lab('transformer', seed=7)['result']\n"
            "show(r['entropia_media'])\n"
            "print('\\nmatriz de atención con máscara causal:')\n"
            "for fila in r['mascara_causal']:\n"
            "    print(' ', fila)"
        ),
        "prediccion": (
            "1. ¿La entropía será mayor con escala `√d_k` o sin ella? ¿Qué significa cada caso?\n"
            "2. ¿Qué forma tendrá la matriz con máscara causal?\n"
            "3. Para n=1000, ¿cuántas veces más operaciones hace la self-attention que la recurrencia con d=8?"
        ),
        "experimento": (
            "for fila in r['complejidad']:\n"
            "    print(f\"n={fila['n']:>5} · self-attention {fila['self_attention_ops']:>10} ops \"\n"
            "          f\"· recurrente {fila['recurrent_ops']:>8} ops \"\n"
            "          f\"· camino RNN {fila['camino_maximo_rnn']:>5} vs attention {fila['camino_maximo_attention']}\")"
        ),
        "salida": (
            "Dos lecturas opuestas y ambas ciertas: el camino entre dos posiciones es **1** en atención y "
            "**n** en recurrencia (ventaja de optimización), pero el coste crece con **n²** (desventaja de "
            "memoria y cómputo). El Transformer compró paralelismo pagando con complejidad cuadrática."
        ),
        "comentario": (
            "El título es una consigna, no un teorema. El modelo del paper **también** necesita redes "
            "feed-forward por posición, residuales, layer norm y codificación posicional. Sin ellas la "
            "atención sola no entrena. Esta es la sección 3 del paper, no una interpretación."
        ),
        "antipatron_md": "Anti-patrón deliberado: quitar la escala `√d_k` y creer que «da casi igual».",
        "antipatron": (
            "import math\n"
            "import random\n"
            "\n"
            "rng = random.Random(0)\n"
            "for d_k in (4, 64, 512):\n"
            "    q = [rng.gauss(0, 1) for _ in range(d_k)]\n"
            "    k = [rng.gauss(0, 1) for _ in range(d_k)]\n"
            "    crudo = sum(a * b for a, b in zip(q, k))\n"
            "    print(f'd_k={d_k:>3} · qᵀk sin escalar = {crudo:+8.2f} · escalado = {crudo / math.sqrt(d_k):+6.2f}')"
        ),
        "correccion_md": "La magnitud del producto escalar crece como √d_k. Al dividir por √d_k, la varianza vuelve a ~1 y el softmax no se satura:",
        "correccion": (
            "def softmax(xs):\n"
            "    m = max(xs)\n"
            "    e = [math.exp(x - m) for x in xs]\n"
            "    return [v / sum(e) for v in e]\n"
            "\n"
            "scores = [12.0, 10.5, 9.0, 8.0]\n"
            "print('sin escalar :', [round(p, 4) for p in softmax(scores)])\n"
            "print('escalado /8 :', [round(p, 4) for p in softmax([s / 8 for s in scores])])\n"
            "print('→ sin escalar, un solo token acapara casi toda la masa y el gradiente del resto ≈ 0')"
        ),
        "desafio_guiado_md": "Verifica que la codificación posicional distingue posiciones y que posiciones cercanas tienen codificaciones parecidas.",
        "desafio_guiado": (
            "from ai_evolution.papers_lab import positional_encoding\n"
            "\n"
            "def coseno(a, b):\n"
            "    na = sum(x * x for x in a) ** 0.5\n"
            "    nb = sum(x * x for x in b) ** 0.5\n"
            "    return sum(x * y for x, y in zip(a, b)) / (na * nb)\n"
            "\n"
            "pe = [positional_encoding(p, 16) for p in range(8)]\n"
            "for p in range(1, 8):\n"
            "    print(f'cos(PE[0], PE[{p}]) = {coseno(pe[0], pe[p]):+.4f}')"
        ),
        "desafio_autonomo": (
            "Implementa las proyecciones aprendidas W_Q, W_K, W_V (aquí ausentes) y entrena el bloque en "
            "una tarea de copia. Mide qué aporta cada cabeza haciendo una ablación: desactiva una cabeza "
            "y reporta la caída de exactitud."
        ),
        "evidencia": (
            "Guarda: entropía con y sin escala, la matriz causal triangular, la tabla de complejidad y una "
            "frase sobre qué compró y qué pagó el Transformer."
        ),
        "cierre": (
            "El bloque está completo. A partir de aquí, la historia se bifurca: usar solo el encoder (P09) "
            "o solo el decoder (P10). Las ocho miniaturas `T01`–`T08` desmontan este bloque pieza por pieza."
        ),
    },
    "P09_bert": {
        "intuicion": (
            "Para adivinar una palabra tapada, un humano mira lo que hay antes **y** después. Un modelo "
            "que solo mira hacia atrás está renunciando a la mitad de la evidencia disponible."
        ),
        "concepto": (
            "MLM: se enmascara ~15 % de los tokens y se predice cada uno usando ambos lados.\n\n"
            "```text\n"
            "L = − Σ_{t ∈ enmascarados} log p(x_t | x_contexto_izquierdo, x_contexto_derecho)\n"
            "```\n\n"
            "No se puede entrenar bidireccionalmente con «predice el siguiente token»: cada token se vería "
            "a sí mismo a través de las capas. Enmascarar es lo que hace legítima la bidireccionalidad."
        ),
        "codigo_md": "El motor cuenta candidatos compatibles con contexto solo-izquierdo frente a contexto bidireccional.",
        "codigo": (
            "r = run_paper_lab('bert_mlm', seed=7)['result']\n"
            "for fila in r['masked_predictions']:\n"
            "    print(f\"«{fila['izquierda']} [MASK] {fila['derecha']}» (gold: {fila['gold']})\")\n"
            "    print('   solo izquierda :', fila['candidatos_solo_izquierda'], f\"({fila['ambiguedad_izquierda']} opciones)\")\n"
            "    print('   bidireccional  :', fila['candidatos_bidireccional'], f\"({fila['ambiguedad_bidireccional']} opciones)\")"
        ),
        "prediccion": (
            "1. ¿Reducirá el contexto derecho el número de candidatos, o lo dejará igual?\n"
            "2. En «el banco [MASK] estaba mojado», ¿qué sentido de «banco» activa el contexto derecho?\n"
            "3. ¿Por qué NO se puede entrenar un modelo bidireccional prediciendo el token siguiente?"
        ),
        "experimento": (
            "for fila in r['masked_predictions']:\n"
            "    reduccion = fila['ambiguedad_izquierda'] - fila['ambiguedad_bidireccional']\n"
            "    print(f\"gold={fila['gold']:<8} · ambigüedad izq={fila['ambiguedad_izquierda']} \"\n"
            "          f\"bi={fila['ambiguedad_bidireccional']} · reducción={reduccion}\")"
        ),
        "salida": (
            "El contexto derecho reduce (o iguala) el conjunto de candidatos, nunca lo amplía: añadir "
            "evidencia solo puede restringir. Ese es, en una línea, el argumento del paper."
        ),
        "comentario": (
            "Cuidado con el anacronismo inverso: BERT **no** es un modelo generativo de propósito general. "
            "Es un codificador para tareas de comprensión. La familia que hoy llamamos «LLM» viene de la "
            "otra rama, la del decoder (P10)."
        ),
        "antipatron_md": "Anti-patrón: usar BERT como generador de texto autorregresivo porque «es un Transformer».",
        "antipatron": (
            "print('Uso incorrecto: pedirle a un encoder MLM que continúe un texto token a token.')\n"
            "print('Su objetivo de entrenamiento nunca fue p(x_t | x_<t): rellena huecos, no continúa.')"
        ),
        "correccion_md": "Elige la familia según el objetivo de preentrenamiento, no según la arquitectura:",
        "correccion": (
            "familias = {\n"
            "    'encoder (BERT)': {'objetivo': 'MLM', 'bueno_para': 'clasificar, extraer, buscar, comparar'},\n"
            "    'decoder (GPT)': {'objetivo': 'siguiente token', 'bueno_para': 'generar, completar, dialogar'},\n"
            "    'encoder-decoder (T5, BART)': {'objetivo': 'denoising / seq2seq', 'bueno_para': 'traducir, resumir'},\n"
            "}\n"
            "show(familias)"
        ),
        "desafio_guiado_md": "Añade una frase nueva al corpus y comprueba cómo cambia la ambigüedad del hueco.",
        "desafio_guiado": (
            "corpus = [\n"
            "    'el banco del parque estaba mojado por la lluvia'.split(),\n"
            "    'el banco del rio estaba mojado por la lluvia'.split(),\n"
            "    'el banco del museo estaba mojado por la lluvia'.split(),   # <-- frase nueva\n"
            "]\n"
            "candidatos = {}\n"
            "for linea in corpus:\n"
            "    i = linea.index('del') + 1\n"
            "    candidatos[linea[i]] = candidatos.get(linea[i], 0) + 1\n"
            "print('candidatos para «el banco del [MASK] estaba mojado»:', candidatos)"
        ),
        "desafio_autonomo": (
            "Con un modelo BERT en español de acceso abierto y ejecución local, compara la probabilidad "
            "del token correcto con contexto completo y truncando el contexto derecho. Usa 20 frases "
            "propias y reporta la diferencia media, la desviación y los casos donde no ayuda."
        ),
        "evidencia": (
            "Guarda la tabla de ambigüedad, la justificación de por qué enmascarar habilita la "
            "bidireccionalidad, y la tabla de familias con su objetivo de preentrenamiento."
        ),
        "cierre": (
            "El preentrenamiento ya es la norma. Falta descubrir qué ocurre cuando la rama del decoder "
            "se escala dos órdenes de magnitud."
        ),
    },
    "P10_gpt3": {
        "intuicion": (
            "En vez de reentrenar el modelo para cada tarea, se le muestran dos o tres ejemplos dentro "
            "del propio texto de entrada y el modelo sigue el patrón. Ningún peso cambia: lo único que "
            "cambia es lo que hay escrito antes de la pregunta."
        ),
        "concepto": (
            "El modelo sigue siendo `p(x_t | x_<t)`. Lo nuevo es el **protocolo de evaluación**:\n\n"
            "```text\n"
            "zero-shot : instrucción                        → respuesta\n"
            "one-shot  : instrucción + 1 ejemplo            → respuesta\n"
            "few-shot  : instrucción + k ejemplos           → respuesta\n"
            "```\n\n"
            "Sin actualización de gradiente en ninguno de los tres casos."
        ),
        "codigo_md": "El motor simula el fenómeno con inducción explícita de hipótesis: cada ejemplo del prompt elimina hipótesis incompatibles.",
        "codigo": (
            "r = run_paper_lab('gpt3_icl', seed=7)['result']\n"
            "print('tarea latente:', r['tarea_latente'], '· pesos actualizados:', not r['sin_actualizar_pesos'])\n"
            "for fila in r['in_context_learning']:\n"
            "    print(f\"{fila['shots']}-shot · hipótesis vivas {len(fila['hipotesis_compatibles'])} \"\n"
            "          f\"· elegida {fila['elegida']:<20} · accuracy {fila['accuracy_held_out']}\")"
        ),
        "prediccion": (
            "1. ¿Cuántos ejemplos harán falta para dejar una sola hipótesis compatible?\n"
            "2. ¿La accuracy con 0 ejemplos será alta o azarosa?\n"
            "3. ¿Este experimento demuestra algo sobre GPT-3, o solo ilustra el concepto?"
        ),
        "experimento": (
            "for semilla in (1, 7, 42):\n"
            "    r = run_paper_lab('gpt3_icl', seed=semilla)['result']\n"
            "    curva = [(f['shots'], f['accuracy_held_out']) for f in r['in_context_learning']]\n"
            "    print(f'semilla {semilla:>2} · curva shots→accuracy: {curva}')"
        ),
        "salida": (
            "La accuracy sube con el número de ejemplos y se estabiliza. Con 0 ejemplos el sistema elige "
            "entre hipótesis igualmente compatibles: acertar ahí es suerte, no capacidad."
        ),
        "comentario": (
            "**Esto no es GPT-3.** Es una maqueta del fenómeno. GPT-3 no enumera hipótesis: condiciona una "
            "distribución aprendida sobre billones de tokens. La maqueta sirve para razonar sobre el "
            "mecanismo, no para hacer afirmaciones sobre el modelo real. Confundir ambas cosas es "
            "exactamente el error que este programa entrena a detectar."
        ),
        "antipatron_md": "Anti-patrón: interpretar «few-shot learning» como que el modelo *aprende* durante la inferencia.",
        "antipatron": (
            "print('Lectura incorrecta: «con 3 ejemplos el modelo aprendió la tarea».')\n"
            "print('No hay aprendizaje: no hay gradiente, no hay actualización, no hay memoria entre llamadas.')\n"
            "print('Cierra la sesión y el modelo no recuerda nada.')"
        ),
        "correccion_md": "Formulación correcta: condicionamiento, no aprendizaje.",
        "correccion": (
            "correcto = {\n"
            "    'que_ocurre': 'el prompt condiciona la distribución de salida',\n"
            "    'que_NO_ocurre': ['actualización de pesos', 'persistencia entre llamadas', 'memoria del ejemplo'],\n"
            "    'consecuencia_practica': 'el coste se paga en tokens de contexto en CADA llamada',\n"
            "}\n"
            "show(correcto)"
        ),
        "desafio_guiado_md": "Cambia la tarea latente a «última letra» y comprueba cuántos ejemplos hacen falta para desambiguar.",
        "desafio_guiado": (
            "palabras = ['gato', 'arbol', 'rio', 'libro']\n"
            "hipotesis = {\n"
            "    'primera_letra': lambda w: w[0].upper(),\n"
            "    'ultima_letra': lambda w: w[-1].upper(),\n"
            "    'longitud': lambda w: str(len(w)),\n"
            "}\n"
            "verdad = 'ultima_letra'\n"
            "for k in (0, 1, 2):\n"
            "    demos = [(w, hipotesis[verdad](w)) for w in palabras[:k]]\n"
            "    vivas = [n for n, f in hipotesis.items() if all(f(w) == y for w, y in demos)]\n"
            "    print(f'{k}-shot → hipótesis compatibles: {sorted(vivas)}')"
        ),
        "desafio_autonomo": (
            "Diseña un experimento de few-shot con un modelo abierto ejecutable localmente. Varía el "
            "**orden** de los ejemplos manteniendo el contenido y mide la varianza del resultado. "
            "Documenta si la sensibilidad al orden invalida alguna conclusión que habrías sacado."
        ),
        "evidencia": (
            "Guarda la curva shots→accuracy, la distinción entre condicionar y aprender, y una frase "
            "explícita sobre qué NO demuestra esta maqueta."
        ),
        "cierre": (
            "El modelo ya se adapta sin reentrenarse, pero todo lo que sabe sigue congelado en sus pesos "
            "y no se puede citar. Ese es el problema del siguiente hito."
        ),
    },
    "P11_rag": {
        "intuicion": (
            "Un examen a libro cerrado frente a un examen a libro abierto. En el primero, si no lo "
            "recuerdas, lo inventas. En el segundo, buscas la página, la citas y quien corrige puede "
            "verificarla."
        ),
        "concepto": (
            "```text\n"
            "p(y | x) ≈ Σ_{z ∈ top-k(x)} p_η(z | x) · p_θ(y | x, z)\n"
            "```\n\n"
            "`p_η` es el recuperador (memoria **no paramétrica**, actualizable sin reentrenar) y `p_θ` el "
            "generador (memoria **paramétrica**). RAG separa lo que se sabe de cómo se razona."
        ),
        "codigo_md": "El motor recupera por similitud léxica, genera con citas y muestra el contraste con la respuesta sin recuperación.",
        "codigo": (
            "r = run_paper_lab('rag', seed=7)['result']\n"
            "print('consulta:', r['query'], '\\n')\n"
            "for fila in r['ranking']:\n"
            "    print(f\"  {fila['doc']} score={fila['score']:.3f} · {fila['text'][:60]}…\")\n"
            "print('\\ncon recuperación :', r['respuesta_con_citas'])\n"
            "print('sin recuperación :', r['respuesta_sin_recuperacion'])"
        ),
        "prediccion": (
            "1. ¿Qué documento quedará primero: el de la sanción o el de la entrada en vigor?\n"
            "2. ¿Qué score tendrá el documento sobre hornear pan?\n"
            "3. Si el recuperador fallara, ¿el generador lo notaría?"
        ),
        "experimento": (
            "consultas = [\n"
            "    'cuando entro en vigor la ley de transparencia algoritmica',\n"
            "    'a que temperatura se hornea el pan',\n"
            "    'quien gano el mundial de 1986',\n"
            "]\n"
            "documentos = {f['doc']: f['text'] for f in r['ranking']}\n"
            "\n"
            "def tf(texto):\n"
            "    d = {}\n"
            "    for t in texto.lower().replace('.', '').split():\n"
            "        d[t] = d.get(t, 0) + 1\n"
            "    return d\n"
            "\n"
            "def coseno(a, b):\n"
            "    claves = set(a) | set(b)\n"
            "    va = [a.get(k, 0) for k in claves]\n"
            "    vb = [b.get(k, 0) for k in claves]\n"
            "    na = sum(x * x for x in va) ** 0.5\n"
            "    nb = sum(x * x for x in vb) ** 0.5\n"
            "    return sum(x * y for x, y in zip(va, vb)) / (na * nb) if na and nb else 0.0\n"
            "\n"
            "for q in consultas:\n"
            "    mejor = max(documentos.items(), key=lambda kv: coseno(tf(q), tf(kv[1])))\n"
            "    print(f'{q[:45]:<47} → {mejor[0]} (score {coseno(tf(q), tf(mejor[1])):.3f})')"
        ),
        "salida": (
            "La tercera consulta (mundial de 1986) **no tiene respuesta en el corpus** y aun así el "
            "recuperador devuelve el documento «menos malo» con un score bajo. Un sistema honesto usa un "
            "umbral: por debajo de él, la respuesta correcta es «no lo sé»."
        ),
        "comentario": (
            "Recuperar no es responder. Los tres fallos típicos son independientes: (1) el documento "
            "correcto no está en el índice, (2) está pero no se recupera, (3) se recupera y el generador "
            "lo contradice. Evaluar RAG exige medir los tres por separado."
        ),
        "antipatron_md": "Anti-patrón: dar por buena una respuesta porque «lleva citas», sin comprobar que la cita sostiene la afirmación.",
        "antipatron": (
            "respuesta_falsa = 'La sanción máxima es del 12 % de la facturación [d4].'\n"
            "print(respuesta_falsa)\n"
            "print('La cita [d4] existe y es relevante… pero el número NO está en d4.')\n"
            "print('Esto es una alucinación CON cita: la más difícil de detectar a simple vista.')"
        ),
        "correccion_md": "La verificación mínima: cada afirmación numérica debe aparecer literalmente en el documento citado.",
        "correccion": (
            "def verificar(afirmacion_numero, doc_texto):\n"
            "    return afirmacion_numero in doc_texto\n"
            "\n"
            "d4 = documentos['d4']\n"
            "print('d4 =', d4)\n"
            "print('¿aparece «4 por ciento»? ', verificar('4 por ciento', d4))\n"
            "print('¿aparece «12 por ciento»?', verificar('12 por ciento', d4))"
        ),
        "desafio_guiado_md": "Añade un umbral de score por debajo del cual el sistema se niega a responder.",
        "desafio_guiado": (
            "UMBRAL = 0.35\n"
            "for q in consultas:\n"
            "    mejor_doc, mejor_txt = max(documentos.items(), key=lambda kv: coseno(tf(q), tf(kv[1])))\n"
            "    score = coseno(tf(q), tf(mejor_txt))\n"
            "    if score < UMBRAL:\n"
            "        print(f'{q[:45]:<47} → ABSTENCIÓN (score {score:.3f} < {UMBRAL})')\n"
            "    else:\n"
            "        print(f'{q[:45]:<47} → responder con [{mejor_doc}] (score {score:.3f})')"
        ),
        "desafio_autonomo": (
            "Construye un RAG sobre 50 documentos propios. Mide por separado: recall@k del recuperador, "
            "fidelidad de la respuesta al contexto y tasa de abstención correcta. Reporta los tres."
        ),
        "evidencia": (
            "Guarda el ranking, el caso de alucinación con cita, la verificación literal y el mecanismo "
            "de abstención con su umbral."
        ),
        "cierre": (
            "El modelo ya puede citar. Todavía no está alineado con lo que una persona espera al pedirle "
            "algo: eso exige aprender de preferencias humanas."
        ),
    },
    "P12_instructgpt_rlhf": {
        "intuicion": (
            "Es mucho más fácil decir «prefiero esta respuesta a esta otra» que puntuar del 1 al 10. "
            "RLHF convierte miles de esas comparaciones en un número que el modelo puede optimizar."
        ),
        "concepto": (
            "Tres etapas:\n\n"
            "```text\n"
            "1. SFT : ajuste supervisado con demostraciones humanas\n"
            "2. RM  : modelo de recompensa Bradley-Terry, p(y_w ≻ y_l) = σ(r(y_w) − r(y_l))\n"
            "3. RL  : maximizar r(y) − β·KL(π ‖ π_SFT) con PPO\n"
            "```\n\n"
            "El término KL impide que la política se aleje tanto del modelo base que empiece a producir "
            "texto degenerado con recompensa alta."
        ),
        "codigo_md": "El motor ajusta el modelo de recompensa sobre 5 comparaciones y reordena las respuestas candidatas.",
        "codigo": (
            "r = run_paper_lab('rlhf', seed=7)['result']\n"
            "show(r['pesos_del_modelo_de_recompensa'])\n"
            "print('\\nranking aprendido:')\n"
            "for fila in r['ranking_aprendido']:\n"
            "    print(f\"  r={fila['reward']:+7.3f} · {fila['texto']}\")"
        ),
        "prediccion": (
            "1. ¿Qué característica recibirá más peso: utilidad, honestidad, inocuidad o verbosidad?\n"
            "2. ¿Quedará la respuesta peligrosa (d) arriba o abajo del ranking?\n"
            "3. Si todas las respuestas preferidas fueran también las más largas, ¿qué aprendería el modelo?"
        ),
        "experimento": (
            "r7 = run_paper_lab('rlhf', seed=7)['result']\n"
            "pesos = r7['pesos_del_modelo_de_recompensa']\n"
            "orden = sorted(pesos.items(), key=lambda kv: -abs(kv[1]))\n"
            "print('características por influencia absoluta:')\n"
            "for nombre, peso in orden:\n"
            "    print(f'  {nombre:<12} {peso:+.3f}')"
        ),
        "salida": (
            "«inocuidad» y «utilidad» dominan porque las comparaciones que le dimos castigan lo peligroso "
            "y premian lo útil. **El modelo de recompensa no descubre valores: reproduce los del conjunto "
            "de comparaciones.** Cambia las comparaciones y cambian los valores."
        ),
        "comentario": (
            "Aquí está el punto político y técnico a la vez: quién etiqueta, con qué guía y con qué "
            "incentivos determina qué significa «mejor». El propio paper documenta el perfil de sus "
            "anotadores; leer esa sección es parte del ejercicio."
        ),
        "antipatron_md": "Anti-patrón: reward hacking. Si «verbosidad» correlaciona con preferencia, la política aprende a ser larga, no mejor.",
        "antipatron": (
            "preferencias_sesgadas = [('largo', 'corto')] * 5\n"
            "print('Si TODAS las preferencias premian la respuesta larga:')\n"
            "print('  el modelo de recompensa aprende r ∝ longitud')\n"
            "print('  la política optimiza longitud')\n"
            "print('  la métrica sube y la calidad real no se mueve')"
        ),
        "correccion_md": "Mitigaciones: penalización KL contra el modelo base, comparaciones controladas por longitud y evaluación humana independiente del RM.",
        "correccion": (
            "import math\n"
            "\n"
            "def objetivo(recompensa, kl, beta=0.2):\n"
            "    return recompensa - beta * kl\n"
            "\n"
            "for kl in (0.0, 1.0, 5.0, 20.0):\n"
            "    print(f'KL={kl:>5.1f} → objetivo con r=3.0: {objetivo(3.0, kl):+.2f}')\n"
            "print('→ alejarse del modelo base se vuelve caro: eso frena el reward hacking extremo')"
        ),
        "desafio_guiado_md": "Invierte una comparación (haz que se prefiera la respuesta evasiva) y observa cómo se reordena todo.",
        "desafio_guiado": (
            "print('pesos originales:', run_paper_lab('rlhf', seed=1)['result']['pesos_del_modelo_de_recompensa'])\n"
            "print('pesos con otra semilla:', run_paper_lab('rlhf', seed=99)['result']['pesos_del_modelo_de_recompensa'])\n"
            "print('→ los pesos son estables porque las COMPARACIONES son las mismas;')\n"
            "print('  la semilla no cambia los datos de preferencia, y eso es lo que manda.')"
        ),
        "desafio_autonomo": (
            "Crea 30 pares de preferencia propios sobre un dominio que conozcas. Entrena el modelo de "
            "recompensa, y luego construye adversarialmente una respuesta que maximice la recompensa "
            "siendo claramente peor. Documenta qué característica explotaste."
        ),
        "evidencia": (
            "Guarda los pesos aprendidos, el ranking, tu ejemplo de reward hacking y la explicación del "
            "papel del término KL."
        ),
        "cierre": (
            "El asistente ya sigue instrucciones. La siguiente pregunta es si hace falta todo el aparato "
            "de RL para conseguirlo — la respuesta llega en P15."
        ),
    },
    "P13_react": {
        "intuicion": (
            "Pensar en voz alta sin mirar nada lleva a inventar. Actuar sin pensar lleva a dar palos de "
            "ciego. ReAct alterna: pienso qué necesito, lo busco, leo lo que salió, y ese resultado real "
            "condiciona mi siguiente pensamiento."
        ),
        "concepto": (
            "```text\n"
            "bucle:  Thought_t → Action_t → Observation_t → Thought_{t+1} → …  → Finish\n"
            "```\n\n"
            "La observación viene del **entorno**, no del modelo. Ese es el anclaje que corrige la "
            "trayectoria: sin él, el razonamiento en cadena se aleja de los hechos sin darse cuenta."
        ),
        "codigo_md": "El motor compara una estrategia solo-acción con el bucle completo sobre la misma pregunta compuesta.",
        "codigo": (
            "r = run_paper_lab('react', seed=7)['result']\n"
            "print('pregunta:', r['pregunta'], '\\n')\n"
            "print('ACT-ONLY →', r['act_only']['answer'], '· pasos:', r['pasos']['act_only'])\n"
            "print('REACT    →', r['react']['answer'], '· pasos:', r['pasos']['react'], '\\n')\n"
            "for paso in r['react']['trace']:\n"
            "    print('  💭', paso['thought'])\n"
            "    print('  🔧', paso['act'], '→', paso['obs'])"
        ),
        "prediccion": (
            "1. ¿Por qué falla la estrategia solo-acción en una pregunta de dos saltos?\n"
            "2. ¿Cuántas llamadas a la herramienta necesita ReAct como mínimo?\n"
            "3. Si la primera observación fuera errónea, ¿el bucle lo detectaría?"
        ),
        "experimento": (
            "KB = {'capital de francia': 'Paris', 'poblacion de paris': '2 100 000'}\n"
            "\n"
            "def buscar(clave):\n"
            "    return KB.get(clave.lower(), 'sin resultados')\n"
            "\n"
            "def bucle(pregunta, max_pasos=4):\n"
            "    traza, respuesta = [], None\n"
            "    consulta = 'capital de francia'\n"
            "    for paso in range(max_pasos):\n"
            "        obs = buscar(consulta)\n"
            "        traza.append({'paso': paso, 'accion': f'buscar({consulta})', 'obs': obs})\n"
            "        if obs == 'sin resultados':\n"
            "            traza.append({'paso': paso, 'decision': 'PARAR: la herramienta no sabe'})\n"
            "            break\n"
            "        if consulta.startswith('poblacion'):\n"
            "            respuesta = obs\n"
            "            break\n"
            "        consulta = f'poblacion de {obs.lower()}'\n"
            "    return {'respuesta': respuesta, 'traza': traza}\n"
            "\n"
            "show(bucle('cuantos habitantes tiene la capital de francia'))"
        ),
        "salida": (
            "La traza muestra cómo la observación `Paris` **construye** la consulta siguiente. Sin ese "
            "encadenamiento la pregunta es irresoluble con una sola búsqueda, por muy bueno que sea el modelo."
        ),
        "comentario": (
            "Una traza legible no garantiza fidelidad: el texto del «pensamiento» es una generación más y "
            "puede no describir el proceso real. Sirve para depurar y auditar decisiones, no como prueba "
            "de cómo razonó el modelo."
        ),
        "antipatron_md": "Anti-patrón: bucle sin criterio de parada. Si la herramienta falla, el agente reintenta para siempre y quema presupuesto.",
        "antipatron": (
            "intentos = 0\n"
            "for _ in range(50):                      # simulación acotada de un bucle infinito\n"
            "    intentos += 1\n"
            "    obs = buscar('dato que no existe')\n"
            "    if obs != 'sin resultados':\n"
            "        break\n"
            "print(f'la herramienta devolvió «sin resultados» {intentos} veces y el agente siguió intentando')"
        ),
        "correccion_md": "Corrección: límite de pasos, detección de repetición y escalamiento explícito.",
        "correccion": (
            "def bucle_seguro(consulta, max_pasos=3):\n"
            "    vistas = set()\n"
            "    for paso in range(max_pasos):\n"
            "        if consulta in vistas:\n"
            "            return {'estado': 'ABORTADO', 'motivo': 'consulta repetida', 'pasos': paso}\n"
            "        vistas.add(consulta)\n"
            "        obs = buscar(consulta)\n"
            "        if obs == 'sin resultados':\n"
            "            return {'estado': 'ESCALADO', 'motivo': 'herramienta sin datos', 'pasos': paso + 1}\n"
            "        return {'estado': 'OK', 'obs': obs, 'pasos': paso + 1}\n"
            "    return {'estado': 'ABORTADO', 'motivo': 'límite de pasos', 'pasos': max_pasos}\n"
            "\n"
            "show(bucle_seguro('dato que no existe'))\n"
            "show(bucle_seguro('capital de francia'))"
        ),
        "desafio_guiado_md": "Haz que la base de conocimiento devuelva un dato erróneo y comprueba que el bucle lo propaga sin dudar.",
        "desafio_guiado": (
            "KB['capital de francia'] = 'Berlin'          # dato corrupto\n"
            "resultado = bucle('cuantos habitantes tiene la capital de francia')\n"
            "show(resultado)\n"
            "print('→ el agente no cuestiona la observación: la fiabilidad de la herramienta es su techo')\n"
            "KB['capital de francia'] = 'Paris'           # restaurar"
        ),
        "desafio_autonomo": (
            "Implementa ReAct sobre una API pública y gratuita. Añade un verificador que compruebe cada "
            "observación contra una segunda fuente. Mide cuántas respuestas cambian al añadir el "
            "verificador y cuánto cuesta en llamadas."
        ),
        "evidencia": (
            "Guarda la traza completa, el caso de bucle sin parada, la versión con criterio de parada y "
            "el experimento del dato corrupto."
        ),
        "cierre": (
            "El modelo ya controla un bucle. Falta que aprenda **cuándo** conviene llamar a una "
            "herramienta, en lugar de que se lo digamos nosotros."
        ),
    },
    "P14_toolformer": {
        "intuicion": (
            "En vez de que un humano anote «aquí deberías usar la calculadora», el modelo prueba a "
            "llamarla en muchos sitios, se queda con las llamadas que le ayudaron a predecir mejor lo que "
            "venía después, y aprende de ese corpus filtrado por sí mismo."
        ),
        "concepto": (
            "```text\n"
            "1. muestrear posiciones y llamadas candidatas\n"
            "2. ejecutar la API y obtener el resultado r\n"
            "3. conservar la llamada si  L(con resultado) < L(sin llamada) − τ\n"
            "4. reentrenar el modelo sobre el texto con las llamadas conservadas\n"
            "```\n\n"
            "El criterio de utilidad es la **pérdida del propio modelo**: nadie etiqueta nada."
        ),
        "codigo_md": "El motor aplica el filtro sobre tres candidatas: una útil, una marginal y una absurda.",
        "codigo": (
            "r = run_paper_lab('toolformer', seed=7)['result']\n"
            "print('umbral τ =', r['umbral'], '\\n')\n"
            "for fila in r['candidatos_evaluados']:\n"
            "    marca = '✅' if fila['se_conserva'] else '❌'\n"
            "    print(f\"{marca} Δpérdida={fila['reduccion_de_perdida']:+.2f} · {fila['llamada']}\")"
        ),
        "prediccion": (
            "1. ¿Se conservará la llamada al buscador que solo reduce la pérdida en 0,04?\n"
            "2. ¿Qué signo tendrá Δpérdida en la llamada absurda?\n"
            "3. Si bajas τ a 0,01, ¿qué problema aparece?"
        ),
        "experimento": (
            "candidatos = r['candidatos_evaluados']\n"
            "for tau in (0.01, 0.30, 1.00, 3.00):\n"
            "    conservados = [c['llamada'] for c in candidatos if c['reduccion_de_perdida'] > tau]\n"
            "    print(f'τ={tau:<5} → {len(conservados)} llamadas conservadas: {conservados}')"
        ),
        "salida": (
            "τ es el mando entre dos fallos opuestos: **τ bajo** conserva llamadas inútiles (el modelo "
            "aprende a llamar herramientas todo el rato, con su coste y su latencia); **τ alto** descarta "
            "llamadas útiles (el modelo vuelve a inventar los cálculos). No existe un τ universal."
        ),
        "comentario": (
            "El método enseña *cuándo* llamar, no garantiza que la herramienta acierte. Un Toolformer "
            "conectado a una API que devuelve basura aprenderá a llamarla con confianza. La calidad de la "
            "herramienta es un supuesto del método, no un resultado."
        ),
        "antipatron_md": "Anti-patrón: medir el éxito por «número de llamadas a herramientas» como si más fuera mejor.",
        "antipatron": (
            "metrica_mala = {'llamadas_por_respuesta': 7, 'conclusion': 'el agente usa mucho las herramientas'}\n"
            "show(metrica_mala)\n"
            "print('→ 7 llamadas pueden significar competencia… o un bucle caro que no converge.')"
        ),
        "correccion_md": "Métricas que sí informan: utilidad marginal por llamada, coste y tasa de llamadas descartadas.",
        "correccion": (
            "util = [c for c in candidatos if c['se_conserva']]\n"
            "metricas = {\n"
            "    'candidatas_evaluadas': len(candidatos),\n"
            "    'conservadas': len(util),\n"
            "    'tasa_de_descarte': round(1 - len(util) / len(candidatos), 3),\n"
            "    'reduccion_media_de_perdida': round(sum(c['reduccion_de_perdida'] for c in util) / max(len(util), 1), 3),\n"
            "}\n"
            "show(metricas)"
        ),
        "desafio_guiado_md": "Añade una candidata nueva con Δpérdida negativa grande y comprueba que el filtro la rechaza sin intervención humana.",
        "desafio_guiado": (
            "nueva = {'texto': 'Erase una vez un bosque.', 'llamada': '[Calc(erase) -> error]',\n"
            "         'loss_sin': 0.80, 'loss_con': 2.40}\n"
            "delta = nueva['loss_sin'] - nueva['loss_con']\n"
            "print(f\"Δpérdida = {delta:+.2f} → se conserva: {delta > r['umbral']}\")"
        ),
        "desafio_autonomo": (
            "Con un modelo abierto pequeño y un calculador local, implementa el filtrado real por "
            "perplejidad sobre 200 frases con operaciones aritméticas. Reporta cuántas llamadas "
            "sobreviven y cómo cambia el resultado al variar τ."
        ),
        "evidencia": (
            "Guarda la tabla de candidatas con su Δpérdida, el barrido de τ y las métricas que sustituyen "
            "al conteo bruto de llamadas."
        ),
        "cierre": (
            "El uso de herramientas ya se autosupervisa. Volvemos a la alineación: ¿se puede conseguir el "
            "efecto de RLHF sin su maquinaria?"
        ),
    },
    "P15_dpo": {
        "intuicion": (
            "RLHF entrena un juez (modelo de recompensa) y luego entrena al alumno a gustar al juez. "
            "DPO demuestra que el alumno **ya contiene** al juez: se puede ajustar directamente con las "
            "comparaciones, sin construir el juez aparte."
        ),
        "concepto": (
            "El óptimo del objetivo RLHF con restricción KL es `π*(y|x) ∝ π_ref(y|x)·exp(r(x,y)/β)`. "
            "Despejando `r` y sustituyendo en Bradley-Terry:\n\n"
            "```text\n"
            "L_DPO = −log σ( β·[ log π(y_w|x)/π_ref(y_w|x) − log π(y_l|x)/π_ref(y_l|x) ] )\n"
            "```\n\n"
            "La recompensa implícita es `r̂ = β·log(π/π_ref)`. No hay RL, no hay muestreo on-policy."
        ),
        "codigo_md": "El motor optimiza la pérdida DPO sobre una política de 3 opciones y muestra la recompensa implícita resultante.",
        "codigo": (
            "r = run_paper_lab('dpo', seed=7)['result']\n"
            "show(r['politica_referencia'])\n"
            "show(r['politica_dpo'])\n"
            "show(r['recompensa_implicita_beta_log_ratio'])"
        ),
        "prediccion": (
            "1. ¿Hacia qué opción se desplazará la política tras optimizar?\n"
            "2. ¿Qué signo tendrá la recompensa implícita de la opción preferida?\n"
            "3. Si β fuera muy grande, ¿la política se movería más o menos respecto a la referencia?"
        ),
        "experimento": (
            "import math\n"
            "\n"
            "def recompensa_implicita(p, p_ref, beta):\n"
            "    return beta * (math.log(p) - math.log(p_ref))\n"
            "\n"
            "pol = r['politica_dpo']\n"
            "ref = r['politica_referencia']\n"
            "for beta in (0.1, 0.5, 1.0):\n"
            "    valores = {k: round(recompensa_implicita(pol[k], ref[k], beta), 3) for k in pol}\n"
            "    print(f'β={beta:<4} → r̂ = {valores}')"
        ),
        "salida": (
            "La opción preferida tiene `r̂ > 0` y las rechazadas `r̂ < 0`: la política **es** el modelo de "
            "recompensa, leído como log-ratio contra la referencia. β escala esa recompensa y, en el "
            "objetivo, controla cuánto se permite alejarse de `π_ref`."
        ),
        "comentario": (
            "DPO es más simple, no automáticamente mejor. Sigue dependiendo por completo de la calidad y "
            "cobertura de los pares de preferencia, y no permite explorar respuestas nuevas fuera de la "
            "distribución de los datos, cosa que el muestreo on-policy de RLHF sí hace."
        ),
        "antipatron_md": "Anti-patrón: quitar `π_ref` de la fórmula porque «se simplifica». Sin referencia no hay restricción KL y la política colapsa.",
        "antipatron": (
            "print('Si eliminas π_ref, la pérdida premia subir p(preferida) sin límite:')\n"
            "for p in (0.5, 0.9, 0.99, 0.9999):\n"
            "    print(f'  p={p:<7} → log p = {math.log(p):+.5f}  (nada frena el colapso a p→1)')\n"
            "print('Resultado: una política degenerada que siempre dice lo mismo.')"
        ),
        "correccion_md": "Con `π_ref` el término es un *log-ratio*: alejarse cuesta, y β pone el precio.",
        "correccion": (
            "p_ref = 0.27\n"
            "for p in (0.5, 0.9, 0.99, 0.9999):\n"
            "    ratio = math.log(p) - math.log(p_ref)\n"
            "    print(f'  p={p:<7} → β·log(π/π_ref) con β=0.5 = {0.5 * ratio:+.4f}')"
        ),
        "desafio_guiado_md": "Comprueba la simetría: la suma de recompensas implícitas ponderadas se mantiene acotada.",
        "desafio_guiado": (
            "for semilla in (1, 7, 42):\n"
            "    res = run_paper_lab('dpo', seed=semilla)['result']\n"
            "    print(f\"semilla {semilla:>2} · π_dpo = {res['politica_dpo']} \"\n"
            "          f\"· pérdida final {res['perdida'][-1]['loss']}\")"
        ),
        "desafio_autonomo": (
            "Implementa DPO sobre un modelo de lenguaje pequeño y abierto con 200 pares de preferencia. "
            "Compara contra best-of-n con un modelo de recompensa entrenado sobre los mismos pares. "
            "Reporta preferencia humana ciega sobre 50 salidas y el coste de cómputo de cada vía."
        ),
        "evidencia": (
            "Guarda π_ref, π_DPO, la recompensa implícita para tres valores de β y tu explicación de por "
            "qué eliminar π_ref rompe el método."
        ),
        "cierre": (
            "Con alineación directa y herramientas autosupervisadas, las piezas del agente moderno están "
            "sobre la mesa. Queda ensamblarlas en un sistema."
        ),
    },
    "P16_agentic_systems": {
        "intuicion": (
            "Un agente que funciona en una demo y falla en producción casi nunca falla por el modelo: "
            "falla porque no tenía presupuesto, ni criterio de parada, ni memoria, ni un plan para el "
            "momento en que una herramienta devuelve un error."
        ),
        "concepto": (
            "Un sistema agentic contemporáneo se describe por sus componentes, no por su prompt:\n\n"
            "```text\n"
            "plan · herramientas tipadas · memoria · presupuesto · criterio de parada · escalamiento\n"
            "```\n\n"
            "Los trabajos posteriores a ReAct añaden autocrítica (Reflexion), memoria episódica con "
            "recuperación (Generative Agents), currículo autónomo (Voyager), orquestación multiagente "
            "(AutoGen) y estandarización del acceso a herramientas (MCP)."
        ),
        "codigo_md": "El motor ejecuta un agente con presupuesto explícito que se topa con un fallo de herramienta.",
        "codigo": (
            "r = run_paper_lab('agentic', seed=7)['result']\n"
            "show(r['presupuesto'])\n"
            "show(r['consumido'])\n"
            "print('\\ntraza:')\n"
            "for paso in r['traza']:\n"
            "    print(' ', paso)\n"
            "print('\\nescalado a humano:', r['escalado_a_humano'])"
        ),
        "prediccion": (
            "1. ¿Agotará el agente su presupuesto de pasos o se detendrá antes?\n"
            "2. Cuando la verificación falle, ¿debe reintentar, seguir sin verificar, o parar?\n"
            "3. ¿Qué componente del sistema es el que hace auditable esta ejecución?"
        ),
        "experimento": (
            "componentes = r['componentes']\n"
            "riesgo_si_falta = {\n"
            "    'plan': 'el agente deambula sin objetivo verificable',\n"
            "    'herramientas': 'el modelo alucina la acción en lugar de ejecutarla',\n"
            "    'memoria': 'repite trabajo y pierde el contexto entre pasos',\n"
            "    'presupuesto': 'coste ilimitado ante un bucle',\n"
            "    'criterio de parada': 'nunca termina; consume hasta el timeout',\n"
            "    'escalamiento': 'un fallo se convierte en una respuesta inventada',\n"
            "}\n"
            "for c in componentes:\n"
            "    print(f'{c:<20} → si falta: {riesgo_si_falta[c]}')"
        ),
        "salida": (
            "El agente se detiene en el paso de verificación y escala en lugar de responder igualmente. "
            "**Parar es un resultado correcto.** Un sistema que siempre devuelve una respuesta está "
            "ocultando sus fallos, no evitándolos."
        ),
        "comentario": (
            "Este nodo es el más volátil del eje y por eso vive con fecha de consulta. Lo estable son las "
            "preguntas (¿quién define el objetivo? ¿quién paga el presupuesto? ¿quién responde por el "
            "error?); lo inestable son los nombres de framework de cada temporada."
        ),
        "antipatron_md": "Anti-patrón: «agente autónomo» sin límite de gasto ni permisos, evaluado por si «funcionó una vez».",
        "antipatron": (
            "demo = {'ejecuciones': 1, 'exito': True, 'conclusion': 'listo para producción'}\n"
            "show(demo)\n"
            "print('→ n=1 no es evidencia. No hay varianza, ni casos límite, ni fallos de herramienta,')\n"
            "print('  ni coste medido, ni comportamiento ante entradas adversarias.')"
        ),
        "correccion_md": "Un reporte mínimamente serio de un agente incluye distribución, no una anécdota:",
        "correccion": (
            "reporte = {\n"
            "    'ejecuciones': 100,\n"
            "    'tasa_de_exito': 0.71,\n"
            "    'tasa_de_escalamiento_correcto': 0.18,\n"
            "    'tasa_de_respuesta_inventada': 0.03,\n"
            "    'coste_medio_por_tarea': '0.9 llamadas de herramienta · 4 pasos',\n"
            "    'p95_pasos': 9,\n"
            "    'casos_adversarios_probados': ['herramienta caída', 'salida malformada', 'instrucción inyectada'],\n"
            "}\n"
            "show(reporte)"
        ),
        "desafio_guiado_md": "Reduce el presupuesto a 2 pasos y comprueba que el agente aborta de forma limpia en lugar de fallar a medias.",
        "desafio_guiado": (
            "presupuesto = {'pasos': 2}\n"
            "plan = ['leer_requisito', 'consultar_datos', 'verificar', 'responder']\n"
            "ejecutados = []\n"
            "for paso in plan:\n"
            "    if len(ejecutados) >= presupuesto['pasos']:\n"
            "        print(f'ABORTADO antes de «{paso}» · pasos ejecutados: {ejecutados}')\n"
            "        break\n"
            "    ejecutados.append(paso)\n"
            "else:\n"
            "    print('completado:', ejecutados)"
        ),
        "desafio_autonomo": (
            "Toma un agente que hayas construido en la parte 09 del programa y añádele los seis "
            "componentes. Ejecútalo 50 veces sobre 10 tareas y reporta tasa de éxito, de escalamiento y "
            "de respuesta inventada, con al menos tres casos adversarios. Fecha el informe."
        ),
        "evidencia": (
            "Guarda la traza con presupuesto, la tabla componente→riesgo-si-falta y el reporte de "
            "evaluación con distribución en lugar de anécdota."
        ),
        "cierre": (
            "Aquí termina la ruta mínima y empieza la frontera. Lo que sigue no está consolidado: se "
            "registra en `frontier/current-topics.yaml` con fecha y fuente, y se relee, no se cita como firme."
        ),
    },
}


SPECS.update({
    "P17_diffusion": {
        "intuicion": (
            "Destruir es fácil y reversible si sabes exactamente cómo destruiste. Añadir ruido gaussiano "
            "tiene fórmula cerrada; el modelo solo tiene que aprender a decir **cuánto ruido hay** en cada "
            "paso. Generar es deshacer ese camino."
        ),
        "concepto": (
            "```text\n"
            "Proceso directo (conocido, sin aprender):\n"
            "    x_t = √ᾱ_t · x₀ + √(1−ᾱ_t) · ε,     ε ~ N(0, I),   ᾱ_t = Π_s (1−β_s)\n\n"
            "Reconstrucción a partir de ε:\n"
            "    x₀ = (x_t − √(1−ᾱ_t)·ε) / √ᾱ_t\n\n"
            "Pérdida (forma simplificada del paper):\n"
            "    L = E ‖ ε − ε_θ(x_t, t) ‖²        ← se predice el RUIDO, no la imagen\n"
            "```"
        ),
        "codigo_md": "El motor calcula la trayectoria de ruido y reconstruye desde el paso más ruidoso con el ε correcto.",
        "codigo": (
            "r = run_paper_lab('diffusion', seed=7)['result']\n"
            "for fila in r['trayectoria_de_ruido']:\n"
            "    print(f\"t={fila['t']:>2} · ᾱ={fila['alpha_barra']:.4f} · SNR={fila['snr']:>10.4f} · x_t={fila['x_t']}\")\n"
            "show(r['reconstruccion'])"
        ),
        "prediccion": (
            "1. ¿Qué le pasa a la SNR al avanzar t: baja lineal o exponencialmente?\n"
            "2. Con el ε exacto, ¿el error de reconstrucción será 0, ~1e-15 o ~0,01?\n"
            "3. ¿En qué paso —el poco ruidoso o el muy ruidoso— duele más equivocarse en ε?"
        ),
        "experimento": (
            "import math\n"
            "T = 20\n"
            "betas = [1e-4 + (0.02 - 1e-4) * t / (T - 1) for t in range(T)]\n"
            "ab, acum = [], 1.0\n"
            "for b in betas:\n"
            "    acum *= (1 - b)\n"
            "    ab.append(acum)\n"
            "print('amplificacion del error de epsilon = sqrt(1-ᾱ)/sqrt(ᾱ):')\n"
            "for t in (0, 5, 10, 15, 19):\n"
            "    print(f'  t={t:>2} → x{math.sqrt(1 - ab[t]) / math.sqrt(ab[t]):.2f}')"
        ),
        "salida": (
            "El factor de amplificación crece con `t`. Un mismo error en ε apenas se nota al principio y "
            "arruina la reconstrucción al final. **Por eso el muestreo va paso a paso** en vez de saltar del "
            "ruido puro a la imagen de una vez."
        ),
        "comentario": (
            "Fíjate en el cambio de marco: el problema generativo —difícil— se convirtió en un problema de "
            "**regresión supervisada** —fácil—, porque el par (entrada ruidosa, ruido) se puede fabricar "
            "gratis a partir de cualquier imagen. Ese truco es la contribución."
        ),
        "antipatron_md": "Anti-patrón: creer que el modelo predice la imagen limpia. Si predices x₀ directamente en un paso muy ruidoso, el objetivo es casi ruido puro.",
        "antipatron": (
            "print('En t=19, ᾱ≈0.006: x_t es casi todo ruido.')\n"
            "print('Predecir x0 desde ahi es adivinar; predecir ε es una tarea bien condicionada')\n"
            "print('porque ε es exactamente lo que domina la señal en ese punto.')"
        ),
        "correccion_md": "La parametrización correcta y su equivalencia:",
        "correccion": (
            "r = run_paper_lab('diffusion', seed=7)['result']['reconstruccion']\n"
            "print('original                :', r['original'])\n"
            "print('reconstruido desde ε    :', r['con_epsilon_correcto'])\n"
            "print('error con ε correcto    :', r['error_con_epsilon_correcto'])\n"
            "print('error con ε desviado 0.5:', r['error_con_epsilon_desviado_0_5'])"
        ),
        "desafio_guiado_md": "Cambia el planificador de β a uno coseno y compara cómo cae la SNR.",
        "desafio_guiado": (
            "import math\n"
            "T = 20\n"
            "lineal = [1e-4 + (0.02 - 1e-4) * t / (T - 1) for t in range(T)]\n"
            "coseno = [min(0.999, 1 - math.cos((t + 1) / T * math.pi / 2) ** 2 / max(math.cos(t / T * math.pi / 2) ** 2, 1e-8)) for t in range(T)]\n"
            "for nombre, betas in (('lineal', lineal), ('coseno', coseno)):\n"
            "    acum = 1.0\n"
            "    for b in betas:\n"
            "        acum *= (1 - b)\n"
            "    print(f'{nombre:<7} → ᾱ_final = {acum:.6f}')"
        ),
        "desafio_autonomo": (
            "Implementa el muestreo inverso completo (DDPM ancestral) sobre datos 2D sintéticos con dos "
            "modos, entrenando una red pequeña para predecir ε. Mide si las muestras cubren ambos modos o "
            "colapsan en uno, y compáralo con lo que haría una GAN de tamaño similar."
        ),
        "evidencia": (
            "Guarda la trayectoria de SNR, la tabla de amplificación del error por paso y tu explicación de "
            "por qué se predice el ruido y no la imagen."
        ),
        "cierre": (
            "La generación de imágenes ya tiene un objetivo estable y entrenable. Falta poder **decirle qué "
            "generar** con palabras: eso exige un espacio compartido entre imagen y texto."
        ),
    },
    "P18_clip": {
        "intuicion": (
            "En vez de enseñar «esto es un gato» con una etiqueta numérica, se enseña con la frase que ya "
            "acompañaba a la foto en internet. El modelo aprende a acercar cada imagen a su texto y a "
            "alejarla de los textos de las demás."
        ),
        "concepto": (
            "```text\n"
            "InfoNCE simétrico sobre un lote de N pares (imagen_i, texto_i):\n\n"
            "    logits_ij = cos(I_i, T_j) / τ\n"
            "    L = ½·CE(logits, diagonal)_filas + ½·CE(logits, diagonal)_columnas\n"
            "```\n\n"
            "La diagonal son los pares correctos; **todo lo demás del lote son negativos**. Por eso el "
            "tamaño del lote es un hiperparámetro de primer orden: más lote, negativos más difíciles."
        ),
        "codigo_md": "El motor entrena el contraste sobre cuatro pares y mide la matriz de similitud antes y después.",
        "codigo": (
            "r = run_paper_lab('clip', seed=7)['result']\n"
            "print('conceptos:', r['conceptos'])\n"
            "print('\\nmatriz de similitud ANTES (filas=imagen, columnas=texto):')\n"
            "for c, fila in zip(r['conceptos'], r['matriz_antes']):\n"
            "    print(f'  {c:<7}', fila)\n"
            "print('\\nDESPUES:')\n"
            "for c, fila in zip(r['conceptos'], r['matriz_despues']):\n"
            "    print(f'  {c:<7}', fila)\n"
            "show(r['diagonal_media'])\n"
            "print('zero-shot:', r['zero_shot'])"
        ),
        "prediccion": (
            "1. ¿Qué debe pasarle a la diagonal de la matriz? ¿Y a lo de fuera de la diagonal?\n"
            "2. Con 4 conceptos, ¿cuántos negativos tiene cada positivo?\n"
            "3. ¿Por qué esto permite clasificar sin haber entrenado un clasificador?"
        ),
        "experimento": (
            "for semilla in (1, 7, 42):\n"
            "    r = run_paper_lab('clip', seed=semilla)['result']\n"
            "    d = r['diagonal_media']\n"
            "    print(f\"semilla {semilla:>2} · diagonal {d['antes']:+.3f} → {d['despues']:+.3f} \"\n"
            "          f\"· fuera {r['fuera_de_diagonal_media_despues']:+.3f} · zero-shot {r['zero_shot']}\")"
        ),
        "salida": (
            "La diagonal sube y lo de fuera baja: los dos espacios quedan alineados. El zero-shot funciona "
            "porque clasificar se reduce a **preguntar qué frase se parece más a esta imagen** — y las "
            "frases se pueden escribir sobre la marcha, sin reentrenar nada."
        ),
        "comentario": (
            "Ojo con el nombre «zero-shot»: no significa que el modelo no haya visto gatos. Significa que no "
            "vio **este conjunto de etiquetas**. Con 400 millones de pares de internet, casi ninguna "
            "categoría común es realmente nueva, y el propio paper discute ese matiz."
        ),
        "antipatron_md": "Anti-patrón: evaluar zero-shot con las mismas plantillas de texto que se ajustaron mirando el conjunto de test.",
        "antipatron": (
            "print('«a photo of a {clase}» vs «{clase}» vs «una foto de un {clase}, primer plano»')\n"
            "print('La exactitud cambia varios puntos solo con la plantilla.')\n"
            "print('Elegir la plantilla mirando el test convierte zero-shot en ajuste encubierto.')"
        ),
        "correccion_md": "El protocolo honesto separa el conjunto donde se eligen las plantillas del conjunto donde se reporta:",
        "correccion": (
            "protocolo = {\n"
            "    'plantillas_elegidas_en': 'conjunto de validación separado',\n"
            "    'resultado_reportado_en': 'test, una sola vez',\n"
            "    'se_reporta': ['plantilla exacta', 'número de plantillas probadas', 'varianza entre ellas'],\n"
            "}\n"
            "show(protocolo)"
        ),
        "desafio_guiado_md": "Comprueba que la matriz es simétrica en su papel: el negativo de una fila es el positivo de otra columna.",
        "desafio_guiado": (
            "r = run_paper_lab('clip', seed=7)['result']\n"
            "m = r['matriz_despues']\n"
            "n = len(m)\n"
            "diag = [m[i][i] for i in range(n)]\n"
            "fuera = [m[i][j] for i in range(n) for j in range(n) if i != j]\n"
            "print('mínimo de la diagonal :', min(diag))\n"
            "print('máximo fuera de ella  :', max(fuera))\n"
            "print('¿separación perfecta? :', min(diag) > max(fuera))"
        ),
        "desafio_autonomo": (
            "Con un modelo CLIP abierto y ejecutable localmente, construye 20 categorías propias y mide la "
            "exactitud zero-shot con tres plantillas distintas. Reporta media y varianza, y localiza una "
            "categoría donde falle sistemáticamente; explica por qué."
        ),
        "evidencia": (
            "Guarda las dos matrices de similitud, el resultado zero-shot y el protocolo de plantillas que "
            "usarías para que el número sea creíble."
        ),
        "cierre": (
            "Imagen y texto ya viven en el mismo espacio. La pregunta siguiente no es de arquitectura sino "
            "de economía: dado un presupuesto de cómputo, ¿en qué conviene gastarlo?"
        ),
    },
    "P19_scaling_laws": {
        "intuicion": (
            "Tienes un presupuesto fijo de cómputo. Puedes gastarlo en un modelo enorme entrenado con pocos "
            "datos, o en uno mediano entrenado con muchos. No son equivalentes, y durante años la industria "
            "eligió sistemáticamente mal."
        ),
        "concepto": (
            "```text\n"
            "Forma paramétrica ajustada empíricamente:\n"
            "    L(N, D) = E + A/N^α + B/D^β\n\n"
            "Restricción de presupuesto (aproximación estándar):\n"
            "    C ≈ 6·N·D          N = parámetros, D = tokens, C = FLOPs de entrenamiento\n\n"
            "El problema es: minimizar L(N, D) sujeto a 6ND = C\n"
            "```\n\n"
            "`E` es el error irreducible (la entropía del lenguaje). Los otros dos términos son lo que se "
            "compra con parámetros y con datos respectivamente."
        ),
        "codigo_md": "El motor evalúa varias asignaciones **con el mismo cómputo** y encuentra el óptimo. Las constantes son didácticas: la forma es lo transferible.",
        "codigo": (
            "r = run_paper_lab('scaling_laws', seed=7)['result']\n"
            "print('forma:', r['forma_parametrica'])\n"
            "show(r['constantes'])\n"
            "print('\\npresupuesto fijo:', r['presupuesto_flops'], 'FLOPs\\n')\n"
            "for c in r['candidatos_a_igual_computo']:\n"
            "    print(f\"N={c['N_parametros']} · D={c['D_tokens']} · {c['tokens_por_parametro']:>8} tok/param · L={c['perdida']}\")"
        ),
        "prediccion": (
            "1. ¿La pérdida será igual en todas las asignaciones del mismo cómputo, o habrá un mínimo claro?\n"
            "2. ¿El óptimo estará en «el modelo más grande posible»?\n"
            "3. Si duplicas el presupuesto, ¿qué duplicarías: N, D, o ambos a medias?"
        ),
        "experimento": (
            "E, A, B, alpha, beta = 1.69, 400.0, 400.0, 0.34, 0.28\n"
            "def L(N, D):\n"
            "    return E + A / N ** alpha + B / D ** beta\n"
            "\n"
            "for factor in (1, 2, 4, 8):\n"
            "    C = factor * 6 * 70e9 * 1.4e12\n"
            "    mejor = min(((N, C / (6 * N)) for N in (10 ** e * m for e in range(10, 13) for m in (1, 2, 5))),\n"
            "                key=lambda nd: L(*nd))\n"
            "    print(f'presupuesto x{factor}: N*={mejor[0]:.1e} D*={mejor[1]:.1e} '\n"
            "          f'tok/param={mejor[1]/mejor[0]:.0f} L={L(*mejor):.4f}')"
        ),
        "salida": (
            "Al crecer el presupuesto, **N y D crecen a la vez**: ninguna de las dos absorbe todo el "
            "incremento. Ese es el resultado que reordenó la industria — antes se subía N y se dejaba D casi "
            "fijo, gastando cómputo en parámetros que nunca llegaban a entrenarse bien."
        ),
        "comentario": (
            "Las constantes de este notebook **son didácticas**, no las del paper: sirven para que la curva "
            "tenga la forma correcta, no para citar un número. Si necesitas los valores ajustados, están en "
            "el artículo. Confundir ambas cosas es exactamente lo que este eje entrena a no hacer."
        ),
        "antipatron_md": "Anti-patrón: extrapolar la ley fuera del rango donde se ajustó, o usarla para predecir *capacidades* en vez de pérdida.",
        "antipatron": (
            "print('L(N,D) predice PERDIDA DE PREENTRENAMIENTO.')\n"
            "print('No predice: si el modelo razonará, si alucinará menos, ni si servirá para tu tarea.')\n"
            "print('Tampoco cubre el coste de INFERENCIA, que hoy suele dominar el coste total.')"
        ),
        "correccion_md": "Lo que la ley sí autoriza a decir, y lo que no:",
        "correccion": (
            "afirmaciones = {\n"
            "    'valido': ['a computo fijo existe un reparto optimo entre N y D',\n"
            "               'los modelos de 2020-2021 estaban infraentrenados en datos'],\n"
            "    'no_valido': ['un modelo con menor perdida es mejor para mi tarea',\n"
            "                  'la ley se extrapola varios ordenes de magnitud',\n"
            "                  'el modelo optimo para entrenar es el optimo para servir'],\n"
            "}\n"
            "show(afirmaciones)"
        ),
        "desafio_guiado_md": "Un modelo servido a millones de usuarios se entrena una vez y se ejecuta siempre. Calcula cuándo conviene un modelo más pequeño que el óptimo de entrenamiento.",
        "desafio_guiado": (
            "coste_entrenamiento = lambda N, D: 6 * N * D\n"
            "coste_inferencia = lambda N, peticiones, tokens: 2 * N * peticiones * tokens\n"
            "N_opt, D_opt = 7e10, 1.4e12\n"
            "for peticiones in (1e6, 1e9, 1e12):\n"
            "    e = coste_entrenamiento(N_opt, D_opt)\n"
            "    i = coste_inferencia(N_opt, peticiones, 500)\n"
            "    print(f'{peticiones:.0e} peticiones → entrenamiento {e:.2e} vs inferencia {i:.2e} '\n"
            "          f\"({'inferencia domina' if i > e else 'entrenamiento domina'})\")"
        ),
        "desafio_autonomo": (
            "Ajusta tu propia ley de escalado entrenando modelos diminutos (10K–10M parámetros) sobre un "
            "corpus público, con varios presupuestos. Estima α y β y comprueba si tu óptimo predicho se "
            "cumple en una configuración que no usaste para ajustar."
        ),
        "evidencia": (
            "Guarda la tabla de asignaciones a igual cómputo, el óptimo encontrado y la lista de lo que la "
            "ley **no** autoriza a afirmar."
        ),
        "cierre": (
            "Ya sabemos cuánto gastar en cada cosa. La pregunta siguiente vuelve a la arquitectura: el coste "
            "cuadrático de la atención sigue ahí, y alguien tenía que atacarlo."
        ),
    },
    "P20_mamba": {
        "intuicion": (
            "Un RNN comprime el pasado en un estado fijo —barato pero olvida—; la atención guarda todo "
            "—recuerda pero cuesta n²—. Mamba se queda con el estado fijo y añade lo que le faltaba: **la "
            "puerta decide según lo que está leyendo**, no según una regla fija."
        ),
        "concepto": (
            "```text\n"
            "SSM invariante en el tiempo (S4 y anteriores):\n"
            "    h_t = A·h_{t−1} + B·x_t          A, B FIJAS  →  se puede convertir en convolución\n\n"
            "SSM selectivo (Mamba):\n"
            "    h_t = A(x_t)·h_{t−1} + B(x_t)·x_t    A, B DEPENDEN DE LA ENTRADA\n"
            "```\n\n"
            "Ese cambio rompe la convolución eficiente —por eso hace falta un escaneo paralelo consciente "
            "del hardware— pero es lo que permite **razonar sobre el contenido**: ignorar relleno y "
            "retener lo relevante."
        ),
        "codigo_md": "El motor compara ambos en una tarea de copia selectiva: recordar tokens marcados entre relleno.",
        "codigo": (
            "r = run_paper_lab('ssm', seed=7)['result']\n"
            "print('tokens:', r['tokens'], '· marcados:', r['marcados'], '\\n')\n"
            "show(r['invariante_en_el_tiempo'])\n"
            "show(r['selectivo'])\n"
            "print('mejora de separacion:', r['mejora_de_separacion'])"
        ),
        "prediccion": (
            "1. ¿Podrá el SSM invariante distinguir los tokens marcados del relleno?\n"
            "2. ¿Qué le pasa a la memoria de la atención cuando n pasa de 1 000 a 100 000?\n"
            "3. ¿Y a la del SSM?"
        ),
        "experimento": (
            "for fila in r['complejidad']:\n"
            "    print(f\"n={fila['n']:>7} · attn {fila['attention_ops']:>15,} ops / KV {fila['attention_memoria_kv']:>10,} \"\n"
            "          f\"· ssm {fila['ssm_ops']:>12,} ops / estado {fila['ssm_memoria_estado']:>6,}\")"
        ),
        "salida": (
            "La memoria del SSM es **constante**: `d·N` no depende de la longitud. La de la atención crece "
            "linealmente con la secuencia (la caché KV) y su cómputo, cuadráticamente. Ese es el argumento "
            "económico; el argumento de calidad es la separación que acabas de medir."
        ),
        "comentario": (
            "El compromiso es real y conviene enunciarlo sin entusiasmo: un estado de tamaño fijo **es** una "
            "compresión con pérdida. La atención puede volver a mirar cualquier token exacto; el SSM solo "
            "tiene lo que decidió guardar. Por eso proliferaron los híbridos que alternan ambos bloques."
        ),
        "antipatron_md": "Anti-patrón: «Mamba sustituye al Transformer». Es una afirmación de arquitectura sin tarea, dato ni escala.",
        "antipatron": (
            "print('«Mamba sustituye al Transformer» ← ¿en qué tarea, a qué escala, con qué presupuesto?')\n"
            "print('El paper reporta resultados hasta cierto tamaño y en ciertas modalidades.')\n"
            "print('Extrapolar de ahi a «sustituye» es narrativa, no evidencia.')"
        ),
        "correccion_md": "Enunciado defendible, con sus condiciones:",
        "correccion": (
            "defendible = {\n"
            "    'coste': 'tiempo lineal en la longitud y estado de memoria constante',\n"
            "    'calidad': 'competitivo con Transformers de tamaño comparable en las tareas del paper',\n"
            "    'mecanismo': 'la seleccion dependiente de la entrada es lo que da razonamiento sobre contenido',\n"
            "    'coste_oculto': 'un estado fijo es compresion con perdida: no hay recuperacion exacta',\n"
            "    'no_demostrado': 'paridad general con la atencion a cualquier escala y tarea',\n"
            "}\n"
            "show(defendible)"
        ),
        "desafio_guiado_md": "Sube la proporción de tokens marcados y observa cuándo la selección deja de ayudar.",
        "desafio_guiado": (
            "for cada in (17, 7, 3, 2):\n"
            "    marcados = len([i for i in range(60) if i % cada == 3])\n"
            "    print(f'1 de cada {cada:>2} tokens marcado → {marcados:>2}/60 relevantes '\n"
            "          f\"({'seleccionar aporta poco' if marcados > 20 else 'seleccionar aporta mucho'})\")"
        ),
        "desafio_autonomo": (
            "Implementa la tarea de copia selectiva del paper con longitudes crecientes y entrena dos "
            "modelos de tamaño comparable: uno con puertas fijas y otro con puertas dependientes de la "
            "entrada. Reporta exactitud frente a longitud y memoria máxima usada."
        ),
        "evidencia": (
            "Guarda la separación de ambos modelos, la tabla de complejidad y tu enunciado defendible sobre "
            "qué gana y qué pierde frente a la atención."
        ),
        "cierre": (
            "Se puede abaratar el **eje de la secuencia**. Queda el otro eje: el de los parámetros, donde "
            "cada token paga por todos aunque no los necesite."
        ),
    },
    "P21_moe": {
        "intuicion": (
            "En un modelo denso, cada palabra que procesas paga la factura completa del modelo. En una "
            "mezcla de expertos hay muchos especialistas pero solo se despiertan dos por token: capacidad de "
            "biblioteca, coste de consulta."
        ),
        "concepto": (
            "```text\n"
            "Capa densa:         y = FFN(x)                      coste ∝ todos los parámetros\n"
            "Capa MoE dispersa:  y = Σ_{i ∈ top-k} g_i(x)·E_i(x)  coste ∝ k expertos\n\n"
            "    g(x) = softmax(top-k(x·W_router))\n"
            "```\n\n"
            "En el modelo del paper: 8 expertos, k=2, ≈47 000 M de parámetros totales y ≈13 000 M activos "
            "por token."
        ),
        "codigo_md": "El motor enruta 400 tokens con un router top-2 sobre 8 expertos y mide el reparto de carga.",
        "codigo": (
            "r = run_paper_lab('moe', seed=7)['result']\n"
            "show(r['parametros'])\n"
            "print('\\ncarga sin balanceo:', r['sin_balanceo']['carga'], '· CV =', r['sin_balanceo']['cv'])\n"
            "print('carga con balanceo:', r['con_balanceo']['carga'], '· CV =', r['con_balanceo']['cv'])"
        ),
        "prediccion": (
            "1. ¿Repartirá el router los tokens de forma pareja entre los 8 expertos?\n"
            "2. Si el 25 % de los parámetros está activo, ¿necesitas el 25 % de la memoria?\n"
            "3. ¿Qué pasa si un experto no recibe ningún token durante el entrenamiento?"
        ),
        "experimento": (
            "for expertos, k in ((8, 1), (8, 2), (8, 4), (64, 2)):\n"
            "    fraccion = k / expertos\n"
            "    print(f'{expertos:>2} expertos, top-{k} → {fraccion:>6.1%} de parámetros activos por token')"
        ),
        "salida": (
            "El CV (coeficiente de variación de la carga) baja al añadir el término de balanceo. Sin él, unos "
            "pocos expertos acaparan los tokens y el resto no recibe gradiente: **se entrena un modelo denso "
            "caro disfrazado de disperso**. Ese colapso del router es el fallo característico."
        ),
        "comentario": (
            "La trampa contable: «13 000 M activos» **no** significa que quepa en la memoria de 13 000 M. "
            "Hay que cargar los 47 000 M porque cualquier token puede activar cualquier experto. MoE ahorra "
            "**cómputo**, no **memoria** — y confundirlo lleva a dimensionar mal el hardware."
        ),
        "antipatron_md": "Anti-patrón: dimensionar la GPU por los parámetros activos.",
        "antipatron": (
            "activos_gb = 13e9 * 2 / 1e9\n"
            "totales_gb = 47e9 * 2 / 1e9\n"
            "print(f'Presupuesto por parametros ACTIVOS (fp16): {activos_gb:.0f} GB ← INCORRECTO')\n"
            "print(f'Memoria realmente necesaria (todos)      : {totales_gb:.0f} GB')\n"
            "print('Comprar una tarjeta por el primer numero es no poder cargar el modelo.')"
        ),
        "correccion_md": "Las dos cuentas separadas, que es como hay que presupuestar:",
        "correccion": (
            "presupuesto = {\n"
            "    'memoria_pesos_fp16_GB': round(47e9 * 2 / 1e9),\n"
            "    'computo_por_token_relativo': round(13 / 47, 3),\n"
            "    'regla': 'MoE ahorra COMPUTO por token, no MEMORIA de pesos',\n"
            "    'consecuencia': 'mejor throughput por FLOP, misma o mayor factura de VRAM',\n"
            "}\n"
            "show(presupuesto)"
        ),
        "desafio_guiado_md": "Comprueba cómo el desbalanceo se agrava al subir el número de expertos.",
        "desafio_guiado": (
            "for semilla in (1, 7, 42):\n"
            "    r = run_paper_lab('moe', seed=semilla)['result']\n"
            "    print(f\"semilla {semilla:>2} · CV sin balanceo {r['sin_balanceo']['cv']:.3f} \"\n"
            "          f\"→ con balanceo {r['con_balanceo']['cv']:.3f}\")"
        ),
        "desafio_autonomo": (
            "Implementa una capa MoE real (expertos = pequeñas MLP) y entrénala en una tarea de "
            "clasificación con clases desbalanceadas. Mide la especialización de cada experto y comprueba si "
            "el término de balanceo la destruye o la ordena."
        ),
        "evidencia": (
            "Guarda la tabla de fracción activa, el CV con y sin balanceo, y el presupuesto de memoria "
            "correcto frente al incorrecto."
        ),
        "cierre": (
            "Ya sabemos abaratar la secuencia y los parámetros. Queda dónde gastar el cómputo que sí "
            "queremos gastar: y la respuesta de 2025 fue moverlo al momento de responder."
        ),
    },
    "P22_deepseek_r1": {
        "intuicion": (
            "Para enseñar a razonar, la vía cara es que un humano escriba miles de razonamientos ejemplares. "
            "La vía de este paper es no escribir ninguno: solo comprobar si la respuesta final es correcta, y "
            "dejar que el modelo descubra por sí mismo que verificar antes de responder le renta."
        ),
        "concepto": (
            "```text\n"
            "RLHF (P12):  recompensa = preferencia humana aprendida     → subjetiva, hackeable\n"
            "Aquí      :  recompensa = ¿la respuesta final es correcta? → objetiva, verificable\n"
            "```\n\n"
            "La señal no dice **cómo** razonar, solo **si acertaste**. El comportamiento de razonamiento "
            "—reflexión, verificación, cambio de estrategia— aparece porque aumenta la probabilidad de "
            "acertar, no porque nadie lo demostrara."
        ),
        "codigo_md": "El motor entrena una política sobre tres estrategias usando solo la corrección del resultado.",
        "codigo": (
            "r = run_paper_lab('rl_reasoning', seed=7)['result']\n"
            "show(r['estrategias'])\n"
            "print('\\nseñal usada:', r['senal_usada'])\n"
            "for h in r['historia']:\n"
            "    print(f\"it={h['iteracion']:>2} · política={h['politica']} \"\n"
            "          f\"· exactitud={h['exactitud_esperada']} · tokens={h['tokens_esperados']}\")"
        ),
        "prediccion": (
            "1. ¿Hacia qué estrategia se desplazará la política?\n"
            "2. ¿Qué le pasará al coste en tokens mientras sube la exactitud?\n"
            "3. ¿Funcionaría esto en una tarea donde no se puede comprobar la respuesta?"
        ),
        "experimento": (
            "for semilla in (1, 7, 42):\n"
            "    h = run_paper_lab('rl_reasoning', seed=semilla)['result']['historia']\n"
            "    print(f\"semilla {semilla:>2} · exactitud {h[0]['exactitud_esperada']} → {h[-1]['exactitud_esperada']} \"\n"
            "          f\"· tokens {h[0]['tokens_esperados']} → {h[-1]['tokens_esperados']}\")"
        ),
        "salida": (
            "La exactitud sube y **el coste sube con ella**. Esa es la lectura completa: el razonamiento "
            "largo no es gratis, se paga en tokens de inferencia. El cómputo se desplazó del entrenamiento "
            "al momento de responder."
        ),
        "comentario": (
            "El límite está en la palabra **verificable**. En matemáticas y código, comprobar la respuesta es "
            "barato y objetivo. En redacción, diagnóstico o consejo legal no existe ese verificador, y ahí "
            "el método no se traslada sin más. Es la pregunta abierta que este paper deja."
        ),
        "antipatron_md": "Anti-patrón: leer la traza de razonamiento como si fuera el proceso real del modelo. Es el mismo error que en ReAct, ahora con textos mucho más largos y convincentes.",
        "antipatron": (
            "print('Una traza larga y segura de si misma NO es una prueba de correccion.')\n"
            "print('Se optimizo para que la RESPUESTA FINAL sea correcta;')\n"
            "print('el texto intermedio es un medio, no un certificado auditado.')"
        ),
        "correccion_md": "Lo que sí se puede afirmar, y cómo se comprueba:",
        "correccion": (
            "auditoria = {\n"
            "    'verificable': 'la respuesta final, contra la solucion conocida',\n"
            "    'no_verificable_sin_trabajo_extra': 'que cada paso intermedio sea valido',\n"
            "    'como_comprobarlo': ['ejecutar el codigo generado',\n"
            "                          'comprobar el resultado numerico por otra via',\n"
            "                          'muestrear N trazas y ver si concuerdan'],\n"
            "    'coste': 'cada comprobacion extra es mas computo en inferencia',\n"
            "}\n"
            "show(auditoria)"
        ),
        "desafio_guiado_md": "Sube el coste de la estrategia que verifica y comprueba a partir de qué punto deja de compensar.",
        "desafio_guiado": (
            "estrategias = {'directo': (0.35, 20), 'cadena': (0.60, 90), 'verificacion': (0.82, 240)}\n"
            "for presupuesto in (50, 120, 300):\n"
            "    viables = {k: v for k, v in estrategias.items() if v[1] <= presupuesto}\n"
            "    mejor = max(viables.items(), key=lambda kv: kv[1][0]) if viables else None\n"
            "    print(f'presupuesto {presupuesto:>3} tokens → mejor viable: {mejor[0] if mejor else \"ninguna\"} '\n"
            "          f'(exactitud {mejor[1][0] if mejor else 0})')"
        ),
        "desafio_autonomo": (
            "Toma un modelo abierto pequeño y un conjunto de problemas aritméticos con solución conocida. "
            "Muestrea k trazas por problema, quédate con las que llegan al resultado correcto y reentrena "
            "sobre ellas. Mide exactitud y tokens por respuesta antes y después, y busca el punto donde "
            "más cómputo deja de mejorar el resultado."
        ),
        "evidencia": (
            "Guarda la curva exactitud/coste, la explicación de por qué la recompensa verificable evita el "
            "reward hacking clásico, y el límite de dominios donde no existe verificador."
        ),
        "cierre": (
            "Aquí termina la ruta ampliada, en 2025. Lo posterior no está consolidado: vive en "
            "`frontier/current-topics.yaml` con fecha, y asciende solo cuando cumple los criterios."
        ),
    },
})


def _spec(intuicion, concepto, codigo_md, codigo, prediccion, experimento, salida, comentario,
          antipatron_md, antipatron, correccion_md, correccion, dg_md, dg, da, evidencia, cierre):
    """Constructor de especificación de notebook: los 13 campos del contrato."""
    return {
        "intuicion": intuicion, "concepto": concepto, "codigo_md": codigo_md, "codigo": codigo,
        "prediccion": prediccion, "experimento": experimento, "salida": salida,
        "comentario": comentario, "antipatron_md": antipatron_md, "antipatron": antipatron,
        "correccion_md": correccion_md, "correccion": correccion, "desafio_guiado_md": dg_md,
        "desafio_guiado": dg, "desafio_autonomo": da, "evidencia": evidencia, "cierre": cierre,
    }


SPECS.update({
    "P23_glove": _spec(
        "Word2Vec mira por una ventanita y aprende de lo que pasa cerca. GloVe cuenta primero todo "
        "el corpus y luego busca vectores que expliquen esa tabla de conteos. Mismo destino, camino opuesto.",
        "```text\nJ = Σ_ij  f(X_ij) · ( w_i·w̃_j + b_i + b̃_j − log X_ij )²\n\n"
        "    X_ij = veces que j aparece en el contexto de i\n"
        "    f(x) = (x/x_max)^0.75 si x < x_max, si no 1   ← no dejar que los pares frecuentes dominen\n```\n\n"
        "El argumento del paper no es la fórmula sino **qué se modela**: la RAZÓN "
        "`P(k|hielo)/P(k|vapor)` discrimina, y la co-ocurrencia bruta no.",
        "El motor ajusta la factorización sobre una matriz de co-ocurrencia de juguete con la estructura del ejemplo del paper.",
        "r = run_paper_lab('glove', seed=7)['result']\n"
        "show(r['razones_de_cooocurrencia'])\n"
        "print()\n"
        "for f in r['ajuste_log_cooocurrencia']:\n"
        "    print(f\"{f['par']:<16} log X = {f['log_X']:>6.3f}   predicho = {f['predicho']:>6.3f}\")",
        "1. ¿Qué razón esperas para «sólido»: mucho mayor que 1, mucho menor, o ≈1?\n"
        "2. ¿Y para «agua», que acompaña a hielo y a vapor por igual?\n"
        "3. ¿Por qué haría falta una función de peso f(x)?",
        "r = run_paper_lab('glove', seed=7)['result']\n"
        "for p in r['perdida']:\n"
        "    print(f\"paso {p['paso']:>3} · pérdida {p['perdida']:.5f}\")\n"
        "print('\\nla pérdida baja: los vectores explican cada vez mejor los conteos')",
        "Las tres razones separan limpiamente: ≫1 para lo propio del hielo, ≪1 para lo propio del vapor "
        "y ≈1 para lo compartido. **Eso** es lo que los vectores tienen que capturar, y por eso se ajusta "
        "al logaritmo: convierte razones en diferencias.",
        "Trabajo posterior (Levy y Goldberg, 2015) mostró que word2vec con muestreo negativo factoriza "
        "implícitamente una matriz relacionada. La distinción «predictivo frente a contador» resultó ser "
        "menos profunda de lo que parecía en 2014: es un buen ejemplo de cómo una dicotomía popular se disuelve.",
        "Anti-patrón: ajustar sin función de peso. Los pares muy frecuentes («de», «la») dominan la pérdida y aplastan a los informativos.",
        "x_max, alpha = 100.0, 0.75\n"
        "for x in (1, 5, 50, 100, 5000):\n"
        "    f = (x / x_max) ** alpha if x < x_max else 1.0\n"
        "    print(f'X_ij={x:>5} → peso {f:.4f}' + ('   ← saturado, no crece más' if x >= x_max else ''))",
        "Con la función de peso, un par que aparece 5 000 veces no pesa 50× más que uno de 100:",
        "sin_peso = {x: x for x in (1, 100, 5000)}\n"
        "con_peso = {x: (min(x, 100) / 100) ** 0.75 for x in (1, 100, 5000)}\n"
        "print('sin peso :', sin_peso, ' ← el par de 5000 domina la pérdida')\n"
        "print('con peso :', {k: round(v, 3) for k, v in con_peso.items()})",
        "Comprueba que los pares raros (X_ij pequeño) también aportan poco: la función de peso los atenúa por el otro extremo.",
        "for x in (1, 2, 3, 10):\n"
        "    print(f'X_ij={x:>3} → peso {(x / 100) ** 0.75:.4f}  (ruido estadístico, se atenúa)')",
        "Construye la matriz de co-ocurrencia de un corpus público pequeño, entrena GloVe y word2vec con "
        "la misma dimensión, y compara ambos en un conjunto de analogías propio. Reporta también el tiempo "
        "de entrenamiento: es el argumento práctico que más pesó en su momento.",
        "Guarda la tabla de razones, el ajuste log X frente a predicho, y tu explicación de por qué se "
        "modela el logaritmo y no la co-ocurrencia directa.",
        "Las palabras ya tienen geometría global. Pero siguen teniendo **un solo vector por palabra**, y "
        "eso sigue sin resolver la polisemia.",
    ),
    "P24_elmo": _spec(
        "Un diccionario da una entrada por palabra. Un lector da un significado por aparición. ELMo deja "
        "de ser diccionario: el vector de «banco» se calcula leyendo la frase entera.",
        "```text\nEstático (P05, P23):   v(banco) = siempre el mismo vector\n\n"
        "ELMo:  ELMo_k = γ · Σ_j s_j · h_{k,j}\n\n"
        "    h_{k,j} = estado de la capa j del LM bidireccional en la posición k\n"
        "    s_j     = pesos por capa, APRENDIDOS para cada tarea\n```\n\n"
        "Las capas bajas capturan sintaxis y las altas semántica, así que cada tarea aprende **cuánto "
        "pesa cada capa** en vez de recibir una mezcla fija.",
        "El motor calcula el vector de «banco» en tres frases con sentidos distintos, de forma estática y contextual.",
        "r = run_paper_lab('elmo', seed=7)['result']\n"
        "for c in r['contextos']:\n"
        "    print(' ·', c)\n"
        "print('\\nestático   :', r['similitud_estatica'])\n"
        "print('contextual :', r['similitud_contextual'])",
        "1. ¿Cuánto valdrá el coseno entre las tres apariciones con embedding estático?\n"
        "2. ¿Qué dos sentidos deberían quedar más cerca entre sí: parque/río o parque/central?\n"
        "3. ¿Por qué combinar varias capas en vez de usar solo la última?",
        "r = run_paper_lab('elmo', seed=7)['result']\n"
        "e, c = r['similitud_estatica'], r['similitud_contextual']\n"
        "for par in e:\n"
        "    print(f'{par:<20} estático {e[par]:+.3f} → contextual {c[par]:+.3f} '\n"
        "          f'(separación {e[par] - c[par]:+.3f})')",
        "Con embedding estático los tres cosenos valen 1,0: son literalmente el mismo vector. Con "
        "representación contextual bajan, y bajan **de forma desigual**: los sentidos parecidos quedan "
        "más cerca que los distantes. Eso es lo que un clasificador aguas abajo puede aprovechar.",
        "ELMo se usaba como **características congeladas**: se calculaban los vectores y se alimentaban a "
        "un modelo específico de tarea. BERT, meses después, ajustaría el modelo entero. La diferencia "
        "entre «extraer características» y «ajustar todo» define dos épocas del PLN.",
        "Anti-patrón: usar solo la última capa porque «es la más profunda».",
        "capas = {'capa 0 (tokens)': 'morfología y ortografía',\n"
        "         'capa 1 (baja)': 'sintaxis: categoría gramatical, dependencias',\n"
        "         'capa 2 (alta)': 'semántica: sentido en contexto'}\n"
        "for k, v in capas.items():\n"
        "    print(f'{k:<18} → {v}')\n"
        "print('\\nUna tarea de etiquetado gramatical quiere la capa baja, no la alta.')",
        "La corrección es dejar que la tarea decida los pesos por capa:",
        "import math\n"
        "for tarea, s in (('etiquetado gramatical', [0.2, 0.6, 0.2]),\n"
        "                 ('respuesta a preguntas', [0.1, 0.3, 0.6])):\n"
        "    print(f'{tarea:<24} pesos por capa {s} (suman {sum(s):.1f})')",
        "Añade una cuarta frase con «banco» en el sentido de asiento y comprueba con cuál de las tres se agrupa.",
        "r = run_paper_lab('elmo', seed=7)['result']\n"
        "print('sentidos distinguidos:', r['sentidos_distinguidos'])\n"
        "print('el par más separado es el de sentidos más distintos:')\n"
        "for par, v in sorted(r['similitud_contextual'].items(), key=lambda kv: kv[1]):\n"
        "    print(f'  {par:<20} {v:+.3f}')",
        "Con un modelo contextual abierto y ejecutable localmente, toma 30 frases con una palabra polisémica "
        "y agrupa sus vectores. Comprueba si los grupos se corresponden con los sentidos del diccionario y "
        "documenta los casos donde no.",
        "Guarda las similitudes estática y contextual, la explicación de por qué se combinan capas y tu "
        "cuarta frase con el resultado de agrupamiento.",
        "Las representaciones ya dependen del contexto. Falta unificar **las tareas**: cada una seguía "
        "necesitando su propia cabeza y su propio formato.",
    ),
    "P25_t5": _spec(
        "Cinco tareas, cinco arquitecturas, cinco formatos, cinco métricas. T5 pregunta: ¿y si todas "
        "fueran «te doy un texto, devuélveme un texto»? Entonces solo hay un modelo y una pérdida.",
        "```text\nAntes:\n"
        "    clasificar → cabeza con 2 logits + entropía cruzada\n"
        "    regresión  → cabeza lineal + error cuadrático\n"
        "    extracción → dos cabezas (inicio, fin) + entropía cruzada\n"
        "    generación → decoder + verosimilitud\n\n"
        "T5:\n"
        "    TODO      → texto de entrada con prefijo → texto de salida\n"
        "    pérdida   → maximizar log p(texto_salida | texto_entrada)\n```",
        "El motor muestra cinco tareas reescritas al mismo formato.",
        "r = run_paper_lab('t5', seed=7)['result']\n"
        "for t in r['tareas']:\n"
        "    print(f\"{t['tarea']:<26} antes: {t['clasico']}\")\n"
        "    print(f\"{'':<26} in : {t['entrada'][:62]}\")\n"
        "    print(f\"{'':<26} out: {t['salida']}\\n\")",
        "1. ¿Cómo se emite una regresión (un número real) como texto?\n"
        "2. ¿Qué se pierde al hacerlo?\n"
        "3. Si todas las tareas comparten pérdida, ¿qué distingue una de otra?",
        "r = run_paper_lab('t5', seed=7)['result']\n"
        "print('cabezas específicas antes :', r['cabezas_especificas_antes'])\n"
        "print('cabezas específicas después:', r['cabezas_especificas_despues'])\n"
        "print('objetivo único            :', r['objetivo_unico'])\n"
        "print('lo único que cambia       :', r['que_cambia_por_tarea'])",
        "Cinco tipos de cabeza distintos se reducen a cero. Lo único que distingue una tarea de otra es el "
        "**prefijo del texto de entrada**. Eso es lo que permite el estudio sistemático del paper: se "
        "pueden comparar objetivos, arquitecturas y corpus sin que la métrica cambie de significado.",
        "La contribución más citada es el marco, pero la más valiosa es el **estudio**: decenas de "
        "experimentos controlados comparando objetivos de preentrenamiento, arquitecturas y tamaños de "
        "corpus. Es un paper de ingeniería empírica rigurosa, no una idea suelta.",
        "Anti-patrón: emitir números como texto sin pensar en la precisión.",
        "for real in (4.2, 4.25, 0.333333, 12345.678):\n"
        "    print(f'valor {real:<12} → texto \"{real:.1f}\"  (se pierde todo lo que sigue)')",
        "Por eso el paper discretiza la escala de la tarea de similitud a incrementos fijos:",
        "def discretizar(x, paso=0.2):\n"
        "    return round(round(x / paso) * paso, 1)\n"
        "for real in (4.2, 4.25, 4.31, 4.9):\n"
        "    print(f'{real} → {discretizar(real)}  (el modelo solo tiene que acertar una de 26 clases)')",
        "Reescribe una tarea propia al formato texto → texto y define su prefijo.",
        "mi_tarea = {'prefijo': 'detectar sentimiento: ',\n"
        "            'entrada': 'detectar sentimiento: el envío llegó tarde y roto',\n"
        "            'salida': 'negativo'}\n"
        "show(mi_tarea)\n"
        "print('¿qué cabeza específica necesita este modelo? ninguna')",
        "Toma tres tareas de un benchmark público, reescríbelas al formato texto → texto y ajusta un modelo "
        "pequeño de encoder-decoder abierto. Compara con entrenar tres modelos con cabezas específicas: "
        "reporta exactitud, parámetros totales y tiempo.",
        "Guarda las cinco tareas reescritas, la cuenta de cabezas antes y después, y tu explicación del "
        "coste de precisión al emitir números como texto.",
        "Un formato único para todas las tareas de texto. La siguiente pregunta ya no es de formato sino de "
        "**decisión**: qué hacer, en qué orden, y cómo saber si salió bien.",
    ),
    "P26_dqn": _spec(
        "Aprender a jugar sin que nadie te explique las reglas: pruebas, ves el marcador, y ajustas. El "
        "problema es que si aprendes solo de lo último que acabas de hacer, te obsesionas con ello y "
        "olvidas lo demás.",
        "```text\nQ-learning:   Q(s,a) ← Q(s,a) + α·[ r + γ·max_a' Q(s',a') − Q(s,a) ]\n\n"
        "Dos estabilizaciones que aporta el paper:\n"
        "  · repetición de experiencia: guardar (s,a,r,s') y muestrear un LOTE al azar\n"
        "      → rompe la correlación entre muestras consecutivas\n"
        "  · red objetivo: usar una copia CONGELADA de Q para calcular el objetivo\n"
        "      → el blanco deja de moverse mientras se dispara\n```",
        "El motor entrena Q tabular en una rejilla 4×4, con y sin las dos estabilizaciones.",
        "r = run_paper_lab('dqn', seed=7)['result']\n"
        "print('entorno:', r['entorno'], '\\n')\n"
        "show(r['con_replay_y_red_objetivo'])\n"
        "show(r['sin_replay_ni_red_objetivo'])",
        "1. ¿Cuál es el número mínimo de pasos de (0,0) a (3,3) moviéndose en cruz?\n"
        "2. ¿Cuál de las dos configuraciones se acercará más a ese óptimo?\n"
        "3. ¿Por qué aprender de transiciones consecutivas es un problema?",
        "for semilla in (1, 7, 42):\n"
        "    r = run_paper_lab('dqn', seed=semilla)['result']\n"
        "    con = r['con_replay_y_red_objetivo']['pasos_medios_ultimos_50']\n"
        "    sin = r['sin_replay_ni_red_objetivo']['pasos_medios_ultimos_50']\n"
        "    print(f'semilla {semilla:>2} · con estabilizaciones {con:.2f} · sin ellas {sin:.2f} '\n"
        "          f'· óptimo 6')",
        "Con las dos estabilizaciones la política converge cerca del óptimo. Sin ellas queda peor y con más "
        "varianza entre semillas. **La contribución del paper no es Q-learning** —que es de 1989— sino "
        "hacerlo estable cuando la función Q es una red neuronal.",
        "Fíjate en lo que el paper NO cambia: la misma arquitectura y los mismos hiperparámetros en decenas "
        "de juegos distintos. Esa uniformidad es la afirmación fuerte —generalidad— y es más difícil de "
        "conseguir que un buen resultado en un juego concreto.",
        "Anti-patrón: mover el objetivo mientras se persigue. Sin red congelada, cada actualización cambia el blanco de la siguiente.",
        "Q = 0.0\n"
        "print('sin red objetivo — el blanco se mueve con cada paso:')\n"
        "for i in range(5):\n"
        "    objetivo = 1.0 + 0.95 * Q      # el objetivo depende de la MISMA Q que se actualiza\n"
        "    Q += 0.5 * (objetivo - Q)\n"
        "    print(f'  paso {i}: objetivo={objetivo:.4f}  Q={Q:.4f}')",
        "Con una copia congelada, el blanco se queda quieto entre sincronizaciones:",
        "Q, Q_obj = 0.0, 0.0\n"
        "print('con red objetivo — el blanco solo cambia al sincronizar:')\n"
        "for i in range(5):\n"
        "    objetivo = 1.0 + 0.95 * Q_obj\n"
        "    Q += 0.5 * (objetivo - Q)\n"
        "    if i == 2:\n"
        "        Q_obj = Q\n"
        "        print('  --- sincronización ---')\n"
        "    print(f'  paso {i}: objetivo={objetivo:.4f}  Q={Q:.4f}')",
        "Sube la tasa de exploración ε y observa el compromiso entre explorar y explotar.",
        "for eps in (0.0, 0.05, 0.2, 0.6):\n"
        "    print(f'ε={eps:<5} → ' + ('nunca descubre rutas nuevas' if eps == 0 else\n"
        "          'explora demasiado, no explota lo aprendido' if eps > 0.5 else 'equilibrio razonable'))",
        "Implementa DQN con una red pequeña sobre un entorno de control clásico y de código abierto. Mide "
        "la curva de recompensa con y sin repetición de experiencia, con tres semillas, y reporta la "
        "varianza además de la media.",
        "Guarda la comparación con y sin estabilizaciones en tres semillas, y tu explicación de por qué "
        "un objetivo móvil desestabiliza el aprendizaje.",
        "Ya hay un agente que aprende a decidir por recompensa. Pero en juegos con un espacio enorme, "
        "probar no basta: hay que **buscar**.",
    ),
    "P27_alphago": _spec(
        "Un buen jugador no calcula todas las jugadas: su intuición descarta el 99 % y solo analiza a "
        "fondo las tres o cuatro que valen la pena. AlphaGo hace exactamente eso: una red da la intuición, "
        "la búsqueda hace el análisis.",
        "```text\nred de políticas p(a|s)   → qué jugadas merecen considerarse (reduce la ANCHURA)\n"
        "red de valor    v(s)      → cómo de buena es esta posición (reduce la PROFUNDIDAD)\n"
        "búsqueda MCTS             → combina ambas, simula y decide\n```\n\n"
        "Sin el prior, la búsqueda se dispersa en un factor de ramificación inabordable. Sin la búsqueda, "
        "el prior propone pero **no verifica nada**.",
        "El motor juega una posición de tres en raya con prior heurístico, con y sin búsqueda guiada.",
        "r = run_paper_lab('alphago', seed=7)['result']\n"
        "print('posición:', r['posicion'])\n"
        "print('solo política     → casilla', r['solo_politica'])\n"
        "print('política+búsqueda → casilla', r['politica_mas_busqueda'])\n"
        "show(r['valores_estimados_por_busqueda'])",
        "1. ¿Cuál es la respuesta correcta cuando el rival ocupa el centro?\n"
        "2. ¿Qué información tiene la búsqueda que el prior no tiene?\n"
        "3. ¿Por qué el prior sigue siendo necesario si la búsqueda evalúa?",
        "for semilla in (1, 7, 42):\n"
        "    r = run_paper_lab('alphago', seed=semilla)['result']\n"
        "    print(f\"semilla {semilla:>2} · prior {r['solo_politica']} · búsqueda {r['politica_mas_busqueda']} \"\n"
        "          f\"· ambas esquina: {r['ambas_eligen_esquina']}\")",
        "Ambas eligen esquina, pero solo la búsqueda produce **un número por casilla**. Esa es la "
        "diferencia operativa: una preferencia no se puede comparar ni auditar; una estimación de valor, sí. "
        "Y con más simulaciones, esa estimación mejora — el prior no mejora con nada.",
        "AlphaGo es donde se juntan las dos tradiciones que el programa enseña por separado: la búsqueda "
        "simbólica de la parte 01 y el aprendizaje profundo de la parte 04. Ninguna de las dos habría "
        "bastado sola, y eso es lo que hay que llevarse.",
        "Anti-patrón: presentarlo como «la red neuronal venció al campeón». La red sola no vence a nadie.",
        "print('Sin busqueda: la red propone la jugada mas plausible SEGUN PARTIDAS VISTAS.')\n"
        "print('No comprueba si funciona en ESTA posicion concreta.')\n"
        "print('El titulo del paper nombra las dos piezas: redes profundas Y busqueda en arbol.')",
        "La formulación correcta separa las tres contribuciones:",
        "contribuciones = {\n"
        "    'red de políticas': 'reduce la anchura del árbol proponiendo jugadas plausibles',\n"
        "    'red de valor': 'reduce la profundidad evaluando posiciones sin llegar al final',\n"
        "    'MCTS': 'usa ambas para repartir un presupuesto de simulaciones y decidir',\n"
        "    'autojuego': 'genera los datos con los que se refinan las redes',\n"
        "}\n"
        "show(contribuciones)",
        "Reparte el presupuesto de simulaciones de forma uniforme en vez de según el prior y compara.",
        "libres = 8\n"
        "for presupuesto in (8, 40, 200):\n"
        "    print(f'{presupuesto:>3} simulaciones · uniforme: {presupuesto // libres} por jugada '\n"
        "          f'· guiado: hasta {int(presupuesto * 0.25)} en la más prometedora')",
        "Implementa MCTS con UCT sobre tres en raya o conecta-4, con y sin prior heurístico. Mide la tasa "
        "de victoria frente a un oponente aleatorio en función del número de simulaciones, y localiza a "
        "partir de cuántas el prior deja de aportar.",
        "Guarda las jugadas elegidas por ambos métodos, los valores estimados por la búsqueda y tu "
        "explicación de qué reduce la anchura y qué reduce la profundidad.",
        "Búsqueda y aprendizaje ya colaboran en un juego con reglas. Trasladar eso al **lenguaje**, donde "
        "no hay reglas ni marcador, exige otra idea.",
    ),
    "P28_chain_of_thought": _spec(
        "Pedir el resultado de una multiplicación de tres cifras «de cabeza» falla; pedirla por pasos, no. "
        "No es que el modelo sepa más: es que le has dado sitio donde hacer la cuenta.",
        "```text\nDirecto:   pregunta → respuesta\n"
        "Cadena :   pregunta → paso 1 → paso 2 → … → respuesta\n```\n\n"
        "La aritmética de por qué funciona:\n\n"
        "```text\nP(acertar directo)  ≈ dificultad del problema entero\n"
        "P(acertar cadena)   ≈ (fiabilidad por paso)^n\n```\n\n"
        "Descomponer gana **si y solo si** cada paso es mucho más fiable que el problema completo. Por eso "
        "no funciona en modelos pequeños: sus pasos no son suficientemente buenos.",
        "El motor modela ambas probabilidades y localiza el umbral de fiabilidad por paso.",
        "r = run_paper_lab('cot', seed=7)['result']\n"
        "show(r['supuestos'])\n"
        "print()\n"
        "for f in r['por_numero_de_pasos']:\n"
        "    print(f\"{f['pasos']:>2} pasos · directo {f['directo']:.4f} · cadena {f['cadena']:.4f} \"\n"
        "          f\"· gana cadena: {f['gana_cadena']}\")",
        "1. ¿La cadena gana siempre, o hay un número de pasos a partir del cual pierde?\n"
        "2. ¿De qué depende realmente que compense: del número de pasos o de la calidad de cada uno?\n"
        "3. ¿Por qué el efecto no aparece en modelos pequeños?",
        "r = run_paper_lab('cot', seed=7)['result']\n"
        "print('umbral de fiabilidad por paso:', r['fiabilidad_por_paso_minima_para_que_compense'])\n"
        "print()\n"
        "for e in r['emergencia_con_la_escala']:\n"
        "    print(f\"{e['parametros_miles_millones']:>6} MM parámetros · cadena {e['cadena_3_pasos']:.4f} \"\n"
        "          f\"· directo {e['directo']:.4f} · ayuda: {e['la_cadena_ayuda']}\")",
        "El cruce **no está en el número de pasos** sino en la fiabilidad de cada uno. Por debajo del "
        "umbral, descomponer empeora: multiplicas errores. Por encima, mejora. Y como la fiabilidad por "
        "paso crece con la escala del modelo, el efecto **emerge**: no es que aparezca una capacidad "
        "mágica, es que un producto de números cruza un umbral.",
        "Ojo con la palabra «emergencia». Aquí se puede explicar con probabilidad elemental. Trabajo "
        "posterior discutió si muchas capacidades «emergentes» lo son de verdad o son artefactos de "
        "métricas discontinuas (acertar/fallar) que ocultan una mejora continua.",
        "Anti-patrón: leer la cadena como una explicación del proceso interno del modelo.",
        "print('La cadena es TEXTO GENERADO, optimizado para que la respuesta final sea correcta.')\n"
        "print('Puede contener pasos invalidos y llegar al resultado correcto, o al reves.')\n"
        "print('Sirve para depurar y para dar sitio al calculo; no es un certificado.')",
        "Lo que sí se puede afirmar, y cómo comprobarlo:",
        "auditoria = {\n"
        "    'comprobable': 'la respuesta final, contra la solución conocida',\n"
        "    'no_comprobable_sin_trabajo': 'la validez de cada paso intermedio',\n"
        "    'como_reforzarlo': ['muestrear varias cadenas y votar (autoconsistencia)',\n"
        "                         'ejecutar el cálculo con una herramienta externa'],\n"
        "}\n"
        "show(auditoria)",
        "Calcula cuántos pasos aguanta una cadena antes de bajar del 50 % de fiabilidad, para varias calidades por paso.",
        "import math\n"
        "for q in (0.80, 0.90, 0.95, 0.99):\n"
        "    n = math.floor(math.log(0.5) / math.log(q))\n"
        "    print(f'fiabilidad por paso {q:.2f} → aguanta {n:>3} pasos por encima del 50%')",
        "Con un modelo abierto pequeño y un conjunto de problemas aritméticos, compara respuesta directa "
        "frente a cadena de pensamiento. Mide además cuántas cadenas contienen un paso inválido pero "
        "llegan al resultado correcto: esa tasa es la que desmonta la lectura ingenua.",
        "Guarda la tabla directo/cadena, el umbral de fiabilidad y tu explicación de por qué la emergencia "
        "aquí es aritmética y no magia.",
        "Razonar en línea recta ayuda, pero no permite volver atrás. Si un paso intermedio es malo, toda la "
        "cadena se pierde — y ahí entra la búsqueda.",
    ),
    "P29_tree_of_thoughts": _spec(
        "Una cadena de pensamiento es como escribir a bolígrafo: si el tercer paso está mal, sigues "
        "adelante con él. Un árbol es escribir a lápiz con varias hojas: exploras, comparas y borras.",
        "```text\nCadena :  s₀ → s₁ → s₂ → s₃            una rama, sin vuelta atrás\n"
        "Árbol  :  s₀ → {s₁ᵃ, s₁ᵇ, s₁ᶜ} → …     varias ramas, con evaluación y poda\n```\n\n"
        "Tres piezas necesarias: **generar** candidatos, **evaluar** estados parciales (el propio modelo "
        "juzga «esto promete / esto no lleva a nada») y una **estrategia de búsqueda** (anchura, "
        "profundidad, poda).",
        "El motor compara una cadena lineal con una búsqueda en árbol con poda sobre el mismo espacio.",
        "r = run_paper_lab('tot', seed=7)['result']\n"
        "print('profundidad:', r['profundidad'], '· ramas por paso:', r['ramas_por_paso'], '\\n')\n"
        "show(r['cadena_lineal'])\n"
        "show(r['busqueda_en_arbol'])\n"
        "print('\\ncoste relativo:', r['coste_relativo'], 'x')",
        "1. ¿Cuántos nodos evalúa una cadena de profundidad 3 con 3 ramas? ¿Y un árbol con anchura 3?\n"
        "2. ¿Qué gana el árbol a cambio de ese coste?\n"
        "3. Si el evaluador fuera aleatorio, ¿serviría de algo explorar?",
        "for anchura in (1, 2, 3, 5):\n"
        "    nodos = sum(min(3 ** (d + 1), anchura * 3) for d in range(3))\n"
        "    print(f'anchura {anchura} → ~{nodos:>2} nodos evaluados '\n"
        "          f\"({'equivale a la cadena lineal' if anchura == 1 else 'mantiene alternativas vivas'})\")",
        "Con anchura 1, el árbol **es** la cadena lineal: ese es el caso límite. Cada unidad de anchura "
        "multiplica el coste y compra la posibilidad de recuperarse de un mal paso. El compromiso es "
        "explícito y se puede presupuestar.",
        "La pieza frágil es el **evaluador**. Si el modelo no sabe juzgar estados parciales, el árbol solo "
        "multiplica el gasto. Por eso ToT funciona bien en problemas donde el progreso parcial es "
        "verificable (Game of 24, crucigramas) y peor donde no lo es.",
        "Anti-patrón: aumentar la anchura para «buscar mejor», sin comprobar la calidad del evaluador.",
        "import random\n"
        "rng = random.Random(0)\n"
        "for calidad in (0.5, 0.7, 0.95):\n"
        "    aciertos = sum(1 for _ in range(1000) if rng.random() < calidad)\n"
        "    print(f'evaluador con {calidad:.0%} de acierto → poda correcta {aciertos/10:.1f}% de las veces')\n"
        "print('\\ncon un evaluador al 50% la poda es una moneda: gastas 3x y no ganas nada')",
        "La corrección es medir el evaluador **antes** de pagar la búsqueda:",
        "protocolo = {\n"
        "    'paso_1': 'medir la calidad del evaluador sobre estados parciales con solución conocida',\n"
        "    'paso_2': 'si acierta poco, mejorar el evaluador ANTES de ampliar la búsqueda',\n"
        "    'paso_3': 'fijar presupuesto de nodos y reportarlo junto con la exactitud',\n"
        "}\n"
        "show(protocolo)",
        "Comprueba el caso límite: con anchura 1 el árbol debe comportarse exactamente como la cadena.",
        "r = run_paper_lab('tot', seed=7)['result']\n"
        "print('cadena lineal   :', r['cadena_lineal']['nodos_evaluados'], 'nodos')\n"
        "print('árbol anchura 3 :', r['busqueda_en_arbol']['nodos_evaluados'], 'nodos')\n"
        "print('frontera final  :', r['busqueda_en_arbol']['frontera_final'], 'hipótesis vivas')",
        "Implementa ToT sobre el juego de las 24 con un modelo abierto: genera candidatos, haz que el "
        "modelo clasifique cada estado parcial como «seguro / quizá / imposible», y compara la tasa de "
        "éxito frente a cadena simple. Reporta también el número de llamadas al modelo.",
        "Guarda la comparación de nodos evaluados, el caso límite de anchura 1 y tu protocolo para medir "
        "el evaluador antes de pagar la búsqueda.",
        "Deliberar mejor dentro de un intento. Falta aprender **entre** intentos: que fallar una vez sirva "
        "para la siguiente.",
    ),
    "P30_reflexion": _spec(
        "Un agente sin memoria de sus fallos es alguien que repite el mismo error con entusiasmo. "
        "Reflexion añade lo mínimo para romper el bucle: escribir qué salió mal y leerlo antes de reintentar.",
        "```text\nBucle sin reflexión:   intento → falla → intento (idéntico) → falla → …\n\n"
        "Bucle con reflexión:   intento → falla → REFLEXIÓN («olvidé el caso vacío»)\n"
        "                       → memoria → intento (condicionado) → …\n```\n\n"
        "No hay gradientes. La política mejora porque **el contexto del siguiente intento es distinto**: "
        "es refuerzo, pero expresado en lenguaje.",
        "El motor compara cuatro intentos con y sin memoria verbal del fallo.",
        "r = run_paper_lab('reflexion', seed=7)['result']\n"
        "print('errores del problema:', r['errores_del_problema'], '\\n')\n"
        "print('SIN reflexión:')\n"
        "for t in r['sin_reflexion']['traza']:\n"
        "    print('  ', t)\n"
        "print('\\nCON reflexión:')\n"
        "for t in r['con_reflexion']['traza']:\n"
        "    print('  ', t)",
        "1. ¿Cuántos intentos necesita el agente sin memoria para superar tres errores distintos?\n"
        "2. ¿Cuántos con memoria?\n"
        "3. ¿Cuántos pesos se actualizan en el proceso?",
        "r = run_paper_lab('reflexion', seed=7)['result']\n"
        "print('pesos actualizados:', r['pesos_actualizados'])\n"
        "print('sin reflexión → éxito:', r['sin_reflexion']['exito'],\n"
        "      '· intentos:', r['sin_reflexion']['intentos_usados'])\n"
        "print('con reflexión → éxito:', r['con_reflexion']['exito'],\n"
        "      '· intentos:', r['con_reflexion']['intentos_usados'])",
        "Sin memoria, el agente no termina: repite el primer fallo indefinidamente. Con memoria, cada "
        "intento elimina un error y converge. Y **cero pesos actualizados**: todo el aprendizaje vive en "
        "el contexto, lo que lo hace barato, inmediato y también efímero.",
        "El método depende por completo de tener una **señal de fallo fiable**: un test que falle, un "
        "compilador que proteste, un entorno que devuelva error. Sin verificador no hay sobre qué "
        "reflexionar, y la reflexión degenera en autoafirmación.",
        "Anti-patrón: reflexionar sin señal externa, dejando que el modelo juzgue su propio trabajo sin evidencia.",
        "print('«Revisa tu respuesta y mejórala» sin ejecutar nada:')\n"
        "print('  - el modelo suele declararse satisfecho, o cambia cosas al azar')\n"
        "print('  - sin senal externa, la reflexion no tiene informacion nueva que incorporar')",
        "La corrección es anclar la reflexión en una observación verificable:",
        "ciclo = {\n"
        "    '1_ejecutar': 'correr los tests / el código / la consulta',\n"
        "    '2_observar': 'capturar el error concreto, no una impresión',\n"
        "    '3_reflexionar': 'escribir qué causó ESE error',\n"
        "    '4_reintentar': 'con la reflexión en el contexto',\n"
        "    'criterio_de_parada': 'máximo de intentos + detección de reflexión repetida',\n"
        "}\n"
        "show(ciclo)",
        "Comprueba qué pasa si la memoria crece sin límite: el contexto es finito.",
        "for intentos in (3, 10, 50, 200):\n"
        "    tokens = intentos * 80\n"
        "    print(f'{intentos:>3} intentos → ~{tokens:>6} tokens de memoria verbal '\n"
        "          f\"({'cabe' if tokens < 8000 else 'ya no cabe: hay que resumir o priorizar'})\")",
        "Implementa Reflexion sobre un conjunto de ejercicios de programación con tests. Mide la tasa de "
        "éxito acumulada por número de intentos, con y sin reflexión, y cuenta cuántas reflexiones son "
        "realmente accionables frente a genéricas («ser más cuidadoso»).",
        "Guarda ambas trazas, el número de pesos actualizados y tu ciclo de reflexión anclado en "
        "observación verificable.",
        "El agente ya aprende de sus fallos dentro de una tarea. Falta que recuerde **entre** tareas y a "
        "lo largo del tiempo.",
    ),
    "P31_generative_agents": _spec(
        "Una persona no recuerda su día en orden cronológico: recuerda lo que viene a cuento. Si un agente "
        "guarda todo y recupera lo último, recordará que compró café en vez de que mañana hay una fiesta.",
        "```text\npuntuación(recuerdo) = relevancia + recencia + importancia\n\n"
        "    relevancia  = similitud con la consulta actual\n"
        "    recencia    = decaimiento exponencial desde la última vez que se accedió\n"
        "    importancia = cuán significativo es el recuerdo en sí (lo puntúa el modelo)\n```\n\n"
        "Y encima, **reflexión**: sintetizar periódicamente los recuerdos en conclusiones de nivel "
        "superior («Klaus está muy metido en su investigación»), que a su vez se guardan como recuerdos.",
        "El motor puntúa cinco recuerdos ante una consulta, con las tres señales y solo con recencia.",
        "r = run_paper_lab('generative_agents', seed=7)['result']\n"
        "print('consulta:', r['consulta'], '\\n')\n"
        "for m in r['ranking_completo']:\n"
        "    print(f\"{m['puntuacion']:.3f} = rel {m['relevancia']:.2f} + rec {m['recencia']:.3f} \"\n"
        "          f\"+ imp {m['importancia']:.2f}  ← {m['texto']}\")",
        "1. ¿Qué recuerdo debería recuperarse ante una consulta sobre la fiesta y Klaus?\n"
        "2. ¿Cuál saldría si ordenáramos solo por lo más reciente?\n"
        "3. ¿Qué señal evita que un recuerdo trivial y reciente gane?",
        "r = run_paper_lab('generative_agents', seed=7)['result']\n"
        "print('con las tres señales :', r['top_con_las_tres_senales'])\n"
        "print('solo por recencia    :', r['top_solo_por_recencia'])",
        "Con las tres señales sube lo relevante e importante. Solo por recencia sube lo trivial. Una "
        "memoria útil **no es un registro cronológico**: es un sistema de recuperación con criterio, y "
        "ese criterio hay que diseñarlo.",
        "Este paper se suele contar como «una simulación tipo Los Sims con LLM». Lo que importa "
        "técnicamente es otra cosa: es de los primeros que trata la **memoria de un agente de larga "
        "duración** como un problema de recuperación con puntuación, no como un log que se concatena.",
        "Anti-patrón: meter toda la historia en el contexto porque «el contexto ya es grande».",
        "for horas in (1, 8, 24, 168):\n"
        "    eventos = horas * 30\n"
        "    tokens = eventos * 25\n"
        "    print(f'{horas:>3} h de vida → ~{eventos:>5} eventos → ~{tokens:>7} tokens '\n"
        "          f\"({'cabe' if tokens < 100000 else 'imposible: hay que recuperar, no concatenar'})\")",
        "La corrección es separar almacenamiento de recuperación, y puntuar:",
        "arquitectura = {\n"
        "    'flujo_de_memoria': 'todo se guarda, con marca de tiempo e importancia',\n"
        "    'recuperacion': 'se puntúa por relevancia + recencia + importancia y se toma el top-k',\n"
        "    'reflexion': 'periódicamente se sintetizan recuerdos en conclusiones de alto nivel',\n"
        "    'lo_que_entra_al_contexto': 'solo el top-k recuperado, no el flujo completo',\n"
        "}\n"
        "show(arquitectura)",
        "Cambia el factor de decaimiento y observa cuánto pesa la recencia frente a la importancia.",
        "for decaimiento in (0.90, 0.99, 0.999):\n"
        "    print(f'decaimiento {decaimiento}:')\n"
        "    for antiguedad in (1, 10, 60):\n"
        "        print(f'   hace {antiguedad:>2} pasos → recencia {decaimiento ** antiguedad:.4f}')",
        "Implementa un flujo de memoria con recuperación puntuada para un asistente que registre tu propia "
        "actividad durante una semana. Compara la utilidad de lo recuperado con las tres señales frente a "
        "solo similitud, sobre 20 consultas reales tuyas.",
        "Guarda el ranking con las tres señales, el que sale solo por recencia, y tu explicación de por qué "
        "concatenar el historial no escala.",
        "El agente ya recuerda lo pertinente. Falta que lo aprendido se convierta en **capacidad "
        "reutilizable**, no solo en texto que recordar.",
    ),
    "P32_voyager": _spec(
        "Aprender a cocinar no es recordar cada vez la receta entera: es que «hacer un sofrito» pase a ser "
        "una sola cosa que sabes hacer. Voyager guarda habilidades, no anécdotas.",
        "```text\nMemoria en contexto:      cada tarea reintroduce todo lo aprendido como TEXTO\n"
        "                          → ocupa contexto, se pierde al terminar\n\n"
        "Biblioteca de habilidades: cada solución verificada se guarda como CÓDIGO con nombre\n"
        "                          → se invoca por nombre, se compone, persiste\n```\n\n"
        "Más un **currículo automático**: el agente propone su siguiente tarea en función de lo que ya "
        "sabe y de lo que ve en el entorno.",
        "El motor construye una biblioteca donde cada habilidad se apoya en las anteriores.",
        "r = run_paper_lab('voyager', seed=7)['result']\n"
        "for c in r['curriculo']:\n"
        "    print(f\"{c['tarea']:<18} · {c['pasos_declarados']} pasos declarados \"\n"
        "          f\"= {c['acciones_primitivas_equivalentes']:>2} primitivas \"\n"
        "          f\"· reutiliza {c['habilidades_reutilizadas']}\")",
        "1. ¿Cuántas acciones primitivas equivale la última tarea, declarada en 3 pasos?\n"
        "2. ¿Qué pasaría si cada tarea tuviera que escribirse desde cero en primitivas?\n"
        "3. ¿Por qué una biblioteca no consume contexto y una memoria textual sí?",
        "r = run_paper_lab('voyager', seed=7)['result']\n"
        "print('habilidades en la biblioteca:', r['habilidades_aprendidas'], '\\n')\n"
        "for c in r['curriculo']:\n"
        "    print(f\"{c['tarea']:<18} factor de compresión {c['factor_de_compresion']:>5}x\")",
        "El factor de compresión crece con el currículo: las tareas tardías se expresan en muy pocos pasos "
        "porque cada uno esconde muchas primitivas. **Eso es lo que significa acumular capacidad**, frente "
        "a acumular texto.",
        "La pieza que hace esto viable, y que la miniatura no muestra, es la **verificación**: una "
        "habilidad solo entra en la biblioteca si su código se ejecutó y funcionó en el entorno. Sin ese "
        "filtro, la biblioteca se llena de habilidades rotas que se propagan a todo lo que las use.",
        "Anti-patrón: guardar en la biblioteca sin verificar. Una habilidad rota contamina todas las que la componen.",
        "biblioteca = {'conseguir_madera': 'ROTA (no comprueba si hay árbol)'}\n"
        "dependen = ['fabricar_mesa', 'fabricar_pico', 'minar_piedra', 'fabricar_horno']\n"
        "print('habilidad rota:', list(biblioteca)[0])\n"
        "print('afectadas por composición:', dependen)\n"
        "print(f'una sola habilidad sin verificar rompe {len(dependen)} tareas posteriores')",
        "La corrección es un contrato de entrada a la biblioteca:",
        "contrato = {\n"
        "    'se_guarda_si': ['el código se ejecutó en el entorno',\n"
        "                      'la tarea se completó de forma verificable',\n"
        "                      'tiene nombre y descripción para poder recuperarla'],\n"
        "    'se_reintenta_si': 'falla, con el error del entorno como retroalimentación',\n"
        "    'nunca': 'guardar código que solo parece correcto',\n"
        "}\n"
        "show(contrato)",
        "Comprueba cómo crece la capacidad al componer: cuenta las primitivas de una tarea inventada de nivel 6.",
        "r = run_paper_lab('voyager', seed=7)['result']\n"
        "biblioteca = r['biblioteca_final']\n"
        "print('biblioteca:')\n"
        "for k, v in biblioteca.items():\n"
        "    print(f'  {k:<18} = {v}')",
        "Construye un agente con biblioteca de habilidades para un entorno programable simple (por ejemplo "
        "un intérprete de comandos de ficheros). Exige verificación antes de guardar y mide cuántos pasos "
        "necesita para la tarea 10 con y sin biblioteca.",
        "Guarda el currículo con su factor de compresión, el experimento de la habilidad rota y tu contrato "
        "de entrada a la biblioteca.",
        "Un agente que aprende y acumula. La última pregunta es si **varios** agentes se coordinan mejor "
        "que uno solo — y qué cuesta.",
    ),
    "P33_autogen": _spec(
        "Quien escribe un texto es mal corrector de su propio texto: lee lo que quiso escribir. Poner a "
        "otro a revisarlo no es redundancia, es un punto de vista distinto sobre el mismo trabajo.",
        "```text\nUn agente:     modelo → salida → (se juzga a sí mismo)\n\n"
        "Multiagente:   planificador → programador → crítico → programador → …\n"
        "               cada uno con su rol, su prompt y su objetivo\n```\n\n"
        "AutoGen lo formula como **conversación**: agentes configurables que se mandan mensajes, con o sin "
        "humano en el bucle, con o sin ejecución de código, y con patrones de conversación programables.",
        "El motor compara una entrega de un solo agente con una conversación de tres roles.",
        "r = run_paper_lab('autogen', seed=7)['result']\n"
        "print('UN SOLO AGENTE:')\n"
        "show(r['un_solo_agente'])\n"
        "print('\\nMULTIAGENTE:')\n"
        "for t in r['multiagente']['traza']:\n"
        "    print(f\"  [{t['rol']:<13}] {t['mensaje']}\")",
        "1. ¿Qué fallo tiene el código del agente único?\n"
        "2. ¿Por qué el crítico lo detecta y el propio autor no?\n"
        "3. ¿Cuántas veces más caro sale en turnos?",
        "r = run_paper_lab('autogen', seed=7)['result']\n"
        "print('un agente   → correcto:', r['un_solo_agente']['correcto'],\n"
        "      '· turnos:', r['un_solo_agente']['turnos'])\n"
        "print('multiagente → correcto:', r['multiagente']['correcto'],\n"
        "      '· turnos:', r['multiagente']['turnos'])\n"
        "print('coste relativo:', r['coste_relativo_en_turnos'], 'x')",
        "La conversación encuentra el fallo y lo corrige, a cambio de **5× más turnos**. Esa es la cuenta "
        "que hay que hacer siempre: multiagente no es gratis y no es mejor por defecto. Hay que demostrar "
        "que el error que captura compensa el coste que añade.",
        "El crítico funciona porque su **objetivo es distinto**: encontrar fallos, no producir código. Si "
        "los dos roles comparten prompt, modelo y objetivo, la crítica se vuelve ceremonial — es la versión "
        "multiagente de la sicofancia.",
        "Anti-patrón: conversación sin criterio de parada. Dos agentes educados pueden felicitarse indefinidamente.",
        "turnos = 0\n"
        "for _ in range(50):\n"
        "    turnos += 1\n"
        "    # cada uno espera que el otro cierre; nadie tiene autoridad para terminar\n"
        "print(f'sin criterio de parada: {turnos} turnos y subiendo, sin converger')\n"
        "print('cada turno es una llamada al modelo: el coste es lineal y no acotado')",
        "La corrección es dar autoridad de cierre y presupuesto:",
        "protocolo = {\n"
        "    'criterio_de_exito': 'los tests pasan (verificable, no opinión)',\n"
        "    'maximo_de_turnos': 8,\n"
        "    'quien_cierra': 'el crítico, y solo con evidencia de ejecución',\n"
        "    'deteccion_de_bucle': 'si dos turnos repiten el mismo mensaje, abortar',\n"
        "    'escalamiento': 'al agotar el presupuesto, entregar a un humano con la traza',\n"
        "}\n"
        "show(protocolo)",
        "Añade un cuarto rol (por ejemplo, un revisor de seguridad) y razona si aporta o solo encarece.",
        "roles = {'planificador': 'descompone', 'programador': 'implementa',\n"
        "         'crítico': 'busca fallos', 'seguridad': 'busca riesgos'}\n"
        "for n in range(2, 5):\n"
        "    activos = list(roles)[:n]\n"
        "    print(f'{n} roles {activos} → ~{n * 2} turnos mínimos')\n"
        "print('\\ncada rol nuevo debe justificar su coste con un tipo de error que SOLO él captura')",
        "Monta un sistema de dos y de cuatro agentes sobre la misma tarea de programación con tests. "
        "Ejecuta 30 veces cada configuración y compara tasa de éxito, turnos y coste. Comprueba si el "
        "multiagente gana a un agente único **bien construido**, que es la línea base honesta.",
        "Guarda ambas trazas, el coste relativo en turnos y tu protocolo con criterio de parada, detección "
        "de bucle y escalamiento.",
        "Aquí se cierra el bloque de agentes. Todo lo que sigue —memoria compartida, protocolos entre "
        "proveedores, evaluación de trayectorias— vive en la frontera, con fecha.",
    ),
})


def _auto(lab, intuicion, concepto, prediccion, salida, comentario, anti_md, anti, corr_md, corr,
          dg_md, da, evidencia, cierre, extra_exp=None):
    """Especificación compacta para motores cuyo notebook sigue el patrón estándar."""
    codigo = f"r = run_paper_lab('{lab}', seed=7)['result']\nshow(r)"
    exp = extra_exp or (
        f"for semilla in (1, 7, 42):\n"
        f"    r = run_paper_lab('{lab}', seed=semilla)\n"
        f"    print(f'semilla {{semilla:>2}} · evidencia principal:')\n"
        f"    for e in r['evidence']:\n"
        f"        print('   +', e)\n"
        f"    break  # determinista: basta una para ver la estructura\n"
        f"for semilla in (1, 7, 42):\n"
        f"    r = run_paper_lab('{lab}', seed=semilla)['result']\n"
        f"    print(f'semilla {{semilla:>2}} → claves: {{list(r)[:4]}}')"
    )
    return _spec(intuicion, concepto, "El motor aísla el mecanismo del paper con datos de juguete y salida inspeccionable.",
                 codigo, prediccion, exp, salida, comentario, anti_md, anti, corr_md, corr,
                 dg_md, f"r = run_paper_lab('{lab}', seed=3)['result']\nshow(r)", da, evidencia, cierre)


SPECS.update({
    "P34_rope": _auto(
        "rope",
        "En vez de sumar una marca de posición, se **rota** el vector según dónde esté. Al comparar "
        "dos tokens, las rotaciones se cancelan parcialmente y lo que queda depende solo de cuánto "
        "se separan. La posición absoluta desaparece del resultado.",
        "```text\nRoPE: q_m = R_m·q,   k_n = R_n·k,   con R_θ una rotación por bloques de 2\n\n"
        "    ⟨R_m·q, R_n·k⟩ = f(q, k, m − n)      ← solo la DIFERENCIA\n```",
        "1. ¿Darán el mismo producto escalar las posiciones (5,3) y (500,498)?\n"
        "2. ¿Qué le pasa al producto conforme crece la distancia?\n"
        "3. ¿Por qué eso es un buen sesgo para lenguaje?",
        "Las tres parejas con la misma diferencia dan **exactamente** el mismo valor. La posición "
        "absoluta se usa para rotar, pero no aparece en el resultado: la atención solo ve distancia relativa.",
        "Esto es lo que hoy llevan casi todos los modelos abiertos. La codificación sinusoidal de "
        "[P08](../../papers/foundational/P08_transformer/README.md) sigue siendo válida, pero RoPE se "
        "impuso porque da la relatividad **gratis**, sin parámetros extra ni tablas de posición.",
        "Anti-patrón: creer que RoPE permite por sí solo extrapolar a contextos mucho más largos.",
        "print('RoPE da posicion relativa; NO garantiza extrapolar mas alla del entrenamiento.')\n"
        "print('Extender el contexto exige tecnicas POSTERIORES (interpolacion de posiciones).')\n"
        "print('Atribuirle eso al paper de 2021 es un anacronismo.')",
        "Lo que sí aporta, enunciado con precisión:",
        "aporta = {'relatividad': 'el producto depende solo de m−n',\n"
        "          'sin parametros': 'la rotacion no anade pesos que aprender',\n"
        "          'decaimiento': 'tiende a bajar con la distancia, buen sesgo para lenguaje',\n"
        "          'no_aporta': 'extrapolacion automatica a longitudes no vistas'}\n"
        "show(aporta)",
        "Comprueba que dos parejas con distinta diferencia dan valores distintos, y que la de diferencia 0 es la mayor.",
        "Implementa RoPE sobre una atención pequeña y mide la exactitud en una tarea de copia con "
        "posiciones desplazadas. Comprueba si el modelo generaliza a posiciones que no vio.",
        "Guarda la tabla de invariancia relativa, la de decaimiento y tu enunciado de qué aporta y qué no.",
        "La posición ya es relativa y barata. El siguiente muro no es matemático: es la memoria del "
        "hardware.",
    ),
    "P35_flashattention": _auto(
        "flashattention",
        "El cálculo de la atención no es lento por hacer muchas cuentas: es lento por escribir y leer "
        "una matriz enorme en la memoria lenta de la GPU. La solución no es calcular menos, sino no "
        "escribirla nunca.",
        "```text\nEstándar:  calcular S = QKᵀ  → ESCRIBIR n×n en HBM → leer → softmax → escribir → leer → ×V\n"
        "Flash   :  recorrer por bloques que caben en SRAM, con softmax incremental reescalado\n\n"
        "    mismos FLOPs · mismo resultado EXACTO · muchísimos menos accesos a memoria\n```",
        "1. ¿Cambian los FLOPs entre ambas versiones?\n"
        "2. ¿Y el resultado numérico?\n"
        "3. ¿Qué crece más rápido con n: el cómputo o la memoria que hay que mover?",
        "Los FLOPs son idénticos y el resultado es **exacto**: no es una aproximación. Lo que cambia es "
        "cuántos elementos viajan entre la memoria rápida del chip y la lenta. Ese era el cuello de botella "
        "real, y durante años se atacó el equivocado.",
        "Es una lección más general que la atención: en hardware moderno, **mover datos cuesta más que "
        "calcular**. Muchas optimizaciones «obvias» de FLOPs no aceleran nada porque el proceso está "
        "limitado por memoria. Conecta directamente con el modelo roofline de la clase 081.",
        "Anti-patrón: optimizar FLOPs sin mirar el tráfico de memoria.",
        "print('Reducir FLOPs con atencion aproximada fue el enfoque dominante 2019-2021.')\n"
        "print('Muchos de esos metodos NO eran mas rapidos en la practica:')\n"
        "print('  bajaban el computo pero seguian materializando matrices en memoria lenta.')",
        "El criterio correcto es contar accesos a memoria, no operaciones:",
        "d, M = 64, 100_000\n"
        "for n in (1024, 16384):\n"
        "    print(f'n={n:>6} · FLOPs={2*n*n*d:>15,} · HBM estandar={2*n*n+2*n*d:>13,} '\n"
        "          f'· HBM flash={int(4*n*d*(n*d/M)):>12,}')",
        "Calcula a partir de qué n la matriz de atención deja de caber en 40 GB, y compáralo con el contexto que anuncian los modelos actuales.",
        "Perfila una implementación de atención en tu GPU con y sin la versión optimizada de tu "
        "biblioteca, a varias longitudes. Reporta tiempo y memoria máxima, no solo tiempo.",
        "Guarda la tabla de FLOPs frente a accesos a memoria y tu explicación de por qué el algoritmo "
        "es exacto y aun así mucho más rápido.",
        "Ya cabe el contexto largo. La pregunta siguiente es incómoda: ¿lo usa el modelo?",
    ),
    "P36_lost_in_middle": _auto(
        "lost_in_middle",
        "Le das al modelo veinte documentos y el dato bueno está en el número once. Rinde peor que si "
        "estuviera en el primero o en el último. El mismo dato, el mismo modelo, la misma pregunta: "
        "solo cambia el sitio.",
        "```text\nexactitud(posición del documento relevante) tiene forma de U:\n\n"
        "    alta al principio  (primacía)\n"
        "    baja en el medio   ← el hallazgo\n"
        "    alta al final      (recencia)\n```",
        "1. ¿En qué posición esperas la mejor exactitud? ¿Y la peor?\n"
        "2. ¿Qué implica esto para un sistema RAG que ordena los pasajes por score?\n"
        "3. Si un modelo anuncia 128 000 tokens de contexto, ¿qué habría que medir antes de creerlo?",
        "La caída entre la mejor y la peor posición es grande, y no hay nada distinto en el contenido. "
        "**Contexto disponible no es contexto utilizable**, y esa distinción no aparece en ninguna ficha "
        "técnica de modelo.",
        "El impacto práctico es directo en RAG: si recuperas diez pasajes y colocas el mejor en medio, "
        "estás saboteando tu propio sistema. Conviene poner lo más relevante al principio **o** al final, "
        "y medirlo en vez de suponerlo.",
        "Anti-patrón: elegir modelo por el tamaño de su ventana de contexto.",
        "for ventana in (8_000, 32_000, 128_000, 1_000_000):\n"
        "    print(f'{ventana:>9,} tokens anunciados → ¿cuantos USA bien? el numero no lo dice')",
        "La comprobación correcta es una prueba de aguja en el pajar por posición:",
        "protocolo = {'1': 'insertar un hecho unico en la posicion p del contexto',\n"
        "             '2': 'preguntar por ese hecho',\n"
        "             '3': 'repetir para p en todo el rango y varias longitudes',\n"
        "             '4': 'reportar la CURVA, no un solo numero'}\n"
        "show(protocolo)",
        "Calcula la caída relativa entre la mejor y la peor posición y decide si es tolerable para un sistema de consulta legal.",
        "Ejecuta una prueba de aguja en el pajar sobre un modelo abierto, con al menos cinco longitudes "
        "y diez posiciones. Dibuja la curva y localiza dónde empieza a degradarse.",
        "Guarda la curva en U, la caída entre extremos y tu protocolo de comprobación por posición.",
        "Si la ventana no basta ni usándola bien, hay que dejar de tratarla como memoria y empezar a "
        "gestionarla como tal.",
    ),
    "P37_memgpt": _auto(
        "memgpt",
        "Tu ordenador te deja abrir archivos mucho más grandes que su memoria RAM. No los carga enteros: "
        "los pagina. MemGPT hace lo mismo con el contexto — y quien decide qué paginar es el propio modelo.",
        "```text\ncontexto principal   (pequeño, rápido, siempre visible)   ← como la RAM\n"
        "almacén externo      (grande, lento, accesible por función) ← como el disco\n\n"
        "    el modelo llama a funciones para mover información entre ambos\n```",
        "1. ¿Qué pasa con el sexto dato si la capacidad es de cinco?\n"
        "2. ¿Se pierde?\n"
        "3. ¿Qué cuesta recuperarlo?",
        "Lo desalojado **no se pierde**: baja al almacén externo y vuelve con una llamada de función. La "
        "ilusión es de memoria grande; la realidad es una jerarquía con coste por acceso.",
        "La analogía con el sistema operativo es literal y ese es su valor: da un vocabulario prestado "
        "—paginación, jerarquía, interrupciones— para un problema que se estaba tratando sin marco.",
        "Anti-patrón: tratar el almacén externo como gratis.",
        "for consultas in (1, 10, 100):\n"
        "    print(f'{consultas:>3} page-ins → {consultas} llamadas extra al modelo '\n"
        "          f'({consultas * 2:>3} segundos aprox. de latencia añadida)')",
        "Lo correcto es presupuestar los accesos igual que cualquier otra llamada:",
        "presupuesto = {'page_ins_maximos_por_respuesta': 3,\n"
        "               'que_va_al_contexto_principal': 'lo que se usa en casi toda interaccion',\n"
        "               'que_va_al_externo': 'historico, detalles puntuales, documentos',\n"
        "               'si_se_agota': 'responder con lo que hay y declarar la limitacion'}\n"
        "show(presupuesto)",
        "Reduce la capacidad del contexto principal a 2 y comprueba cuántos datos acaban en el almacén externo.",
        "Implementa una jerarquía de memoria de dos niveles para un asistente propio, con política de "
        "desalojo explícita. Mide cuántas veces hay que paginar en 50 conversaciones reales.",
        "Guarda la traza de desalojos y recuperaciones, y tu presupuesto de accesos por respuesta.",
        "Con esto se cierra el bloque de memoria y contexto. Lo que sigue es el andamiaje que hace "
        "entrenable todo lo anterior.",
    ),
    "P38_vae": _auto(
        "vae",
        "Quieres derivar respecto a la media de una distribución de la que estás muestreando. Pero "
        "muestrear es un dado: no tiene derivada. El truco es sacar el dado fuera — tirarlo aparte y "
        "meter su resultado ya fijado en la fórmula.",
        "```text\nSin reparametrizar:  z ~ N(μ, σ²)          ← nodo estocástico, gradiente bloqueado\n"
        "Reparametrizado   :  z = μ + σ·ε,  ε ~ N(0,1)  ← el azar está FUERA del camino\n\n"
        "ELBO = E_q[log p(x|z)] − KL(q(z|x) ‖ p(z))\n```",
        "1. ¿La distribución de z cambia al reparametrizar?\n"
        "2. ¿Cuánto vale ∂z/∂μ?\n"
        "3. ¿Por qué eso hace entrenable el modelo?",
        "La distribución es la misma —media y varianza coinciden— pero ahora `∂z/∂μ = 1` existe y se "
        "puede estimar, porque `ε` no depende de los parámetros. Ese es todo el truco, y es lo que hizo "
        "entrenable una familia entera de modelos.",
        "El truco de reparametrización trasciende al VAE: aparece en política estocástica, en atención "
        "con puertas, en cuantización diferenciable. Cuando algo «no es derivable», la pregunta útil es "
        "si se puede reescribir moviendo el azar fuera.",
        "Anti-patrón: creer que el término KL es un detalle de regularización opcional.",
        "print('Sin el termino KL, el codificador puede mapear cada x a una gaussiana')\n"
        "print('estrechisima y separada de las demas: el espacio latente deja de ser')\n"
        "print('continuo y muestrear de la prior ya no genera nada coherente.')",
        "El ELBO tiene dos términos y ambos hacen falta:",
        "elbo = {'reconstruccion': 'que el decodificador recupere x desde z',\n"
        "        'KL': 'que q(z|x) no se aleje de la prior, para que el espacio sea muestreable',\n"
        "        'tension': 'demasiada KL → muestras borrosas; poca → espacio latente roto'}\n"
        "show(elbo)",
        "Comprueba que la varianza empírica de las muestras coincide con σ² y que el gradiente respecto a σ es insesgado.",
        "Implementa un VAE sobre un conjunto de imágenes pequeño y visualiza el espacio latente en 2D. "
        "Interpola entre dos puntos y comprueba si las muestras intermedias son coherentes.",
        "Guarda la comprobación de media y varianza, el valor del gradiente respecto a μ y tu explicación "
        "de los dos términos del ELBO.",
        "Ya se puede entrenar un modelo generativo latente, pero sus muestras son borrosas. La respuesta "
        "de 2014 fue radicalmente distinta: convertirlo en un juego.",
    ),
    "P39_gan": _auto(
        "gan",
        "Un falsificador y un policía que aprenden a la vez. El falsificador mejora porque el policía lo "
        "pilla; el policía mejora porque el falsificador se refina. Nadie le enseña al falsificador qué "
        "es un billete bueno: solo si coló o no.",
        "```text\nmin_G max_D  E_x[log D(x)] + E_z[log(1 − D(G(z)))]\n\n"
        "    D quiere acertar quién es real     → maximiza\n"
        "    G quiere que D se equivoque        → minimiza\n```\n\n"
        "No hay verosimilitud explícita: la señal de entrenamiento la produce **otra red**.",
        "1. ¿Tiene que cubrir el generador los tres modos de la distribución real para engañar al discriminador?\n"
        "2. ¿Qué pasará con la diversidad de sus muestras?\n"
        "3. ¿Cómo lo detectarías si solo miras muestras individuales?",
        "El generador converge a **un solo modo** de los tres. Y desde el punto de vista de su objetivo, "
        "hace bien: engañar al discriminador no exige cubrir la distribución, basta con ser convincente "
        "en una región. Eso es el colapso de modos.",
        "El colapso es difícil de detectar mirando muestras: cada una puede ser excelente. Hay que medir "
        "**cobertura**, no solo calidad. Es el mismo error que en RAG con las citas: la muestra individual "
        "se ve bien y el sistema está roto.",
        "Anti-patrón: evaluar un modelo generativo enseñando las mejores muestras.",
        "print('20 imagenes preciosas elegidas a mano NO son evidencia de nada.')\n"
        "print('Un generador colapsado produce muestras excelentes... todas parecidas.')\n"
        "print('Sin medida de cobertura/diversidad, la evaluacion es publicidad.')",
        "Lo mínimo que hay que reportar en un modelo generativo:",
        "reporte = {'calidad': 'metrica perceptual sobre muestras no elegidas',\n"
        "           'diversidad': 'cobertura de los modos de la distribucion real',\n"
        "           'muestras': 'aleatorias con semilla, no seleccionadas',\n"
        "           'estabilidad': 'varias semillas de entrenamiento, no una'}\n"
        "show(reporte)",
        "Cambia la posición inicial del generador y observa a qué modo colapsa: siempre al más cercano.",
        "Entrena una GAN pequeña sobre una mezcla de gaussianas 2D y mide cuántos modos cubre a lo largo "
        "del entrenamiento. Compara con un VAE y con difusión sobre los mismos datos.",
        "Guarda la trayectoria del generador, el conteo de modos cubiertos y tu lista de lo que hay que "
        "reportar en un modelo generativo.",
        "Generar ya es posible por dos vías. Ahora el andamiaje: qué hace que una red profunda se pueda "
        "entrenar sin memorizar.",
    ),
    "P40_dropout": _auto(
        "dropout",
        "Si en un equipo cada tarea depende de dos personas concretas, el día que una falte no se hace "
        "nada. Si todos pueden cubrir varias tareas, el equipo aguanta. Dropout obliga a lo segundo "
        "haciendo faltar a gente al azar cada día.",
        "```text\nEntrenamiento:  h̃ = h ⊙ m,   m ~ Bernoulli(1−p)\n"
        "Inferencia   :  se usan todas, escaladas por (1−p)\n\n"
        "Con n unidades hay 2ⁿ subredes posibles, todas compartiendo pesos.\n```",
        "1. ¿Con qué probabilidad están activas a la vez dos unidades concretas, si p=0,5?\n"
        "2. ¿Y al menos una de tres?\n"
        "3. ¿Qué tipo de representación premia eso?",
        "Una función que depende de dos unidades concretas solo está disponible una cuarta parte de las "
        "veces; una repartida entre tres, casi siempre. Dropout no «añade ruido»: **cambia qué "
        "representaciones son rentables**.",
        "Dropout dominó la regularización durante años y hoy se usa mucho menos en visión y en "
        "Transformers grandes, donde otras técnicas y la escala de datos cumplen ese papel. Es un buen "
        "recordatorio de que las recetas caducan.",
        "Anti-patrón: dejar dropout activo en inferencia.",
        "print('Con dropout activo en inferencia, la misma entrada da salidas distintas.')\n"
        "print('Y la magnitud de las activaciones es (1-p) veces la esperada.')\n"
        "print('Es un fallo clasico: el modelo \"funciona peor en produccion\" sin causa aparente.')",
        "La corrección es la escala, y el motivo es que la esperanza cuadre:",
        "p = 0.5\n"
        "print('en entrenamiento: se apaga la fraccion p, la suma esperada baja a (1-p) del total')\n"
        "print(f'en inferencia   : o se multiplica por (1-p)={1-p}, o se divide en entrenamiento')\n"
        "print('las dos convenciones existen; usar las dos a la vez rompe el modelo')",
        "Calcula la probabilidad de que una función que depende de 4 unidades concretas esté disponible.",
        "Entrena una red pequeña con y sin dropout sobre un conjunto con pocos datos. Compara la brecha "
        "entre error de entrenamiento y de validación, no solo el error final.",
        "Guarda las probabilidades de disponibilidad, el conteo de subredes y tu explicación del escalado "
        "en inferencia.",
        "La red ya no memoriza. Pero sigue siendo difícil de optimizar si cada dirección tiene una "
        "curvatura distinta.",
    ),
    "P41_adam": _auto(
        "adam",
        "Bajar un valle largo y estrecho: en la dirección estrecha, un paso normal te hace rebotar de "
        "pared a pared; en la larga, ese mismo paso no avanza nada. Adam mide cuánto se mueve cada "
        "dirección y ajusta su paso por separado.",
        "```text\nm_t = β₁·m_{t−1} + (1−β₁)·g          primer momento (dirección)\n"
        "v_t = β₂·v_{t−1} + (1−β₂)·g²         segundo momento (escala)\n"
        "m̂ = m_t/(1−β₁ᵗ),  v̂ = v_t/(1−β₂ᵗ)   corrección de sesgo\n"
        "θ ← θ − η · m̂ / (√v̂ + ε)\n```\n\n"
        "El paso efectivo de cada coordenada es ~η, independientemente de la escala de su gradiente.",
        "1. Con L = x² + 100y², ¿qué gradiente es mayor: el de x o el de y?\n"
        "2. ¿Qué le pasa a SGD con una tasa que sirva para x?\n"
        "3. ¿Y a Adam?",
        "SGD se queda con una pérdida enorme: con una tasa que sirva para la dirección plana, **oscila** "
        "en la empinada sin converger. Adam llega a ~1e-8 porque normaliza cada coordenada por su propia "
        "escala de gradiente.",
        "Adam es el optimizador por defecto de casi todo lo que estudias en este eje. Pero «por defecto» "
        "no es «siempre mejor»: hay trabajos que reportan mejor generalización con SGD con momento bien "
        "ajustado, sobre todo en visión.",
        "Anti-patrón: usar el decaimiento de pesos de SGD tal cual dentro de Adam.",
        "print('En SGD, weight decay equivale a sumar lambda*theta al gradiente.')\n"
        "print('En Adam ese termino se divide tambien por sqrt(v): la regularizacion')\n"
        "print('acaba siendo distinta por coordenada, que NO es lo que se queria.')\n"
        "print('AdamW (2017) lo corrige desacoplandolo del paso adaptativo.')",
        "Los tres componentes y qué aporta cada uno:",
        "componentes = {'primer momento': 'suaviza la direccion, como el momento clasico',\n"
        "               'segundo momento': 'normaliza por la escala tipica de cada coordenada',\n"
        "               'correccion de sesgo': 'evita pasos diminutos en las primeras iteraciones'}\n"
        "show(componentes)",
        "Sube el número de condición del problema a 10 000 y comprueba si Adam sigue convergiendo.",
        "Entrena la misma red con SGD, SGD+momento, Adam y AdamW sobre un conjunto pequeño. Compara "
        "curvas de entrenamiento **y** de validación: el mejor entrenamiento no siempre generaliza mejor.",
        "Guarda la comparación en el problema mal condicionado y tu explicación de por qué el decaimiento "
        "de pesos necesita tratamiento aparte.",
        "Ya se entrena estable y rápido. Toca la pregunta incómoda: ¿es robusto lo que se ha entrenado?",
    ),
    "P42_adversarial": _auto(
        "adversarial",
        "Cambia cada píxel de una foto en una milésima —invisible— pero **todos en la dirección que más "
        "confunde al modelo**. En una imagen con miles de píxeles, esas milésimas suman lo suficiente "
        "para cambiar la predicción.",
        "```text\nFGSM:  x' = x + ε · sign(∇ₓ L(θ, x, y))\n\n"
        "Para un modelo lineal wᵀx:\n"
        "    cambio = wᵀ(x' − x) = ε · Σᵢ |wᵢ|      ← crece con la DIMENSIÓN\n```",
        "1. Con ε=0,01, ¿cuánto cambia la salida en dimensión 10? ¿Y en 10 000?\n"
        "2. ¿Es un problema de la profundidad de la red?\n"
        "3. ¿Por qué la perturbación es imperceptible y el efecto no?",
        "El cambio crece proporcionalmente a la dimensión. Con 10 000 componentes y ε=0,01, la salida se "
        "mueve ~100 unidades. **La causa es la linealidad en alta dimensión**, no la complejidad del "
        "modelo — que es justo lo contrario de lo que se creía.",
        "El resultado más inquietante del paper no está en esta miniatura: los ejemplos adversarios "
        "**transfieren** entre modelos distintos entrenados con datos distintos. Eso significa que no son "
        "un bug de un modelo, sino una propiedad de los datos y de la clase de funciones.",
        "Anti-patrón: creer que un modelo con alta exactitud es un modelo robusto.",
        "print('Exactitud 99% en el conjunto de test ← distribucion natural')\n"
        "print('Exactitud  0% bajo perturbacion adversaria ← distribucion elegida por un atacante')\n"
        "print('Son dos metricas distintas, y la segunda casi nunca se reporta.')",
        "Lo que hay que medir si el modelo se despliega donde alguien puede atacarlo:",
        "evaluacion = {'exactitud_limpia': 'sobre el test estandar',\n"
        "              'exactitud_robusta': 'bajo ataque, con epsilon declarado',\n"
        "              'ataque_usado': 'FGSM, PGD, adaptativo... y sus parametros',\n"
        "              'transferencia': 'si el ataque generado en otro modelo tambien funciona'}\n"
        "show(evaluacion)",
        "Calcula qué ε hace falta en dimensión 784 (una imagen 28×28) para mover la salida 10 unidades.",
        "Implementa FGSM sobre un clasificador pequeño y mide la exactitud en función de ε. Después prueba "
        "entrenamiento adversario y comprueba cuánta exactitud limpia cuesta la robustez.",
        "Guarda la tabla de cambio frente a dimensión, y tu protocolo de evaluación con exactitud limpia "
        "y robusta por separado.",
        "La robustez es un problema abierto. Volvamos al entrenamiento: qué hace que una red profunda "
        "sea entrenable.",
    ),
    "P43_batchnorm": _auto(
        "batchnorm",
        "Una tubería de doce filtros donde cada uno amplifica un poco. Al final, la señal está saturada o "
        "extinguida. Normalizar entre etapas es reajustar el caudal para que cada filtro reciba lo que "
        "sabe procesar.",
        "```text\nx̂ = (x − μ_lote) / √(σ²_lote + ε)\n"
        "y  = γ·x̂ + β                    γ y β se APRENDEN\n```\n\n"
        "γ y β permiten deshacer la normalización si conviene: no se pierde capacidad expresiva.",
        "1. ¿Qué fracción de activaciones estará saturada en la capa 11 sin normalizar?\n"
        "2. ¿Y con normalización?\n"
        "3. ¿Por qué importa la saturación de tanh?",
        "Sin normalizar, casi todas las activaciones acaban en la zona plana de tanh, donde la derivada "
        "es prácticamente cero: **el gradiente no puede volver**. Con normalización, la desviación se "
        "mantiene cerca de 1 y las unidades siguen en su rango útil.",
        "La explicación del paper —«internal covariate shift»— fue **discutida después**. Hay evidencia "
        "de que el beneficio real viene de suavizar el paisaje de optimización. Es un caso didáctico "
        "excelente: la técnica funciona y su explicación original resultó incompleta.",
        "Anti-patrón: usar batch norm con lotes muy pequeños.",
        "for lote in (1, 2, 8, 64, 256):\n"
        "    error = 1 / (lote ** 0.5)\n"
        "    print(f'lote {lote:>3} → error relativo de la estadistica ~{error:.2f} '\n"
        "          f\"({'inutilizable' if lote < 8 else 'aceptable'})\")",
        "Por eso existen LayerNorm y GroupNorm, que no dependen del lote:",
        "variantes = {'BatchNorm': 'normaliza por LOTE — depende del tamano de lote',\n"
        "             'LayerNorm': 'normaliza por MUESTRA — la que usa el Transformer',\n"
        "             'GroupNorm': 'por grupos de canales — para lotes pequenos en vision'}\n"
        "show(variantes)",
        "Comprueba qué pasa con la desviación en la capa 11 si subes el peso de 1,6 a 2,5.",
        "Entrena una red profunda con y sin normalización, variando la tasa de aprendizaje en un rango "
        "amplio. Reporta el rango de tasas que converge en cada caso: ahí está el beneficio real.",
        "Guarda las trazas de media, desviación y saturación por capa, y tu comparación de las tres "
        "variantes de normalización.",
        "Con normalización se entrena más profundo. Pero pasado cierto punto, más capas volvían a "
        "empeorar — y no por sobreajuste.",
    ),
    "P44_resnet": _auto(
        "resnet",
        "Si una capa nueva no aporta, debería poder no hacer nada. Con capas normales, «no hacer nada» "
        "—la identidad— es sorprendentemente difícil de aprender. Con un atajo, es gratis: basta con que "
        "el bloque aprenda cero.",
        "```text\nBloque plano   :  y = F(x)          aprender la identidad es difícil\n"
        "Bloque residual:  y = F(x) + x      la identidad es F ≡ 0\n\n"
        "    ∂y/∂x = F'(x) + 1     ← el 1 sostiene el producto a través de las capas\n```",
        "1. ¿Qué gradiente queda tras 152 capas con un factor de 0,85 por capa?\n"
        "2. ¿Y con el atajo?\n"
        "3. ¿Por qué el paper llama «degradación» al problema y no «sobreajuste»?",
        "Sin atajo, el gradiente a 152 capas es del orden de 1e-11: la señal no llega. Con atajo se "
        "mantiene en un rango utilizable. La diferencia es de nueve órdenes de magnitud, y explica por "
        "qué de golpe se pudieron entrenar redes diez veces más profundas.",
        "La observación clave del paper es que el error de **entrenamiento** subía con la profundidad. "
        "Eso descarta el sobreajuste: no era falta de capacidad, era imposibilidad de optimizar. "
        "Distinguir ambas cosas es una habilidad diagnóstica que sirve para toda la vida.",
        "Anti-patrón: diagnosticar «sobreajuste» sin mirar el error de entrenamiento.",
        "casos = [('entrenamiento bajo, validacion alta', 'sobreajuste'),\n"
        "         ('entrenamiento ALTO, validacion alta', 'subajuste u optimizacion rota'),\n"
        "         ('entrenamiento sube al anadir capas', 'DEGRADACION: el caso de ResNet')]\n"
        "for sintoma, diagnostico in casos:\n"
        "    print(f'{sintoma:<40} → {diagnostico}')",
        "El mismo principio aditivo aparece en tres sitios de este eje:",
        "principio = {'LSTM (P03)': 'c_t = f*c_{t-1} + i*g — ruta aditiva en el TIEMPO',\n"
        "             'ResNet (P44)': 'y = F(x) + x — ruta aditiva en la PROFUNDIDAD',\n"
        "             'Transformer (P08)': 'LayerNorm(x + Sublayer(x)) — en cada subcapa'}\n"
        "show(principio)",
        "Calcula a partir de cuántas capas el gradiente sin atajo baja de 1e-6 con factor 0,85.",
        "Entrena dos redes de 30 capas, con y sin atajos, sobre un conjunto pequeño. Compara el error de "
        "**entrenamiento**: si el plano es peor, has reproducido la degradación.",
        "Guarda la tabla de gradientes por profundidad, la tabla de diagnóstico y tu explicación de por "
        "qué la identidad es difícil sin atajo.",
        "Ya se entrenan redes enormes. El problema pasa a ser el contrario: cómo servirlas sin arruinarse.",
    ),
    "P45_distillation": _auto(
        "distillation",
        "Un examen tipo test corregido solo con «bien/mal» enseña menos que uno donde el profesor te dice "
        "qué otras respuestas estuvieron cerca de ser correctas. Esa información extra es lo que el "
        "maestro le pasa al alumno.",
        "```text\nEtiqueta dura :  perro=1, lobo=0, gato=0, coche=0\n"
        "Objetivo suave:  perro=0.6, lobo=0.25, gato=0.13, coche=0.02   ← con temperatura T\n\n"
        "    p_i = softmax(z_i / T)      T alta → distribución más informativa\n```",
        "1. ¿Qué información contiene el objetivo suave que la etiqueta dura no?\n"
        "2. ¿Qué le pasa a la entropía al subir T?\n"
        "3. ¿Por qué eso ayuda a un modelo pequeño?",
        "El maestro dice que un perro se parece más a un lobo que a un gato, y muchísimo más que a un "
        "coche. Esa **estructura de similitud entre clases** es conocimiento que la etiqueta dura tira a "
        "la basura, y es lo que permite al alumno aprender con muchos menos datos.",
        "La destilación es hoy la razón de que existan modelos pequeños sorprendentemente buenos, "
        "incluidos los de razonamiento de [P22](../../papers/foundational/P22_deepseek_r1/README.md). "
        "El alumno hereda comportamiento — incluidos los errores del maestro.",
        "Anti-patrón: destilar de un maestro sin evaluar al maestro.",
        "print('El alumno aprende la distribucion del maestro, sesgos y errores incluidos.')\n"
        "print('Si el maestro confunde sistematicamente dos clases, el alumno lo heredara')\n"
        "print('y ademas con mas confianza, porque lo aprendio como objetivo suave.')",
        "Lo que hay que comprobar antes de destilar:",
        "checklist = {'maestro evaluado': 'en el mismo conjunto donde se medira al alumno',\n"
        "             'errores caracterizados': 'que clases confunde y con que frecuencia',\n"
        "             'temperatura': 'elegida en validacion, no copiada de un paper',\n"
        "             'alumno evaluado aparte': 'nunca solo contra el maestro'}\n"
        "show(checklist)",
        "Sube la temperatura a 20 y observa si la distribución sigue siendo informativa o se vuelve uniforme.",
        "Destila un modelo pequeño a partir de uno mayor en una tarea de clasificación. Compara con "
        "entrenar el pequeño solo con etiquetas duras, y mide también si hereda los errores del maestro.",
        "Guarda la tabla de distribuciones por temperatura, la entropía y tu checklist previo a destilar.",
        "Modelos pequeños que heredan capacidad. Ahora, un cambio de arquitectura que nadie esperaba en visión.",
    ),
    "P46_vit": _auto(
        "vit",
        "Trocea la imagen en cuadraditos, ponlos en fila y trátalos como si fueran palabras de una frase. "
        "Suena absurdo —se pierde toda la noción de vecindad— y funciona, si tienes datos suficientes.",
        "```text\nimagen 224×224  →  parches 16×16  →  (224/16)² = 196 tokens  (+1 de clase)\n\n"
        "cada parche: 16·16·3 = 768 valores → proyección lineal → token\n```\n\n"
        "A partir de ahí, es el encoder de [P08](../../papers/foundational/P08_transformer/README.md) "
        "sin ninguna modificación.",
        "1. ¿Cuántos tokens salen de una imagen 224×224 con parches de 16?\n"
        "2. ¿Qué pasa con el coste si bajas el parche a 8?\n"
        "3. ¿Qué sesgo inductivo pierde respecto a una CNN?",
        "Una imagen se convierte en una secuencia de ~200 tokens: exactamente el mismo problema que una "
        "frase. Y bajar el tamaño de parche multiplica el coste **al cuadrado**, porque la atención es "
        "cuadrática en el número de tokens.",
        "El resultado del paper viene con una condición grande: **funciona si se preentrena con muchísimos "
        "datos**. Con conjuntos medianos, la CNN gana, porque su sesgo inductivo vale más que la "
        "flexibilidad. Es un ejemplo limpio del compromiso sesgo/datos.",
        "Anti-patrón: citar ViT como «los Transformers superan a las CNN» sin la condición de datos.",
        "for datos in ('1M imagenes', '14M imagenes', '300M imagenes'):\n"
        "    ganador = 'CNN' if '1M' in datos else 'ViT' if '300M' in datos else 'depende'\n"
        "    print(f'preentrenado con {datos:<15} → suele ganar: {ganador}')",
        "El enunciado correcto incluye el régimen:",
        "enunciado = {'valido': 'con preentrenamiento a gran escala, ViT iguala o supera a CNN comparables',\n"
        "             'no_valido': 'los Transformers son mejores que las CNN en vision',\n"
        "             'razon': 'sin sesgo inductivo hace falta mas dato para aprender lo mismo',\n"
        "             'consecuencia': 'la eleccion depende de tu regimen de datos, no de la moda'}\n"
        "show(enunciado)",
        "Calcula los tokens y el coste relativo de una imagen 512×512 con parches de 8.",
        "Entrena un ViT pequeño y una CNN de parámetros comparables sobre un conjunto de 10 000 imágenes. "
        "Repite con aumento de datos agresivo y comprueba si la brecha se cierra.",
        "Guarda la tabla de tokens y coste, y tu enunciado con la condición de régimen de datos.",
        "El mismo bloque sirve para texto e imagen. Y también para problemas científicos que llevaban "
        "décadas abiertos.",
    ),
    "P47_alphafold": _auto(
        "alphafold",
        "Si sabes a qué distancia está cada par de puntos, la forma queda determinada. Predecir la "
        "estructura de una proteína se parece a reconstruir un objeto conociendo solo las distancias "
        "entre sus vértices.",
        "```text\nsecuencia de aminoácidos → (predicción) → distancias entre pares → geometría 3D\n\n"
        "Las distancias entre todos los pares determinan las coordenadas\n"
        "salvo rotación, traslación y reflexión.\n```",
        "1. Partiendo de posiciones aleatorias, ¿se puede recuperar la forma solo con las distancias?\n"
        "2. ¿Qué queda indeterminado?\n"
        "3. ¿Cuál es la parte verdaderamente difícil del problema real?",
        "Desde posiciones aleatorias y solo con la matriz de distancias, la geometría se recupera con "
        "error muy pequeño. Lo que queda indeterminado es la orientación: rotar o reflejar la estructura "
        "no cambia ninguna distancia.",
        "Ojo con lo que esta miniatura **no** hace: aquí la matriz de distancias se **da**. Predecirla a "
        "partir de la secuencia es el problema entero, y para eso AlphaFold usa alineamientos múltiples "
        "de secuencias evolutivas y atención sobre pares de residuos.",
        "Anti-patrón: contar AlphaFold como «la IA resolvió la biología».",
        "print('Resolvio con alta precision UN problema concreto: estructura desde secuencia.')\n"
        "print('No resuelve: funcion de la proteina, interacciones, dinamica, plegamiento in vivo,')\n"
        "print('complejos grandes, ni proteinas sin homologos conocidos.')",
        "Lo que sí cambió, que ya es enorme:",
        "impacto = {'antes': 'meses o anos de trabajo experimental por proteina',\n"
        "           'despues': 'prediccion en minutos, con estimacion de confianza por residuo',\n"
        "           'escala': 'base de datos abierta con cientos de millones de estructuras',\n"
        "           'leccion': 'la IA puede producir conocimiento cientifico, no solo productos'}\n"
        "show(impacto)",
        "Comprueba que la estructura recuperada tiene las mismas distancias aunque las coordenadas sean distintas.",
        "Reconstruye una estructura pequeña desde su matriz de distancias usando escalado multidimensional "
        "y compara con el descenso de gradiente. Mide el error con distintos niveles de ruido en las "
        "distancias: eso simula un predictor imperfecto.",
        "Guarda la curva de convergencia, el error medio por par y tu lista de lo que AlphaFold **no** resuelve.",
        "Modelos enormes con impacto real. Queda el problema práctico: adaptarlos sin poder permitirse "
        "reentrenarlos.",
    ),
    "P48_lora": _auto(
        "lora",
        "Para adaptar un modelo enorme a tu tarea no hace falta reescribirlo entero: basta con una nota "
        "al margen. LoRA aprende esa nota —pequeña— y deja el original intacto.",
        "```text\nAjuste completo:  W' = W_entrenada           d×d parámetros por matriz\n"
        "LoRA          :  W' = W + B·A               2·d·r parámetros,  r ≪ d\n\n"
        "    W congelada · B ∈ ℝ^{d×r} · A ∈ ℝ^{r×d}\n```\n\n"
        "Al desplegar, B·A se **suma** a W: no queda coste extra en inferencia.",
        "1. Con d=128 y r=4, ¿cuántos parámetros se entrenan frente al ajuste completo?\n"
        "2. ¿Cuántas copias del modelo hacen falta para diez tareas?\n"
        "3. ¿Qué coste añade en inferencia?",
        "Con rango 4 se entrena una fracción diminuta de los parámetros. Y como la matriz base queda "
        "congelada, **una sola copia del modelo sirve para todas las tareas**: cada una aporta solo su "
        "adaptador. En inferencia, cero coste añadido porque BA se fusiona con W.",
        "La hipótesis de fondo es empírica: que la actualización útil para adaptar un modelo es de rango "
        "bajo. No está garantizada para toda tarea, y elegir r y a qué matrices aplicarlo son decisiones "
        "que el paper estudia con ablaciones.",
        "Anti-patrón: subir r «por si acaso» hasta que deja de haber ahorro.",
        "d = 4096\n"
        "for r in (1, 8, 64, 512, 2048):\n"
        "    lora, completo = 2 * d * r, d * d\n"
        "    print(f'r={r:>4} → {lora:>10,} params ({lora/completo:>6.1%} del completo)'\n"
        "          + ('  ← ya no ahorra' if lora > completo * 0.5 else ''))",
        "El criterio correcto es empírico y barato de obtener:",
        "protocolo = {'1': 'empezar con r pequeno (4-16)',\n"
        "             '2': 'subir r solo si la metrica de validacion mejora',\n"
        "             '3': 'reportar r junto con el resultado, siempre',\n"
        "             '4': 'probar tambien a QUE matrices aplicarlo, no solo con que rango'}\n"
        "show(protocolo)",
        "Comprueba que una actualización de rango 2 se representa exactamente con r=2 y no con r=1.",
        "Ajusta un modelo abierto pequeño con LoRA a varios rangos sobre la misma tarea. Compara métrica, "
        "parámetros entrenados y tiempo. Localiza el rango donde deja de mejorar.",
        "Guarda la tabla de parámetros por rango, la forma de la actualización factorizada y tu protocolo "
        "de elección de r.",
        "Ya se adapta barato. Falta que el modelo base quepa en la máquina.",
    ),
    "P49_qlora": _auto(
        "quantization",
        "Guardar cada peso con menos decimales. Suena a pérdida garantizada, y lo es — pero mucho menor "
        "de lo que parece, porque los pesos se agrupan en un rango estrecho y no hace falta tanta "
        "precisión para distinguirlos.",
        "```text\n16 bits → 65 536 niveles      140 GB para un modelo de 70 000 M\n"
        " 4 bits →     16 niveles       35 GB para el mismo modelo\n\n"
        "QLoRA:  base cuantizada a 4 bits y CONGELADA + adaptadores LoRA en precisión alta\n```",
        "1. ¿Cuánta memoria ahorra pasar de 16 a 4 bits?\n"
        "2. ¿Qué le pasa al error de cuantización?\n"
        "3. ¿Por qué los adaptadores van en precisión alta?",
        "Pasar de 16 a 4 bits divide la memoria por cuatro, y el error de reconstrucción crece pero se "
        "mantiene pequeño frente a la escala de los pesos. Los adaptadores van en precisión alta porque "
        "son la parte que **se entrena**: ahí el gradiente sí necesita resolución.",
        "El error de reconstrucción de los pesos **no es** el error del modelo. Un modelo puede tolerar "
        "mucho ruido en pesos poco influyentes y muy poco en otros. Por eso la cuantización se valida "
        "midiendo calidad en tareas, nunca por el error numérico.",
        "Anti-patrón: elegir el número de bits mirando solo el error de reconstrucción.",
        "print('error de pesos bajo ≠ modelo igual de bueno')\n"
        "print('  · unos pocos pesos atipicos dominan el resultado y se cuantizan mal')\n"
        "print('  · la degradacion aparece en tareas concretas, no en la media')\n"
        "print('  · hay que medir en la tarea, no en la norma del error')",
        "El protocolo mínimo para aceptar una cuantización:",
        "protocolo = {'medir': 'la tarea real, no la perplejidad sola',\n"
        "             'comparar': 'contra el modelo sin cuantizar, mismo prompt y semilla',\n"
        "             'buscar': 'degradacion concentrada en casos raros, no solo la media',\n"
        "             'reportar': 'bits, formato, que capas se dejaron sin cuantizar'}\n"
        "show(protocolo)",
        "Calcula cuánta VRAM necesitas para un modelo de 70 000 M a 4, 8 y 16 bits, y con cuál cabe en 24 GB.",
        "Cuantiza un modelo abierto pequeño a 8 y 4 bits y compara su calidad en una tarea concreta, no "
        "solo la perplejidad. Busca casos donde la degradación sea desproporcionada.",
        "Guarda la tabla de bits, error y memoria, y tu protocolo de aceptación de una cuantización.",
        "El modelo ya cabe y se adapta barato. Queda decidir cuándo un modelo es **aceptable**.",
    ),
    "P50_constitutional_ai": _auto(
        "constitutional_ai",
        "En vez de que miles de personas señalen una por una qué respuestas les gustan, se escriben los "
        "principios y se le pide al modelo que critique y reescriba las suyas contra esa lista. Los "
        "criterios dejan de estar implícitos en los datos y pasan a poder discutirse.",
        "```text\nRLHF (P12):   preferencias humanas → modelo de recompensa → RL\n"
        "             criterios IMPLÍCITOS en los datos, no inspeccionables\n\n"
        "CAI       :   principios escritos → autocrítica → revisión → preferencias de IA → RL\n"
        "             criterios EXPLÍCITOS y auditables\n```",
        "1. ¿Cuántas etiquetas humanas nuevas hacen falta para la fase de crítica?\n"
        "2. ¿Qué gana la organización al escribir los principios?\n"
        "3. ¿Qué problema NO resuelve el método?",
        "La revisión se produce con **cero etiquetas humanas nuevas**, y contra una lista que cualquiera "
        "puede leer y objetar. Eso cambia la conversación: se discute sobre los principios, no sobre el "
        "resultado opaco de un modelo de recompensa.",
        "Y aquí está el límite honesto: **quién escribe los principios y con qué autoridad** es una "
        "pregunta política que el método no resuelve. Lo que hace es hacerla explícita, que ya es "
        "bastante más de lo que ofrecía RLHF.",
        "Anti-patrón: creer que los principios explícitos hacen el sistema objetivo.",
        "print('Explicito ≠ objetivo. Una constitucion es un conjunto de VALORES elegidos.')\n"
        "print('Lo que cambia es que ahora se pueden leer, criticar y versionar,')\n"
        "print('en vez de quedar sepultados en 100.000 comparaciones de anotadores.')",
        "Lo que aporta y lo que no:",
        "balance = {'aporta': ['criterios auditables', 'menos etiquetado humano',\n"
        "                       'menos exposicion de anotadores a contenido danino'],\n"
        "           'no_aporta': ['objetividad', 'legitimidad de quien escribe los principios',\n"
        "                          'garantia de que el modelo los aplique bien']}\n"
        "show(balance)",
        "Añade un cuarto principio contradictorio con otro y observa qué debería hacer el sistema.",
        "Escribe una constitución de cinco principios para un asistente de tu dominio. Genera 20 "
        "respuestas, critícalas contra ella y mide cuántas mejoran, cuántas empeoran y cuántas quedan "
        "igual. Documenta los conflictos entre principios.",
        "Guarda la traza de crítica y revisión, y tu balance de lo que el método aporta y lo que no.",
        "Ya hay criterios explícitos de comportamiento. Falta un criterio de **capacidad** que no se pueda "
        "convencer con prosa.",
    ),
    "P51_swebench": _auto(
        "swebench",
        "La pregunta no es si el código parece correcto. Es si, aplicado al repositorio real, los tests "
        "que ya existían pasan. Un test no se deja convencer.",
        "```text\nBenchmarks previos:  problema autocontenido → ¿la salida coincide?\n"
        "SWE-bench        :  incidencia REAL de un repo real\n"
        "                     → aplicar el parche generado\n"
        "                     → ejecutar los tests DEL PROPIO repositorio\n```",
        "1. ¿Qué proporción «parece correcta» en el ejemplo? ¿Y cuál pasa los tests?\n"
        "2. ¿Por qué es tan grande la diferencia?\n"
        "3. ¿Basta con que compile?",
        "Medido por apariencia el sistema resuelve mucho más que medido por tests. Esa brecha es el "
        "problema entero: **los criterios blandos inflan**, y en programación es especialmente fácil que "
        "algo parezca correcto y no lo sea.",
        "El propio benchmark tiene una debilidad conocida: las incidencias son públicas y anteriores al "
        "corte de datos de muchos modelos, así que hay riesgo de contaminación. Existen variantes "
        "verificadas y filtradas justamente por eso.",
        "Anti-patrón: reportar «resuelve el 60 %» sin decir con qué criterio.",
        "criterios = {'parece correcto': 'juicio humano rapido o de otro modelo',\n"
        "             'compila': 'necesario, muy lejos de suficiente',\n"
        "             'tests pasan': 'el criterio del benchmark',\n"
        "             'revision humana acepta': 'el criterio del mundo real, aun mas duro'}\n"
        "for k, v in criterios.items():\n"
        "    print(f'{k:<24} → {v}')",
        "Un reporte creíble nombra el criterio y las condiciones:",
        "reporte = {'criterio': 'tests del repositorio pasan',\n"
        "           'conjunto': 'que subconjunto y de que fecha',\n"
        "           'contaminacion': 'si se comprobo solapamiento con el corpus',\n"
        "           'coste': 'llamadas al modelo e intentos por incidencia',\n"
        "           'andamiaje': 'que agente/herramientas, no solo que modelo'}\n"
        "show(reporte)",
        "Calcula la tasa con cada criterio y ordénalos de más blando a más duro.",
        "Toma cinco incidencias cerradas de un repositorio propio, pide a un modelo que las resuelva y "
        "evalúa con los tests reales. Compara con tu impresión al leer el parche: mide tu propia brecha.",
        "Guarda la tabla de tasas por criterio y tu formato de reporte con criterio, contaminación y coste.",
        "Ya se puede medir capacidad con un criterio duro. Queda mirar dentro del modelo.",
    ),
    "P52_superposition": _auto(
        "superposition",
        "Ocho ejes y ochenta conceptos que guardar. No caben ortogonales, así que se colocan casi "
        "ortogonales y se aceptan pequeñas interferencias. Por eso al mirar una neurona se ven varios "
        "conceptos sin relación: no es un fallo, es la estrategia.",
        "```text\nSi n_características > n_dimensiones, no pueden ser todas ortogonales.\n\n"
        "En dimensión alta caben MUCHAS direcciones casi ortogonales:\n"
        "    solape medio pequeño, pero no cero → interferencia\n\n"
        "Consecuencia: una neurona responde a varios conceptos (polisemanticidad).\n```",
        "1. ¿Cuántos conceptos ortogonales caben en 8 dimensiones?\n"
        "2. ¿Y casi ortogonales?\n"
        "3. ¿Qué se paga por guardar más de los que caben?",
        "En 8 dimensiones caben 8 direcciones ortogonales, pero **80 casi ortogonales** con un solape "
        "medio pequeño. Se paga con interferencia: los conceptos se pisan un poco. El modelo acepta ese "
        "ruido a cambio de representar mucho más.",
        "Esto explica por qué la interpretabilidad neurona a neurona fracasó durante años: se buscaba "
        "una correspondencia que **no existe**. La unidad de significado no es la neurona, es una "
        "dirección en el espacio de activaciones — y por eso se usan autoencoders dispersos para buscarla.",
        "Anti-patrón: concluir que «la neurona 1 437 detecta perros».",
        "print('Una neurona puede activarse con perros, con texto en aleman y con codigo Python.')\n"
        "print('No es un fallo del modelo ni una casualidad: es superposicion.')\n"
        "print('Buscar significado NEURONA a neurona es buscar en la base equivocada.')",
        "Lo que sí se puede afirmar, y qué haría falta para más:",
        "afirmaciones = {'sostenible': 'esta DIRECCION del espacio se activa con este concepto',\n"
        "                'no_sostenible': 'esta NEURONA significa este concepto',\n"
        "                'siguiente_paso': 'comprobar causalidad interviniendo sobre la direccion',\n"
        "                'limite': 'que un autoencoder la encuentre no prueba que el modelo la USE'}\n"
        "show(afirmaciones)",
        "Comprueba cómo crece el solape máximo al pasar de 8 a 24 y a 80 conceptos en 8 dimensiones.",
        "Entrena un autoencoder disperso sobre las activaciones de una capa de un modelo abierto pequeño "
        "y examina las características que encuentra. Comprueba cuántas son interpretables y diseña una "
        "intervención para verificar que son causales.",
        "Guarda la tabla de solapes por número de conceptos y tu distinción entre lo que se puede afirmar "
        "sobre una dirección y sobre una neurona.",
        "Aquí termina la cadena que va del perceptrón a la interpretabilidad. Lo que sigue no avanza "
        "en el tiempo: vuelve al principio, a los cimientos del campo y a las dos tradiciones que "
        "el aprendizaje profundo dejó atrás sin resolver.",
    ),
})


SPECS.update({
    "P53_pca": _auto(
        "pca",
        "Una nube de puntos y la pregunta «¿cuál es la recta que mejor la resume?». Parece una sola "
        "pregunta y son tres, porque hay tres formas de medir la distancia de un punto a una recta: "
        "en vertical, en horizontal y por el camino más corto. Pearson toma la tercera.",
        "```text\nMínimos cuadrados de y sobre x : minimiza Σ (y − ŷ)²        ← error VERTICAL\n"
        "Mínimos cuadrados de x sobre y : minimiza Σ (x − x̂)²        ← error HORIZONTAL\n"
        "Eje principal (Pearson)        : minimiza Σ d⊥²             ← distancia PERPENDICULAR\n\n"
        "    dirección del eje: la del mayor autovalor de la matriz de covarianzas\n"
        "    tan(2θ) = 2·Sxy / (Sxx − Syy)\n```",
        "1. ¿Darán las tres rectas la misma pendiente?\n"
        "2. ¿Cuál tendrá el menor error vertical?\n"
        "3. ¿Cuál tendrá el menor error perpendicular?",
        "Tres pendientes distintas —0,7782, 0,9097 y 1,0956— para los **mismos** diez puntos. Cada recta "
        "gana en su propio criterio y pierde en el ajeno: no hay una «mejor», hay una mejor **para cada "
        "error**. El eje de Pearson queda siempre entre las dos rectas de mínimos cuadrados.",
        "Aquí nace la reducción de dimensionalidad. Si el primer eje explica el 92 % de la varianza, "
        "proyectar sobre él tira una dimensión y conserva casi toda la estructura. Eso es PCA, y es la "
        "misma idea que sostiene los espacios de representación de "
        "[P05](../../papers/foundational/P05_word2vec/README.md): direcciones que significan.",
        "Anti-patrón: leer la pendiente de mínimos cuadrados como «la relación» entre dos variables "
        "simétricas.",
        "r = run_paper_lab('pca', seed=7)['result']['rectas']\n"
        "print('y sobre x :', r['minimos_cuadrados_y_sobre_x']['pendiente'])\n"
        "print('x sobre y :', r['minimos_cuadrados_x_sobre_y']['pendiente'])\n"
        "print('Las dos describen LA MISMA nube y no coinciden.')\n"
        "print('Elegir una sin justificar el criterio es una decision oculta.')",
        "La versión que no privilegia ninguna variable, y el precio que paga:",
        "r = run_paper_lab('pca', seed=7)['result']\n"
        "eje = r['rectas']['eje_principal_pearson']\n"
        "ols = r['rectas']['minimos_cuadrados_y_sobre_x']\n"
        "print('eje principal  -> perpendicular', eje['error_perpendicular'], '| vertical', eje['error_vertical'])\n"
        "print('minimos cuadr. -> perpendicular', ols['error_perpendicular'], '| vertical', ols['error_vertical'])\n"
        "print('Cada una gana en SU criterio. Eso no es un empate: es que la pregunta estaba incompleta.')",
        "Comprueba con el resultado del motor que el eje principal queda entre las dos rectas de mínimos "
        "cuadrados en las 50 nubes perturbadas, y explica por qué eso tiene que pasar siempre.",
        "Implementa PCA sobre un conjunto de datos real de más de dos dimensiones, proyecta a dos "
        "componentes y comprueba cuánta varianza conservas. Después escala las variables a media 0 y "
        "desviación 1 y repite: si el resultado cambia mucho, explica por qué.",
        "Guarda la tabla de las tres pendientes con sus dos errores y tu enunciado de qué criterio "
        "minimiza cada recta.",
        "Ya hay una forma de resumir datos con geometría. Falta una forma de calcular con ellos: la "
        "siguiente ficha reduce la neurona a una operación de umbral y demuestra que con eso basta para "
        "hacer lógica.",
    ),
    "P54_mcculloch_pitts": _auto(
        "mcculloch_pitts",
        "Una neurona que suma lo que le llega y se dispara si pasa de un umbral. Nada más. La sorpresa "
        "de 1943 no es que se parezca a una neurona real —no se parece—, sino que con esa pieza tan "
        "pobre se puede construir cualquier circuito lógico.",
        "```text\nsalida = 1  si  Σ wᵢ·xᵢ ≥ θ     y  ninguna entrada inhibitoria está activa\nsalida = 0  en otro caso\n\n"
        "    AND  : w = (1, 1),  θ = 2\n"
        "    OR   : w = (1, 1),  θ = 1\n"
        "    NAND : w = (−1, −1), θ = −1\n"
        "    XOR  : NO EXISTE con una sola unidad\n```",
        "1. ¿Cuántas de las 175 configuraciones probadas calculan AND?\n"
        "2. ¿Y cuántas calculan XOR?\n"
        "3. ¿Cuántos parámetros aprende esta neurona?",
        "AND sale con 4 configuraciones y OR con 5; XOR con **ninguna** de las 175. Con dos capas —OR y "
        "NAND por debajo, AND por encima— XOR aparece exacto. Y el contador de parámetros aprendidos "
        "marca 0: aquí los pesos se ponen a mano.",
        "Esta ficha y la del perceptrón se confunden constantemente. McCulloch y Pitts responden «¿qué "
        "puede CALCULAR una red de neuronas?»; Rosenblatt, quince años después en "
        "[P01](../../papers/foundational/P01_perceptron/README.md), responde «¿puede APRENDER sus propios "
        "pesos?». Son dos preguntas distintas y el orden importa.",
        "Anti-patrón: contar el resultado de 1943 como un límite del conexionismo.",
        "print('El paper NO dice que las redes no puedan hacer XOR.')\n"
        "print('Dice que UNA unidad de umbral no puede, y que una RED si.')\n"
        "print('El limite de 1969 (Minsky y Papert) es sobre el perceptron de UNA capa y su APRENDIZAJE.')",
        "La versión precisa, comprobada con la salida del motor:",
        "r = run_paper_lab('mcculloch_pitts', seed=7)['result']\n"
        "print('XOR con una unidad :', r['xor_con_una_unidad'], 'configuraciones')\n"
        "print('XOR con dos capas  :', r['xor_con_dos_capas']['obtenido'])\n"
        "print('parametros aprendidos:', r['parametros_aprendidos'])\n"
        "print('Conclusion: es un resultado de COMPUTABILIDAD, no de aprendizaje.')",
        "Diseña a mano los pesos y el umbral de una unidad que implemente «x AND NOT y» y compruébalos "
        "contra la salida `inhibicion_x_and_not_y` del motor.",
        "Construye con unidades de umbral un sumador binario de un bit (suma y acarreo) y comprueba las "
        "cuatro filas de su tabla de verdad. Después cuenta cuántas unidades te hicieron falta y compara "
        "con la profundidad mínima teórica.",
        "Guarda la tabla de cuántas configuraciones resuelven cada función booleana y tu explicación de "
        "por qué XOR necesita dos capas.",
        "La neurona ya calcula, pero alguien tiene que poner los pesos. Antes de que aparezca el "
        "aprendizaje hace falta una forma de medir cuánta información hay en un mensaje: eso es lo "
        "siguiente.",
    ),
    "P55_shannon": _auto(
        "shannon",
        "Si sabes qué va a pasar, que pase no te informa de nada. La información es la sorpresa, y la "
        "sorpresa media de una fuente tiene un nombre —entropía— y una unidad —el bit—. Todo lo demás "
        "sale de ahí: cuánto se puede comprimir y cuánto se puede transmitir.",
        "```text\nH(X) = − Σ p(x) · log₂ p(x)        ← bits de sorpresa media por símbolo\n\n"
        "Teorema de codificación de fuente:   H ≤ L < H + 1\n"
        "    L = longitud media del mejor código por símbolo\n\n"
        "Canal binario simétrico con error p: C = 1 − H(p)   bits por uso\n```",
        "1. ¿Cuál será la entropía de una fuente con cuatro símbolos equiprobables?\n"
        "2. ¿Se podrá comprimir esa fuente por debajo de 2 bits por símbolo?\n"
        "3. ¿Y una fuente que emite «A» el 97 % de las veces?",
        "La fuente uniforme mide 2 bits exactos y su mejor código también: no hay nada que comprimir. La "
        "sesgada baja a 1,319 bits y su código a 1,45 —un 27,5 % de ahorro—, y la casi determinista a "
        "0,2419 bits. En las tres se cumple `H ≤ L < H+1`: la cota se toca, no se cruza.",
        "Todo el aprendizaje automático moderno vive dentro de esta ecuación. La entropía cruzada que "
        "minimiza un clasificador es esta misma cantidad; la perplejidad de un modelo de lenguaje es su "
        "exponencial. Cuando [P19](../../papers/foundational/P19_scaling_laws/README.md) habla de pérdida, "
        "habla de bits.",
        "Anti-patrón: leer «información» como «contenido útil» o «significado».",
        "print('Un texto en un idioma que no entiendes tiene ALTA entropia para ti.')\n"
        "print('Una demostracion matematica correcta puede tener entropia BAJA.')\n"
        "print('La teoria mide sorpresa, no valor. Shannon lo advierte en la primera pagina.')",
        "Qué mide y qué no, con los números del motor:",
        "r = run_paper_lab('shannon', seed=7)['result']\n"
        "for f in r['fuentes']:\n"
        "    print(f\"{f['fuente']:<18} H = {f['entropia_bits']:>6} bits | codigo medio = {f['longitud_media_huffman']}\")\n"
        "print('Ninguna fila habla de lo que los mensajes SIGNIFICAN.')",
        "Comprueba en la salida que ninguna fuente viola `H ≤ L`, y explica por qué la fuente uniforme no "
        "consigue ningún ahorro sobre el código de longitud fija.",
        "Toma un texto real de unos miles de caracteres, estima la entropía por carácter y compárala con "
        "la entropía condicionada al carácter anterior. Explica qué parte del ahorro viene de la "
        "frecuencia y qué parte de la dependencia.",
        "Guarda la tabla de las tres fuentes con entropía, longitud de código y ahorro, y tu explicación "
        "de por qué la cota no se puede cruzar.",
        "Ya se puede medir la información. La pregunta siguiente es más incómoda y no se deja medir "
        "igual: qué significaría que una máquina piense.",
    ),
    "P56_turing": _auto(
        "turing",
        "Turing no responde «¿pueden pensar las máquinas?». Declara que la pregunta está mal planteada y "
        "propone otra que sí se puede ejecutar: si un interrogador conversa por escrito con una persona "
        "y con una máquina y no las distingue, ¿qué queda de la pregunta original?",
        "```text\nJuego de imitación:\n"
        "    interrogador  ──preguntas escritas──▶  A (máquina)  y  B (persona)\n"
        "    objetivo del interrogador: decidir cuál es cuál\n\n"
        "No hay fórmula. Hay un PROTOCOLO, y su poder depende de las preguntas que se hagan.\n```",
        "1. ¿Pasará la misma máquina el test con los dos protocolos?\n"
        "2. ¿Qué tipo de pregunta obliga a un compromiso verificable?\n"
        "3. ¿Qué mide entonces el test?",
        "La **misma** máquina pasa con el juez ingenuo y no pasa con el protocolo completo. De siete "
        "preguntas, solo cuatro obligan a algo comprobable: aritmética, memoria entre turnos, producción "
        "sostenida y coherencia con lo ya dicho. El resultado del test es una propiedad del interrogatorio.",
        "Setenta y cinco años después, la lectura útil no es «¿ya lo pasó alguien?» sino la advertencia "
        "metodológica: una evaluación conversacional mide tanto al evaluador como al evaluado. Es "
        "exactamente el problema que [P62](../../papers/foundational/P62_benchmark_validez/README.md) "
        "formaliza como validez de constructo.",
        "Anti-patrón: anunciar que un sistema «superó el test de Turing».",
        "print('El paper no define un umbral de aprobado universal.')\n"
        "print('Turing estima 70% de aciertos del juez tras 5 minutos, con maquinas de 10^9 bits.')\n"
        "print('Sin protocolo, jueces y duracion, la frase no significa nada comprobable.')",
        "Lo que sí se puede afirmar, y con qué condiciones:",
        "r = run_paper_lab('turing', seed=7)['result']\n"
        "for nombre, p in r['protocolos'].items():\n"
        "    print(f\"{nombre:<16} preguntas {p['preguntas_formuladas']} | discriminan {p['preguntas_que_discriminan']} | {p['veredicto']}\")\n"
        "print('La maquina es la misma en las dos filas.')",
        "Añade a la lista una pregunta propia y clasifícala: ¿discrimina o no? Justifica qué compromiso "
        "verificable exige.",
        "Diseña un protocolo de diez preguntas para distinguir un modelo de lenguaje actual de una "
        "persona, ejecútalo y documenta cuáles funcionaron. Después analiza cuáles de tus preguntas "
        "medían capacidad y cuáles solo medían estilo.",
        "Guarda la comparación de los dos protocolos sobre la misma máquina y tu definición de qué es una "
        "pregunta que discrimina.",
        "La pregunta ya tiene forma operativa. Falta que alguien convierta eso en un programa de "
        "investigación con nombre propio: ocurre cinco años después, en Dartmouth.",
    ),
    "P57_dartmouth": _auto(
        "dartmouth",
        "Diez personas, dos meses de verano y una lista de siete problemas. La propuesta de 1955 no trae "
        "resultados: trae un nombre —«inteligencia artificial»— y una agenda. Setenta años después, seis "
        "de esos siete temas tienen respuesta y uno sigue abierto.",
        "```text\nLos siete temas propuestos en 1955:\n"
        "    1. computadoras automáticas          5. automejora\n"
        "    2. usar lenguaje                     6. abstracciones\n"
        "    3. redes de neuronas                 7. aleatoriedad y creatividad\n"
        "    4. teoría del tamaño de un cálculo\n\n"
        "Conjetura fundacional: todo aspecto del aprendizaje puede describirse con\n"
        "precisión suficiente para que una máquina lo simule.\n```",
        "1. ¿Cuántos años tardó de media cada tema en tener un resultado sólido?\n"
        "2. ¿Cuál tardó más?\n"
        "3. ¿Cuál sigue abierto?",
        "La media es de 25,5 años frente a los dos meses previstos. El que más tardó es el lenguaje: 62 "
        "años hasta el Transformer. Y el que sigue abierto es la **automejora**, que es justamente lo que "
        "hoy se discute en los agentes que se corrigen a sí mismos.",
        "Este es el documento que hay que tener a mano cada vez que alguien anuncia un plazo. No porque "
        "sus autores fueran ingenuos —eran de los mejores del campo— sino porque el error de estimación "
        "en IA es estructural: se subestima lo que parece fácil para una persona.",
        "Anti-patrón: tratar la propuesta como un paper con resultados.",
        "print('No hay experimentos, ni datos, ni evaluacion: es una solicitud de financiacion.')\n"
        "print('Pedian 13.500 dolares. Citarla como evidencia de algo es un error de categoria.')\n"
        "print('Su valor es historico y programatico, no empirico.')",
        "Lo que sí aporta el documento:",
        "r = run_paper_lab('dartmouth', seed=7)['result']\n"
        "print('temas propuestos      :', len(r['temas']))\n"
        "print('con resultado solido  :', r['temas_con_resultado_solido'])\n"
        "print('abiertos              :', r['temas_abiertos'])\n"
        "print('media de anios        :', r['media_de_anios_hasta_el_resultado'])\n"
        "print('aporta un NOMBRE y una AGENDA, no un metodo.')",
        "Discute la columna `anio_resultado`: elige un tema y argumenta una fecha distinta a la del motor. "
        "Cualquier fecha defendible sirve si viene con criterio.",
        "Escribe la propuesta de Dartmouth para 2026: siete problemas abiertos, con criterio explícito de "
        "qué contaría como resuelto. Después busca en el temario del programa dónde vive cada uno.",
        "Guarda la tabla de los siete temas con su año de resolución y tu argumento sobre el tema que "
        "sigue abierto.",
        "El campo ya tiene nombre y agenda. Veinte años después, dos de sus fundadores enuncian qué han "
        "aprendido: que todo se reduce a símbolos y a búsqueda.",
    ),
    "P58_simbolos_y_busqueda": _auto(
        "simbolos_y_busqueda",
        "La conferencia del premio Turing de 1976 resume veinte años en dos frases. La primera: pensar es "
        "manipular símbolos. La segunda: resolver problemas es buscar en un espacio de estados, y lo que "
        "hace viable esa búsqueda no es la potencia de cálculo sino saber **dónde no mirar**.",
        "```text\nHipótesis del sistema de símbolos físicos:\n"
        "    símbolos + estructuras + procesos = medios necesarios y suficientes\n"
        "    para la acción inteligente general\n\n"
        "Hipótesis de la búsqueda heurística:\n"
        "    resolver = generar y probar caminos en un espacio de estados,\n"
        "    guiados por información sobre el problema\n\n"
        "Coste de la búsqueda ciega: b^d      ← el muro\n```",
        "1. ¿Cuántos nodos expandirá la búsqueda ciega en el 8-puzzle?\n"
        "2. ¿Y la guiada por distancia Manhattan?\n"
        "3. ¿Encuentran ambas una solución?",
        "La ciega expande 83 nodos y la heurística 7: una razón de 11,86× sobre el **mismo** problema, el "
        "mismo espacio y los mismos operadores. Lo único que cambia es el orden en que se miran los "
        "estados. Y con ramificación 2,7 a profundidad 20 la búsqueda exhaustiva pediría 423 millones de "
        "nodos: ningún hardware cierra ese hueco.",
        "Esta es la raíz de la que sale todo lo demás. La búsqueda en árbol de "
        "[AlphaGo](../../papers/foundational/P27_alphago/README.md) es esta idea con una red que aporta la "
        "heurística; el bucle de [ReAct](../../papers/foundational/P13_react/README.md) es esta idea con un "
        "modelo de lenguaje generando los operadores. Cambia quién propone: no cambia la estructura.",
        "Anti-patrón: leer la hipótesis de los símbolos como un hecho establecido.",
        "print('Es una HIPOTESIS EMPIRICA, y Newell y Simon la presentan asi.')\n"
        "print('La robotica situada (Brooks, 1990) la niega: hay competencia sin representacion simbolica.')\n"
        "print('El aprendizaje profundo la esquiva: representaciones distribuidas, no simbolos discretos.')",
        "Lo que la miniatura sí demuestra:",
        "r = run_paper_lab('simbolos_y_busqueda', seed=7)['result']\n"
        "print('ciega     :', r['busqueda_ciega'])\n"
        "print('heuristica:', r['busqueda_heuristica'])\n"
        "print('razon     :', r['razon_de_nodos'], 'x menos nodos con la MISMA formulacion del problema')",
        "Cambia mentalmente la heurística por una constante (h = 0 para todo estado) y predice qué "
        "búsqueda obtienes. Comprueba tu predicción razonando sobre el código del motor.",
        "Implementa el 8-puzzle con una heurística peor (número de fichas mal colocadas) y compara nodos "
        "expandidos con la distancia Manhattan. Después construye una heurística **no admisible** y "
        "comprueba qué pasa con la longitud de la solución encontrada.",
        "Guarda la comparación de nodos expandidos y tu explicación de por qué la heurística no cambia el "
        "problema sino el orden de exploración.",
        "La búsqueda ya tiene guía, pero nadie ha dicho todavía qué es exactamente el sistema que busca. "
        "Esa definición llega en los noventa, con el vocabulario de los agentes.",
    ),
    "P59_agente_racional": _auto(
        "agente_racional",
        "Dos aspiradoras en un mundo de dos casillas. Una reacciona a lo que ve; la otra recuerda dónde "
        "ha estado. Con una medida de desempeño las dos empatan. Con otra, una gana y la otra pierde. "
        "Nada cambió en los agentes: cambió lo que decidimos contar.",
        "```text\nagente = f(secuencia de percepciones) → acción\n\n"
        "racional ≠ omnisciente ≠ perfecto\n"
        "racional = maximiza la MEDIDA DE DESEMPEÑO esperada,\n"
        "           dado lo que ha percibido y lo que sabe\n\n"
        "El diseño se especifica con cuatro cosas: medida, entorno, actuadores y sensores.\n```",
        "1. ¿Qué agente gana si la medida solo cuenta casillas limpias?\n"
        "2. ¿Y si además penaliza cada movimiento?\n"
        "3. ¿Por qué el agente reflejo no puede parar?",
        "Con la medida A los dos empatan a 8. Con la medida B el reflejo cae a −2,0 y el que tiene modelo "
        "sube a 6,0. El reflejo no puede parar porque no recuerda haber visto ya las dos casillas limpias: "
        "su límite no está en la decisión, está en la **percepción**.",
        "De aquí sale la disciplina de escribir la medida de desempeño antes que el agente. Es el mismo "
        "error que reaparece treinta años después en los agentes con modelos de lenguaje: se construye el "
        "bucle y luego se discute qué contaba como éxito. "
        "[P16](../../papers/foundational/P16_agentic_systems/README.md) lo llama presupuesto y criterio de "
        "parada; aquí ya se llamaba medida de desempeño.",
        "Anti-patrón: evaluar «lo que el agente hace» en lugar de «lo que consigue en su entorno».",
        "print('Aspirar mucho no es limpiar bien: un agente que ensucia y limpia puntua alto por accion.')\n"
        "print('La medida tiene que estar sobre el ESTADO DEL ENTORNO, no sobre la actividad del agente.')\n"
        "print('Es el error clasico y el mas caro de descubrir tarde.')",
        "La comparación correcta, con las dos medidas sobre los mismos agentes:",
        "r = run_paper_lab('agente_racional', seed=7)['result']\n"
        "for nombre, a in r['agentes'].items():\n"
        "    print(f\"{nombre:<16} medida A = {a['medida_A_solo_limpieza']:>4} | medida B = {a['medida_B_limpieza_menos_coste']:>5}\")\n"
        "print('mismo codigo, misma ejecucion, distinto veredicto.')",
        "Define una tercera medida que penalice también las aspiraciones innecesarias y decide, con los "
        "datos del motor, qué agente ganaría.",
        "Especifica con las cuatro dimensiones (medida, entorno, actuadores, sensores) un agente para una "
        "tarea de tu trabajo. Después construye dos versiones —una reactiva y una con estado— y compara "
        "bajo dos medidas distintas.",
        "Guarda la tabla de los dos agentes bajo las dos medidas y tu definición operativa de "
        "racionalidad.",
        "Ya se sabe qué es un agente y cómo juzgarlo. Queda la pregunta que atraviesa todo el programa: "
        "cómo se juzga si un resultado publicado es cierto.",
    ),
    "P60_valor_predictivo": _auto(
        "valor_predictivo",
        "Un resultado con p < 0,05 no tiene un 95 % de probabilidades de ser cierto. Esa probabilidad "
        "depende de cuántas hipótesis falsas se estaban probando, de cuánto poder tenía el estudio y de "
        "cuánta gente estaba compitiendo por publicarlo primero. Ioannidis le pone fórmula.",
        "```text\nR   = odds previas de que la hipótesis sea cierta\n"
        "1−β = poder estadístico            α = nivel de significancia\n\n"
        "        PPV = (1−β)·R / (R − β·R + α)\n\n"
        "Con sesgo u:   PPV = [(1−β)R + u·β·R] / [R + α − β·R + u − u·α + u·β·R]\n"
        "Con n equipos: PPV = (R − R·βⁿ) / (R + 1 − (1−α)ⁿ − R·βⁿ)\n```",
        "1. ¿Qué PPV tiene un exploratorio con poder 0,5 y odds previas 1:10?\n"
        "2. ¿Qué le pasa si añadimos un 30 % de sesgo?\n"
        "3. ¿Y si hay cinco equipos compitiendo?",
        "El exploratorio típico da PPV = 0,5: la mitad de esos hallazgos son falsos **antes** de contar el "
        "sesgo. Con un 30 % de sesgo cae a 0,1625, y con cinco equipos en carrera, a 0,2998. En un barrido "
        "masivo sin corrección el PPV es 0,0044.",
        "Trasladado a la IA, las variables cambian de nombre pero no de papel: las odds previas son cuán "
        "plausible era la mejora, el poder es cuántas semillas y cuántos conjuntos se probaron, y el sesgo "
        "es la libertad para elegir la comparación favorable. "
        "[P63](../../papers/foundational/P63_reproducibilidad/README.md) ataca justamente ese sesgo.",
        "Anti-patrón: leer el valor p como «probabilidad de que la hipótesis sea falsa».",
        "print('p = P(dato tan extremo | hipotesis nula cierta)')\n"
        "print('lo que se quiere es P(hipotesis cierta | dato)')\n"
        "print('Para pasar de uno a otro hacen falta las odds previas. El valor p solo NO basta.')",
        "La cuenta correcta, con los escenarios del motor:",
        "r = run_paper_lab('valor_predictivo', seed=7)['result']\n"
        "for e in r['escenarios']:\n"
        "    print(f\"{e['caso']:<38} PPV = {e['ppv']:<7} falso = {e['probabilidad_de_ser_falso']}\")\n"
        "print('mismo alfa = 0,05 en todas las filas.')",
        "Localiza en la tabla `efecto_del_poder_con_R_0_1` cuánto sube el PPV al pasar el poder de 0,2 a "
        "0,95, y explica por qué el poder importa más que el umbral de significancia.",
        "Aplica el modelo a un anuncio reciente de mejora en un benchmark de IA: estima R, poder, sesgo y "
        "número de equipos, calcula el PPV y documenta cada supuesto. El ejercicio no es acertar el "
        "número: es hacer explícitos los supuestos.",
        "Guarda la tabla de escenarios con su PPV y tu explicación de la diferencia entre α y P(hipótesis "
        "| dato).",
        "Ya hay un modelo de por qué se publican cosas falsas. Falta el otro filo del mismo problema: qué "
        "pasa cuando lo que se publica es cierto pero el corpus con el que se entrenó no representa a "
        "quien lo va a usar.",
    ),
    "P61_stochastic_parrots": _auto(
        "stochastic_parrots",
        "Un corpus «de toda la web» no es un espejo del mundo: es un espejo de quién publica en la web. Y "
        "cuando se limpia con una lista de palabras prohibidas, el filtro no cae por igual sobre todos —"
        "cae más fuerte sobre las comunidades que reapropian los términos que la lista bloquea.",
        "```text\nAntes del filtro:  mayoritaria 94,0 %  ·  minoritaria_A 4,0 %  ·  minoritaria_B 2,0 %\n"
        "Filtro por lista:  retira 1,3 %          ·  retira 47,5 %          ·  retira 15,0 %\n"
        "Después:           96,07 %               ·  2,17 %                ·  1,76 %\n\n"
        "El filtro se aplica igual a todos y NO afecta igual a todos.\n```",
        "1. ¿Qué porcentaje pierde cada comunidad con el mismo filtro?\n"
        "2. ¿Sube o baja la cuota de la mayoritaria tras «limpiar»?\n"
        "3. ¿Qué verá quien audite el corpus con una muestra de 20 documentos?",
        "La comunidad minoritaria A pierde el 47,5 % y la mayoritaria el 1,3 %. Tras filtrar, la cuota de "
        "la mayoritaria **sube** 2,07 puntos: una operación presentada como higiene técnica redistribuye "
        "quién está representado. Y una muestra de 20 documentos contiene 20 de la mayoritaria: quien "
        "audite así no verá siquiera que existen las otras.",
        "El artículo se cita mucho y se lee poco. Su argumento no es «los modelos grandes son malos», sino "
        "que tres costes —ambiental, de representación y de atribución de comprensión— no aparecen en "
        "ninguna tabla de resultados. Documentar el corpus antes de entrenar es la propuesta concreta, y "
        "es la que menos se ha adoptado.",
        "Anti-patrón: leer «loro estocástico» como un insulto o como una tesis sobre capacidades.",
        "print('La tesis es linguistica: el modelo ordena FORMAS por probabilidad.')\n"
        "print('No es una prediccion sobre que tareas podra resolver ni sobre su techo.')\n"
        "print('Confundir las dos cosas convierte un argumento discutible en un eslogan.')",
        "Lo que el artículo sí sostiene, separado de lo que no:",
        "afirmaciones = {'sostiene': 'un corpus grande por conveniencia no es representativo',\n"
        "                'sostiene_2': 'el filtrado por lista silencia a quien reapropia terminos',\n"
        "                'sostiene_3': 'el coste de entrenar no aparece en la tabla de resultados',\n"
        "                'no_sostiene': 'que exista un techo de capacidades demostrado'}\n"
        "show(afirmaciones)",
        "Calcula con los datos del motor cuántos puntos de cuota gana la comunidad mayoritaria y explica "
        "por qué una operación «neutral» puede tener un efecto que no lo es.",
        "Toma un conjunto de datos que uses y escríbele una hoja de datos: de dónde viene, qué "
        "poblaciones representa, qué filtros se le aplicaron y a quién dejaron fuera. Después estima qué "
        "decisiones de tu sistema cambiarían si esa composición fuese otra.",
        "Guarda la tabla de cuotas antes y después del filtro y tu separación entre lo que el artículo "
        "sostiene y lo que se le atribuye.",
        "Si el corpus condiciona lo que un modelo puede decir, la siguiente pregunta es qué condiciona lo "
        "que un benchmark puede medir.",
    ),
    "P62_benchmark_validez": _auto(
        "benchmark_validez",
        "Un benchmark que se llama «comprensión» promete medir comprensión. Pero sus ítems miden lo que "
        "miden, y si existe un atajo —responder siempre la opción más larga— el ranking mide el atajo. "
        "El problema no es la métrica: es la distancia entre lo medido y lo afirmado.",
        "```text\nValidez de constructo:  ¿la tarea medida ES la capacidad nombrada?\n\n"
        "    capacidad declarada : «comprensión de lenguaje natural»\n"
        "    subhabilidades      : 6 declaradas\n"
        "    subhabilidades medidas: 2\n"
        "    estrategia sin comprensión: 11/12 aciertos\n\n"
        "Un número alto es compatible con no tener la capacidad.\n```",
        "1. ¿Cuánto acierta una regla que ignora el contenido del ítem?\n"
        "2. ¿Cuántas de las seis subhabilidades declaradas se evalúan?\n"
        "3. ¿Qué mide entonces el ranking?",
        "La regla «responder siempre la opción más larga» acierta 11 de 12, frente a los 3 de 12 del azar. "
        "Y de las seis subhabilidades declaradas solo se evalúan dos. El ranking mide el atajo y la "
        "etiqueta promete un constructo que los ítems no cubren.",
        "Esta es la ficha que convierte el escepticismo en método. Antes de creer una tabla comparativa: "
        "mirar los ítems, buscar el atajo y comprobar la cobertura. "
        "[SWE-bench](../../papers/foundational/P51_swebench/README.md) es interesante justamente porque "
        "reduce el hueco —los tests del repositorio son difíciles de fingir—, no porque sea un benchmark "
        "más grande.",
        "Anti-patrón: comparar dos modelos por su puntuación sin haber mirado un solo ítem.",
        "print('Un ranking es una medida CON un instrumento, no una propiedad del modelo.')\n"
        "print('Si el instrumento admite atajos, la puntuacion mide el atajo.')\n"
        "print('Y si el conjunto de test se filtro al entrenamiento, no mide nada.')",
        "El procedimiento mínimo antes de citar un número:",
        "r = run_paper_lab('benchmark_validez', seed=7)['result']\n"
        "print('cobertura declarada vs real :', r['cobertura'])\n"
        "print('atajo sin capacidad         :', r['modelo_atajo']['aciertos'])\n"
        "print('azar                        :', r['modelo_al_azar']['aciertos_esperados'])\n"
        "print('items a inspeccionar a mano :', r['items_a_inspeccionar_a_mano'])",
        "Con la salida del motor, calcula cuánta ventaja saca el atajo sobre el azar y argumenta qué "
        "conclusión se puede y no se puede sacar de una exactitud del 91,7 %.",
        "Elige un benchmark real que se use en tu área, lee veinte de sus ítems y responde por escrito: "
        "qué constructo declara, qué subhabilidades cubre y qué atajo se te ocurre. Después busca si "
        "alguien ya lo publicó.",
        "Guarda la tabla de cobertura y la puntuación del atajo, junto con tu procedimiento de tres pasos "
        "para auditar un benchmark.",
        "Ya sabemos desconfiar del instrumento. Queda desconfiar del procedimiento: qué hace falta para "
        "que otra persona obtenga el mismo número.",
    ),
    "P63_reproducibilidad": _auto(
        "reproducibilidad",
        "Una mejora de 4,2 puntos y una mejora de 0,66 puntos pueden ser el mismo experimento. La "
        "diferencia está en si se reporta una semilla o cinco. No hace falta mala fe: basta un formato de "
        "publicación que no obligue a declararlas.",
        "```text\nbaseline  : 71,2 · 73,8 · 70,4 · 74,9 · 72,1   → media 72,48 ± 1,851\n"
        "propuesta : 73,0 · 72,4 · 74,6 · 71,8 · 73,9   → media 73,14 ± 1,126\n\n"
        "    con la semilla 42:  +4,2  ← lo que se publica\n"
        "    en media        :  +0,66 ← lo que hay\n"
        "    los rangos se SOLAPAN\n```",
        "1. ¿Cuánta «mejora» sale si se reporta una sola semilla?\n"
        "2. ¿Cuánta sale en media sobre cinco?\n"
        "3. ¿En cuántas semillas gana realmente la propuesta?",
        "Con la semilla 42 la propuesta mejora 4,2 puntos; en media, 0,66 con desviaciones de 1,851 y "
        "1,126. Los rangos se solapan y la propuesta gana solo en 3 de 5 semillas. Sin media, desviación y "
        "número de corridas, el lector no puede distinguir un caso del otro.",
        "El checklist no garantiza que un resultado sea cierto: garantiza que sea **comprobable**. Son dos "
        "cosas distintas y confundirlas lleva a la decepción con los checklists. Lo que cambia es que el "
        "coste de auditar baja lo suficiente como para que alguien lo haga.",
        "Anti-patrón: publicar el mejor resultado de varias corridas sin declarar cuántas hubo.",
        "print('No hace falta mala fe. Se prueban cinco semillas, se reporta la que sale mejor.')\n"
        "print('Sin obligacion de declarar el numero de corridas, eso es indistinguible de un resultado real.')\n"
        "print('El checklist no acusa a nadie: cambia el formato para que la pregunta se pueda responder.')",
        "El reporte mínimo que hace la diferencia:",
        "r = run_paper_lab('reproducibilidad', seed=7)['result']\n"
        "print('con una semilla :', r['mejora_si_reporta_una_semilla'])\n"
        "print('en media        :', r['mejora_real_en_media'])\n"
        "print('gana en         :', r['semillas_en_las_que_gana_la_propuesta'])\n"
        "print('rangos solapan  :', r['solapan_los_rangos'])\n"
        "show(r['puntuacion_por_articulo'])",
        "Compara las puntuaciones de los tres artículos del checklist y señala qué ítem, si faltara solo "
        "ese, haría imposible auditar el resultado.",
        "Coge un experimento tuyo, ejecútalo con cinco semillas y publica media, desviación y rango junto "
        "al número de corridas. Después comprueba si alguna conclusión que ya habías escrito no sobrevive "
        "a ese reporte.",
        "Guarda la comparación entre la mejora de una semilla y la mejora en media, junto con tu "
        "checklist mínimo de reporte.",
        "Aquí se cierra el suelo del programa: geometría, información, agencia y método. Lo que sigue es "
        "la primera tradición que construyó sobre él — la IA simbólica, con sus espacios de estados y sus "
        "lógicas.",
    ),
})


SPECS.update({
    "P64_gps": _auto(
        "gps",
        "En vez de probar acciones a ver qué pasa, mira **qué falta**. Compara dónde estás con dónde "
        "quieres estar, quédate con la diferencia y busca en una tabla qué operador reduce esa "
        "diferencia concreta. Si no puedes aplicarlo todavía, tu nuevo objetivo es poder aplicarlo.",
        "```text\nmientras haya diferencias(estado, meta):\n"
        "    d  ← la diferencia más importante\n"
        "    op ← tabla[d]                       ← el conocimiento del dominio\n"
        "    si op no es aplicable:\n"
        "        subobjetivo: reducir la diferencia que bloquea su precondición\n"
        "    aplicar(op)\n```",
        "1. ¿Cuántos pasos tendrá el plan?\n"
        "2. ¿Qué hace GPS cuando el operador que necesita no es aplicable?\n"
        "3. ¿Cuántas secuencias habría que probar a ciegas para esa longitud?",
        "El plan sale en **5 pasos** y alcanza la meta. Cuando toca conducir y la puerta está cerrada, "
        "GPS no abandona ni prueba otra cosa: convierte «puerta abierta» en un subobjetivo. A ciegas "
        "habría **3 125** secuencias de esa longitud con cinco operadores.",
        "Aquí nace la separación entre **motor** y **dominio**, que es la arquitectura de todo lo que "
        "viene después: STRIPS ([P68](../../papers/foundational/P68_strips/README.md)) formaliza esta "
        "misma idea, y un agente con herramientas hoy tiene exactamente esta estructura con el modelo "
        "de lenguaje en el lugar de la tabla.",
        "Anti-patrón: creer que GPS es general porque resuelve varios problemas.",
        "print('La tabla diferencia->operador la escribe una persona, para cada dominio.')\n"
        "print('Lo general es el METODO, no el conocimiento. Sin tabla, GPS no hace nada.')\n"
        "print('Ese fue el limite que acabo con la promesa de un resolvedor universal.')",
        "Lo que sí es general y lo que no:",
        "r = run_paper_lab('gps', seed=7)['result']\n"
        "print('metodo general  : analisis medios-fines, vale para cualquier dominio')\n"
        "print('conocimiento    :', r['tabla_diferencia_operador'])\n"
        "print('lo segundo hay que escribirlo cada vez.')",
        "Sigue la traza paso a paso e identifica en qué momento aparece el subobjetivo y por qué.",
        "Modela un problema de tu trabajo como diferencias y operadores: define el estado, la meta y la "
        "tabla diferencia→operador. Después comprueba cuánto esfuerzo te llevó la tabla frente al motor.",
        "Guarda la traza del plan con la diferencia atacada en cada paso y tu tabla "
        "diferencia→operador.",
        "El método ya sabe qué operador aplicar. La pregunta siguiente es cómo elegir bien cuando hay "
        "muchos caminos y todos parecen razonables.",
    ),
    "P65_dpll": _auto(
        "dpll",
        "Antes de adivinar, deduce. Si una cláusula ha quedado con un solo literal, ese literal no es "
        "una opción: es una obligación. Aplicar todas las obligaciones antes de tomar cualquier "
        "decisión es lo que separa un solucionador viable de una tabla de verdad.",
        "```text\nDPLL(F, asignación):\n"
        "    si F está vacía        → SATISFACIBLE\n"
        "    si hay cláusula vacía  → conflicto, retroceder\n"
        "    si hay cláusula unitaria (L)  → asignar L, repetir      ← deducción\n"
        "    si hay literal puro L         → asignar L, repetir      ← deducción\n"
        "    elegir variable v y probar v=1, luego v=0               ← decisión\n```",
        "1. ¿Cuántos nodos visitará DPLL frente a las 32 filas de la tabla de verdad?\n"
        "2. ¿Cuántos de esos pasos son deducción y cuántos decisión?\n"
        "3. ¿Cuántas asignaciones satisfacen la fórmula?",
        "DPLL visita **5 nodos** frente a las 32 filas de la tabla: un factor de 6,4× con solo cinco "
        "variables. De esos pasos, 3 son propagaciones unitarias, es decir deducción pura. Solo 3 de "
        "las 32 asignaciones satisfacen la fórmula.",
        "Este algoritmo tiene sesenta años y sigue siendo el esqueleto de los solucionadores actuales, "
        "que resuelven instancias de millones de cláusulas. Lo que se añadió después —aprendizaje de "
        "cláusulas, reinicios, heurísticas de actividad— se monta encima de este bucle, no lo sustituye.",
        "Anti-patrón: tratar la propagación unitaria como una heurística que se puede deshacer.",
        "print('Una clausula unitaria (L) no deja eleccion: L TIENE que ser cierto.')\n"
        "print('Eso es una deduccion, no una apuesta, y no se retrocede sobre ella.')\n"
        "print('Confundir deduccion con decision es el error clasico al implementar DPLL.')",
        "La separación correcta entre lo que se deduce y lo que se decide:",
        "r = run_paper_lab('dpll', seed=7)['result']\n"
        "print('nodos totales        :', r['nodos_dpll'])\n"
        "print('propagacion unitaria :', r['propagaciones_unitarias'], '<- deduccion')\n"
        "print('literales puros      :', r['literales_puros'], '<- deduccion')\n"
        "print('tabla completa       :', r['asignaciones_tabla_completa'], 'filas')",
        "Comprueba en la salida cuántas asignaciones satisfacen la fórmula y compáralo con lo que "
        "costaría encontrarlas por sondeo aleatorio si hubiera 50 variables en vez de 5.",
        "Codifica un sudoku de 4×4 en forma normal conjuntiva y resuélvelo con este motor. Cuenta "
        "cuántas variables y cláusulas necesitas, y cuántos nodos hacen falta con y sin propagación.",
        "Guarda el conteo de nodos frente a la tabla completa y tu distinción entre los pasos que son "
        "deducción y los que son decisión.",
        "Ya se decide en lógica proposicional. El salto siguiente es poder hablar de objetos y "
        "relaciones, y para eso hace falta una regla de inferencia que sepa igualar términos.",
    ),
    "P66_resolucion": _auto(
        "resolucion",
        "Dos frases que se contradicen en un punto se pueden fundir en una tercera que ya no menciona "
        "ese punto. Repite hasta llegar a la nada —la cláusula vacía— y habrás demostrado que las "
        "premisas eran incompatibles. Para que funcione con variables hace falta saber igualarlas: eso "
        "es la unificación.",
        "```text\nResolución:  de (A ∨ L)  y  (B ∨ ¬L')  con σ = mgu(L, L')\n"
        "             se sigue  (A ∨ B)σ\n\n"
        "Unificador más general (mgu): la sustitución MÍNIMA que iguala dos términos\n"
        "    Humano(x)      y  Humano(Sócrates)   →  {x = Sócrates}\n"
        "    Padre(x, y)    y  Padre(Juan, z)     →  {x = Juan, y = z}\n"
        "    Humano(Sócrates) y Humano(Platón)    →  no unifican\n```",
        "1. ¿Cuáles de los cuatro pares de términos unifican?\n"
        "2. ¿Qué liga el unificador en `Padre(x,y)` con `Padre(Juan,z)`?\n"
        "3. ¿Con qué se cierra una demostración por refutación?",
        "Tres de los cuatro pares unifican; «Sócrates» y «Platón» son constantes distintas y ninguna "
        "sustitución las iguala. El unificador de `Padre` liga `x = Juan` y deja `y = z` sin resolver: "
        "no compromete nada de más. Y la refutación cierra con **la cláusula vacía**, que es la "
        "contradicción.",
        "Este resultado es la base de Prolog y de todos los demostradores automáticos. La idea de negar "
        "la conclusión y buscar contradicción es además el patrón que reaparece en la verificación "
        "formal moderna: no se demuestra que algo es cierto, se demuestra que su negación es imposible.",
        "Anti-patrón: olvidar la comprobación de ocurrencia al unificar.",
        "print('Unificar x con f(x) daria x = f(f(f(...))), un termino infinito.')\n"
        "print('La comprobacion de ocurrencia lo impide, y cuesta tiempo.')\n"
        "print('Muchos Prolog la omiten por velocidad: es correcto y es un riesgo declarado.')",
        "Qué demuestra la refutación y qué no:",
        "r = run_paper_lab('resolucion', seed=7)['result']\n"
        "print('cierra con clausula vacia :', r['cierra_por_refutacion'])\n"
        "print('regla unica               :', r['regla_unica'])\n"
        "print('Demostrar que Socrates es mortal = negarlo y llegar a contradiccion.')",
        "Revisa los cuatro casos de unificación y explica, para el que falla, por qué ninguna "
        "sustitución puede arreglarlo.",
        "Escribe en cláusulas un dominio pequeño de tu elección —tres o cuatro hechos y dos reglas— y "
        "demuestra una conclusión por refutación a mano. Después comprueba qué pasa si la conclusión "
        "NO se sigue: ¿termina el procedimiento?",
        "Guarda la tabla de unificación con sus unificadores y tu explicación de por qué la refutación "
        "cierra con el vacío.",
        "Ya se puede deducir. Falta decidir por dónde buscar cuando hay muchos caminos posibles y "
        "todos son válidos: eso lo resuelve una heurística con garantía.",
    ),
    "P67_a_estrella": _auto(
        "a_estrella",
        "Una heurística te dice qué parece prometedor. El problema es que «parece» no es «es»: la "
        "búsqueda voraz encuentra rápido y encuentra mal. A* suma las dos mitades —lo que ya llevas "
        "gastado y lo que estimas que falta— y demuestra que, si la estimación nunca se pasa, el "
        "camino que devuelve es el mejor.",
        "```text\nf(n) = g(n) + h(n)\n\n"
        "    g(n) = coste REAL desde el inicio hasta n\n"
        "    h(n) = coste ESTIMADO desde n hasta la meta\n\n"
        "Admisibilidad:  h(n) ≤ coste real restante para todo n\n"
        "Teorema:        h admisible  ⟹  A* devuelve el camino óptimo\n```",
        "1. ¿Qué coste tiene el camino óptimo?\n"
        "2. ¿Qué devuelve la búsqueda voraz, que solo mira h?\n"
        "3. ¿Y A* con una heurística que sobrestima en un nodo?",
        "El óptimo cuesta **8**. La búsqueda voraz expande menos nodos y devuelve un camino de coste "
        "**10**: rápida y equivocada. Y A* con la heurística que sobrestima en D —el nodo del camino "
        "óptimo— también devuelve **10**. La garantía se pierde exactamente donde se rompe la "
        "admisibilidad, y no antes.",
        "Lo que aporta el paper no es una heurística mejor: es un **teorema**. Y por eso sobrevive: la "
        "búsqueda en árbol de [AlphaGo](../../papers/foundational/P27_alphago/README.md) es esta "
        "estructura con una red aportando la estimación, y cualquier planificador de rutas que uses "
        "hoy es esto con un mapa detrás.",
        "Anti-patrón: usar una heurística «que funciona bien» sin comprobar que es admisible.",
        "print('Una heuristica optimista (nunca se pasa) garantiza el camino optimo.')\n"
        "print('Una que se pasa aunque sea en UN nodo, no garantiza nada.')\n"
        "print('Y el fallo es silencioso: devuelve un camino, solo que no el mejor.')",
        "La comprobación que hay que hacer, nodo a nodo:",
        "r = run_paper_lab('a_estrella', seed=7)['result']\n"
        "print('h admisible en todos los nodos :', r['admisible_en_todos_los_nodos'])\n"
        "print('la otra falla en              :', r['inadmisible_falla_en'])\n"
        "for nombre, res in r['resultados'].items():\n"
        "    print(f\"{nombre:<24} coste {res['coste']} · expandidos {res['expandidos']} · optimo {res['es_optimo']}\")",
        "Compara los nodos expandidos por costo uniforme y por A* admisible, y explica por qué A* "
        "expande menos sin perder la garantía.",
        "Implementa A* sobre una rejilla con obstáculos usando la distancia Manhattan, comprueba que es "
        "admisible y después multiplícala por 1,5. Mide cuánto ganas en nodos y cuánto pierdes en "
        "calidad del camino.",
        "Guarda la tabla de las cuatro búsquedas con coste, nodos y optimalidad, y tu comprobación de "
        "admisibilidad nodo a nodo.",
        "La búsqueda ya tiene garantía. Pero para planificar hace falta algo más: una forma de "
        "describir acciones que no obligue a decir todo lo que NO cambia.",
    ),
    "P68_strips": _auto(
        "strips",
        "Describir una acción parece fácil hasta que intentas escribir todo lo que **no** cambia. Si "
        "muevo un bloque, sigue habiendo una mesa, sigo teniendo dos manos y el color de las paredes "
        "no varía. STRIPS resuelve eso por convención: solo se declara lo que cambia, y lo demás "
        "persiste.",
        "```text\nOperador = ⟨precondiciones, lista de añadir, lista de borrar⟩\n\n"
        "    mover(C, A→mesa):\n"
        "        pre : sobre(C,A), libre(C)\n"
        "        add : sobre(C,mesa), libre(A)\n"
        "        del : sobre(C,A)\n\n"
        "Todo literal no mencionado en add ni en del SIGUE SIENDO CIERTO.\n```",
        "1. ¿Cuántos literales que el operador no menciona siguen siendo ciertos?\n"
        "2. ¿Resuelve el planificador lineal la meta si ataca «A sobre B» primero?\n"
        "3. ¿Y si ataca «B sobre C» primero?",
        "Cuatro literales persisten sin que nadie los reafirme: ese es el problema del marco resuelto "
        "por convención. Y el planificador lineal consigue **1 de 2** submetas con un orden y **1 de "
        "2** con el inverso: ningún orden funciona. Existe, sin embargo, un plan de 3 pasos que sí "
        "resuelve — pero intercala las submetas en vez de cerrarlas por turnos.",
        "La anomalía de Sussman no es un defecto de implementación: es una propiedad del esquema. "
        "Cerrar una submeta antes de tocar la siguiente falla cuando las submetas interactúan, y eso "
        "motiva toda la planificación no lineal posterior. El mismo problema reaparece hoy en los "
        "agentes que descomponen una tarea en subtareas y las ejecutan en orden.",
        "Anti-patrón: leer la anomalía como un fallo del dominio o del código.",
        "print('El mundo de bloques es trivial y el plan correcto tiene 3 pasos.')\n"
        "print('Lo que falla es el ESQUEMA: cerrar una submeta antes de tocar la siguiente.')\n"
        "print('Cambiar de dominio no lo arregla; cambiar de planificador, si.')",
        "El plan que sí funciona, y por qué:",
        "r = run_paper_lab('strips', seed=7)['result']\n"
        "print('orden A->B primero :', r['plan_con_A_sobre_B_primero']['logra'])\n"
        "print('orden B->C primero :', r['plan_con_B_sobre_C_primero']['logra'])\n"
        "print('intercalado        :', r['plan_no_lineal_intercalado']['plan'])\n"
        "print('resuelve           :', r['plan_no_lineal_intercalado']['todas'])",
        "Aplica a mano el operador `mover(C,A→mesa)` sobre el estado inicial y lista qué literales "
        "cambian y cuáles persisten.",
        "Escribe en PDDL el mundo de bloques con estos operadores y resuelve la anomalía de Sussman con "
        "un planificador real. Después compara la longitud del plan con los 3 pasos del intercalado.",
        "Guarda la representación del operador con sus tres listas y tu explicación de por qué ningún "
        "orden lineal resuelve la meta.",
        "La planificación ya tiene representación. Pero el mundo real no da hechos ciertos: da indicios "
        "de fuerza variable, y hay que razonar con ellos.",
    ),
    "P69_mycin": _auto(
        "mycin",
        "Un médico no dice «es una infección por E. coli» ni «no lo es»: dice «bastante probable, por "
        "estos tres indicios». MYCIN reproduce eso con un número por regla y un álgebra para "
        "combinarlos, y con algo que resultó ser tan importante como el número: la lista de reglas que "
        "sostienen cada conclusión.",
        "```text\nRegla:  SI premisas ENTONCES conclusión, con CF ∈ [−1, 1]\n\n"
        "Disparo:      CF(conclusión) = min(CF de las premisas) × CF(regla)\n"
        "Dos a favor:  CF = a + b·(1 − a)          ← satura, nunca llega a 1\n"
        "Dos en contra:CF = a + b·(1 + a)\n"
        "Mezcladas:    CF = (a + b) / (1 − min(|a|, |b|))\n```",
        "1. ¿Con qué grado sale la conclusión `enterobacteria`?\n"
        "2. ¿Se llega a la certeza acumulando indicios a favor?\n"
        "3. ¿Qué aporta la regla con factor negativo?",
        "`enterobacteria` sale con **0,933** y `e_coli` con **0,701**: el sistema no responde sí o no. "
        "Y no se llega a la certeza: `a + b(1−a)` satura por debajo de 1 por muchos indicios que se "
        "acumulen. La regla negativa resta en el mismo eje, que es una decisión de diseño sin "
        "equivalente directo en probabilidad.",
        "Lo que hizo aceptable a MYCIN entre médicos no fue su exactitud —que era comparable a la de "
        "los especialistas— sino que **podía explicar cada conclusión**. Cincuenta años después esa "
        "sigue siendo la ventaja estructural del razonamiento simbólico frente a un modelo denso, y la "
        "razón de que [P72](../../papers/foundational/P72_neurosimbolico/README.md) proponga combinarlos.",
        "Anti-patrón: leer los factores de certeza como probabilidades.",
        "print('Un CF de 0,7 no es una probabilidad de 0,7.')\n"
        "print('Su algebra no se deriva de los axiomas de Kolmogorov ni respeta la regla de Bayes.')\n"
        "print('Es un formalismo pragmatico de 1975, y sus propios autores lo revisaron despues.')",
        "La comparación honesta con la alternativa probabilística:",
        "r = run_paper_lab('mycin', seed=7)['result']\n"
        "print('combinacion MYCIN de 0,7 y 0,5 :', r['combinacion_dos_evidencias_a_favor']['resultado'])\n"
        "print('misma cuenta con independencia :', r['misma_cuenta_con_probabilidades_independientes'])\n"
        "print('Coinciden en ESTE caso. No coinciden en general: no es una equivalencia.')",
        "Sigue la traza de inferencia e identifica qué regla aporta cada incremento al factor de "
        "`enterobacteria`.",
        "Escribe una base de diez reglas para un dominio que conozcas, con sus factores de certeza, y "
        "prueba a cambiar el orden de disparo. Después documenta qué conclusiones cambian y por qué no "
        "deberían.",
        "Guarda la traza con el aporte de cada regla y tu comparación entre la combinación de MYCIN y "
        "la probabilística.",
        "Las reglas ya manejan incertidumbre. Queda el problema inverso: cuando las restricciones son "
        "duras y muchas, conviene podar antes de empezar a buscar.",
    ),
    "P70_arco_consistencia": _auto(
        "arco_consistencia",
        "Si un valor de una variable no tiene ningún compañero legal en su vecina, ese valor no puede "
        "estar en ninguna solución. Descubrirlo cuesta una comprobación local, y hacerlo **antes** de "
        "buscar ahorra descubrirlo una y otra vez en cada rama del retroceso.",
        "```text\nArco (x, y) consistente ⟺ todo valor de dom(x) tiene algún compañero legal en dom(y)\n\n"
        "AC-3:  cola ← todos los arcos\n"
        "       mientras la cola no esté vacía:\n"
        "           (x,y) ← sacar\n"
        "           si podar dom(x) cambia algo → volver a encolar los arcos (z,x)\n\n"
        "Coste O(e·d³). No decide satisfacibilidad: reduce dominios.\n```",
        "1. ¿Cuántos valores elimina AC-3 antes de asignar nada?\n"
        "2. ¿Cuántos nodos visita el retroceso con y sin esa poda?\n"
        "3. ¿Devuelven las dos búsquedas la misma solución?",
        "AC-3 elimina **60 de los 72** valores iniciales sin asignar nada. Después el retroceso resuelve "
        "con **7 nodos y 0 retrocesos**, frente a **233 nodos y 226 retrocesos** sin podar. Y la "
        "solución es la misma: la consistencia de arco no descarta soluciones, descarta valores que no "
        "participan en ninguna.",
        "El resultado fuerte está en la última línea de la evidencia: en una red con estructura de "
        "**árbol** —como esta cadena— la consistencia de arco deja la búsqueda sin retrocesos. En una "
        "red con ciclos ayuda pero no lo garantiza, y ahí es donde vive la investigación posterior en "
        "descomposición de restricciones.",
        "Anti-patrón: creer que si AC-3 deja todos los dominios no vacíos, hay solución.",
        "print('AC-3 elimina valores localmente inconsistentes. Nada mas.')\n"
        "print('Puede dejar todos los dominios llenos y que el problema no tenga solucion.')\n"
        "print('Consistencia local no implica consistencia global.')",
        "Lo que sí garantiza y lo que no:",
        "r = run_paper_lab('arco_consistencia', seed=7)['result']\n"
        "print('valores podados      :', r['valores_podados'], 'de', r['tamano_del_espacio'] and 72)\n"
        "print('sin AC-3             :', r['backtracking_sin_ac3']['nodos'], 'nodos ·',\n"
        "      r['backtracking_sin_ac3']['retrocesos'], 'retrocesos')\n"
        "print('con AC-3             :', r['backtracking_con_ac3']['nodos'], 'nodos ·',\n"
        "      r['backtracking_con_ac3']['retrocesos'], 'retrocesos')\n"
        "print('misma solucion       :', r['misma_solucion'])",
        "Mira los dominios tras AC-3 y explica por qué la primera variable pierde diez de sus doce "
        "valores sin que se haya asignado nada.",
        "Modela el coloreado del mapa de Australia como CSP y aplica AC-3. Comprueba que ahí la poda "
        "ayuda menos y explica por qué: la red tiene ciclos y la propiedad del árbol no vale.",
        "Guarda la comparación de nodos y retrocesos con y sin poda, y tu enunciado de qué garantiza la "
        "consistencia de arco.",
        "Las restricciones ya se propagan. Falta la pieza que permite que dos sistemas distintos hablen "
        "del mismo mundo: un acuerdo explícito sobre qué significa cada término.",
    ),
    "P71_ontologia": _auto(
        "ontologia",
        "Dos equipos usan la palabra «publicación» y cuentan cosas distintas. No hay error de datos: "
        "hay dos conceptualizaciones. Una ontología no describe el mundo — fija qué se acuerda decir "
        "de él, para que dos sistemas puedan intercambiar información sin malentenderse.",
        "```text\nOntología = especificación explícita de una conceptualización\n\n"
        "Jerarquía + subsunción → inferencia gratis:\n"
        "    P08 es ArtículoDeRevista\n"
        "      ⟹ es Artículo ⟹ es Documento ⟹ es Entidad\n\n"
        "Cinco criterios: claridad · coherencia · extensibilidad ·\n"
        "                 sesgo de codificación mínimo · compromiso ontológico mínimo\n```",
        "1. ¿Cuántos hechos se infieren al declarar que P08 es un ArtículoDeRevista?\n"
        "2. ¿Cuántas «publicaciones» hay en el corpus según cada agente?\n"
        "3. ¿Quién tiene razón?",
        "Se infieren **3 hechos** que nadie escribió, solo por subsunción. Y los dos agentes responden "
        "**1** y **2** a la misma pregunta sobre el mismo corpus: uno cuenta los preprints como "
        "publicaciones y el otro no. Ninguno tiene razón — tienen compromisos distintos, y por eso hay "
        "que declararlos.",
        "Este artículo es de 1993 y su definición sigue siendo la que se cita. Lo que ha cambiado es la "
        "escala: hoy la conceptualización compartida vive en esquemas de API, en contratos de "
        "herramientas de agentes y en el vocabulario de un índice para "
        "[RAG](../../papers/foundational/P11_rag/README.md). El problema es el mismo.",
        "Anti-patrón: confundir una ontología con un diccionario o una taxonomía.",
        "print('Un diccionario recoge como se usa una palabra.')\n"
        "print('Una ontologia DECIDE que se va a decir con ella, y compromete a quien la adopta.')\n"
        "print('Por eso el articulo habla de compromiso ontologico y no de definiciones.')",
        "La consecuencia práctica del compromiso:",
        "r = run_paper_lab('ontologia', seed=7)['result']['desacuerdo_sobre_el_mismo_termino']\n"
        "print('agente A cuenta :', r['cuenta_A'])\n"
        "print('agente B cuenta :', r['cuenta_B'])\n"
        "print('misma pregunta, mismo corpus, distinta respuesta:', r['misma_pregunta_distinta_respuesta'])",
        "Recorre los cinco criterios de diseño y aplica uno de ellos a la jerarquía del motor: ¿la "
        "cumple? Justifica.",
        "Escribe la ontología mínima de un dominio que conozcas —seis o siete clases— y pásale los "
        "cinco criterios. Después dásela a otra persona y comprueba si cuenta lo mismo que tú sobre "
        "los mismos datos.",
        "Guarda la jerarquía con sus inferencias por subsunción y el caso de los dos agentes que "
        "cuentan distinto.",
        "La tradición simbólica está completa: buscar, deducir, planificar, restringir y acordar. Falta "
        "la pregunta que la reabre — qué pasa cuando se junta con lo que aprende de los datos.",
    ),
    "P72_neurosimbolico": _auto(
        "neurosimbolico",
        "Una red estima y a veces se equivoca con confianza. Una regla no estima nada, pero sabe que en "
        "un salón no hay coches. Juntar las dos no es hacer una media: es dejar que la regla filtre el "
        "espacio de salidas de la red. Funciona muy bien cuando la regla es cierta, y destruye cuando "
        "no lo es.",
        "```text\npercepción → distribución sobre etiquetas\n"
        "restricción → elimina las etiquetas incompatibles con el contexto\n"
        "decisión    → argmax sobre lo que queda\n\n"
        "escena(salón) ∧ etiqueta(x, coche) → ⊥\n\n"
        "No hay reentrenamiento: hay filtrado del espacio de salida.\n```",
        "1. ¿Cuántos objetos del salón acierta la percepción sola?\n"
        "2. ¿Y añadiendo la regla del contexto?\n"
        "3. ¿Qué pasa si se aplica esa misma regla en un garaje?",
        "En el salón la percepción sola acierta **2 de 4** y con la regla, **4 de 4**: la restricción "
        "corrige dos objetos donde la red se equivocaba con confianza 0,55 y 0,48. En el garaje —donde "
        "sí hay coches— la misma regla es falsa y el resultado cae de **2 a 0 de 2**.",
        "Esa asimetría es la tesis, y es lo que hace difícil el enfoque: el conocimiento simbólico "
        "aporta mucho cuando es correcto y cuesta todo cuando no lo es. De ahí que el requisito central "
        "no sea la integración técnica sino que las reglas estén **declaradas y sean auditables**, que "
        "es exactamente la ventaja que tenía [MYCIN](../../papers/foundational/P69_mycin/README.md) en "
        "1975.",
        "Anti-patrón: tratar el artículo como un método con resultados comparables.",
        "print('Garcez y Lamb publican un manifiesto y una hoja de ruta, no un sistema evaluado.')\n"
        "print('No hay tabla de resultados que reproducir ni benchmark que superar.')\n"
        "print('Se lee como agenda abierta, con fecha, no como estado del arte cerrado.')",
        "Lo que la miniatura sí demuestra:",
        "r = run_paper_lab('neurosimbolico', seed=7)['result']\n"
        "print('salon  :', r['escena_salon']['aciertos'], '<- la regla vale')\n"
        "print('garaje :', r['escena_garaje']['aciertos'], '<- la regla NO vale')\n"
        "print('ganancia', r['ganancia_donde_la_regla_vale'], '| coste', r['coste_donde_no_vale'])",
        "Localiza en la salida los dos objetos que la regla corrige y comprueba con qué confianza se "
        "equivocaba la percepción en cada uno.",
        "Coge un clasificador tuyo, escribe dos restricciones de dominio que sepas ciertas y aplícalas "
        "sobre sus salidas. Mide la ganancia, y después busca deliberadamente un caso donde la "
        "restricción sea falsa y documenta el coste.",
        "Guarda la comparación entre las dos escenas y tu enunciado de por qué una restricción "
        "incorrecta no degrada sino que destruye.",
        "Aquí se cierra la ruta simbólica. Lo que viene es la otra tradición: aprender la regla de los "
        "datos en vez de escribirla, que es lo que hace el machine learning clásico.",
    ),
})


SPECS.update({
    "P73_kmeans": _auto(
        "kmeans",
        "Pon k banderas al azar. Cada punto se va con la bandera más cercana; cada bandera se mueve al "
        "centro de los que le tocaron. Repite. Se para siempre — y no siempre en el mismo sitio.",
        "```text\nRepetir hasta que nada cambie:\n"
        "    asignar : cada punto al centro más cercano       ← baja la inercia\n"
        "    mover   : cada centro al promedio de los suyos   ← baja la inercia\n\n"
        "Inercia = Σ ‖x − centro(x)‖².  Como baja en los dos pasos y hay un número\n"
        "finito de asignaciones, el algoritmo TERMINA. En un óptimo LOCAL.\n```",
        "1. ¿Cuántas iteraciones tardará en converger?\n"
        "2. ¿Darán todos los arranques la misma inercia final?\n"
        "3. ¿Qué le pasa a la inercia al aumentar k?",
        "Converge en pocos pasos y la inercia nunca sube. Pero con ocho arranques aleatorios aparecen "
        "**inercias finales distintas**: una de 1,41 y otra de 61,59 sobre los mismos doce puntos. "
        "Converger no es encontrar el óptimo. Y la inercia decrece siempre al subir k.",
        "Las dos consecuencias prácticas están en esa salida. Primera: hay que ejecutar varias veces y "
        "quedarse con la mejor —o usar k-means++ para inicializar—. Segunda: **no se puede elegir k "
        "minimizando la inercia**, porque el mínimo está en un grupo por punto. Hace falta otro criterio, "
        "y esa decisión no la toma el algoritmo.",
        "Anti-patrón: elegir el número de grupos por la inercia.",
        "r = run_paper_lab('kmeans', seed=7)['result']\n"
        "for fila in r['inercia_por_k']:\n"
        "    print(f\"k = {fila['k']:>2}  inercia = {fila['inercia']}\")\n"
        "print('Minimizar esta columna lleva a k = n. La inercia no elige k.')",
        "El criterio tiene que venir de fuera del algoritmo:",
        "print('opciones razonables: codo, silueta, criterio de informacion, o el dominio')\n"
        "print('la mejor suele ser la ultima: cuantos grupos NECESITA quien va a usar esto')\n"
        "r = run_paper_lab('kmeans', seed=7)['result']\n"
        "print('inercias finales distintas con 8 arranques:', r['inercias_finales_distintas'])",
        "Compara el mejor y el peor arranque en la salida y explica por qué el peor no es un error del "
        "algoritmo.",
        "Aplica k-medias a un conjunto real con variables en escalas distintas, primero sin estandarizar y "
        "después estandarizando. Documenta cuánto cambian los grupos y por qué.",
        "Guarda la tabla de inercias por arranque y por k, y tu criterio para elegir k.",
        "Ya se pueden agrupar puntos sin etiquetas. Con etiquetas, la pregunta cambia: qué pregunta hacer "
        "primero para separarlos.",
    ),
    "P74_id3": _auto(
        "id3",
        "En cada nodo, elegir la pregunta que más incertidumbre elimina. Se mide con la entropía: cuánto "
        "sabes antes de preguntar, cuánto sabes después. La diferencia es la ganancia. El problema es "
        "que preguntar «¿cuál es tu número de fila?» elimina TODA la incertidumbre.",
        "```text\nGanancia(S, A) = H(S) − Σ_v (|S_v|/|S|)·H(S_v)\n\n"
        "Razón de ganancia = Ganancia / InfoDivisión,\n"
        "    con InfoDivisión = −Σ_v (|S_v|/|S|)·log₂(|S_v|/|S|)\n\n"
        "InfoDivisión crece con el número de valores → penaliza los atributos muy troceados\n```",
        "1. ¿Qué atributo elige la ganancia de información?\n"
        "2. ¿Y si dejamos el identificador de fila dentro de la tabla?\n"
        "3. ¿Lo arregla la razón de ganancia?",
        "Con la tabla completa gana **«id»**, el identificador, con la ganancia máxima posible: separa "
        "perfectamente y no generaliza nada. El caso realista es «zona», con siete valores: gana en "
        "ganancia a «cielo» (0,3149 frente a 0,2467) y **pierde en razón de ganancia**. Ahí la corrección "
        "sí funciona; con el identificador dentro, no la salva ningún criterio.",
        "Esa es la lección honesta y la que se cuenta mal en casi todos los cursos. La razón de ganancia "
        "corrige el sesgo hacia atributos muy troceados en el caso realista. No convierte un identificador "
        "en un atributo aceptable: eso es responsabilidad de quien prepara los datos, no del criterio de "
        "división.",
        "Anti-patrón: dejar identificadores, fechas exactas o claves en la matriz de entrada.",
        "print('Un identificador separa perfectamente el entrenamiento y no generaliza nada.')\n"
        "print('El arbol resultante tiene exactitud 100% dentro y la del azar fuera.')\n"
        "print('Y lo mismo pasa con marcas de tiempo exactas o claves de cliente.')",
        "Lo que sí corrige el criterio, comprobado sobre atributos reales:",
        "r = run_paper_lab('id3', seed=7)['result']\n"
        "for fila in r['tabla_de_ganancias']:\n"
        "    print(f\"{fila['atributo']:<12} valores={fila['valores']:>2} \"\n"
        "          f\"ganancia={fila['ganancia']:<7} razon={fila['razon_de_ganancia']}\")\n"
        "print()\n"
        "print('sin el identificador:', r['sin_el_identificador'])",
        "Compara «zona» y «cielo» en las dos columnas y explica por qué la razón de ganancia invierte el "
        "orden.",
        "Construye el árbol completo sobre estos datos sin límite de profundidad, mide su exactitud dentro "
        "y fuera de muestra, y después pódalo. Documenta cuánto pierde dentro y cuánto gana fuera.",
        "Guarda la tabla de ganancias y razones de ganancia, y tu explicación de por qué un identificador "
        "no es un atributo.",
        "El árbol se lee, y sobreajusta. La pregunta siguiente es qué criterio usar cuando varios modelos "
        "aciertan lo mismo en entrenamiento.",
    ),
    "P75_svm": _auto(
        "svm",
        "Ocho puntos y una recta que los separa. Y otra. Y otra. Todas aciertan el 100 % en "
        "entrenamiento, así que la exactitud no sirve para elegir. Vapnik propone otro criterio: quedarse "
        "con la que pasa más lejos de todos los puntos.",
        "```text\nMargen geométrico:  γ = mín_i  yᵢ(w·xᵢ + b) / ‖w‖\n\n"
        "Problema:  maximizar γ  ⟺  minimizar ‖w‖²/2  sujeto a  yᵢ(w·xᵢ + b) ≥ 1\n\n"
        "Solo los puntos con yᵢ(w·xᵢ + b) = 1 definen la solución: los VECTORES SOPORTE.\n```",
        "1. ¿Cuántos separadores distintos aciertan el 100 %?\n"
        "2. ¿Cuánto varía su margen?\n"
        "3. ¿Cuántos puntos definen la frontera del mejor?",
        "Quince hiperplanos separan correctamente los ocho puntos, con márgenes que van de **0,2306 a "
        "0,956**: un factor de cuatro. Todos son perfectos en entrenamiento. Y el mejor queda definido "
        "por **3 de los 8 puntos**: mover cualquier otro sin cruzar el margen no cambia el modelo.",
        "De ahí sale una propiedad muy útil: el modelo no depende del tamaño del conjunto sino del número "
        "de vectores soporte. Y una idea que reaparece en todas partes: cuando varias hipótesis explican "
        "los datos igual de bien, hace falta un criterio adicional. Aquí es el margen; en "
        "[P77](../../papers/foundational/P77_lasso/README.md) será la parsimonia.",
        "Anti-patrón: elegir entre modelos que empatan en entrenamiento mirando el entrenamiento.",
        "r = run_paper_lab('svm', seed=7)['result']\n"
        "print('separadores perfectos en entrenamiento:', r['separadores_validos_probados'])\n"
        "print('margen del mejor :', r['mejor_por_margen']['margen'])\n"
        "print('margen del peor  :', r['peor_separador_valido']['margen'])\n"
        "print('Los dos aciertan 100%. La exactitud no los distingue.')",
        "El criterio que sí los distingue, y su justificación:",
        "r = run_paper_lab('svm', seed=7)['result']\n"
        "print('vectores soporte:', r['puntos_que_definen_la_frontera'])\n"
        "for v in r['vectores_soporte']:\n"
        "    print('  ', v)\n"
        "print('El resto de puntos podria moverse sin cambiar la frontera.')",
        "Identifica en la salida los tres vectores soporte y explica por qué el modelo no cambiaría si "
        "moviéramos los otros cinco.",
        "Entrena una SVM con núcleo lineal y otra con núcleo RBF sobre un conjunto no separable "
        "linealmente. Compara el número de vectores soporte y explica qué te dice sobre la complejidad de "
        "cada modelo.",
        "Guarda la tabla de separadores con sus márgenes y tu enunciado de por qué el margen máximo es un "
        "criterio y no una preferencia estética.",
        "Ya hay criterio para elegir modelo. Falta uno para medirlo: qué número se reporta y con cuánta "
        "incertidumbre.",
    ),
    "P76_validacion_cruzada": _auto(
        "validacion_cruzada",
        "Dos personas evalúan el mismo modelo sobre los mismos datos y reportan 0,70 y 0,97. Ninguna "
        "hace trampa. La diferencia está en cómo partieron los datos, y ese detalle —que casi nunca se "
        "declara— pesa más que muchas mejoras publicadas.",
        "```text\nHoldout 70/30       : entrena con 70, evalúa con 30      ← 30 ejemplos de test\n"
        "Validación cruzada k : k particiones; cada ejemplo pasa por\n"
        "                       el test EXACTAMENTE una vez             ← n ejemplos de test\n\n"
        "Mismo sesgo aproximado.  La diferencia está en la VARIANZA del estimador.\n```",
        "1. ¿Acertarán los tres estimadores la exactitud real en media?\n"
        "2. ¿Cuál tendrá más dispersión?\n"
        "3. ¿Por qué?",
        "Los tres aciertan en media —los sesgos son de milésimas—, así que el problema no es el sesgo. Es "
        "la **varianza**: el holdout estima con desviación 0,0753 y la validación cruzada de 10 pliegues "
        "con 0,0454. Sobre 200 conjuntos simulados, el holdout devuelve valores entre **0,60 y 0,97**.",
        "La razón es aritmética y conviene tenerla clara: el holdout evalúa sobre 30 ejemplos y la "
        "validación cruzada sobre los 100, porque cada ejemplo pasa por el test una vez. Menos ejemplos "
        "de test, más ruido. Por eso el artículo recomienda diez pliegues estratificados — no por "
        "tradición, por medición.",
        "Anti-patrón: reportar una exactitud sin decir cómo se estimó.",
        "print('«El modelo alcanza un 92% de exactitud».')\n"
        "print('Sin decir: particion, semilla, numero de corridas ni estratificacion.')\n"
        "print('Con holdout sobre 30 ejemplos de test, ese 92% puede ser un 78% con otra particion.')",
        "El reporte mínimo que hace comparable un número:",
        "r = run_paper_lab('validacion_cruzada', seed=7)['result']\n"
        "for nombre, e in r['estimadores'].items():\n"
        "    print(f\"{nombre:<22} media={e['media']:<8} desv={e['desviacion']:<8} \"\n"
        "          f\"rango=[{e['min']}, {e['max']}]\")\n"
        "print('exactitud real de la poblacion:', r['exactitud_real_de_la_poblacion'])",
        "Calcula cuántas veces más disperso es el holdout que la validación cruzada de 10 pliegues, y "
        "relaciónalo con el número de ejemplos de test de cada uno.",
        "Toma un modelo tuyo y evalúalo con holdout repetido 20 veces y con validación cruzada de 10 "
        "pliegues. Publica media, desviación y número de corridas de ambos, y decide cuál reportarías.",
        "Guarda la tabla de los tres estimadores con media, desviación y rango, y tu regla de reporte "
        "mínimo.",
        "Ya se sabe medir. Volvemos al modelo: cómo evitar que use todas las variables que le des, incluso "
        "las que no aportan.",
    ),
    "P77_lasso": _auto(
        "lasso",
        "La regresión de cresta encoge todos los coeficientes hacia cero y no llega nunca. El lasso "
        "cambia el círculo por un rombo, y los rombos tienen esquinas justo sobre los ejes. El óptimo "
        "tiende a caer en una esquina — y una esquina significa un coeficiente exactamente cero.",
        "```text\nCresta (L2):  minimizar  RSS + α·Σ βⱼ²      → encoge, no anula\nLasso  (L1):  minimizar  RSS + α·Σ |βⱼ|     → ANULA\n\n"
        "Umbral suave (la operación que lo produce):\n"
        "    β ← signo(z) · máx(0, |z| − α·lr)\n"
        "        si |z| ≤ α·lr  →  β = 0  exactamente\n```",
        "1. ¿Cuántos coeficientes dejará el lasso exactamente en cero?\n"
        "2. ¿Y la regresión de cresta?\n"
        "3. ¿Acertará el lasso qué variables son irrelevantes?",
        "De ocho variables, solo tres tienen efecto real. El lasso deja **4 coeficientes exactamente en "
        "cero** y la cresta, **0**: encoge todos pero no anula ninguno. Y de las cinco variables "
        "verdaderamente nulas, el lasso identifica cuatro.",
        "Selecciona y estima en la misma operación, que es lo que lo hizo tan influyente. La misma idea "
        "reaparece treinta años después en "
        "[LoRA](../../papers/foundational/P48_lora/README.md): restringir el espacio de soluciones para "
        "obtener algo más simple y manejable, en vez de ajustar sin restricción y podar después.",
        "Anti-patrón: leer un coeficiente en cero como «esta variable no influye».",
        "print('Cero significa: dadas LAS DEMAS variables y ESTA penalizacion, no aporta.')\n"
        "print('Con dos variables muy correlacionadas, el lasso se queda con una casi al azar.')\n"
        "print('Es una afirmacion condicional sobre el modelo, no causal sobre el mundo.')",
        "La lectura correcta, con el camino de regularización delante:",
        "r = run_paper_lab('lasso', seed=7)['result']\n"
        "for paso in r['camino_de_regularizacion']:\n"
        "    print(f\"alpha={paso['alpha']:<6} variables vivas={paso['no_nulos']}\")\n"
        "print('El conjunto seleccionado DEPENDE de alpha. Elegir alpha es parte del modelo.')",
        "Compara los coeficientes de la variable 4 —copia ruidosa de la primera— en las tres soluciones "
        "y explica qué hace cada penalización con ella.",
        "Ajusta un lasso sobre datos reales con validación cruzada para elegir alpha, y compáralo con una "
        "red elástica. Documenta qué variables sobreviven en cada caso y si el conjunto es estable al "
        "cambiar la partición.",
        "Guarda los tres vectores de coeficientes y el camino de regularización, con tu criterio para "
        "elegir alpha.",
        "Un modelo con menos variables es más fácil de defender. La vía opuesta —muchos modelos malos "
        "combinados— resulta funcionar igual de bien.",
    ),
    "P78_adaboost": _auto(
        "adaboost",
        "Un clasificador que apenas supera al azar parece inútil. Entrena uno, mira qué falla, sube el "
        "peso de esos ejemplos y entrena otro que se concentre en ellos. Repite. La suma ponderada de "
        "todos ellos resuelve lo que ninguno sabía resolver.",
        "```text\nPara t = 1..T:\n"
        "    hₜ ← aprendiz débil sobre la distribución de pesos Dₜ\n"
        "    εₜ ← error PONDERADO de hₜ\n"
        "    αₜ ← ½·ln((1 − εₜ)/εₜ)          ← más voto a quien menos falla\n"
        "    Dₜ₊₁(i) ∝ Dₜ(i)·exp(−αₜ·yᵢ·hₜ(xᵢ))   ← sube el peso de lo fallado\n\n"
        "H(x) = signo( Σ αₜ·hₜ(x) )\n```",
        "1. ¿Cuánto acierta el mejor tocón individual sobre una banda central?\n"
        "2. ¿Y el conjunto?\n"
        "3. ¿Qué le pasa al peso del ejemplo más difícil?",
        "Ningún tocón describe una banda: el mejor de los 22 acierta el **75 %**. El conjunto ponderado "
        "llega al **91,7 %** en la tercera ronda. Y el peso máximo pasa de 0,0833 —el reparto uniforme "
        "inicial— a 0,293: la atención se concentra donde el conjunto todavía falla.",
        "La clave está en `α`: no es una media de opiniones, es una media **ponderada por competencia**, "
        "y el peso sale de una fórmula, no de un ajuste manual. Ese esquema —modelos en serie, cada uno "
        "corrigiendo el residuo del anterior— es el que domina hoy los datos tabulares en forma de "
        "gradient boosting y XGBoost.",
        "Anti-patrón: aplicar boosting a datos con etiquetas ruidosas sin pensarlo.",
        "print('AdaBoost sube el peso de lo que falla. Si un ejemplo esta MAL etiquetado,')\n"
        "print('nunca lo va a acertar, y su peso crece ronda tras ronda.')\n"
        "print('El conjunto acaba dedicando su capacidad a memorizar el error.')",
        "Dónde mirar para detectarlo:",
        "r = run_paper_lab('adaboost', seed=7)['result']\n"
        "print('peso maximo final:', max(r['pesos_finales']))\n"
        "print('reparto inicial  :', round(1/r['ejemplos'], 4))\n"
        "print('Un peso que se dispara sobre uno o dos ejemplos es una senal de alarma,')\n"
        "print('no una senal de que el algoritmo esta trabajando bien.')",
        "Sigue la historia del conjunto ronda a ronda y localiza en qué momento supera al mejor tocón "
        "individual.",
        "Aplica boosting a un conjunto real, mide exactitud en entrenamiento y en prueba a lo largo de las "
        "rondas, e identifica dónde empieza a sobreajustar. Después introduce un 5 % de etiquetas "
        "erróneas y repite.",
        "Guarda la historia del conjunto por rondas y tu explicación de por qué el ruido de etiqueta es "
        "el punto débil del método.",
        "Los modelos en serie funcionan. Falta la otra forma de combinar: en paralelo, y buscando que se "
        "parezcan lo menos posible.",
    ),
    "P79_random_forest": _auto(
        "random_forest",
        "Si promedias cien opiniones idénticas, obtienes la misma opinión. Para que promediar sirva, las "
        "opiniones tienen que ser distintas. Breiman fuerza esa diferencia limitando a propósito lo que "
        "cada árbol puede mirar — y sus árboles empeoran, y el bosque mejora.",
        "```text\nError del bosque ≲ ρ̄·(1 − s²)/s²\n\n"
        "    ρ̄ = correlación media entre árboles     ← bajar esto es la aportación\n"
        "    s  = fuerza media de cada árbol         ← subir esto es lo obvio\n\n"
        "bagging          → diversidad por los DATOS\n"
        "subespacio de m  → diversidad por las PREGUNTAS que cada árbol puede hacer\n```",
        "1. ¿Mejora el bosque a su árbol medio en todos los casos?\n"
        "2. ¿Qué le pasa al acuerdo entre árboles al bajar las variables por árbol?\n"
        "3. ¿Y al árbol individual?",
        "El bosque mejora a su árbol medio en las cuatro configuraciones. Al bajar de 8 variables por "
        "árbol a 2, el **acuerdo cae de 0,7238 a 0,5399** —los árboles se descorrelacionan— y el **árbol "
        "medio empeora de 0,3087 a 0,4047**. Las dos cosas se mueven a la vez, en direcciones opuestas.",
        "Por eso `m` es un hiperparámetro y no una constante: arbitra entre fuerza y correlación, y su "
        "óptimo depende de los datos. En esta tabla gana `m = 8`; en otros conjuntos gana un valor "
        "pequeño. Lo transferible no es el número: es que existe el compromiso y hay que buscarlo.",
        "Anti-patrón: creer que un bosque mejora siempre por tener más árboles.",
        "print('Anadir arboles reduce la varianza del voto y satura pronto.')\n"
        "print('Lo que NO hace es reducir el sesgo: si todos los arboles se equivocan igual,')\n"
        "print('promediar mil de ellos devuelve el mismo error.')",
        "Lo que sí mueve la aguja, con el barrido delante:",
        "r = run_paper_lab('random_forest', seed=7)['result']\n"
        "for b in r['barrido_de_variables_por_arbol']:\n"
        "    print(f\"m={b['variables_por_arbol']:>2}  arbol medio={b['error_medio_de_un_arbol']:<8}\"\n"
        "          f\" bosque={b['error_del_bosque']:<8} acuerdo={b['acuerdo_medio_entre_arboles']}\")\n"
        "print('mejor configuracion aqui:', r['mejor_configuracion'])",
        "Comprueba en la salida que el acuerdo baja de forma monótona al reducir `m`, y que el error del "
        "árbol individual sube de forma monótona. Explica por qué eso implica que existe un óptimo.",
        "Entrena un bosque real sobre un conjunto tabular, barre `m` y dibuja las dos curvas: error del "
        "árbol medio y error del bosque. Localiza el óptimo y compáralo con la heurística `√p`.",
        "Guarda el barrido con las tres columnas y tu explicación del compromiso entre fuerza y "
        "correlación.",
        "Dos artículos del mismo autor y del mismo año. El segundo no propone un método: propone una "
        "discusión sobre para qué sirven los modelos.",
    ),
    "P80_dos_culturas": _auto(
        "dos_culturas",
        "Hay dos formas de usar un modelo. Una supone que los datos salen de un mecanismo con forma "
        "conocida y usa el modelo para describirlo. La otra trata el mecanismo como desconocido y solo "
        "pregunta si predice. Breiman sostiene que la primera se ha equivocado durante décadas.",
        "```text\nCultura del modelo de datos     Cultura algorítmica\n"
        "────────────────────────────    ─────────────────────────\n"
        "supone la forma del mecanismo    trata el mecanismo como desconocido\n"
        "valida supuestos                 mide exactitud FUERA DE MUESTRA\n"
        "interpreta coeficientes          acepta modelos difíciles de leer\n\n"
        "Efecto Rashomon: muchos modelos con exactitud casi igual\n"
        "                 y explicaciones incompatibles entre sí\n```",
        "1. ¿Cuánto acierta el modelo lineal si el mecanismo real es una interacción?\n"
        "2. ¿Y añadiendo el término de interacción?\n"
        "3. ¿Cuántos modelos distintos alcanzan una exactitud parecida?",
        "El modelo lineal en las variables originales llega a **0,70** y con el término de interacción, a "
        "**0,90**. Y cuatro modelos distintos alcanzan exactitudes entre 0,8625 y 0,9 —una banda de "
        "0,0375— con **coeficientes muy distintos** para la primera variable y para su copia ruidosa.",
        "Ese es el efecto Rashomon y es el argumento más incómodo del artículo: si varios modelos casi "
        "equivalentes cuentan historias distintas sobre qué variable importa, entonces la historia no "
        "está determinada por los datos. Interpretar los coeficientes de uno de ellos como «el efecto» de "
        "cada variable es elegir una narración entre varias compatibles.",
        "Anti-patrón: interpretar coeficientes de un modelo cuya forma no se ha validado.",
        "print('Si el mecanismo real es x1*x2 y ajustas un modelo lineal en x1 y x2,')\n"
        "print('los coeficientes NO son «el efecto de cada variable»: son el mejor')\n"
        "print('ajuste lineal a algo que no es lineal. Describen un mecanismo inexistente.')",
        "La separación que propone Breiman entre los dos objetivos:",
        "r = run_paper_lab('dos_culturas', seed=7)['result']\n"
        "print('mecanismo real  :', r['mecanismo_real'])\n"
        "print('modelo de datos :', r['cultura_del_modelo_de_datos']['exactitud_prueba'])\n"
        "print('algoritmico     :', r['cultura_algoritmica']['exactitud_prueba'])\n"
        "for m in r['efecto_rashomon']:\n"
        "    print('  rashomon:', m)",
        "Compara los coeficientes de x1 y de x4 —su copia ruidosa— entre los modelos Rashomon, y explica "
        "por qué un ranking de importancia de variables puede ser inestable.",
        "Ajusta a un mismo conjunto tres modelos de familias distintas con exactitudes parecidas y compara "
        "sus explicaciones de qué variable importa. Documenta si coinciden.",
        "Guarda la banda de exactitud de los modelos Rashomon con sus coeficientes, y tu criterio para "
        "decidir cuándo la interpretación de un coeficiente está justificada.",
        "Si el modelo se juzga por predecir, hay que saber qué variables darle. Y elegirlas de una en una "
        "falla de dos formas distintas.",
    ),
    "P81_seleccion_de_caracteristicas": _auto(
        "seleccion_de_caracteristicas",
        "Ordenar las variables por su correlación con la etiqueta y quedarse con las mejores parece "
        "sensato. Falla en las dos direcciones: descarta variables inútiles solas e imprescindibles "
        "juntas, y descarta variables «redundantes» que juntas cancelan ruido.",
        "```text\nCaso 1 — complementariedad:\n"
        "    a, b ∈ {−1, +1},  y = 1 si a·b > 0\n"
        "    correlación(a, y) ≈ 0   correlación(b, y) ≈ 0   y JUNTAS lo determinan\n\n"
        "Caso 2 — redundancia útil:\n"
        "    r1 = señal + ruido₁,  r2 = señal + ruido₂\n"
        "    promediarlas reduce la varianza del ruido a la mitad\n```",
        "1. ¿Cuánto acierta un clasificador con «a» sola? ¿Y con «b» sola?\n"
        "2. ¿Y con las dos?\n"
        "3. ¿Mejora promediar dos variables que miden lo mismo?",
        "Con «a» sola se acierta **0,5** y con «b» sola, **0,5083**: el azar. Con las dos, **1,0**. Y sus "
        "correlaciones univariantes con la etiqueta son 0,09 y 0,009 — un ranking las descartaría antes "
        "de llegar a mirarlas juntas. En sentido contrario, promediar «r1» y «r2» baja el error de "
        "estimación de 0,5379 a 0,3003.",
        "Los dos casos tienen la misma consecuencia práctica: el ranking univariante es un método con "
        "modos de fallo conocidos, y conviene usarlo sabiéndolos. El artículo ordena las alternativas —"
        "filtros, envolturas, métodos embebidos— y el lasso de "
        "[P77](../../papers/foundational/P77_lasso/README.md) es un ejemplo de la tercera familia.",
        "Anti-patrón: eliminar variables correlacionadas entre sí «porque son redundantes».",
        "print('Dos variables que miden lo mismo con ruido independiente NO sobran:')\n"
        "print('promediarlas reduce la varianza del ruido.')\n"
        "print('«Redundante» es una propiedad de la informacion, no de la correlacion.')",
        "La comprobación numérica, sobre las mismas variables:",
        "r = run_paper_lab('seleccion_de_caracteristicas', seed=7)['result']\n"
        "print('complementariedad:', r['caso_1_variables_inutiles_por_separado'])\n"
        "print('redundancia util :', r['caso_2_variables_redundantes'])",
        "Revisa el ranking univariante de la salida y señala en qué posición quedarían «a» y «b», las dos "
        "variables que determinan por completo la etiqueta.",
        "Toma un conjunto propio y compara tres estrategias: ranking univariante, selección hacia delante "
        "con envoltura, y lasso. Documenta cuántas variables selecciona cada una y si coinciden.",
        "Guarda los dos contraejemplos con sus números y tu enunciado de los dos modos de fallo del "
        "ranking univariante.",
        "Ya sabemos qué darle al modelo. Falta comprobar que el número que devuelve significa lo que "
        "parece significar.",
    ),
    "P82_calibracion": _auto(
        "calibracion",
        "Un modelo dice «0,9». ¿Significa que de cada diez casos así, nueve ocurren? No necesariamente. "
        "Un modelo puede ordenar perfectamente y estimar fatal, y las dos cosas se miden con métricas "
        "distintas que casi nunca se reportan juntas.",
        "```text\nOrdenar bien   → AUC alto\n"
        "Estimar bien   → calibración: de los casos con p̂ ≈ 0,9, ocurre el 90 %\n\n"
        "Diagrama de fiabilidad: p̂ media por tramo  frente a  frecuencia observada\n"
        "Brier = media((p̂ − y)²)     ← castiga orden Y calibración a la vez\n```",
        "1. ¿Qué AUC tiene el modelo?\n"
        "2. ¿Coinciden sus probabilidades con las frecuencias observadas?\n"
        "3. ¿Cambia el AUC al recalibrar?",
        "El modelo tiene AUC **0,8214** —ordena bien— y un error medio de calibración de **0,0542**: en "
        "los tramos altos predice más de lo que ocurre y en los bajos, menos. Tras recalibrar, el Brier "
        "baja y el AUC apenas se mueve: la calibración es monótona, **reescala pero no reordena**.",
        "Importa cuando la salida se usa para algo más que ordenar: decidir con un umbral de coste, "
        "combinar la probabilidad con otra, o presentarla a una persona. Un modelo bien ordenado y mal "
        "calibrado toma decisiones sistemáticamente sesgadas, y ningún ranking lo delata.",
        "Anti-patrón: calibrar con los mismos datos con los que se evalúa la calibración.",
        "print('La calibracion se AJUSTA a unos datos: si evaluas sobre esos mismos,')\n"
        "print('el error de calibracion sale casi cero por construccion.')\n"
        "print('Hace falta un conjunto aparte, igual que para cualquier otro ajuste.')",
        "Lo que hay que reportar, y en qué conjunto:",
        "r = run_paper_lab('calibracion', seed=7)['result']\n"
        "print('AUC antes / despues :', r['auc_del_modelo'], '/', r['auc_tras_calibrar'])\n"
        "print('Brier antes / despues:', r['brier_antes'], '/', r['brier_despues'])\n"
        "for fila in r['diagrama_de_fiabilidad_antes']:\n"
        "    print(f\"  {fila['intervalo']}  predicho={fila['prob_media_predicha']:<8}\"\n"
        "          f\" observado={fila['frecuencia_observada']:<8} desv={fila['desviacion']}\")",
        "Localiza en el diagrama de fiabilidad el tramo con mayor desviación y di en qué dirección se "
        "equivoca el modelo allí.",
        "Calibra un modelo tuyo con escalado de Platt y con regresión isotónica, usando un conjunto "
        "reservado. Compara AUC y Brier antes y después, y decide cuál usarías según el tamaño de los "
        "datos.",
        "Guarda el diagrama de fiabilidad antes y después con los dos números —AUC y Brier— y tu criterio "
        "de cuándo la calibración importa.",
        "Ya se mide bien lo que el modelo predice. Volvemos a mirar los datos: cómo verlos cuando tienen "
        "demasiadas dimensiones para dibujarlos.",
    ),
    "P83_tsne": _auto(
        "tsne",
        "En dimensión alta hay muchísimo más «sitio lejos» que cerca. Al aplastar a dos dimensiones, todo "
        "lo moderadamente lejano se apiña en el centro. La solución de t-SNE es usar en el mapa una "
        "distribución con cola pesada, que deja sitio a lo lejano sin comprimir lo cercano.",
        "```text\nEn el espacio original:  p_ij  ∝ exp(−‖xᵢ − xⱼ‖² / 2σ²)      gaussiana\n"
        "En el mapa:              q_ij  ∝ (1 + ‖yᵢ − yⱼ‖²)⁻¹           t de Student, 1 g.l.\n\n"
        "Minimizar  KL(P ‖ Q)  por descenso de gradiente\n\n"
        "La cola de Student deja MUCHÍSIMA más masa lejos: eso resuelve el apiñamiento.\n```",
        "1. ¿Conservarán dos ejecuciones distintas los mismos vecinos?\n"
        "2. ¿Colocarán los puntos en los mismos sitios?\n"
        "3. ¿Cuánta más masa deja la t de Student a distancia 8?",
        "Las dos ejecuciones conservan la misma proporción de vecinos (**0,9556** ambas) y colocan los "
        "puntos en sitios distintos: el desplazamiento medio es **2,85**. A distancia 8, la t de Student "
        "deja una masa del orden de **10¹²** veces mayor que la gaussiana.",
        "De ahí las tres reglas de lectura que casi nadie aplica: la posición absoluta no significa nada, "
        "la distancia entre grupos no es interpretable y el tamaño aparente de un grupo tampoco. Lo único "
        "que t-SNE promete preservar es la **vecindad**. Es una herramienta de exploración, no una "
        "reducción de dimensionalidad para alimentar otro modelo.",
        "Anti-patrón: interpretar la distancia entre dos grupos en un mapa t-SNE.",
        "print('«Estos dos grupos estan lejos, luego son muy distintos»: no se sigue.')\n"
        "print('t-SNE optimiza vecindades locales; las distancias grandes no estan restringidas.')\n"
        "print('Y con otra semilla, los mismos grupos pueden quedar mas cerca o mas lejos.')",
        "Lo que sí se puede afirmar de un mapa t-SNE:",
        "r = run_paper_lab('tsne', seed=7)['result']\n"
        "print('vecinos conservados, ejecucion 1:', r['vecinos_conservados_ejecucion_1'])\n"
        "print('vecinos conservados, ejecucion 2:', r['vecinos_conservados_ejecucion_2'])\n"
        "print('desplazamiento medio entre ambas:', r['desplazamiento_medio_entre_ejecuciones'])\n"
        "print('-> la VECINDAD es estable; la POSICION no.')",
        "Mira la tabla de colas y calcula a partir de qué distancia la diferencia entre gaussiana y "
        "Student pasa de ser un factor pequeño a varios órdenes de magnitud.",
        "Aplica t-SNE a un conjunto real con dos perplejidades muy distintas y dos semillas. Documenta qué "
        "conclusiones sobreviven a los cuatro mapas y cuáles no.",
        "Guarda la comparación entre las dos ejecuciones y tus tres reglas de lectura de un mapa t-SNE.",
        "Ya se ve la estructura. Ahora lo contrario: encontrar los puntos que no pertenecen a ninguna.",
    ),
    "P84_isolation_forest": _auto(
        "isolation_forest",
        "Todos los métodos de detección de anomalías modelaban primero qué es normal. Este da la vuelta a "
        "la pregunta: corta el espacio al azar y cuenta cuántos cortes hacen falta para dejar cada punto "
        "solo. Lo raro está donde hay poca gente, y se queda solo enseguida.",
        "```text\nh(x) = número de cortes aleatorios para aislar x\n\n"
        "Puntuación:  s(x) = 2^(−E[h(x)] / c(m))\n"
        "    c(m) = longitud media de camino en un árbol de búsqueda binaria con m nodos\n\n"
        "s → 1  : se aísla enseguida     → anomalía\n"
        "s → 0,5: camino medio            → normal\n```",
        "1. ¿En cuántos cortes se aísla un punto anómalo?\n"
        "2. ¿Y uno normal?\n"
        "3. ¿Quedan las anomalías en las primeras posiciones del ranking?",
        "Los anómalos se aíslan en **2,27 cortes** de media y los normales en **6,64**. La puntuación "
        "traduce eso a 0,772 frente a 0,471. Y las **3 de 3** anomalías reales quedan en las tres "
        "primeras posiciones del ranking.",
        "La inversión conceptual es lo valioso: no hay que suponer ninguna forma para la distribución "
        "normal, no hay que calcular distancias entre todos los pares, y el coste es lineal. El método "
        "detecta bien anomalías **globales** —puntos alejados de todo— y mal las **locales**, que viven "
        "dentro de la nube con densidad distinta.",
        "Anti-patrón: usar un bosque de aislamiento para anomalías locales.",
        "print('Un punto dentro de la nube pero en una zona de densidad distinta')\n"
        "print('NO se aisla antes que sus vecinos: este metodo no lo va a ver.')\n"
        "print('Para eso existe el factor de anomalia local (LOF), con otra idea.')",
        "Lo que sí detecta bien, con los números delante:",
        "r = run_paper_lab('isolation_forest', seed=7)['result']\n"
        "print('camino medio normales :', r['longitud_media_de_camino_normales'])\n"
        "print('camino medio anomalos :', r['longitud_media_de_camino_anomalos'])\n"
        "for fila in r['top_5_del_ranking']:\n"
        "    print('  ', fila)",
        "Comprueba en el top del ranking cuántas de las tres anomalías reales aparecen, y qué puntuación "
        "separa a las anomalías del resto.",
        "Aplica un bosque de aislamiento a un registro real de eventos, ajusta la proporción esperada de "
        "anomalías y revisa a mano las veinte primeras. Documenta cuántas eran anomalías de verdad.",
        "Guarda la comparación de longitudes de camino y tu criterio para elegir entre detección global y "
        "local.",
        "Los datos ya se agrupan, se visualizan y se auditan. Queda el problema de predecir cuando la "
        "mayor parte de la tabla está vacía.",
    ),
    "P85_factorizacion_matricial": _auto(
        "factorizacion_matricial",
        "Una matriz de usuarios por artículos con el 99 % de celdas vacías. La idea: cada usuario y cada "
        "artículo se describen con unos pocos números —factores latentes— que nadie declara y que salen "
        "del ajuste. La predicción es el producto escalar de ambos, más los sesgos.",
        "```text\nr̂(u,i) = μ + b_u + b_i + p_u · q_i\n\n"
        "    μ    media global\n"
        "    b_u  ¿este usuario puntúa alto o bajo en general?\n"
        "    b_i  ¿este artículo gusta a todos o a nadie?\n"
        "    p_u·q_i  el gusto propiamente dicho\n\n"
        "Se ajusta SOLO sobre las celdas observadas, con regularización.\n```",
        "1. ¿Qué error da predecir siempre la media?\n"
        "2. ¿Y añadiendo solo los sesgos?\n"
        "3. ¿Y con dos factores latentes?",
        "Sobre las celdas que el modelo nunca vio: predecir la media da RMSE **0,7989**; solo los sesgos, "
        "**0,5786**; con dos factores latentes, **0,3691**. Los sesgos hacen más de la mitad del camino "
        "antes de que aparezca ningún «gusto».",
        "Ese es el mensaje práctico del artículo y el que más se salta: modelar primero lo aburrido. Hay "
        "usuarios que puntúan alto todo y artículos que gustan a todos, y si no lo separas, tus factores "
        "latentes acaban aprendiendo eso en vez de aprender preferencias. Sin las dos líneas base, un "
        "RMSE suelto no dice nada.",
        "Anti-patrón: evaluar un recomendador solo por el error de predicción de la nota.",
        "print('El Netflix Prize se gano optimizando RMSE. Netflix nunca desplego el modelo ganador.')\n"
        "print('Lo que importa en produccion es el orden de los diez primeros, la diversidad,')\n"
        "print('la novedad y el coste de servirlo. Acertar la nota es otro objetivo.')",
        "Las líneas base sin las que el número no se puede leer:",
        "r = run_paper_lab('factorizacion_matricial', seed=7)['result']\n"
        "print('densidad de la matriz     :', r['densidad'])\n"
        "print('RMSE prediciendo la media :', r['rmse_prediciendo_la_media'])\n"
        "print('RMSE solo con sesgos      :', r['rmse_solo_con_sesgos'])\n"
        "print('RMSE con factores latentes:', r['rmse_con_factores_latentes'])",
        "Mira los vectores de factores de usuario y comprueba si se separan en dos grupos. Nadie le dijo "
        "al modelo que existieran.",
        "Implementa la factorización sobre un conjunto público de valoraciones, con regularización elegida "
        "por validación. Compara con las dos líneas base y con un recomendador por popularidad.",
        "Guarda la comparación con las dos líneas base y tu explicación de por qué los sesgos van antes "
        "que los factores.",
        "Queda un tipo de dato que no se comporta como los demás: el que llega ordenado en el tiempo, "
        "donde el futuro no se puede barajar con el pasado.",
    ),
    "P86_m4": _auto(
        "m4",
        "Cien mil series reales, sesenta y un métodos, evaluación a ciegas y métricas declaradas de "
        "antemano. Es lo más parecido a un experimento controlado que ha tenido la predicción de series "
        "temporales, y su resultado incomoda a todo el mundo.",
        "```text\nDentro de muestra : ajustar el pasado. Un polinomio de grado alto siempre gana.\nFuera de muestra  : predecir lo que no se ha visto. Ahí gana otra cosa.\n\n"
        "El error de todo backtesting mal hecho es evaluar con datos que el modelo\n"
        "ya vio, aunque sea indirectamente al elegir hiperparámetros.\n```",
        "1. ¿Qué método ajusta mejor dentro de muestra?\n"
        "2. ¿Y fuera de muestra?\n"
        "3. ¿Dónde queda la combinación de tres métodos?",
        "El polinomio de grado 11 ajusta mejor dentro de muestra (MAE 6,31 frente a 7,71 del lineal) y "
        "fuera de muestra se dispara a **6 983**. El mejor fuera de muestra es el polinomio de grado 1, "
        "con 7,48. Y la combinación de tres métodos queda **3ª de 7**: no gana, y tampoco se hunde.",
        "El hallazgo de la M4 sobre 100 000 series es exactamente ese perfil: la combinación rara vez es "
        "la mejor y casi nunca es la peor, así que en ausencia de información sobre la serie concreta es "
        "la apuesta razonable. Y las líneas base ingenuas no son un trámite: son el listón que un método "
        "sofisticado tiene que superar **fuera de muestra** antes de haber demostrado nada.",
        "Anti-patrón: elegir el modelo por su ajuste al histórico.",
        "print('Un polinomio de grado alto reproduce el pasado casi exactamente.')\n"
        "print('Y extrapola a cualquier cosa: en esta serie, un MAE de 6983 a doce pasos.')\n"
        "print('Ajustar el pasado y predecir el futuro son objetivos distintos y a menudo opuestos.')",
        "El protocolo que separa una cosa de la otra:",
        "r = run_paper_lab('m4', seed=7)['result']\n"
        "print('ajuste DENTRO de muestra:', r['ajuste_dentro_de_muestra'])\n"
        "print()\n"
        "for fila in r['resultados_fuera_de_muestra']:\n"
        "    print(f\"  {fila['metodo']:<22} MAE fuera = {fila['mae_fuera_de_muestra']}\")",
        "Compara el orden de los polinomios dentro y fuera de muestra, y explica por qué el ranking se "
        "invierte.",
        "Coge una serie de tu trabajo y evalúala con validación en ventanas deslizantes: varios cortes, "
        "mismo horizonte. Compara tu método favorito contra el ingenuo estacional y contra la combinación "
        "de tres métodos simples.",
        "Guarda las dos tablas —dentro y fuera de muestra— y tu protocolo de backtesting con el número de "
        "ventanas y el horizonte.",
        "Aquí se cierra la ruta clásica: agrupar, dividir, separar, regularizar, combinar y, sobre todo, "
        "medir fuera de muestra. Lo que sigue en el programa es lo que ocurre cuando el modelo aprende "
        "también la representación.",
    ),
})


TRANSFORMER_SPECS: list[dict[str, Any]] = [
    {
        "id": "T01_recurrencia_vs_paralelismo",
        "titulo": "T01 — Por qué había que quitar la recurrencia",
        "tema": "el problema que motiva el paper",
        "objetivos": [
            "Cuantificar el coste secuencial de un RNN frente a una capa de atención.",
            "Distinguir «longitud del camino entre posiciones» de «número de operaciones».",
        ],
        "intuicion": (
            "Un RNN es una fila de personas pasándose un mensaje al oído: la persona 100 no puede empezar "
            "hasta que la 99 termine. La atención es una sala donde todos leen el mismo tablón a la vez."
        ),
        "concepto": (
            "```text\n"
            "               operaciones por capa   pasos secuenciales   camino máximo\n"
            "recurrente      O(n · d²)                   O(n)               O(n)\n"
            "self-attention  O(n² · d)                   O(1)               O(1)\n"
            "```\n\n"
            "(Tabla 1 del paper. `n` = longitud de secuencia, `d` = dimensión de representación.)"
        ),
        "codigo": (
            "def tabla(n, d):\n"
            "    return {\n"
            "        'n': n,\n"
            "        'recurrente_ops': n * d * d,\n"
            "        'attention_ops': n * n * d,\n"
            "        'pasos_secuenciales_rnn': n,\n"
            "        'pasos_secuenciales_attn': 1,\n"
            "    }\n"
            "\n"
            "for n in (10, 100, 512, 2048):\n"
            "    show(tabla(n, d=512))"
        ),
        "prediccion": "¿A partir de qué `n` la atención hace MÁS operaciones que la recurrencia, con d=512?",
        "experimento": (
            "d = 512\n"
            "for n in (64, 256, 512, 1024, 4096):\n"
            "    rec, att = n * d * d, n * n * d\n"
            "    print(f'n={n:>5} · recurrente={rec:>12,} · attention={att:>14,} · '\n"
            "          f\"{'attention más cara' if att > rec else 'attention más barata'}\")"
        ),
        "salida": (
            "El cruce está en `n = d`. Por debajo de la dimensión del modelo, la atención sale barata; por "
            "encima, el término cuadrático manda. Por eso las ventanas de contexto largas son un problema "
            "de ingeniería, no un detalle."
        ),
        "antipatron": (
            "print('«El Transformer es más eficiente que el RNN» ← sin condiciones, es falso.')\n"
            "print('Es más PARALELIZABLE siempre; es más eficiente en operaciones solo si n < d.')"
        ),
        "correccion": (
            "enunciado = {\n"
            "    'siempre_cierto': 'pasos secuenciales O(1) frente a O(n) → se aprovecha el hardware paralelo',\n"
            "    'condicionado': 'menos operaciones solo cuando n < d',\n"
            "    'coste_oculto': 'memoria de la matriz de atención: O(n²)',\n"
            "}\n"
            "show(enunciado)"
        ),
        "desafio": "Calcula la memoria de la matriz de atención (n² floats) para n=1024, 8192 y 128000, en MB.",
        "conexion": "Si quitamos la recurrencia, hace falta un mecanismo que relacione posiciones: Q, K y V (T02).",
    },
    {
        "id": "T02_qkv_scaled_dot_product",
        "titulo": "T02 — Q, K, V y el producto escalar escalado",
        "tema": "la ecuación 1 del paper",
        "objetivos": [
            "Explicar qué papel juega cada uno de Q, K y V.",
            "Implementar `softmax(QKᵀ/√d_k)·V` desde cero y verificar sus propiedades.",
        ],
        "intuicion": (
            "Una búsqueda en una biblioteca: **Q** es lo que preguntas, **K** son las etiquetas de los "
            "lomos con las que comparas, y **V** es el contenido que te llevas. Comparas contra K, pero "
            "te llevas V."
        ),
        "concepto": (
            "```text\n"
            "Attention(Q, K, V) = softmax(QKᵀ / √d_k) · V\n"
            "```\n\n"
            "`QKᵀ` mide compatibilidad; `√d_k` normaliza la escala; `softmax` convierte en pesos que "
            "suman 1; multiplicar por `V` mezcla la información."
        ),
        "codigo": (
            "from ai_evolution.papers_lab import scaled_dot_product_attention\n"
            "\n"
            "Q = [[1.0, 0.0, 0.0, 0.0]]\n"
            "K = [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.9, 0.1, 0.0, 0.0]]\n"
            "V = [[10.0, 0.0], [0.0, 10.0], [5.0, 5.0]]\n"
            "r = scaled_dot_product_attention(Q, K, V)\n"
            "print('pesos :', [round(w, 4) for w in r['weights'][0]], '· suma:', round(sum(r['weights'][0]), 6))\n"
            "print('salida:', [round(v, 4) for v in r['output'][0]])"
        ),
        "prediccion": "Q coincide con K[0] y se parece a K[2]. ¿Cuál de los tres valores dominará la salida?",
        "experimento": (
            "for etiqueta, escala in (('con √d_k', True), ('sin escala', False)):\n"
            "    r = scaled_dot_product_attention(Q, K, V, scale=escala)\n"
            "    print(f\"{etiqueta:<11} pesos={[round(w, 4) for w in r['weights'][0]]}\")"
        ),
        "salida": (
            "Los pesos suman exactamente 1 y la salida es una **combinación convexa** de las filas de V: "
            "nunca puede salirse del casco convexo de los valores. La atención mezcla, no inventa."
        ),
        "antipatron": (
            "malos = [2.0, -1.0, 0.5]\n"
            "s = sum(malos)\n"
            "print('normalizar dividiendo por la suma:', [round(m / s, 3) for m in malos])\n"
            "print('→ hay pesos negativos y > 1: ya no es una distribución de probabilidad')"
        ),
        "correccion": (
            "import math\n"
            "e = [math.exp(m) for m in malos]\n"
            "print('softmax:', [round(v / sum(e), 4) for v in e], '· suma:', round(sum(v / sum(e) for v in e), 6))"
        ),
        "desafio": "Haz Q ortogonal a todas las filas de K. ¿Qué distribución sale y qué significa esa entropía máxima?",
        "conexion": "El softmax es la pieza que convierte compatibilidad en distribución. Vale la pena mirarlo solo (T03).",
    },
    {
        "id": "T03_softmax_y_temperatura",
        "titulo": "T03 — Softmax, escala y saturación",
        "tema": "por qué √d_k no es cosmética",
        "objetivos": [
            "Ver cómo la escala de los scores cambia la entropía de la atención.",
            "Relacionar saturación del softmax con gradientes que se apagan.",
        ],
        "intuicion": (
            "El softmax es un mando de contraste. Scores muy grandes → la atención se vuelve un foco que "
            "ilumina un solo punto y deja el resto a oscuras (gradiente ≈ 0 para los demás)."
        ),
        "concepto": (
            "```text\n"
            "softmax(z)_i = exp(z_i) / Σ_j exp(z_j)\n"
            "```\n\n"
            "Si `q` y `k` tienen componentes independientes de media 0 y varianza 1, `q·k` tiene varianza "
            "`d_k`: su magnitud crece como `√d_k`. Dividir por `√d_k` devuelve la varianza a 1."
        ),
        "codigo": (
            "import math\n"
            "\n"
            "def softmax(zs):\n"
            "    m = max(zs)\n"
            "    e = [math.exp(z - m) for z in zs]\n"
            "    return [v / sum(e) for v in e]\n"
            "\n"
            "def entropia(ps):\n"
            "    return -sum(p * math.log(p + 1e-12) for p in ps)\n"
            "\n"
            "base = [2.0, 1.0, 0.5, 0.0]\n"
            "for factor in (0.25, 1, 4, 16):\n"
            "    p = softmax([z * factor for z in base])\n"
            "    print(f'escala ×{factor:<3} → {[round(v, 4) for v in p]} · H={entropia(p):.4f}')"
        ),
        "prediccion": "¿La entropía sube o baja al multiplicar los scores por 16? ¿Qué le pasa al gradiente de los tokens ignorados?",
        "experimento": (
            "import random\n"
            "rng = random.Random(0)\n"
            "for d_k in (4, 64, 512):\n"
            "    q = [rng.gauss(0, 1) for _ in range(d_k)]\n"
            "    ks = [[rng.gauss(0, 1) for _ in range(d_k)] for _ in range(4)]\n"
            "    crudos = [sum(a * b for a, b in zip(q, k)) for k in ks]\n"
            "    escalados = [c / math.sqrt(d_k) for c in crudos]\n"
            "    print(f'd_k={d_k:>3} · H(sin escala)={entropia(softmax(crudos)):.4f}'\n"
            "          f' · H(con escala)={entropia(softmax(escalados)):.4f}')"
        ),
        "salida": (
            "Al crecer `d_k`, la entropía sin escalar se desploma: un token acapara la masa. Con la escala "
            "la entropía se mantiene en un rango sano. **La saturación del softmax es el problema; √d_k es "
            "la solución.**"
        ),
        "antipatron": (
            "grande = [800.0, 799.0]\n"
            "try:\n"
            "    print([math.exp(z) for z in grande])\n"
            "except OverflowError as exc:\n"
            "    print('OverflowError:', exc, '← softmax ingenuo desborda')"
        ),
        "correccion": (
            "print('softmax estable (restando el máximo):', [round(p, 6) for p in softmax(grande)])\n"
            "print('mismo resultado matemático, sin desbordar')"
        ),
        "desafio": "Con d_k=512 y scores sin escalar, calcula el peso del segundo token. ¿Cuánto gradiente le llega?",
        "conexion": "Con la atención bajo control, se puede aplicar a una secuencia consigo misma: self-attention (T04).",
    },
    {
        "id": "T04_self_attention_y_mascara_causal",
        "titulo": "T04 — Self-attention y máscara causal",
        "tema": "atender a la propia secuencia, y no atender al futuro",
        "objetivos": [
            "Distinguir self-attention de cross-attention.",
            "Implementar la máscara causal y comprobar que impide ver el futuro.",
        ],
        "intuicion": (
            "Self-attention es que cada palabra pregunte al resto de **su propia** frase. La máscara "
            "causal es taparle los ojos hacia adelante: si el modelo va a generar el token siguiente, no "
            "puede haberlo visto ya."
        ),
        "concepto": (
            "```text\n"
            "self-attention  : Q, K, V salen de la MISMA secuencia\n"
            "cross-attention : Q del decoder, K y V del encoder\n"
            "máscara causal  : score_ij = −∞ para j > i  →  α_ij = 0\n"
            "```"
        ),
        "codigo": (
            "from ai_evolution.papers_lab import scaled_dot_product_attention\n"
            "\n"
            "X = [[1.0, 0.0], [0.9, 0.1], [0.0, 1.0], [0.1, 0.9]]\n"
            "libre = scaled_dot_product_attention(X, X, X)\n"
            "causal = scaled_dot_product_attention(X, X, X, causal=True)\n"
            "print('sin máscara:')\n"
            "for fila in libre['weights']:\n"
            "    print('  ', [round(w, 3) for w in fila])\n"
            "print('con máscara causal:')\n"
            "for fila in causal['weights']:\n"
            "    print('  ', [round(w, 3) for w in fila])"
        ),
        "prediccion": "¿Qué forma tendrá la matriz enmascarada? ¿Cuánto sumará la primera fila?",
        "experimento": (
            "for i, fila in enumerate(causal['weights']):\n"
            "    futuro = sum(fila[i + 1:])\n"
            "    print(f'fila {i}: suma={sum(fila):.6f} · masa sobre el futuro={futuro:.6f}')"
        ),
        "salida": (
            "Matriz triangular inferior: la masa sobre el futuro es exactamente 0 y cada fila sigue sumando 1. "
            "La posición 0 solo puede atenderse a sí misma, por eso su peso es 1,0."
        ),
        "antipatron": (
            "print('Error frecuente: aplicar la máscara DESPUÉS del softmax.')\n"
            "import math\n"
            "def softmax(zs):\n"
            "    m = max(zs)\n"
            "    e = [math.exp(z - m) for z in zs]\n"
            "    return [v / sum(e) for v in e]\n"
            "p = softmax([2.0, 1.0, 3.0])\n"
            "p_mal = [p[0], p[1], 0.0]\n"
            "print('tras poner a cero el futuro:', [round(v, 4) for v in p_mal], '· suma =', round(sum(p_mal), 4))\n"
            "print('→ ya no suma 1: la distribución quedó rota')"
        ),
        "correccion": (
            "p_bien = softmax([2.0, 1.0, -1e9])\n"
            "print('máscara ANTES del softmax:', [round(v, 6) for v in p_bien], '· suma =', round(sum(p_bien), 6))"
        ),
        "desafio": "Construye la máscara de padding (ignorar tokens de relleno) y comprueba que es independiente de la causal.",
        "conexion": "Una sola cabeza captura un tipo de relación. El paper usa varias en paralelo (T05).",
    },
    {
        "id": "T05_multi_head_attention",
        "titulo": "T05 — Multi-head attention",
        "tema": "varias relaciones a la vez, sin coste extra",
        "objetivos": [
            "Explicar por qué h cabezas de dimensión d/h cuestan lo mismo que una de dimensión d.",
            "Observar que cabezas distintas producen distribuciones distintas.",
        ],
        "intuicion": (
            "Una sola cabeza tiene que decidir una única forma de relacionar palabras. Varias cabezas "
            "permiten que una siga la concordancia, otra la dependencia sintáctica y otra la correferencia "
            "— y luego se concatena todo."
        ),
        "concepto": (
            "```text\n"
            "MultiHead(X) = Concat(head₁, …, head_h) · W^O\n"
            "head_i = Attention(X·W_i^Q, X·W_i^K, X·W_i^V),   d_k = d_v = d_model / h\n"
            "```\n\n"
            "En el modelo base del paper: `d_model = 512`, `h = 8`, `d_k = 64`."
        ),
        "codigo": (
            "from ai_evolution.papers_lab import multi_head_attention\n"
            "\n"
            "X = [[1.0, 0.0, 0.0, 1.0], [0.0, 1.0, 1.0, 0.0], [1.0, 1.0, 0.0, 0.0]]\n"
            "r = multi_head_attention(X, heads=2)\n"
            "for i, cabeza in enumerate(r['heads']):\n"
            "    print(f'cabeza {i}:')\n"
            "    for fila in cabeza:\n"
            "        print('   ', [round(w, 3) for w in fila])"
        ),
        "prediccion": "Las dos cabezas ven mitades distintas del vector. ¿Producirán la misma distribución de atención?",
        "experimento": (
            "for h in (1, 2, 4):\n"
            "    d_model = 8\n"
            "    print(f'h={h} → d_k = {d_model // h} · parámetros de proyección ≈ {3 * d_model * d_model} (constante)')"
        ),
        "salida": (
            "El número de parámetros no depende de `h`: partir `d_model` en más cabezas no cuesta más "
            "memoria. Lo que cambia es la **capacidad de especialización**, no el presupuesto."
        ),
        "antipatron": (
            "try:\n"
            "    multi_head_attention([[1.0] * 5], heads=2)\n"
            "except ValueError as exc:\n"
            "    print('ValueError:', exc)\n"
            "print('→ d_model debe ser divisible entre h; no es una convención, es aritmética')"
        ),
        "correccion": (
            "r = multi_head_attention([[1.0, 0.5, 0.0, 0.2], [0.1, 0.9, 0.3, 0.4]], heads=2)\n"
            "print('salida concatenada:', [[round(v, 3) for v in fila] for fila in r['output']])"
        ),
        "desafio": "Interpreta cada cabeza sobre una frase de 6 tokens y decide si alguna es prescindible (ablación).",
        "conexion": "Falta un detalle grave: hasta aquí el modelo no sabe en qué ORDEN venían los tokens (T06).",
    },
    {
        "id": "T06_positional_encoding",
        "titulo": "T06 — Codificación posicional",
        "tema": "la atención es permutación-equivariante y eso es un problema",
        "objetivos": [
            "Demostrar que sin posición, «el gato come» y «come gato el» son idénticos para la atención.",
            "Verificar las propiedades de la codificación sinusoidal.",
        ],
        "intuicion": (
            "La atención es un conjunto, no una lista: si barajas los tokens, la salida se baraja igual "
            "pero no cambia. Hay que inyectar la posición en el propio vector."
        ),
        "concepto": (
            "```text\n"
            "PE(pos, 2i)   = sin(pos / 10000^{2i/d_model})\n"
            "PE(pos, 2i+1) = cos(pos / 10000^{2i/d_model})\n"
            "```\n\n"
            "Se **suma** al embedding. Las frecuencias distintas por dimensión dan una firma única por "
            "posición y permiten extrapolar a longitudes no vistas en entrenamiento."
        ),
        "codigo": (
            "from ai_evolution.papers_lab import positional_encoding, scaled_dot_product_attention\n"
            "\n"
            "A = [[1.0, 0.0], [0.0, 1.0], [0.5, 0.5]]\n"
            "B = [A[2], A[0], A[1]]                     # misma bolsa de tokens, otro orden\n"
            "sa = scaled_dot_product_attention(A, A, A)['output']\n"
            "sb = scaled_dot_product_attention(B, B, B)['output']\n"
            "print('salida A :', [[round(v, 4) for v in f] for f in sa])\n"
            "print('salida B :', [[round(v, 4) for v in f] for f in sb])\n"
            "print('¿es B una permutación de A?', sorted(map(str, sa)) == sorted(map(str, sb)))"
        ),
        "prediccion": "Si sumamos PE a cada token, ¿seguirá siendo la salida de B una permutación de la de A?",
        "experimento": (
            "def con_posicion(seq):\n"
            "    return [[v + p for v, p in zip(tok, positional_encoding(i, len(tok)))]\n"
            "            for i, tok in enumerate(seq)]\n"
            "\n"
            "sa2 = scaled_dot_product_attention(*[con_posicion(A)] * 3)['output']\n"
            "sb2 = scaled_dot_product_attention(*[con_posicion(B)] * 3)['output']\n"
            "print('con PE, A:', [[round(v, 4) for v in f] for f in sa2])\n"
            "print('con PE, B:', [[round(v, 4) for v in f] for f in sb2])\n"
            "print('¿siguen siendo permutación una de otra?',\n"
            "      sorted(map(str, sa2)) == sorted(map(str, sb2)))"
        ),
        "salida": (
            "Sin PE, reordenar la entrada solo reordena la salida: el modelo es ciego al orden. Con PE, las "
            "salidas dejan de ser permutaciones entre sí: **el orden ya es información**."
        ),
        "antipatron": (
            "print('Error: CONCATENAR la posición en vez de sumarla, «para no contaminar el embedding».')\n"
            "print('Concatenar cambia d_model, multiplica los parámetros de todas las proyecciones')\n"
            "print('y rompe la compatibilidad con las conexiones residuales, que exigen misma dimensión.')"
        ),
        "correccion": (
            "emb = [0.4, -0.2, 0.1, 0.7]\n"
            "pe = positional_encoding(3, 4)\n"
            "print('embedding:', emb)\n"
            "print('PE(pos=3):', [round(v, 4) for v in pe])\n"
            "print('suma     :', [round(a + b, 4) for a, b in zip(emb, pe)], '· dimensión intacta:', len(emb))"
        ),
        "desafio": "Comprueba si PE(pos+k) se puede expresar como una transformación lineal de PE(pos) para k fijo.",
        "conexion": "Con posición y atención resueltas, falta el andamiaje que permite apilar capas: residual y layer norm (T07).",
    },
    {
        "id": "T07_residual_layernorm_ffn",
        "titulo": "T07 — Residual, layer norm y feed-forward",
        "tema": "el andamiaje sin el que la atención no entrena",
        "objetivos": [
            "Ver por qué la conexión residual mantiene vivo el gradiente al apilar capas.",
            "Comprobar el efecto normalizador de layer norm y el papel de la FFN por posición.",
        ],
        "intuicion": (
            "La residual es una autopista por la que la información (y el gradiente) circula sin peajes: "
            "cada subcapa **añade** un ajuste en vez de reemplazar la señal. Layer norm evita que esa suma "
            "se descontrole capa tras capa."
        ),
        "concepto": (
            "```text\n"
            "salida = LayerNorm(x + Sublayer(x))\n"
            "FFN(x) = max(0, x·W₁ + b₁)·W₂ + b₂      aplicada a CADA posición por separado\n"
            "```\n\n"
            "En el modelo base: `d_model = 512`, `d_ff = 2048`. La FFN es donde vive la mayor parte de los "
            "parámetros de cada bloque."
        ),
        "codigo": (
            "from ai_evolution.papers_lab import layer_norm\n"
            "\n"
            "x = [3.0, -1.0, 0.5, 7.5]\n"
            "n = layer_norm(x)\n"
            "print('entrada   :', x)\n"
            "print('layer norm:', [round(v, 4) for v in n])\n"
            "print('media ≈', round(sum(n) / len(n), 6), '· varianza ≈', round(sum(v * v for v in n) / len(n), 4))"
        ),
        "prediccion": "Tras layer norm, ¿cuánto valdrán exactamente la media y la varianza del vector?",
        "experimento": (
            "señal = 1.0\n"
            "print('SIN residual (cada capa multiplica por 0.8):')\n"
            "s = señal\n"
            "for capa in range(1, 13):\n"
            "    s *= 0.8\n"
            "    if capa % 4 == 0:\n"
            "        print(f'  capa {capa:>2} → {s:.6f}')\n"
            "print('CON residual (x + 0.8·x_ajuste, la identidad sobrevive):')\n"
            "s = señal\n"
            "for capa in range(1, 13):\n"
            "    s = s + 0.8 * 0.1 * s\n"
            "    if capa % 4 == 0:\n"
            "        print(f'  capa {capa:>2} → {s:.6f}')"
        ),
        "salida": (
            "Sin residual la señal se apaga exponencialmente con la profundidad; con residual, el camino "
            "identidad la mantiene. Esto es lo que hace **apilables** los 6 bloques del paper (y los "
            "cientos de los modelos actuales)."
        ),
        "antipatron": (
            "import math\n"
            "print('Layer norm sin epsilon, con un vector constante:')\n"
            "v = [2.0, 2.0, 2.0]\n"
            "media = sum(v) / len(v)\n"
            "var = sum((z - media) ** 2 for z in v) / len(v)\n"
            "print('varianza =', var, '→ división por cero')\n"
            "try:\n"
            "    print([(z - media) / math.sqrt(var) for z in v])\n"
            "except ZeroDivisionError as exc:\n"
            "    print('ZeroDivisionError:', exc)"
        ),
        "correccion": (
            "print('con epsilon:', [round(z, 6) for z in layer_norm([2.0, 2.0, 2.0])])\n"
            "print('→ el epsilon no es un detalle de implementación: evita un NaN que se propaga a toda la red')"
        ),
        "desafio": "Cuenta los parámetros de la FFN (d_model=512, d_ff=2048) y compáralos con los de la atención multi-cabeza del mismo bloque.",
        "conexion": "Con el bloque completo se ensamblan encoder y decoder, y aparecen los límites (T08).",
    },
    {
        "id": "T08_encoder_decoder_y_limites",
        "titulo": "T08 — Encoder, decoder, complejidad y qué NO dice el título",
        "tema": "el modelo completo y su lectura honesta",
        "objetivos": [
            "Describir el flujo encoder → cross-attention → decoder.",
            "Enunciar con precisión los límites del paper y del título.",
        ],
        "intuicion": (
            "El encoder lee toda la frase de origen sin restricciones. El decoder escribe de izquierda a "
            "derecha, mirando lo ya escrito (self-attention causal) y lo que el encoder entendió "
            "(cross-attention)."
        ),
        "concepto": (
            "```text\n"
            "encoder ×N : self-attention → FFN                (sin máscara)\n"
            "decoder ×N : self-attention causal → cross-attention → FFN\n"
            "```\n\n"
            "Modelo base del paper: N=6, d_model=512, h=8, d_ff=2048. La familia BERT usa solo el encoder; "
            "la familia GPT, solo el decoder."
        ),
        "codigo": (
            "r = run_paper_lab('transformer', seed=7)['result']\n"
            "show(r['complejidad'])\n"
            "print('normas tras residual + layer norm:', r['norma_tras_layernorm'])"
        ),
        "prediccion": "¿Qué crece más rápido al multiplicar n por 10: el coste de la atención o el del bloque recurrente?",
        "experimento": (
            "memoria_bytes = lambda n: n * n * 4          # matriz de atención en float32\n"
            "for n in (512, 2048, 8192, 128000):\n"
            "    mb = memoria_bytes(n) / 1024 ** 2\n"
            "    print(f'n={n:>7} → matriz de atención ≈ {mb:>12,.1f} MB por cabeza y capa')"
        ),
        "salida": (
            "Con n=128 000 la matriz de atención de UNA cabeza y UNA capa ocupa decenas de gigabytes. Por "
            "eso el contexto largo real no usa atención densa ingenua: usa variantes (atención dispersa, "
            "kernels de E/S optimizada, compresión). Ese es trabajo **posterior** al paper."
        ),
        "antipatron": (
            "print('«Attention Is All You Need» leído literalmente diría que basta la atención.')\n"
            "print('El propio modelo del paper necesita, además:')\n"
            "for pieza in ['FFN por posición', 'conexiones residuales', 'layer normalization',\n"
            "              'codificación posicional', 'embeddings compartidos', 'label smoothing', 'warmup del LR']:\n"
            "    print('  -', pieza)"
        ),
        "correccion": (
            "lectura_correcta = {\n"
            "    'que_elimina': ['recurrencia', 'convolución'],\n"
            "    'que_conserva': ['FFN', 'residual', 'layer norm', 'embeddings', 'codificación posicional'],\n"
            "    'que_gana': 'paralelización y camino O(1) entre posiciones',\n"
            "    'que_paga': 'coste y memoria O(n²) en la longitud de secuencia',\n"
            "    'que_NO_dice': 'que la atención sola baste para construir un modelo entrenable',\n"
            "}\n"
            "show(lectura_correcta)"
        ),
        "desafio": "Escribe en cinco líneas qué hereda BERT del encoder y qué hereda GPT del decoder, sin usar la palabra «Transformer».",
        "conexion": "Con el bloque desmontado, las dos ramas —encoder (P09) y decoder (P10)— se leen sin misterio.",
    },
]


# --------------------------------------------------------------------------- #
# construcción de notebooks
# --------------------------------------------------------------------------- #


def md(source: str) -> dict[str, Any]:
    return {"cell_type": "markdown", "metadata": {}, "source": source.splitlines(keepends=True)}


def code(source: str) -> dict[str, Any]:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source.splitlines(keepends=True),
    }


def notebook(cells: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def build_paper_notebook(paper: dict[str, Any]) -> dict[str, Any]:
    spec = SPECS[paper["dir"]]
    autores = ", ".join(paper["authors"])
    anteriores = "\n".join(f"- {item}" for item in paper["anteriores"])
    posteriores = "\n".join(f"- {item}" for item in paper["posteriores"])
    fuentes = "\n".join(f"- [{f['label']}]({f['url']})" for f in paper["fuentes_primarias"])
    cells = [
        md(
            f"# {paper['id']} — {paper['title_es']}\n\n"
            f"## 1. Título y paper\n\n"
            f"**Paper:** *{paper['title']}*  \n"
            f"**Autoría:** {autores}  \n"
            f"**Año y venue:** {paper['year']} · {paper['venue']}  \n"
            f"**Nivel:** {paper['level']} · **Motor:** `{paper['lab']}`  \n"
            f"**Ficha completa:** [`{paper['dir']}`](../../papers/foundational/{paper['dir']}/README.md)\n\n"
            f"**Hito:** {paper['hito']}\n\n"
            f"{fuentes}\n\n"
            f"> Este notebook implementa una **miniatura** del mecanismo. No reproduce el experimento "
            f"original ni sus métricas: reproduce la idea para que se pueda inspeccionar y discutir.\n"
        ),
        md(
            "## 2. Objetivos\n\n"
            f"1. Explicar qué problema resolvió el paper: {paper['problema']}\n"
            f"2. Ejecutar una implementación mínima de la propuesta: {paper['propuesta']}\n"
            "3. Predecir el resultado antes de ejecutar, y contrastar la predicción con la salida.\n"
            "4. Identificar al menos una limitación de la miniatura y una del paper original.\n"
            "5. Conectar el hito con el siguiente eslabón de la ruta.\n"
        ),
        md(
            "## 3. Prerrequisitos\n\n"
            "- Python 3.11+ y el paquete del programa instalado (`pip install -e .`).\n"
            "- Haber leído la guía [método de lectura en 5 pasadas](../../papers/guides/METODO_DE_LECTURA_EN_5_PASADAS.md).\n"
            "- Hitos previos:\n"
            f"{anteriores}\n"
        ),
        md(f"## 4. Intuición\n\n{spec['intuicion']}\n"),
        md(f"## 5. Concepto mínimo\n\n{spec['concepto']}\n"),
        md(f"## 6. Código explicado\n\n{spec['codigo_md']}\n"),
        code(BOOTSTRAP),
        code(spec["codigo"]),
        md(f"## 7. Predicción antes de ejecutar\n\n{spec['prediccion']}\n\n> Escribe tu respuesta aquí antes de continuar.\n"),
        md("## 8. Experimento controlado\n\nSe varía una sola cosa y se observa el efecto.\n"),
        code(spec["experimento"]),
        md(f"## 9. Salida interpretable\n\n{spec['salida']}\n"),
        md(f"## 10. Comentario pedagógico\n\n{spec['comentario']}\n"),
        md(f"## 11. Error o anti-patrón deliberado\n\n{spec['antipatron_md']}\n"),
        code(spec["antipatron"]),
        md(f"## 12. Corrección\n\n{spec['correccion_md']}\n"),
        code(spec["correccion"]),
        md(f"## 13. Desafío guiado\n\n{spec['desafio_guiado_md']}\n"),
        code(spec["desafio_guiado"]),
        md(f"## 14. Desafío autónomo\n\n{spec['desafio_autonomo']}\n"),
        md(
            "## 15. Evidencia de aprendizaje\n\n"
            f"{spec['evidencia']}\n\n"
            f"Autoevaluación y respuestas esperadas: [ficha del paper](../../papers/foundational/{paper['dir']}/README.md) · "
            f"evaluación formal: [`assessments/papers/{paper['dir']}.md`](../../assessments/papers/{paper['dir']}.md)\n"
        ),
        md(f"## 16. Cierre\n\n{spec['cierre']}\n"),
        md(
            "## 17. Conexión con el siguiente hito\n\n"
            f"{posteriores}\n\n"
            "Ruta completa: [`papers/ROADMAP.md`](../../papers/ROADMAP.md)\n"
        ),
    ]
    return notebook(cells)


def build_transformer_notebook(spec: dict[str, Any]) -> dict[str, Any]:
    objetivos = "\n".join(f"{i}. {item}" for i, item in enumerate(spec["objetivos"], start=1))
    cells = [
        md(
            f"# {spec['titulo']}\n\n"
            "## 1. Título y paper\n\n"
            "**Paper:** *Attention Is All You Need* (Vaswani et al., 2017)  \n"
            "**Fuente primaria:** [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)  \n"
            f"**Foco de esta miniatura:** {spec['tema']}  \n"
            "**Ficha completa:** [`P08_transformer`](../../papers/foundational/P08_transformer/README.md)\n"
        ),
        md(f"## 2. Objetivos\n\n{objetivos}\n"),
        md(
            "## 3. Prerrequisitos\n\n"
            "- Python 3.11+ con el paquete instalado (`pip install -e .`).\n"
            "- Notebook [`P08_transformer`](P08_transformer.ipynb) al menos hojeado.\n"
            "- Álgebra de vectores: producto escalar, norma y softmax.\n"
        ),
        md(f"## 4. Intuición\n\n{spec['intuicion']}\n"),
        md(f"## 5. Concepto mínimo\n\n{spec['concepto']}\n"),
        md("## 6. Código explicado\n\nCódigo mínimo, sin dependencias externas.\n"),
        code(BOOTSTRAP),
        code(spec["codigo"]),
        md(f"## 7. Predicción antes de ejecutar\n\n{spec['prediccion']}\n\n> Escribe tu respuesta antes de continuar.\n"),
        md("## 8. Experimento controlado\n"),
        code(spec["experimento"]),
        md(f"## 9. Salida interpretable\n\n{spec['salida']}\n"),
        md(
            "## 10. Comentario pedagógico\n\n"
            "Esta miniatura aísla **una** pieza del bloque. Aislar es didáctico y también es una "
            "simplificación: en el modelo real todas las piezas interactúan y se entrenan juntas.\n"
        ),
        md("## 11. Error o anti-patrón deliberado\n"),
        code(spec["antipatron"]),
        md("## 12. Corrección\n"),
        code(spec["correccion"]),
        md(f"## 13. Desafío guiado\n\n{spec['desafio']}\n"),
        md(
            "## 14. Desafío autónomo\n\n"
            "Reescribe esta pieza con proyecciones aprendidas y comprueba que tu implementación reproduce "
            "las propiedades verificadas aquí (sumas, formas, invariantes). Documenta la semilla.\n"
        ),
        md(
            "## 15. Evidencia de aprendizaje\n\n"
            "Guarda la salida del experimento, tu predicción previa y una frase sobre qué invariante "
            "acabas de verificar.\n"
        ),
        md(
            "## 16. Cierre\n\n"
            f"Pieza cubierta: **{spec['tema']}**. Ya puede describirse con precisión, sin metáforas.\n"
        ),
        md(f"## 17. Conexión con el siguiente hito\n\n{spec['conexion']}\n"),
    ]
    return notebook(cells)


# --------------------------------------------------------------------------- #
# artefactos derivados
# --------------------------------------------------------------------------- #


RUTA_ETIQUETA = {
    "ruta_minima": "🔗 cadena",
    "ruta_ampliada": "📚 ampliada",
    "ruta_representacion": "🔤 representación",
    "ruta_agentes": "🤖 agentes",
    "ruta_memoria": "🧠 memoria",
    "ruta_arquitectura": "🏗️ arquitectura",
    "ruta_evaluacion": "🛡️ evaluación",
    "ruta_fundamentos": "🧭 fundamentos",
    "ruta_simbolica": "♟️ simbólica",
    "ruta_clasica": "📈 clásica",
}


RUTA_TITULO = {
    "ruta_minima": "🔗 Ruta mínima — la cadena canónica",
    "ruta_ampliada": "📚 Ruta ampliada — lo que la cadena mínima no cubre",
    "ruta_representacion": "🔤 Ruta de representación — cómo el lenguaje llegó a un formato único",
    "ruta_agentes": "🤖 Ruta de agentes — decisión secuencial, razonamiento y multiagente",
    "ruta_memoria": "🧠 Ruta de memoria y contexto — qué recuerda el modelo y cómo",
    "ruta_arquitectura": "🏗️ Ruta de arquitectura y entrenamiento — el andamiaje de todo lo demás",
    "ruta_evaluacion": "🛡️ Ruta de evaluación y seguridad — cómo se decide que un modelo sirve",
    "ruta_fundamentos": "🧭 Ruta de fundamentos — de dónde sale el campo y con qué método se juzga",
    "ruta_simbolica": "♟️ Ruta simbólica — buscar, deducir, planificar y acordar",
    "ruta_clasica": "📈 Ruta clásica — aprender la regla de los datos, y medirla bien",
}

CARDINAL = {4: "Cuatro", 5: "Cinco", 6: "Seis", 7: "Siete", 8: "Ocho", 9: "Nueve", 10: "Diez"}


def nombre_corto(item: dict[str, Any]) -> str:
    """El nombre con el que se conoce al paper, tomado del H1 de su propia ficha.

    `title_es` es el título completo traducido y no cabe en una tabla; el H1 de la
    ficha («# P08 — Transformer») ya lleva el nombre corto curado a mano.
    """
    encabezado = (ROOT / "papers" / "foundational" / item["dir"] / "README.md").read_text(
        encoding="utf-8"
    ).splitlines()[0]
    _, _, corto = encabezado.lstrip("# ").partition("—")
    return corto.strip() or item["title_es"]


def primera_frase(texto: str) -> str:
    """La primera frase del hito: lo demás es matiz que no cabe en una celda."""
    corte = texto.find(". ")
    return texto[: corte + 1] if corte != -1 else texto


def build_readme_routes(data: dict[str, Any]) -> str:
    """Sección de rutas de `papers/README.md`, generada desde el catálogo.

    Estaba escrita a mano y se quedó atrás: anunciaba seis rutas cuando ya había
    siete, y sus tablas paraban en P33. Generarla desde `papers.json` hace
    imposible que vuelva a mentir sobre su propio contenido.
    """
    bloques = [b for b in data.get("rutas", []) if data.get(b)]
    por_id = {item["id"]: item for item in data["papers"]}
    total = len(data["papers"])
    cardinal = CARDINAL.get(len(bloques), str(len(bloques)))

    lines = [
        f"## 🧭 {cardinal} rutas · {total} papers",
        "",
        f"El eje tiene {len(bloques)} bloques con propósitos distintos. **No se estudian igual.**",
        "Dentro de cada uno, los papers van **en orden cronológico**; entre bloques no hay orden,",
        "porque responden a preguntas diferentes.",
        "",
        "```mermaid",
        "flowchart TD",
    ]
    for n, bloque in enumerate(bloques, start=1):
        ids = data[bloque]
        anios = [por_id[pid]["year"] for pid in ids]
        etiqueta = RUTA_ETIQUETA.get(bloque, bloque)
        lines.append(
            f'    R{n}["{etiqueta}<br/>{ids[0]}–{ids[-1]} · {len(ids)} papers'
            f'<br/>{min(anios)}–{max(anios)}"]'
        )
    lines += [
        f"    R1 -.->|\"se estudia primero,<br/>en orden\"| R2",
        "```",
        "",
    ]
    for bloque in bloques:
        ids = data[bloque]
        nota = data.get("notas_de_ruta", {}).get(bloque, "")
        lines += [f"### {RUTA_TITULO.get(bloque, RUTA_ETIQUETA.get(bloque, bloque))}", ""]
        if nota:
            lines += [nota, ""]
        lines += [
            "| # | Paper | Año | Nivel | Lo que aportó |",
            "|---|---|---:|:---:|---|",
        ]
        for pid in ids:
            item = por_id[pid]
            lines.append(
                f"| [{item['id']}](foundational/{item['dir']}/README.md) | {nombre_corto(item)} "
                f"| {item['year']} | {item['level']} | {primera_frase(item['hito'])} |"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_readme_stats(data: dict[str, Any]) -> str:
    """La tabla de conteos de la portada del eje, desde la verdad verificable."""
    clases = {c for item in data["papers"] for c in item["clases_del_programa"]}
    notebooks = len(list((ROOT / "notebooks" / "papers").glob("*.ipynb")))
    anexos = len(list((ROOT / "papers" / "annexes").glob("A*.md")))
    return (
        "| 📄 Papers | 📓 Notebooks | 🧪 Motores | 🧮 Anexos | 🎓 Niveles | 🔗 Clases enlazadas |\n"
        "|:---:|:---:|:---:|:---:|:---:|:---:|\n"
        f"| **{len(data['papers'])}** | **{notebooks}** | **{len(data['papers'])}** "
        f"| **{anexos}** | **L0–L5** | **{len(clases)}** |\n"
    )


def replace_block(path: Path, marca: str, contenido: str, written: list[str]) -> None:
    """Sustituye el bloque entre `<!-- marca:inicio -->` y `<!-- marca:fin -->`.

    Idempotente: el resto del fichero —que sí está escrito a mano— no se toca.
    """
    inicio, fin = f"<!-- {marca}:inicio -->", f"<!-- {marca}:fin -->"
    texto = path.read_text(encoding="utf-8")
    if inicio not in texto or fin not in texto:
        raise SystemExit(f"{path}: faltan los marcadores `{inicio}` / `{fin}`")
    antes = texto[: texto.index(inicio) + len(inicio)]
    despues = texto[texto.index(fin):]
    nuevo = f"{antes}\n{contenido.rstrip()}\n{despues}"
    if nuevo != texto:
        path.write_text(nuevo, encoding="utf-8", newline="\n")
    written.append(path.relative_to(ROOT).as_posix())


def build_matriz(data: dict[str, Any]) -> str:
    """La vinculación clase ↔ paper en las dos direcciones, desde una sola fuente.

    Existía el enlace en cada ficha y el bloque de vuelta en cada clase, pero no
    había ningún sitio donde ver la relación completa ni comprobar su cobertura.
    """
    import yaml  # local: solo hace falta aquí

    curriculo = yaml.safe_load((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))
    titulo_de, parte_de = {}, {}
    numero_de = {}
    for parte in curriculo["parts"]:
        for leccion in parte["lessons"]:
            titulo_de[leccion["path"]] = leccion["title"]
            parte_de[leccion["path"]] = parte
            numero_de[leccion["path"]] = str(leccion["id"]).zfill(3)

    por_clase: dict[str, list[dict[str, Any]]] = {}
    for item in data["papers"]:
        for clase in item["clases_del_programa"]:
            por_clase.setdefault(clase, []).append(item)

    enlaces = sum(len(v) for v in por_clase.values())
    lines = [
        "# 🔁 Matriz de vinculación clase ↔ paper",
        "",
        "> Generado por `python scripts/generate_papers.py`. No editar a mano.",
        "> La fuente es el campo `clases_del_programa` de [`papers.json`](papers.json).",
        "",
        f"**{len(data['papers'])} papers** · **{len(por_clase)} clases enlazadas** de "
        f"{len(titulo_de)} · **{enlaces} enlaces** · cada enlace se escribe en las dos "
        "direcciones y CI falla si alguna se desincroniza.",
        "",
        "## 📜 De paper a clase",
        "",
        "| # | Paper | Año | Clases que fundamenta |",
        "|---|---|---:|---|",
    ]
    for item in sorted(data["papers"], key=lambda x: (x["year"], x["id"])):
        destinos = " · ".join(
            f"[{numero_de[c]} {titulo_de[c]}](../../{c}/README.md)"
            for c in item["clases_del_programa"]
        )
        lines.append(
            f"| [{item['id']}](../foundational/{item['dir']}/README.md) "
            f"| {nombre_corto(item)} | {item['year']} | {destinos} |"
        )

    lines += ["", "## 🏫 De clase a paper", "",
              "| Clase | Parte | Papers que la fundamentan |", "|---|---|---|"]
    for clase in sorted(por_clase, key=lambda c: numero_de[c]):
        papers = " · ".join(
            f"[{p['id']} {nombre_corto(p)}](../foundational/{p['dir']}/README.md)"
            for p in sorted(por_clase[clase], key=lambda x: x["id"])
        )
        lines.append(
            f"| [{numero_de[clase]} {titulo_de[clase]}](../../{clase}/README.md) "
            f"| {parte_de[clase]['id']} | {papers} |"
        )

    lines += ["", "## 📊 Cobertura por parte", "",
              "| Parte | Clases con paper | Total |", "|---|---:|---:|"]
    for parte in curriculo["parts"]:
        total = len(parte["lessons"])
        con = sum(1 for x in parte["lessons"] if x["path"] in por_clase)
        barra = "█" * con + "·" * (total - con)
        lines.append(f"| {parte['id']} · {parte['title']} | {con} `{barra}` | {total} |")

    lines += [
        "",
        "> [!NOTE]",
        "> Las partes con menos cobertura —MLOps, robótica, generativa por medios— lo están porque",
        "> **el eje todavía no las recorre**, no por olvido. Hoy cubre los fundamentos del campo, la",
        "> IA simbólica, el machine learning clásico, el aprendizaje profundo, los modelos de",
        "> lenguaje y los agentes. Forzar asociaciones en lo que falta sería peor que declararlo.",
        "",
        "---",
        "",
        "[📇 Índice de papers](PAPERS_INDEX.md) · [📜 Eje de papers](../README.md) · "
        "[🏫 Programa](../../README.md)",
    ]
    return "\n".join(lines) + "\n"


def build_index(data: dict[str, Any]) -> str:
    """Índice unificado: UNA tabla maestra ordenada por año, más vistas alternativas.

    Los identificadores PXX son estables y se asignan al incorporar cada paper, así
    que su orden es de incorporación y no significa nada. Para leer, lo que sirve es
    el orden cronológico o el temático.
    """
    ruta_de = {}
    for bloque in data.get("rutas", []):
        for pid in data.get(bloque, []):
            ruta_de[pid] = RUTA_ETIQUETA.get(bloque, bloque)

    por_anio = sorted(data["papers"], key=lambda item: (item["year"], item["id"]))
    lines = [
        "# 📇 Índice de papers fundacionales",
        "",
        "> Generado por `python scripts/generate_papers.py`. No editar a mano.",
        "",
        f"**Papers:** {len(data['papers'])} · **Actualizado:** {data['updated']} · "
        f"**Cobertura:** {por_anio[0]['year']}–{por_anio[-1]['year']}",
        "",
        "> [!NOTE]",
        "> Los identificadores `PXX` son **estables**: se asignan al incorporar cada paper y no",
        "> se renumeran nunca, para no romper enlaces, notebooks ni evaluaciones. Por eso su orden",
        "> es de incorporación y **no significa nada**. Para estudiar, usa el orden cronológico de",
        "> esta tabla o la [vista temática](#vista-tematica).",
        "",
        "## 📅 Tabla maestra — todos los papers, por año",
        "",
        "| Año | # | Paper | Bloque | Nivel | Motor | Ficha | Notebook |",
        "|---:|---|---|---|:---:|---|---|---|",
    ]
    for item in por_anio:
        lines.append(
            f"| **{item['year']}** | {item['id']} | {item['title_es']} "
            f"| {ruta_de.get(item['id'], '—')} | {item['level']} | `{item['lab']}` | "
            f"[ficha](../foundational/{item['dir']}/README.md) | "
            f"[nb](../../notebooks/papers/{item['dir']}.ipynb) |"
        )

    lines += ["", '<a id="vista-tematica"></a>', "", "## 🧭 Vista temática — por bloque", ""]
    for bloque in data.get("rutas", []):
        ids = data.get(bloque, [])
        if not ids:
            continue
        nota = data.get("notas_de_ruta", {}).get(bloque, "")
        lines += [f"### {RUTA_ETIQUETA.get(bloque, bloque)}", "", nota, ""]
        for pid in ids:
            item = next(x for x in data["papers"] if x["id"] == pid)
            lines.append(
                f"- **{item['year']}** · [{item['id']} · {item['title_es']}]"
                f"(../foundational/{item['dir']}/README.md) — {item['hito']}"
            )
        lines.append("")

    if data.get("pendientes_de_ficha"):
        lines += [
            "## 🚧 En construcción",
            "",
            "Papers con **motor y notebook ya implementados y probados**, a los que les falta su",
            "ficha de 18 secciones. No aparecen en la tabla maestra hasta estar completos, para que",
            "el contrato del eje siga siendo verificable.",
            "",
            "| Año | # | Paper | Motor |",
            "|---:|---|---|---|",
        ]
        for item in sorted(data["pendientes_de_ficha"], key=lambda x: x["anio"]):
            lines.append(f"| {item['anio']} | {item['id']} | {item['titulo']} | `{item['motor']}` |")
        lines.append("")

    lines += ["## 📖 Qué resolvió cada uno", ""]
    for item in por_anio:
        lines += [
            f"### {item['id']} · {item['title']} ({item['year']})",
            "",
            f"- **Autoría:** {', '.join(item['authors'])}",
            f"- **Problema anterior:** {item['problema']}",
            f"- **Propuesta:** {item['propuesta']}",
            f"- **Hito:** {item['hito']}",
            f"- **Conceptos:** {', '.join(item['keywords'])}",
            "- **Clases del programa:** "
            + ", ".join(
                f"[{Path(path).name[:3]}](../../{path}/README.md)" for path in item["clases_del_programa"]
            ),
            "- **Fuentes primarias:** "
            + " · ".join(f"[{f['label']}]({f['url']})" for f in item["fuentes_primarias"]),
            "",
        ]
    lines += [
        "## Miniaturas del Transformer",
        "",
        "El tratamiento especial de *Attention Is All You Need* se reparte en ocho notebooks:",
        "",
        "| Miniatura | Foco |",
        "|---|---|",
    ]
    for spec in TRANSFORMER_SPECS:
        lines.append(
            f"| [{spec['titulo']}](../../notebooks/papers/{spec['id']}.ipynb) | {spec['tema']} |"
        )
    lines += [
        "",
        "---",
        "",
        "[⬅️ Volver al eje de papers](../README.md) · "
        "[🗺️ Ruta](../ROADMAP.md) · "
        "[🌐 Fuentes y venues](../guides/FUENTES_Y_VENUES.md)",
        "",
    ]
    return "\n".join(lines)


def build_instructor(item: dict[str, Any]) -> str:
    clases = "\n".join(
        f"- [{Path(path).name}](../../{path}/README.md)" for path in item["clases_del_programa"]
    )
    return f"""# 👩‍🏫 Guía docente — {item['id']} · {item['title_es']}

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *{item['title']}* ({item['year']}, {item['venue']})
**Nivel:** {item['level']} · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *{item['problema']}* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *{item['propuesta']}* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `{item['dir']}.ipynb`, secciones 6–9 | Salida del experimento controlado |
| Interpretación | 15 | Contraste predicción/resultado y anti-patrón (secciones 11–12) | Corrección argumentada |
| Límites y cierre | 15 | Qué NO demuestra la miniatura, qué NO dice el paper | Una limitación por estudiante |

## Errores que aparecerán en clase

1. Atribuir al paper ideas posteriores (revisar la sección 12 de la ficha antes de la sesión).
2. Confundir la miniatura del notebook con una reproducción del experimento original.
3. Aceptar una métrica sin preguntar por tarea, dataset, línea base y protocolo.

## Preguntas para dinamizar

- ¿Qué habría que observar para considerar refutada la propuesta del paper?
- ¿Qué parte del resultado depende de los datos y qué parte del método?
- Si este paper no existiera, ¿qué habría bloqueado el hito siguiente?

## Enlaces de aula

- Ficha completa: [`{item['dir']}`](../../papers/foundational/{item['dir']}/README.md)
- Notebook: [`{item['dir']}.ipynb`](../../notebooks/papers/{item['dir']}.ipynb)
- Evaluación: [`{item['dir']}.md`](../../assessments/papers/{item['dir']}.md)
- Clases del programa relacionadas:
{clases}

---

[⬅️ Guías docentes del eje](README.md)
"""


def build_student(item: dict[str, Any]) -> str:
    return f"""# 🎒 Ficha de estudio — {item['id']} · {item['title_es']}

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *{item['title']}* ({item['year']})
**Nivel:** {item['level']} · **Notebook:** [`{item['dir']}.ipynb`](../../notebooks/papers/{item['dir']}.ipynb)

## En una frase

{item['hito']}

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «{item['problema']}»
3. Abre el notebook y **escribe tu predicción** (sección 7) antes de ejecutar nada.
4. Ejecuta y contrasta. Si acertaste, explica por qué; si fallaste, explica qué supusiste mal.
5. Haz el anti-patrón (sección 11) y su corrección. Es la parte que más se evalúa.
6. Escribe una limitación de la miniatura y una del paper. No las copies de la ficha.

## Checklist de «lo entendí»

- [ ] Sé qué se hacía antes de este paper y por qué no bastaba.
- [ ] Puedo dibujar el mecanismo sin mirar.
- [ ] Ejecuté la miniatura e interpreté su salida sin repetir el texto de la ficha.
- [ ] Sé nombrar una cosa que el paper **no** demostró.
- [ ] Sé qué idea de las que suelen atribuírsele llegó en realidad después.
- [ ] Puedo conectar este hito con el siguiente en una frase.

## Conceptos que debes poder definir

{chr(10).join(f'- `{k}`' for k in item['keywords'])}

## Fuentes primarias

{chr(10).join(f"- [{f['label']}]({f['url']})" for f in item['fuentes_primarias'])}

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/{item['dir']}/README.md)
"""


def build_assessment(item: dict[str, Any]) -> str:
    return f"""# 📝 Evaluación — {item['id']} · {item['title_es']}

> Generado por `python scripts/generate_papers.py`.
> Se evalúa comprensión histórica, lectura crítica e interpretación — no memorización de definiciones.

**Paper:** *{item['title']}* ({item['year']}, {item['venue']}) · **Nivel:** {item['level']}

## Parte A — Contexto histórico (20 pts)

1. (10) Describe el estado del arte **inmediatamente anterior** a este paper y por qué era insuficiente.
   No menciones la solución del paper en tu respuesta.
2. (10) Nombra un trabajo anterior del que este paper depende y explica qué le tomó prestado.

## Parte B — Lectura crítica (20 pts)

3. (10) Localiza en el paper original una afirmación **cuantitativa** y reescríbela indicando tarea,
   dataset, métrica, línea base y condiciones. Cita la tabla o sección.
4. (10) Identifica una idea que hoy se asocia a este paper pero que **apareció después**. Aporta la
   referencia posterior con año.

## Parte C — Interpretación matemática (15 pts)

5. (15) Explica la ecuación central con tus palabras y señala qué ocurre en un caso límite
   (valor 0, dimensión muy grande, secuencia muy larga… según corresponda).

## Parte D — Implementación e interpretación (25 pts)

6. (10) Ejecuta [`{item['dir']}.ipynb`](../../notebooks/papers/{item['dir']}.ipynb) con **tres semillas**
   y reporta qué varía y qué se mantiene.
7. (10) Reproduce el anti-patrón de la sección 11 y explica por qué produce una conclusión errónea.
8. (5) Aporta la corrección con su evidencia.

## Parte E — Límites y transferencia (20 pts)

9. (10) Escribe una limitación de la **miniatura** y una del **paper original**. No pueden ser la misma idea.
10. (10) Conecta este hito con el siguiente de la ruta: ¿qué quedó sin resolver que motivó el paso siguiente?

## Rúbrica

| Nivel | Descripción |
|---|---|
| **A — Excelente** | Distingue hecho documentado, simplificación didáctica e inferencia propia. Cita fuentes primarias con sección o tabla. Sus límites son propios, no copiados. |
| **B — Suficiente** | Explica el mecanismo y ejecuta la miniatura correctamente, pero repite los límites de la ficha y cita de forma imprecisa. |
| **C — Insuficiente** | Describe el paper con narrativa retrospectiva, atribuye ideas posteriores, o presenta la salida de la miniatura como reproducción del experimento original. |

## Criterio automático de rechazo

Se devuelve sin nota cualquier entrega que:

- atribuya al paper resultados, métricas o autores que no aparecen en la fuente primaria;
- presente la ejecución del notebook como reproducción de los resultados del paper;
- cite un paper que no se abrió (se comprueba pidiendo el número de figura o tabla).

---

[⬅️ Evaluaciones del eje](README.md) · [Ficha](../../papers/foundational/{item['dir']}/README.md)
"""


DERIVED_READMES = {
    "instructor/papers/README.md": (
        "# 👩‍🏫 Guías docentes del eje de papers\n\n"
        "Una guía por paper con plan de sesión de 90 minutos, errores esperables en el aula y "
        "preguntas para dinamizar. Generadas por `python scripts/generate_papers.py`.\n\n"
        "| Paper | Guía |\n|---|---|\n"
    ),
    "student/papers/README.md": (
        "# 🎒 Fichas de estudio del eje de papers\n\n"
        "Una ficha por paper con ruta de trabajo y checklist de comprensión. "
        "Tu registro personal va en [`BITACORA.md`](BITACORA.md).\n\n"
        "| Paper | Ficha |\n|---|---|\n"
    ),
    "assessments/papers/README.md": (
        "# 📝 Evaluaciones del eje de papers\n\n"
        "Cada evaluación mide contexto histórico, lectura crítica, interpretación matemática, "
        "implementación, límites y transferencia. Nunca solo definiciones.\n\n"
        "| Paper | Evaluación |\n|---|---|\n"
    ),
}


def write(path: Path, content: str, written: list[str]) -> None:
    """Escribe siempre con LF, en cualquier sistema operativo.

    Sin `newline="\\n"`, Python traduce a CRLF en Windows: el artefacto sería
    distinto según dónde se generó y el manifiesto dejaría de cuadrar en CI.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = content if content.endswith("\n") else content + "\n"
    # se compara en bytes: `read_text(newline=...)` no existe antes de Python 3.13
    if not path.exists() or path.read_bytes() != normalized.encode("utf-8"):
        path.write_text(normalized, encoding="utf-8", newline="\n")
    written.append(path.relative_to(ROOT).as_posix())


def generate() -> list[str]:
    data = load_papers()
    written: list[str] = []

    write(ROOT / "papers" / "catalog" / "PAPERS_INDEX.md", build_index(data), written)
    write(ROOT / "papers" / "catalog" / "MATRIZ_CLASES_PAPERS.md", build_matriz(data), written)

    for item in data["papers"]:
        write(ROOT / "notebooks" / "papers" / f"{item['dir']}.ipynb",
              json.dumps(build_paper_notebook(item), ensure_ascii=False, indent=1), written)
        write(ROOT / "instructor" / "papers" / f"{item['dir']}.md", build_instructor(item), written)
        write(ROOT / "student" / "papers" / f"{item['dir']}.md", build_student(item), written)
        write(ROOT / "assessments" / "papers" / f"{item['dir']}.md", build_assessment(item), written)

    for spec in TRANSFORMER_SPECS:
        write(ROOT / "notebooks" / "papers" / f"{spec['id']}.ipynb",
              json.dumps(build_transformer_notebook(spec), ensure_ascii=False, indent=1), written)

    # la tabla de conteos se escribe DESPUÉS de generar los notebooks: cuenta
    # ficheros en disco, y hacerlo antes dejaba el número corto en cada tanda nueva
    readme = ROOT / "papers" / "README.md"
    replace_block(readme, "stats", build_readme_stats(data), written)
    replace_block(readme, "rutas", build_readme_routes(data), written)

    for rel, header in DERIVED_READMES.items():
        rows = "\n".join(
            f"| {item['id']} · {item['title_es']} | [{item['dir']}.md]({item['dir']}.md) |"
            for item in data["papers"]
        )
        extra = ""
        if rel.startswith("student"):
            extra = (
                "\n\n## Contrato de estudio\n\n"
                "Antes de ejecutar: **predecir**. Después de ejecutar: **interpretar**. "
                "Una ejecución sin predicción previa no cuenta como evidencia de aprendizaje.\n"
            )
        write(ROOT / rel, header + rows + extra + "\n\n---\n\n[⬅️ Eje de papers](../../papers/README.md)\n", written)

    write(
        ROOT / "student" / "papers" / "BITACORA.md",
        "# 🗒️ Bitácora de lectura\n\n"
        "> Plantilla personal. Una entrada por paper. No se genera automáticamente: se escribe.\n\n"
        "## Plantilla\n\n"
        "```text\n"
        "Paper:\nFecha de lectura:\nPasada alcanzada (1-5):\n\n"
        "Qué problema resolvía (con mis palabras):\n"
        "Predicción antes de ejecutar:\n"
        "Resultado observado:\n"
        "¿Acerté? ¿Qué supuse mal?\n"
        "Una limitación que NO estaba en la ficha:\n"
        "Una idea que suele atribuirse a este paper y llegó después:\n"
        "Pregunta que me quedó abierta:\n"
        "```\n\n"
        "## Registro\n\n"
        "| Paper | Fecha | Pasada | Estado |\n|---|---|---|---|\n"
        + "\n".join(f"| {item['id']} | | | ⬜ pendiente |" for item in load_papers()["papers"])
        + "\n\n---\n\n[⬅️ Fichas de estudio](README.md)\n",
        written,
    )

    manifest_files = sorted(set(written)) + sorted(
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "papers").rglob("*")
        if path.is_file() and path.name not in {"manifest.json"}
    )
    manifest = {
        "generated_by": "scripts/generate_papers.py",
        "catalog_updated": data["updated"],
        "papers": len(data["papers"]),
        "notebooks": len(data["papers"]) + len(TRANSFORMER_SPECS),
        "hash": (
            "sha256_lf = SHA-256 del contenido con los saltos de línea normalizados a LF. "
            "No coincide con `sha256sum` si el fichero está en CRLF: se normaliza a propósito "
            "para que el manifiesto sea el mismo en Windows, Linux y macOS."
        ),
        "contrato_ficha": list(FICHA_SECTIONS),
        "contrato_notebook": list(NOTEBOOK_SECTIONS),
        "files": [
            {"path": rel, "sha256_lf": sha256_of(ROOT / rel)}
            for rel in sorted(set(manifest_files))
            if (ROOT / rel).exists()
        ],
    }
    (ROOT / "papers" / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    written.append("papers/manifest.json")
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description="Genera los artefactos del eje papers/")
    parser.add_argument("--check", action="store_true", help="falla si algún artefacto cambia")
    args = parser.parse_args()

    if args.check:
        before = {
            path: path.read_bytes()
            for path in list((ROOT / "notebooks" / "papers").glob("*.ipynb"))
            + list((ROOT / "assessments" / "papers").glob("*.md"))
            + list((ROOT / "instructor" / "papers").glob("*.md"))
            + list((ROOT / "student" / "papers").glob("*.md"))
        }
        generate()
        changed = [
            path.relative_to(ROOT).as_posix()
            for path, blob in before.items()
            if path.read_bytes() != blob
        ]
        if changed:
            print("artefactos desactualizados:", changed)
            return 1
        print("artefactos del eje papers al día")
        return 0

    written = generate()
    print(f"eje papers generado: {len(written)} artefactos")
    for rel in written:
        print(" ·", rel)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
