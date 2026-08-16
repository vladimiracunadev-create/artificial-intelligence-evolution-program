# A02 · Probabilidad y verosimilitud

> Casi toda la IA moderna optimiza lo mismo: **hacer más probable lo que ocurrió**. Cambia el
> objeto —el siguiente token, la respuesta preferida, el ruido añadido— pero no la maquinaria.
>
> **Usado en:** [P08](../foundational/P08_transformer/README.md) ·
> [P09](../foundational/P09_bert/README.md) · [P10](../foundational/P10_gpt3/README.md) ·
> [P12](../foundational/P12_instructgpt_rlhf/README.md) ·
> [P15](../foundational/P15_dpo/README.md) · [P17](../foundational/P17_diffusion/README.md) ·
> [P22](../foundational/P22_deepseek_r1/README.md)

## 1. Softmax

```text
softmax(z)ᵢ = e^{zᵢ} / Σⱼ e^{zⱼ}
```

Convierte cualquier vector de números reales en una **distribución de probabilidad**: todos los
valores quedan en `(0,1)` y suman 1.

**Ejemplo resuelto.** `z = (2, 1, 0)`:

```text
e² = 7,389    e¹ = 2,718    e⁰ = 1,000     suma = 11,107

softmax = (0,665 ,  0,245 ,  0,090)        suma = 1,000 ✓
```

**Dos propiedades que hay que conocer:**

**(a) Invariante ante desplazamientos.** `softmax(z) = softmax(z − c)` para cualquier `c`. Por
eso se implementa restando el máximo: evita que `e^{800}` desborde sin cambiar el resultado.

**(b) La escala lo cambia todo.** Multiplicar `z` por un factor concentra o reparte la masa:

| `z` escalado | resultado | interpretación |
|---|---|---|
| `(0,5 · z)` | (0,506, 0,307, 0,186) | repartido |
| `z` | (0,665, 0,245, 0,090) | normal |
| `(4 · z)` | (0,999, 0,0003, 0,0000) | **saturado** |

Esta es exactamente la razón del `√d_k` del Transformer: sin él, los productos escalares crecen
con la dimensión, el softmax se satura y **el gradiente de todo lo no seleccionado se anula**.

> ⚠️ **Error común:** aplicar una máscara **después** del softmax poniendo pesos a cero. La
> distribución deja de sumar 1. La máscara va **antes**, poniendo los logits a `−∞`.

## 2. Entropía

```text
H(p) = − Σᵢ pᵢ · log(pᵢ)
```

Mide **cuán repartida** está una distribución. Alta = indecisión; baja = concentración.

**Ejemplo resuelto** con 4 opciones:

```text
p = (0,25, 0,25, 0,25, 0,25)  →  H = −4·(0,25·log 0,25) = 1,386   ← máxima (= log 4)
p = (0,97, 0,01, 0,01, 0,01)  →  H ≈ 0,169                         ← casi determinista
```

En el eje se usa para medir si la atención está **enfocada** o **repartida**
([T03](../../notebooks/papers/T03_softmax_y_temperatura.ipynb)).

## 3. Verosimilitud y entropía cruzada

Entrenar un modelo de lenguaje es **maximizar la verosimilitud** de un texto que ya ocurrió:

```text
maximizar  Π_t p(x_t | x_<t)        ⟺     minimizar  − Σ_t log p(x_t | x_<t)
```

Se usan logaritmos por dos razones prácticas: convierten productos en sumas (más estable
numéricamente) y evitan que multiplicar miles de probabilidades pequeñas colapse a cero.

**Ejemplo resuelto.** El modelo asigna 0,7 al token correcto:

```text
pérdida = −log(0,7) = 0,357

Si asignara 0,99  →  −log(0,99) = 0,010   (casi sin penalización)
Si asignara 0,01  →  −log(0,01) = 4,605   (penalización enorme)
```

La forma de `−log` es lo que hace que el modelo **odie estar muy seguro y equivocado**.

> ⚠️ **Error común:** comparar pérdidas entre modelos con tokenizadores distintos. La pérdida
> es por token; si un modelo parte las palabras en más trozos, sus números no son comparables.

## 4. Divergencia KL

```text
KL(p ‖ q) = Σᵢ pᵢ · log(pᵢ / qᵢ)
```

Mide **cuánto se aleja** una distribución `q` de otra `p`. Vale 0 solo si son idénticas, y es
**asimétrica**: `KL(p‖q) ≠ KL(q‖p)`.

**Dónde aparece.** En [RLHF](../foundational/P12_instructgpt_rlhf/README.md) penaliza que la
política se aleje del modelo base:

```text
objetivo = E[ r(x, y) ]  −  β · KL( π ‖ π_ref )
```

Sin ese término, la política deriva hacia texto degenerado con recompensa alta. En
[DPO](../foundational/P15_dpo/README.md) la misma restricción queda **absorbida** dentro del
log-ratio `β·log(π/π_ref)`.

> ⚠️ **Error común:** tratar la KL como una distancia. No lo es: no es simétrica y no cumple la
> desigualdad triangular.

## 5. Bradley-Terry: aprender de comparaciones

```text
p(a ≻ b) = σ( r(a) − r(b) )        con  σ(z) = 1/(1+e^{−z})
```

Modela la probabilidad de que `a` se prefiera a `b` en función de la **diferencia** de sus
puntuaciones. Solo importa la diferencia: la escala absoluta de `r` no está determinada.

**Ejemplo resuelto.** `r(a) = 2,0`, `r(b) = 0,5`:

```text
p(a ≻ b) = σ(1,5) = 1/(1+e^{−1,5}) = 0,818
```

Un 82 % de las veces se preferiría `a`. Si ambas puntuaran igual, saldría exactamente 0,5.

**Por qué se piden comparaciones y no notas.** Pedir «¿cuál prefieres?» es más consistente entre
anotadores que pedir «puntúa del 1 al 10»: la escala numérica la interpreta cada persona a su
manera y deriva con el tiempo.

## 6. Gaussianas y el proceso de difusión

```text
N(x; μ, σ²)    la campana:  media μ, desviación σ
```

Propiedad clave que usa [P17](../foundational/P17_diffusion/README.md): **la composición de
gaussianas es gaussiana**. Por eso se puede saltar de `x₀` a `x_t` en un paso sin simular los
`t` intermedios:

```text
x_t = √ᾱ_t · x₀ + √(1−ᾱ_t) · ε,        ε ~ N(0, I)
```

**Ejemplo resuelto.** Con `ᾱ_t = 0,25`:

```text
x_t = 0,5·x₀ + 0,866·ε          (√0,25 = 0,5;  √0,75 = 0,866)
SNR = ᾱ/(1−ᾱ) = 0,25/0,75 = 0,333
```

La señal ya vale un tercio del ruido. Y despejando la imagen original:

```text
x₀ = (x_t − 0,866·ε) / 0,5      ← el factor 1/0,5 = 2 AMPLIFICA cualquier error en ε
```

Ese factor `1/√ᾱ_t` crece según avanza `t`, y es la razón de que el muestreo vaya paso a paso.

---

[⬅️ Anexos](README.md) ·
[A01 · Álgebra](A01_ALGEBRA_Y_GEOMETRIA.md) ·
[A03 · Cálculo](A03_CALCULO_Y_GRADIENTES.md) ·
[🏫 Clase 006 del programa](../../classes/part-00-foundations-history-and-scientific-method/006-probabilidad-incertidumbre-y-estadistica-basica/README.md)
