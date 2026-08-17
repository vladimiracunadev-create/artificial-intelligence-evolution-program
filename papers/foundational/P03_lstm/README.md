# P03 — LSTM

> La arquitectura que convirtió «recordar durante mucho tiempo» en un problema de ingeniería
> resoluble, sustituyendo una multiplicación encadenada por una suma con compuertas.

**Nivel:** L2 · **Motor:** `lstm` · **Notebook:** [`P03_lstm.ipynb`](../../../notebooks/papers/P03_lstm.ipynb)
· **Anexo:** [cálculo y gradientes](../../annexes/A03_CALCULO_Y_GRADIENTES.md)

## 1. Identificación

| Campo | Valor |
|---|---|
| **Título original** | *Long Short-Term Memory* |
| **Autoría** | Sepp Hochreiter, Jürgen Schmidhuber |
| **Año** | 1997 |
| **Venue** | *Neural Computation*, 9(8), 1735–1780 |
| **Fuente primaria** | [doi.org/10.1162/neco.1997.9.8.1735](https://doi.org/10.1162/neco.1997.9.8.1735) |
| **Acceso** | Restringido |
| **Fecha de consulta** | 2026-08-16 |

## 2. Problema anterior

Una red recurrente procesa una secuencia reutilizando el mismo estado. Para entrenarla se
despliega en el tiempo y se aplica [retropropagación](../P02_backpropagation/README.md): el
gradiente atraviesa un paso por cada instante.

Ahí está el problema. En cada paso el gradiente se multiplica por (aproximadamente) `W·σ'`.
Si ese factor es menor que 1, el producto colapsa exponencialmente; si es mayor, explota.
Hochreiter lo había diagnosticado formalmente en su tesis de 1991. La consecuencia práctica:
**una RNN clásica no aprende dependencias separadas por más de unas decenas de pasos**, y no
por falta de datos ni de capacidad, sino por aritmética.

## 3. Propuesta

Introducir una **celda de memoria** cuyo estado se actualiza **sumando**, no aplicando una
transformación no lineal encadenada. Esa ruta aditiva es el *constant error carousel* (CEC):
por ella el gradiente viaja sin multiplicarse por derivadas de activación.

Alrededor del CEC se colocan **compuertas multiplicativas** que aprenden qué información entra
(`i`) y qué información se expone al resto de la red (`o`). Las compuertas protegen la celda
de escrituras y lecturas irrelevantes.

> **Precisión histórica obligatoria:** la versión de 1997 tiene compuertas de **entrada** y
> **salida**. La compuerta de **olvido** —la que hoy aparece en todos los diagramas— la
> añadieron Gers, Schmidhuber y Cummins (1999/2000).

## 4. Intuición sin fórmulas

Una cinta transportadora que atraviesa toda la fábrica. Los operarios pueden depositar cosas
encima (compuerta de entrada) y consultar lo que lleva (compuerta de salida), pero la cinta
avanza sin que su contenido se transforme por el camino. Lo que subió al principio puede
seguir intacto al final.

**Dónde deja de funcionar la analogía:** la cinta real no borra nada; la LSTM moderna sí, y
lo hace con una compuerta aprendida. Y si esa compuerta aprende a cerrarse, el contenido se
desvanece igual que en una RNN.

## 5. Matemática mínima

Formulación moderna (con compuerta de olvido, posterior al paper):

```text
f_t = σ(W_f · [h_{t−1}, x_t] + b_f)        olvido
i_t = σ(W_i · [h_{t−1}, x_t] + b_i)        entrada
o_t = σ(W_o · [h_{t−1}, x_t] + b_o)        salida
g_t = tanh(W_g · [h_{t−1}, x_t] + b_g)     candidato

c_t = f_t ⊙ c_{t−1} + i_t ⊙ g_t            ← SUMA: aquí está el CEC
h_t = o_t ⊙ tanh(c_t)
```

La clave está en la penúltima línea:

```text
∂c_t / ∂c_{t−1} = f_t

Con f_t ≈ 1 durante T pasos:  ∂c_T/∂c_0 ≈ 1
Con una RNN tanh y factor 0,4: 0,4⁴⁰ ≈ 1,2·10⁻¹⁶
```

<!-- puente:inicio -->
> [!TIP]
> **Puente matemático.** Esta sección da por sabido lo siguiente. Si algo no te suena,
> léelo primero: está explicado una sola vez, en un solo sitio, y sirve para todas las fichas.

| Dónde | Qué necesitas de ahí |
|---|---|
| [**A03 §4** · Por qué el gradiente se desvanece](../../annexes/A03_CALCULO_Y_GRADIENTES.md#4-por-qué-el-gradiente-se-desvanece) | por qué un producto de derivadas menores que 1 colapsa, que es el problema exacto que la celda resuelve |
<!-- puente:fin -->

## 6. Arquitectura o flujo

```text
              ┌──────────── c_{t−1} ─────────────┐
              │                                  │
              ▼                                  ▼
   x_t ──┬──► ⊗ f_t ──────────────► ⊕ ──────────► c_t ──► tanh ──► ⊗ ──► h_t
         │                          ▲                              ▲
 h_{t−1}─┤                          │                              │
         ├──► ⊗ (i_t · g_t) ────────┘                              │
         └──────────────────────────────────► o_t ─────────────────┘

⊕ = suma (carrusel de error constante)   ⊗ = producto elemento a elemento (compuerta)
```

## 7. Qué observar en el paper original

- El artículo es **largo** (46 páginas) y buena parte es el **análisis del flujo de error**:
  ahí está el argumento, no en la arquitectura.
- La justificación de por qué las compuertas deben ser multiplicativas y el estado aditivo.
- Los experimentos con **problemas sintéticos de dependencia larga** (retardos de cientos de
  pasos) diseñados para que ninguna RNN previa pudiera resolverlos.
- Comprueba tú mismo: busca la palabra «forget gate» en el artículo de 1997. No está.

## 8. Evidencia y resultados

El paper compara la LSTM con RNN clásicas, BPTT truncado y otras alternativas de la época
sobre tareas construidas para exigir memoria a largo plazo. La LSTM resuelve retardos con los
que las alternativas fracasan.

> Los detalles de tareas, retardos y tasas de éxito están en la sección de experimentos del
> artículo. Este eje no reproduce esas cifras: verificarlas en la fuente antes de citarlas.

La miniatura de este eje aporta la evidencia del mecanismo: tras 40 pasos, un factor de
decaimiento `0,378` deja el gradiente en `≈10⁻¹⁷`, mientras que una compuerta de olvido en
`0,98` lo deja en `≈0,45`.

## 9. Impacto

- Durante casi dos décadas fue la arquitectura por defecto para secuencias: reconocimiento de
  voz, escritura manuscrita, traducción, series temporales.
- Hizo posible [Seq2Seq](../P06_seq2seq/README.md) y, con él, la traducción automática
  neuronal — el problema que llevó a la atención y al Transformer.
- Instaló una idea que sobrevive a la arquitectura: **las rutas aditivas preservan el
  gradiente**. Es exactamente el mismo principio que las conexiones residuales de ResNet y de
  cada bloque Transformer.

## 10. Limitaciones

1. **Sigue siendo secuencial.** El paso `t` necesita el `t−1`: no se puede paralelizar sobre
   la longitud. Este es el límite que motiva P08.
2. **No elimina el gradiente desvaneciente; lo pone bajo control de una compuerta aprendida.**
   Si `f` aprende valores bajos, el desvanecimiento vuelve.
3. **Cuatro veces más parámetros** que una RNN simple del mismo tamaño de estado.
4. **Sigue comprimiendo** toda la historia en un estado de tamaño fijo.
5. **Difícil de interpretar**: qué guarda cada dimensión de la celda no es legible.
6. **La versión de 1997 carece de compuerta de olvido**, y sin ella el estado de celda puede
   crecer sin límite en secuencias largas — motivo por el que se añadió después.

## 11. Errores comunes

| Error | Corrección |
|---|---|
| «La LSTM de 1997 tiene compuerta de olvido» | No. Gers, Schmidhuber y Cummins (1999/2000). Es el anacronismo más repetido del campo. |
| «La LSTM resuelve el gradiente desvaneciente» | Lo **mitiga** cuando la compuerta de olvido se mantiene cerca de 1 en el intervalo relevante. |
| «La GRU es una LSTM simplificada del mismo paper» | La GRU es de Cho et al. (2014), 17 años después. |
| «Las LSTM quedaron obsoletas» | Siguen siendo competitivas en series temporales, dispositivos con poca memoria y latencia baja. «Obsoleto» es una afirmación sobre un contexto, no sobre una arquitectura. |
| «El estado de celda y el estado oculto son lo mismo» | `c_t` es la memoria protegida; `h_t` es lo que la celda **expone**, filtrado por `o_t`. |

## 12. Relación con trabajos anteriores

- **[P02 Backpropagation](../P02_backpropagation/README.md) (1986)** — el método de
  entrenamiento cuyo problema en el tiempo se ataca aquí.
- **Elman (1990)** — redes recurrentes simples.
- **Hochreiter (1991)** — tesis que diagnostica formalmente el gradiente desvaneciente.
- **Werbos (1990)** — retropropagación en el tiempo (BPTT).

## 13. Relación con trabajos posteriores

- **Gers, Schmidhuber y Cummins (2000)** — compuerta de olvido.
  [doi.org/10.1162/089976600300015015](https://doi.org/10.1162/089976600300015015)
- **Cho et al. (2014)** — GRU, versión con menos compuertas.
  [arXiv:1406.1078](https://arxiv.org/abs/1406.1078)
- **[P06 Seq2Seq](../P06_seq2seq/README.md) (2014)** — dos LSTM encadenadas para traducir.
- **He et al. (2015), ResNet** — el mismo principio aditivo aplicado a la profundidad.
- **[P08 Transformer](../P08_transformer/README.md) (2017)** — elimina la recurrencia entera.

## 14. Notebook asociado

[`P03_lstm.ipynb`](../../../notebooks/papers/P03_lstm.ipynb)

**Qué implementa:** una pasada completa de la celda con valores explícitos de las cuatro
compuertas, y la comparación cuantitativa del decaimiento del gradiente entre una RNN tanh y
la ruta aditiva de la celda.

**Qué NO implementa:** entrenamiento real de una LSTM, BPTT, ni las tareas sintéticas del
paper.

```bash
ai-evolution paper-lab P03 --seed 7
```

## 15. Actividades Bloom

| Nivel | Actividad |
|---|---|
| **Recordar** | Enumera las cuatro compuertas de la LSTM moderna y di cuáles estaban en 1997. |
| **Explicar** | Explica por qué una suma preserva el gradiente y un producto encadenado no. |
| **Aplicar** | Calcula el estado de celda tras 3 pasos con `f = 0,9`, `i = 0,5` y `g = 1` constantes. |
| **Analizar** | ¿Cuál es el valor mínimo de `f` que conserva el 1 % del gradiente tras 100 pasos? Resuélvelo analíticamente y compruébalo. |
| **Evaluar** | Un artículo divulgativo dice: «la LSTM recuerda porque tiene memoria». Reescríbelo con precisión técnica en dos frases. |
| **Crear** | Diseña una tarea sintética mínima donde una RNN simple falle y una LSTM acierte, y justifica por qué tu tarea discrimina entre ambas. |

## 16. Autoevaluación

1. ¿Qué significa exactamente «carrusel de error constante»?
2. ¿Por qué las compuertas usan sigmoide y el candidato usa tanh?
3. ¿Cuál es la diferencia funcional entre `c_t` y `h_t`?
4. Si `f_t = 1` e `i_t = 0` para siempre, ¿qué hace la celda?
5. ¿Qué límite de la LSTM **no** resuelve el mecanismo de compuertas?
6. ¿Por qué la LSTM no se puede paralelizar sobre la longitud de la secuencia?
7. ¿Qué componente de la LSTM actual no aparece en el paper de 1997?

## 17. Respuestas esperadas

1. La ruta por la que el estado de celda se actualiza sumando, de modo que la derivada
   `∂c_t/∂c_{t−1}` vale `f_t` en lugar de un producto de derivadas de activación. Con `f ≈ 1`,
   el error se conserva a través de muchos pasos.
2. La sigmoide devuelve `[0,1]`: es una compuerta, un porcentaje de paso. La tanh devuelve
   `[−1,1]`: es contenido con signo, que puede sumar o restar de la memoria.
3. `c_t` es la memoria interna protegida. `h_t = o_t ⊙ tanh(c_t)` es la parte que la celda
   expone al resto de la red. Se puede recordar algo sin exponerlo.
4. Conserva su contenido indefinidamente sin admitir nada nuevo: memoria congelada.
5. La secuencialidad. El cómputo sigue siendo `O(n)` pasos no paralelizables, y el camino
   entre dos posiciones distantes sigue siendo largo.
6. Porque `h_t` depende de `h_{t−1}`: hay una dependencia de datos estricta entre pasos.
7. La compuerta de olvido (y también la conexión *peephole*, de Gers y Schmidhuber, 2000).

## 18. Fuentes primarias

- Hochreiter, S. y Schmidhuber, J. (1997). *Long Short-Term Memory*. **Neural Computation**,
  9(8), 1735–1780.
  [doi.org/10.1162/neco.1997.9.8.1735](https://doi.org/10.1162/neco.1997.9.8.1735) · consultado 2026-08-16.
- Gers, F. A., Schmidhuber, J. y Cummins, F. (2000). *Learning to Forget: Continual Prediction
  with LSTM*. **Neural Computation**, 12(10), 2451–2471.
  [doi.org/10.1162/089976600300015015](https://doi.org/10.1162/089976600300015015) · consultado 2026-08-16.
- Cho, K. et al. (2014). *Learning Phrase Representations using RNN Encoder–Decoder*.
  [arXiv:1406.1078](https://arxiv.org/abs/1406.1078) · consultado 2026-08-16.

---

[⬅️ Anterior: P02 Backpropagation](../P02_backpropagation/README.md) ·
[📇 Índice](../../catalog/PAPERS_INDEX.md) ·
[📝 Evaluación](../../../assessments/papers/P03_lstm.md) ·
[🏫 Clase 054 del programa](../../../classes/part-04-neural-networks-and-deep-learning/054-rnn-lstm-y-secuencias/README.md) ·
[➡️ Siguiente: P04 AlexNet](../P04_alexnet/README.md)
