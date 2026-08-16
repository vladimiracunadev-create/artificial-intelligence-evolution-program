# 🔁 Método de lectura en 5 pasadas

> **Origen y honestidad de la fuente:** el método de **tres pasadas** es de S. Keshav,
> *How to Read a Paper* (ACM SIGCOMM CCR, 2007) — [DOI](https://doi.org/10.1145/1273445.1273458).
> Las **pasadas 4 y 5** son una extensión pedagógica de este programa, no del paper de Keshav.
> Se marcan como tales para no atribuirle algo que no escribió.

La idea central: **nunca leas un paper una sola vez de principio a fin**. Haz varias
pasadas, cada una con un objetivo distinto, y decide después de cada una si merece la
siguiente. La mayoría de los papers no pasan de la pasada 1, y eso está bien.

## 🗺️ El método de un vistazo

| Pasada | Tiempo | Objetivo | Salida | ¿Sigo? |
|:---:|---|---|---|---|
| **1** | 10 min | ¿De qué va y me sirve? | 5 frases | Si no me sirve, paro |
| **2** | 1 h | ¿Qué propone y con qué evidencia? | Ficha secciones 1–9 | Si no lo voy a usar ni evaluar, paro |
| **3** | 4–5 h | ¿Podría reimplementarlo? | Miniatura ejecutable | Si no necesito el detalle, paro |
| **4** | 1–2 días | ¿Se sostiene al replicarlo? | Figura o ablación reproducida | Solo para papers que van a fundamentar trabajo propio |
| **5** | continuo | ¿Dónde encaja hoy? | Nota de linaje con fecha | Solo para el núcleo de tu área |

## 1️⃣ Pasada 1 — Reconocimiento (10 minutos)

**Lee:** título, abstract, introducción, encabezados de sección, figuras, conclusiones,
referencias (solo por encima).
**No leas:** método, ecuaciones, tablas de resultados.

Al terminar responde las **cinco C**:

1. **Categoría** — ¿es un método nuevo, un análisis, un dataset, una evaluación, una posición?
2. **Contexto** — ¿con qué trabajos dialoga?
3. **Corrección** — ¿los supuestos parecen razonables a primera vista?
4. **Contribución** — ¿qué aporta, en una frase?
5. **Claridad** — ¿está bien escrito? (mala escritura correlaciona con trabajo confuso)

**Criterio de parada:** si no responde a una pregunta que tienes, cierra. Guarda la
referencia y sigue. Leer todo lo que llega no es rigor: es falta de criterio.

## 2️⃣ Pasada 2 — Comprensión (1 hora)

**Lee:** todo el cuerpo con atención a figuras y tablas. **Ignora** las demostraciones.

Objetivos concretos:

- Escribir la **afirmación central** sin usar el vocabulario del paper.
- Identificar **tarea, dataset, métrica y línea base** de cada resultado principal.
- Marcar las referencias que necesitarás leer.
- Anotar cada punto que no entendiste (no lo disimules: la lista es tu plan de estudio).

Al terminar deberías poder **describir el paper a otra persona** con sus evidencias
principales. Con esto ya puedes rellenar las secciones 1 a 9 de la
[ficha](PLANTILLA_FICHA_PAPER.md).

> [!WARNING]
> Si al final de esta pasada no puedes nombrar la línea base, no has entendido el resultado:
> has memorizado un número.

## 3️⃣ Pasada 3 — Reimplementación mental (4–5 horas)

**El objetivo:** poder reconstruir el trabajo con los mismos supuestos.

Método: **haz de nuevo el paper**. Asume lo que asumen los autores y recrea el trabajo.
Comparar tu reconstrucción con la real revela no solo las innovaciones del paper, sino sus
supuestos ocultos y sus fallos.

En este eje, la pasada 3 tiene una salida obligatoria y concreta: **la miniatura ejecutable**,
que ya está construida en [`notebooks/papers/`](../../notebooks/papers/). Tu trabajo es
predecir la salida antes de ejecutarla y explicar cualquier diferencia.

Preguntas de esta pasada:

- ¿Qué hiperparámetro decide el resultado, y está documentado?
- ¿Qué pasaría si cambio este componente por el más simple posible?
- ¿Puedo derivar la ecuación central en una servilleta?

## 4️⃣ Pasada 4 — Reproducción parcial *(extensión de este programa)*

No siempre es posible reproducir un paper: el cómputo original puede costar cientos de miles
de dólares. Pero casi siempre es posible reproducir **algo**:

- una **figura** con datos sintéticos o un subconjunto público;
- una **ablación** a escala reducida;
- una **tendencia** (que la métrica suba con el tamaño, aunque no llegues a sus valores).

**Regla de honestidad:** una tendencia reproducida a escala 1/1000 es evidencia de que
entendiste el mecanismo, **no** de que el resultado del paper sea correcto. Decláralo así.

Salida: un notebook con semilla fija, la figura reproducida y una frase sobre qué parte del
resultado original queda fuera de tu alcance y por qué.

## 5️⃣ Pasada 5 — Linaje y estado del arte *(extensión de este programa)*

Un paper no es un punto: es un nodo. Esta pasada lo sitúa.

1. Busca en [Semantic Scholar](https://www.semanticscholar.org/) qué papers lo citan.
2. Identifica: quién lo **extendió**, quién lo **contradijo** y quién lo **reemplazó**.
3. Comprueba si su resultado principal **sigue vigente** o fue matizado.
4. Anota la **fecha de consulta**. Esta pasada caduca.

Salida: una nota de linaje de 5 líneas con fecha, que en este repositorio vive en la
sección 13 de cada ficha y, para lo aún no consolidado, en
[`frontier/current-topics.yaml`](../../frontier/current-topics.yaml).

## ⏱️ Cuánto invertir, según para qué

| Tu objetivo | Pasada suficiente |
|---|---|
| Saber si existe algo relevante | 1 |
| Citarlo en un informe | 2 |
| Explicarlo en clase | 3 |
| Construir sobre él | 4 |
| Investigar en su área | 5 |

## ✅ Autoevaluación del método

- [ ] He parado en la pasada 1 al menos una vez esta semana (señal de tener criterio).
- [ ] Puedo nombrar la línea base de los últimos tres papers que leí.
- [ ] Tengo una lista escrita de lo que no entendí, no una sensación difusa.
- [ ] Antes de ejecutar cualquier miniatura, escribí mi predicción.
- [ ] Sé distinguir, en mis propias notas, hecho documentado de inferencia mía.

---

[⬅️ Eje de papers](../README.md) ·
[📖 Cómo leer un paper](COMO_LEER_UN_PAPER_DE_IA.md) ·
[🧾 Plantilla de ficha](PLANTILLA_FICHA_PAPER.md) ·
[🌐 Fuentes y venues](FUENTES_Y_VENUES.md)
