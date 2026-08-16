# P06 — Seq2Seq

> Una sola red aprende a convertir una secuencia de longitud variable en otra de longitud
> distinta, de extremo a extremo. Y, al hacerlo, revela el cuello de botella que definirá los
> tres papers siguientes.

**Nivel:** L3 · **Motor:** `seq2seq` · **Notebook:** [`P06_seq2seq.ipynb`](../../../notebooks/papers/P06_seq2seq.ipynb)

## 1. Identificación

| Campo | Valor |
|---|---|
| **Título original** | *Sequence to Sequence Learning with Neural Networks* |
| **Autoría** | Ilya Sutskever, Oriol Vinyals, Quoc V. Le |
| **Año** | 2014 |
| **Venue** | arXiv:1409.3215 · NeurIPS (NIPS) 2014 |
| **Fuente primaria** | [arXiv:1409.3215](https://arxiv.org/abs/1409.3215) |
| **Acceso** | Abierto |
| **Fecha de consulta** | 2026-08-16 |

## 2. Problema anterior

Las redes profundas funcionaban con entradas y salidas de **dimensión fija**: una imagen de
224×224, un vector de características. Pero traducir «el gato negro duerme» a inglés produce
una secuencia de longitud distinta a la de entrada, y esa longitud no se conoce de antemano.

La traducción automática del momento se hacía con **sistemas estadísticos por frases**:
muchos componentes ajustados por separado (modelo de traducción, modelo de lenguaje,
reordenamiento, ajuste de pesos). Funcionaban bien, pero cada pieza se optimizaba con un
criterio propio y no con el objetivo final.

## 3. Propuesta

Dos LSTM encadenadas:

1. el **codificador** lee la secuencia de entrada token a token y termina con un estado
   interno `c`, un vector de tamaño fijo que pretende resumirla entera;
2. el **decodificador** parte de `c` y genera la salida token a token, alimentándose de lo que
   ya generó.

Todo se entrena con un único objetivo: maximizar la probabilidad de la traducción correcta.

El artículo aporta además un truco empírico decisivo: **invertir el orden de la secuencia
fuente**. Con la entrada invertida, las primeras palabras de origen quedan temporalmente cerca
de las primeras de destino, lo que acorta las dependencias que la LSTM debe mantener.

## 4. Intuición sin fórmulas

Leer una frase entera, cerrar los ojos y escribir la traducción solo de memoria. Con frases
cortas funciona. Con un párrafo, cuando llegas al final ya no recuerdas con precisión cómo
empezaba.

**Dónde deja de funcionar la analogía:** una persona puede releer. El decodificador de este
modelo no puede: solo dispone de `c`.

## 5. Matemática mínima

```text
Codificador:   c = h_n,   con  h_t = LSTM(h_{t−1}, x_t)

Decodificador: p(y₁…y_m | x₁…x_n) = Πₜ p(y_t | y_<t, c)

Entrenamiento: maximizar  Σ log p(y | x)  sobre el corpus paralelo
Inferencia:    búsqueda en haz (beam search) sobre la secuencia de salida
```

**El punto crítico:** `c ∈ ℝᵈ` tiene dimensión **constante**, mientras que la información de
`x₁…x_n` crece con `n`. Comprimir algo de tamaño creciente en algo de tamaño fijo tiene un
coste, y ese coste crece con la longitud.

## 6. Arquitectura o flujo

```text
   x₁   x₂   x₃   x₄                       y₁   y₂   y₃  <fin>
   │    │    │    │                         ▲    ▲    ▲    ▲
   ▼    ▼    ▼    ▼                         │    │    │    │
 ┌────┬────┬────┬────┐   c   ┌────┬────┬────┬────┐
 │LSTM│LSTM│LSTM│LSTM│ ────► │LSTM│LSTM│LSTM│LSTM│
 └────┴────┴────┴────┘       └────┴────┴────┴────┘
      CODIFICADOR                  DECODIFICADOR
                            ▲
                   todo pasa por AQUÍ:
                   un único vector fijo
```

## 7. Qué observar en el paper original

- La **discusión sobre invertir la secuencia fuente**: es una de las observaciones empíricas
  más comentadas del artículo, y los autores admiten no tener una explicación completa.
- El uso de **LSTM profundas** (varias capas apiladas) y su efecto en el resultado.
- La **búsqueda en haz** en inferencia y el efecto del tamaño del haz.
- La **visualización PCA** de los estados `c`: frases con significado parecido quedan cerca, y
  el espacio muestra sensibilidad al orden de las palabras y a la voz activa/pasiva.
- El experimento de **rescorear** las n-mejores hipótesis del sistema estadístico, en lugar de
  traducir directamente.

## 8. Evidencia y resultados

Evaluación sobre traducción **inglés → francés** de WMT'14, medida en BLEU, comparada contra
un sistema estadístico por frases de referencia.

El artículo reporta dos regímenes: traducción directa con un conjunto de LSTM, y rescoreo de
las hipótesis del sistema estadístico —este último mejor que el primero—. También documenta
que la calidad **cae con la longitud de la frase**, y que invertir la fuente mejora el
resultado de forma consistente.

> Los valores exactos de BLEU para cada configuración están en las tablas del artículo.
> Verificarlos allí: circulan cifras mezcladas entre el modelo único, el conjunto y el
> rescoreo.

La miniatura de este eje mide el fenómeno estructural, no el BLEU: al pasar de longitud 2 a
32, la similitud del vector de contexto con el **primer** token se desploma mientras la del
**último** se mantiene alta.

## 9. Impacto

- Convierte la traducción automática en un problema de aprendizaje de extremo a extremo, y en
  pocos años el paradigma estadístico por frases queda desplazado.
- Establece el patrón **codificador–decodificador** que sigue siendo la arquitectura de
  referencia para transformar una secuencia en otra.
- Populariza la **búsqueda en haz** como procedimiento estándar de decodificación.
- Y, sobre todo, **hace visible el cuello de botella**: al medir la caída de calidad con la
  longitud, define el problema que Bahdanau resolverá el mismo año.

## 10. Limitaciones

1. **Cuello de botella del vector fijo.** Es el límite estructural: capacidad constante frente
   a información creciente.
2. **La calidad cae con la longitud de la frase.** Documentado en el propio artículo.
3. **Sigue siendo secuencial**: no paraleliza sobre la longitud.
4. **Invertir la fuente es un parche**, no una solución. Reordena qué información se pierde.
5. **Coste de entrenamiento alto** para la época, y dependencia de grandes corpus paralelos.
6. **Sin alineación explícita**: no hay forma de saber qué parte de la entrada generó qué parte
   de la salida.

## 11. Errores comunes

| Error | Corrección |
|---|---|
| «Seq2Seq usa atención» | No. La atención llega con [P07](../P07_attention_bahdanau/README.md), unas semanas después. |
| «El problema se arregla agrandando el estado» | Un estado mayor retrasa el problema; no cambia que la capacidad sea constante y la longitud variable. |
| «Invertir la entrada resuelve el cuello de botella» | Lo mitiga reordenando las dependencias. El cuello sigue ahí. |
| «Seq2Seq inventó el codificador–decodificador» | Cho et al. (2014) publicó una formulación muy próxima meses antes (arXiv:1406.1078). Ambos trabajos son contemporáneos e independientes. |
| «BLEU mide calidad de traducción» | Mide solapamiento de n-gramas con referencias. Correlaciona, imperfectamente, y no es comparable entre tokenizaciones distintas. |

## 12. Relación con trabajos anteriores

- **[P03 LSTM](../P03_lstm/README.md) (1997)** — la celda que hace viable el codificador.
- **Cho et al. (2014)** — RNN encoder–decoder y GRU, contemporáneo.
  [arXiv:1406.1078](https://arxiv.org/abs/1406.1078)
- **Modelos estadísticos de traducción** (Brown et al., 1993; Koehn et al., 2003) — la línea
  base contra la que se compara.

## 13. Relación con trabajos posteriores

- **[P07 Attention](../P07_attention_bahdanau/README.md) (2014)** — elimina el vector fijo.
- **[P08 Transformer](../P08_transformer/README.md) (2017)** — conserva el patrón
  codificador–decodificador y elimina la recurrencia.
- **BART, T5 (2019–2020)** — codificador–decodificador preentrenado.
- **Modelos de imagen a texto y voz a texto** — el mismo patrón aplicado a otras modalidades.

## 14. Notebook asociado

[`P06_seq2seq.ipynb`](../../../notebooks/papers/P06_seq2seq.ipynb)

**Qué implementa:** una medición directa del cuello de botella. Un codificador de juguete
comprime secuencias de longitud creciente en un vector fijo y se mide cuánta información del
principio sobrevive.

**Qué NO implementa:** LSTM entrenadas, traducción real, búsqueda en haz ni BLEU. El
codificador es una mezcla con decaimiento fijo: aísla el fenómeno, no lo mide en un modelo real.

```bash
ai-evolution paper-lab P06 --seed 7
```

## 15. Actividades Bloom

| Nivel | Actividad |
|---|---|
| **Recordar** | Escribe la factorización `p(y \| x)` del decodificador y explica de qué depende cada término. |
| **Explicar** | Explica por qué invertir la secuencia fuente ayuda, en términos de distancia entre dependencias. |
| **Aplicar** | Ejecuta el notebook y anota a partir de qué longitud el primer token deja de ser recuperable. |
| **Analizar** | Argumenta por qué el problema es estructural y no de capacidad, con un contraejemplo numérico. |
| **Evaluar** | Alguien propone «duplicar la dimensión del estado» como solución. Evalúa la propuesta con evidencia. |
| **Crear** | Diseña una métrica que capture la pérdida de información del principio de la secuencia y justifícala. |

## 16. Autoevaluación

1. ¿Por qué las redes profundas previas no servían para traducir?
2. ¿Qué es exactamente el vector `c` y qué se le pide?
3. ¿Por qué la calidad cae con la longitud de la frase?
4. ¿Qué hace la búsqueda en haz y por qué no se usa simplemente el token más probable en cada paso?
5. ¿Invertir la fuente resuelve o mitiga el problema? Justifica.
6. ¿Qué información se pierde por completo en este modelo respecto a la alineación?
7. ¿Qué idea que hoy asociamos a Seq2Seq **no** está en este paper?

## 17. Respuestas esperadas

1. Porque exigían entrada y salida de dimensión fija, y la traducción tiene longitudes
   variables y desconocidas de antemano.
2. El estado final del codificador: un vector de dimensión fija que debe contener toda la
   información necesaria para reconstruir la salida.
3. Porque la información de entrada crece con `n` mientras la capacidad de `c` es constante.
   El estado acaba dominado por los últimos tokens leídos.
4. Mantiene las `k` hipótesis parciales más probables. La decodificación voraz puede quedar
   atrapada tras una primera elección localmente buena y globalmente mala.
5. Mitiga. Acorta la distancia entre las primeras palabras de origen y de destino, pero la
   compresión a tamaño fijo permanece intacta.
6. Qué parte de la entrada dio lugar a qué parte de la salida: no hay ningún mecanismo que lo
   exponga ni lo aprenda.
7. La atención. Es de Bahdanau, Cho y Bengio, y la publicación de arXiv es de septiembre de
   2014, prácticamente simultánea.

## 18. Fuentes primarias

- Sutskever, I., Vinyals, O. y Le, Q. V. (2014). *Sequence to Sequence Learning with Neural
  Networks*. **NIPS 2014**.
  [arXiv:1409.3215](https://arxiv.org/abs/1409.3215) · consultado 2026-08-16.
- Cho, K. et al. (2014). *Learning Phrase Representations using RNN Encoder–Decoder for
  Statistical Machine Translation*. **EMNLP 2014**.
  [arXiv:1406.1078](https://arxiv.org/abs/1406.1078) · consultado 2026-08-16.

---

[⬅️ Anterior: P05 Word2Vec](../P05_word2vec/README.md) ·
[📇 Índice](../../catalog/PAPERS_INDEX.md) ·
[📝 Evaluación](../../../assessments/papers/P06_seq2seq.md) ·
[🏫 Clase 054 del programa](../../../classes/part-04-neural-networks-and-deep-learning/054-rnn-lstm-y-secuencias/README.md) ·
[➡️ Siguiente: P07 Attention](../P07_attention_bahdanau/README.md)
