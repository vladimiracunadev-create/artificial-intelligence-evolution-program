# A04 · La atención, paso a paso

> La ecuación 1 del Transformer desarrollada **con números concretos**, para que deje de ser una
> fórmula y pase a ser un cálculo que puedes hacer a mano.
>
> **Usado en:** [P07](../foundational/P07_attention_bahdanau/README.md) ·
> [P08](../foundational/P08_transformer/README.md) ·
> [T01–T08](../catalog/PAPERS_INDEX.md)

## La ecuación

```text
Attention(Q, K, V) = softmax( Q·Kᵀ / √d_k ) · V
```

Cuatro operaciones encadenadas. Vamos una por una con el mismo ejemplo.

## El ejemplo que usaremos

Tres tokens, `d_k = d_v = 2`. Consulta = el primer token.

```text
Q = [ 1,0   0,0 ]                     ← una sola consulta

K = [ 1,0   0,0 ]   ← clave 0: idéntica a Q
    [ 0,0   1,0 ]   ← clave 1: perpendicular a Q
    [ 0,9   0,1 ]   ← clave 2: muy parecida a Q

V = [ 10,0   0,0 ]  ← valor 0
    [  0,0  10,0 ]  ← valor 1
    [  5,0   5,0 ]  ← valor 2
```

## Paso 1 — Compatibilidad: `Q·Kᵀ`

Producto escalar de la consulta con cada clave (ver [A01](A01_ALGEBRA_Y_GEOMETRIA.md)):

```text
Q·K₀ = 1,0·1,0 + 0,0·0,0 = 1,00
Q·K₁ = 1,0·0,0 + 0,0·1,0 = 0,00
Q·K₂ = 1,0·0,9 + 0,0·0,1 = 0,90
```

Los tres números `(1,00 · 0,00 · 0,90)` dicen cuánto «le interesa» cada posición a la consulta.
**Aún no son probabilidades**: pueden ser negativos y no suman nada en particular.

## Paso 2 — Escala: `/ √d_k`

```text
√d_k = √2 = 1,414

scores escalados = (0,707 ,  0,000 ,  0,636)
```

**¿Por qué dividir?** Si `q` y `k` tienen componentes independientes de media 0 y varianza 1,
entonces `q·k` tiene **varianza `d_k`**: su magnitud típica crece como `√d_k`. Dividir devuelve
la varianza a 1.

Qué pasa si no se hace, con dimensiones realistas:

| `d_k` | magnitud típica de `q·k` | softmax resultante |
|---:|---|---|
| 2 | ~1,4 | repartido, sano |
| 64 | ~8 | ya concentrado |
| 512 | ~23 | **saturado**: un token se lleva ~1,0 y el resto ~0 |

Con el softmax saturado, el gradiente de todas las posiciones no seleccionadas es
prácticamente cero: **la capa deja de aprender**.

## Paso 3 — Normalizar: `softmax`

```text
e^{0,707} = 2,028
e^{0,000} = 1,000
e^{0,636} = 1,889
                     suma = 4,917

α = (0,412 ,  0,203 ,  0,384)          suma = 1,000 ✓
```

Tres propiedades que hay que verificar siempre:

1. Todos los pesos son **positivos**.
2. **Suman exactamente 1**.
3. El orden se conserva: la clave más compatible tiene el mayor peso.

> ⚠️ Si «normalizas» dividiendo por la suma de los scores en vez de con softmax, con scores
> `(2, −1, 0,5)` obtienes `(1,33 , −0,67 , 0,33)`: pesos **negativos** y mayores que 1. Deja de
> ser una distribución. Por eso es softmax y no una división.

## Paso 4 — Mezclar: `α · V`

```text
salida = 0,412·(10,0)  +  0,203·( 0,0)  +  0,384·(5,0)
         0,412·( 0,0)  +  0,203·(10,0)  +  0,384·(5,0)

       = ( 4,12 + 0,00 + 1,92 ,  0,00 + 2,03 + 1,92 )
       = ( 6,04 ,  3,95 )
```

**Propiedad clave:** como los pesos son positivos y suman 1, la salida es una **combinación
convexa** de las filas de `V`. Nunca puede salirse de la envolvente de los valores.

> La atención **mezcla**, no inventa. Si un dato no está en `V`, no puede aparecer en la salida.

## La máscara causal

Para generar de izquierda a derecha, la posición `i` no puede mirar a `j > i`. Se aplica
**antes** del softmax poniendo esos scores a `−∞`:

```text
scores = [ 0,71   −∞     −∞  ]      e^{−∞} = 0
         [ 0,32   0,67   −∞  ]
         [ 0,16   0,15   0,69 ]

α      = [ 1,000  0,000  0,000 ]    ← la posición 0 solo se ve a sí misma
         [ 0,327  0,673  0,000 ]
         [ 0,164  0,145  0,691 ]
              ↑ cada fila sigue sumando 1
```

Matriz **triangular inferior**, y la masa sobre el futuro es exactamente 0.

> ⚠️ **Error común:** poner los pesos a cero *después* del softmax. La fila deja de sumar 1 y la
> mezcla queda mal escalada. Comprobación rápida: suma cada fila; si no da 1, la máscara está
> mal puesta.

## Multi-cabeza

```text
MultiHead(X) = Concat(head₁, …, head_h) · W^O
head_i = Attention(X·W_i^Q, X·W_i^K, X·W_i^V),    d_k = d_model / h
```

Con `d_model = 512` y `h = 8`, cada cabeza trabaja en 64 dimensiones. El presupuesto total de
parámetros **no cambia** (ver [A01 §5](A01_ALGEBRA_Y_GEOMETRIA.md)): lo que cambia es que hay
ocho subespacios donde especializarse en vez de uno.

## Autocomprobación

Repite el cálculo con `Q = [0,0  1,0]` (la consulta ahora apunta a la segunda dimensión) y
verifica:

- [ ] Los tres productos escalares valen `(0,00 · 1,00 · 0,10)`.
- [ ] Tras escalar y aplicar softmax, los pesos suman 1.
- [ ] El peso mayor corresponde ahora a la **clave 1**.
- [ ] La salida está entre el mínimo y el máximo de cada columna de `V`.
- [ ] Con máscara causal en la primera fila, `α = (1, 0, 0)` sea cual sea `Q`.

Si las cinco te salen, entiendes la ecuación 1. Compruébalo ejecutando
[`T02`](../../notebooks/papers/T02_qkv_scaled_dot_product.ipynb).

---

[⬅️ Anexos](README.md) ·
[A01 · Álgebra](A01_ALGEBRA_Y_GEOMETRIA.md) ·
[A02 · Probabilidad](A02_PROBABILIDAD_Y_VEROSIMILITUD.md) ·
[📜 Ficha del Transformer](../foundational/P08_transformer/README.md) ·
[🏫 Clase 055 del programa](../../classes/part-04-neural-networks-and-deep-learning/055-atencion-y-arquitectura-transformer/README.md)
