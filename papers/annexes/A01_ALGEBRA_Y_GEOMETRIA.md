# A01 · Álgebra y geometría

> Los vectores no son «listas de números»: son **flechas con dirección y longitud**. Casi todo
> lo que hace un modelo de IA es medir ángulos entre flechas y moverlas.
>
> **Usado en:** [P01](../foundational/P01_perceptron/README.md) ·
> [P05](../foundational/P05_word2vec/README.md) ·
> [P07](../foundational/P07_attention_bahdanau/README.md) ·
> [P08](../foundational/P08_transformer/README.md) ·
> [P18](../foundational/P18_clip/README.md)

## 1. Producto escalar

```text
a · b = Σᵢ aᵢbᵢ = a₁b₁ + a₂b₂ + … + aₙbₙ
```

**Qué mide.** Cuánto «van en la misma dirección» dos vectores, escalado por sus longitudes:

```text
a · b = ‖a‖ · ‖b‖ · cos(θ)
```

- `a · b > 0` → ángulo agudo, apuntan hacia el mismo lado.
- `a · b = 0` → **perpendiculares**, no comparten nada.
- `a · b < 0` → apuntan en sentidos opuestos.

**Ejemplo resuelto.** `a = (3, 4)`, `b = (4, 3)`:

```text
a · b = 3·4 + 4·3 = 24
‖a‖ = √(9+16) = 5        ‖b‖ = √(16+9) = 5
cos(θ) = 24 / (5·5) = 0,96   →  θ ≈ 16,3°
```

Casi alineados, como cabía esperar de dos vectores tan parecidos.

**Dónde aparece.** Es la operación **QKᵀ** de la atención ([P08](../foundational/P08_transformer/README.md)),
la puntuación `w·x` del perceptrón ([P01](../foundational/P01_perceptron/README.md)) y la
similitud de CLIP ([P18](../foundational/P18_clip/README.md)).

> ⚠️ **Error común:** creer que un producto escalar grande significa «muy parecidos». Puede ser
> grande simplemente porque los vectores son **largos**. Para comparar dirección hay que
> normalizar — y eso es exactamente el coseno.

## 2. Norma y coseno

```text
‖a‖ = √(a · a)                    longitud del vector

cos(a, b) = (a · b) / (‖a‖ ‖b‖)   similitud independiente de la longitud, en [−1, 1]
```

**Ejemplo resuelto.** `a = (1, 0)`, `b = (100, 0)`: el producto escalar vale 100 —enorme— pero
`cos = 100/(1·100) = 1`. Son **la misma dirección** con longitudes muy distintas.

**Dónde aparece.** Toda medida de similitud semántica del eje: vecinos de Word2Vec, ranking de
RAG, matriz de CLIP.

> ⚠️ **Error común:** usar coseno cuando la magnitud sí importa. En recuperación, un documento
> largo y uno corto con la misma proporción de términos dan el mismo coseno; a veces eso es lo
> que quieres y a veces no.

## 3. Hiperplanos y separabilidad

```text
w · x + b = 0
```

Esa ecuación define una **recta** en 2D, un **plano** en 3D y un **hiperplano** en n
dimensiones. Divide el espacio en dos mitades: donde `w·x + b > 0` y donde es `< 0`.

- `w` es **perpendicular** al hiperplano: marca hacia dónde crece la puntuación.
- `b` lo **desplaza** del origen. Sin `b`, la frontera pasaría siempre por el punto `(0,…,0)`.
- La distancia de un punto `x` al hiperplano es `|w·x + b| / ‖w‖`.

**Ejemplo resuelto (el perceptrón de AND).** Con `w = (2, 1)` y `b = −3`:

| x | `w·x + b` | lado | clase |
|---|---|---|---|
| (0,0) | 0+0−3 = −3 | negativo | 0 |
| (0,1) | 0+1−3 = −2 | negativo | 0 |
| (1,0) | 2+0−3 = −1 | negativo | 0 |
| (1,1) | 2+1−3 = **0** | frontera (≥0) | 1 |

La recta `2x₁ + x₂ = 3` deja solo `(1,1)` en el lado positivo. Compruébalo dibujándolo.

**Por qué XOR no se puede.** Con `y=1` en `(0,1)` y `(1,0)`, y `y=0` en `(0,0)` y `(1,1)`:

```text
(0,0)→0:  b < 0
(0,1)→1:  w₂ + b ≥ 0
(1,0)→1:  w₁ + b ≥ 0
(1,1)→0:  w₁ + w₂ + b < 0

Sumando las filas 2 y 3:  w₁ + w₂ + 2b ≥ 0  →  w₁ + w₂ + b ≥ −b > 0
que contradice la fila 4.  No existe (w₁, w₂, b).
```

> ⚠️ **Error común:** decir «XOR no converge porque faltan épocas». No es un problema de
> presupuesto: es que **no existe** ningún hiperplano que lo resuelva. Ver
> [P01](../foundational/P01_perceptron/README.md).

## 4. Matrices como transformaciones

Una matriz `W ∈ ℝ^{m×n}` convierte un vector de `n` dimensiones en uno de `m`:

```text
y = W·x           yᵢ = Σⱼ Wᵢⱼ xⱼ
```

Cada **fila** de `W` es un vector con el que se hace producto escalar. Por eso una capa densa
`y = Wx + b` es literalmente «`m` puntuaciones, una por fila».

**Comprobación de dimensiones — el mejor depurador que existe.** Si multiplicas `(m×n)` por
`(n×k)`, obtienes `(m×k)`: la dimensión interior debe coincidir y desaparece.

```text
Q (n×d_k) · Kᵀ (d_k×n)  →  (n×n)     ← la matriz de atención: un peso por par de posiciones
(n×n) · V (n×d_v)       →  (n×d_v)   ← la salida, una fila por posición
```

Si las formas no cuadran, has entendido mal el mecanismo. Comprobar dimensiones antes de
programar ahorra horas.

> ⚠️ **Error común:** confundir `Wx` con `xW`. El orden importa y determina qué dimensión se
> contrae. En los papers, mira siempre si los vectores son fila o columna.

## 5. Proyección y subespacios

Multi-cabeza ([P08](../foundational/P08_transformer/README.md)) parte `d_model` en `h` trozos de
`d_model/h`. Cada cabeza trabaja en un **subespacio** distinto: una proyección de menor
dimensión donde puede especializarse.

```text
d_model = 512,  h = 8  →  d_k = 64 por cabeza

Parámetros de 8 cabezas de 64  =  8 · (512·64)  =  512·512
Parámetros de 1 cabeza de 512  =  512·512
                                  ↑ el MISMO total
```

Por eso multi-cabeza no cuesta más parámetros: se reparte el mismo presupuesto en más
subespacios más pequeños.

---

[⬅️ Anexos](README.md) ·
[A02 · Probabilidad](A02_PROBABILIDAD_Y_VEROSIMILITUD.md) ·
[A04 · La atención paso a paso](A04_ATENCION_PASO_A_PASO.md) ·
[🏫 Clase 005 del programa](../../classes/part-00-foundations-history-and-scientific-method/005-vectores-matrices-y-geometria-para-ia/README.md)
