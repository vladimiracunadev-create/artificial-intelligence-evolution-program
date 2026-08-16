# A05 · Complejidad, coste y escalado

> La diferencia entre una idea que funciona y una que se despliega casi siempre es una cuenta de
> servilleta. Este anexo enseña a hacerla.
>
> **Usado en:** [P06](../foundational/P06_seq2seq/README.md) ·
> [P08](../foundational/P08_transformer/README.md) ·
> [P19](../foundational/P19_scaling_laws/README.md) ·
> [P20](../foundational/P20_mamba/README.md) · [P21](../foundational/P21_moe/README.md) ·
> [P22](../foundational/P22_deepseek_r1/README.md)

## 1. Notación O(): qué dice y qué no

`O(f(n))` describe **cómo crece** el coste al crecer `n`, ignorando constantes.

```text
O(n)    duplicar n duplica el coste
O(n²)   duplicar n cuadruplica el coste
O(n³)   duplicar n multiplica por 8
```

**Lo que NO dice:** cuál es más rápido *hoy, en tu máquina, con tu n*. Un algoritmo `O(n²)` con
constante pequeña puede ganar a uno `O(n)` con constante enorme durante todo el rango que te
importa.

> ⚠️ **Error común:** «es O(n), luego es más rápido». Siempre hay que preguntar **a partir de
> qué `n`**.

## 2. El cruce: atención frente a recurrencia

Del [Transformer](../foundational/P08_transformer/README.md), tabla 1:

| Tipo de capa | Operaciones | Pasos secuenciales | Camino máximo |
|---|---|---|---|
| Self-attention | `O(n²·d)` | `O(1)` | `O(1)` |
| Recurrente | `O(n·d²)` | `O(n)` | `O(n)` |

**¿Cuándo cuesta más la atención?**

```text
n²·d  >  n·d²      ⟺      n > d
```

Con `d = 512`, la atención es **más barata** en operaciones hasta secuencias de 512 tokens, y
más cara por encima.

**Pero las otras dos columnas no dependen de `n`:** la atención siempre gana en paralelismo
(`O(1)` pasos secuenciales) y siempre gana en distancia entre posiciones (`O(1)` frente a
`O(n)`). Por eso se impuso aunque el cómputo crezca al cuadrado: **el hardware moderno paraleliza
bien y espera mal**.

## 3. La cuenta que decide el hardware: memoria

Coste de la matriz de atención, en `float32` (4 bytes), **por cabeza y por capa**:

```text
memoria = n² · 4 bytes
```

| `n` | matriz de atención | ¿viable? |
|---:|---|---|
| 512 | 1 MB | trivial |
| 2 048 | 16 MB | cómodo |
| 8 192 | 268 MB | notable |
| 32 768 | 4,3 GB | problemático |
| 128 000 | **65,5 GB** | inviable por cabeza y capa |

Multiplica por el número de cabezas y de capas y verás por qué el contexto largo real **no** usa
atención densa ingenua: usa variantes dispersas, con E/S optimizada o compresión.

Frente a eso, un [SSM](../foundational/P20_mamba/README.md) mantiene un estado de tamaño `d·N`
**constante**: con `d = 512` y `N = 16` son 8 192 valores, valga la secuencia 1 000 o 1 000 000.

## 4. FLOPs de entrenamiento: la regla de 6ND

```text
C ≈ 6 · N · D          N = parámetros,  D = tokens de entrenamiento
```

El 6 sale de contar, por parámetro y por token, las multiplicaciones-acumulaciones de la pasada
hacia adelante (≈2) y hacia atrás (≈4).

**Ejemplo resuelto.** `N = 7·10¹⁰`, `D = 1,4·10¹²`:

```text
C ≈ 6 · 7·10¹⁰ · 1,4·10¹² ≈ 5,9·10²³ FLOPs
```

Para dimensionar: una GPU de gama alta con ~10¹⁵ FLOP/s **efectivos** tardaría ~5,9·10⁸ s ≈ 19
años. Con 1 000 GPU al 40 % de utilización, unos 17 días. Ahí se ve por qué esto es una
actividad industrial.

## 5. Escalado: dónde gastar el presupuesto

De [Chinchilla](../foundational/P19_scaling_laws/README.md):

```text
L(N, D) = E + A/N^α + B/D^β        sujeto a  6ND = C
```

- `E` es el **error irreducible**: no baja con cómputo.
- Los otros dos términos son lo que compras con parámetros y con datos.
- El óptimo iguala las contribuciones marginales de ambos → `N` y `D` deben crecer **a la vez**.

> ⚠️ **Error común:** citar «20 tokens por parámetro» como constante universal. Es una razón
> derivada de exponentes ajustados en un rango concreto y una arquitectura concreta.

## 6. La cuenta que casi nadie hace: inferencia

```text
Coste de entrenamiento (una vez):     C_train ≈ 6·N·D
Coste de inferencia (cada petición):  C_inf   ≈ 2·N·tokens_generados
```

**Ejemplo resuelto.** `N = 7·10¹⁰`, `D = 1,4·10¹²`, respuestas de 500 tokens:

| peticiones | coste de inferencia | ¿domina? |
|---:|---|---|
| 10⁶ | 7,0·10¹⁹ | no (entrenamiento: 5,9·10²³) |
| 10⁹ | 7,0·10²² | todavía no |
| 10¹² | **7,0·10²⁵** | **sí, 100× el entrenamiento** |

**Consecuencia de diseño:** si vas a servir a gran escala, conviene entrenar un modelo **más
pequeño que el óptimo de Chinchilla** y darle aún más datos. El óptimo de entrenamiento y el de
despliegue son problemas distintos.

## 7. Dispersión: cuando los parámetros dejan de ser uno

En una [mezcla de expertos](../foundational/P21_moe/README.md), `N` deja de ser un solo número:

```text
N_totales  = 47·10⁹     ← determina la MEMORIA necesaria
N_activos  = 13·10⁹     ← determina el CÓMPUTO por token
```

```text
Memoria de pesos en fp16 = N_totales · 2 bytes = 94 GB
Cómputo por token        ∝ N_activos          = 28 % del denso equivalente
```

> ⚠️ **El error más caro de esta arquitectura:** dimensionar la GPU por los parámetros
> **activos**. Hay que cargar todos los expertos, porque cualquier token puede activar
> cualquiera. MoE ahorra cómputo, **no** memoria.

## 8. Checklist antes de creerte una cifra de rendimiento

Cuando alguien diga «nuestro modelo es más eficiente», pregunta:

- [ ] ¿Eficiente en **qué**: FLOPs, memoria, latencia, coste en dinero, energía?
- [ ] ¿A qué **`n`** (longitud de secuencia)? ¿Dónde está el cruce?
- [ ] ¿En **entrenamiento** o en **inferencia**? No se optimizan igual.
- [ ] ¿Con qué **lote**? Muchas ventajas desaparecen con lote 1.
- [ ] ¿Se cuenta la **memoria de pesos** o solo la activa?
- [ ] ¿Con qué **hardware** y qué utilización efectiva?
- [ ] ¿Se compara contra una línea base **igual de optimizada**?

Las tres últimas son las que más veces faltan.

---

[⬅️ Anexos](README.md) ·
[A01 · Álgebra](A01_ALGEBRA_Y_GEOMETRIA.md) ·
[A03 · Cálculo](A03_CALCULO_Y_GRADIENTES.md) ·
[🏫 Clase 081 · Aceleradores y roofline](../../classes/part-06-foundation-models-and-llm-engineering/081-aceleradores-memoria-y-el-limite-real-del-computo/README.md)
