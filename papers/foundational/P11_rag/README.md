# P11 — RAG

> Separar lo que el sistema **sabe** de cómo **razona**: el conocimiento pasa a un índice
> consultable, actualizable y citable, en vez de quedar congelado en los pesos.

**Nivel:** L3 · **Motor:** `rag` · **Notebook:** [`P11_rag.ipynb`](../../../notebooks/papers/P11_rag.ipynb)
· **Anexo:** [álgebra y geometría](../../annexes/A01_ALGEBRA_Y_GEOMETRIA.md)

## 1. Identificación

| Campo | Valor |
|---|---|
| **Título original** | *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* |
| **Autoría** | Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni y otros |
| **Año** | 2020 |
| **Venue** | arXiv:2005.11401 · NeurIPS 2020 |
| **Fuente primaria** | [arXiv:2005.11401](https://arxiv.org/abs/2005.11401) |
| **Acceso** | Abierto |
| **Fecha de consulta** | 2026-08-16 |

## 2. Problema anterior

Todo lo que un modelo preentrenado sabe está en sus pesos. Eso tiene cuatro consecuencias
incómodas:

1. **No se puede actualizar** sin reentrenar o ajustar.
2. **No se puede auditar**: no hay forma de saber de dónde salió una afirmación.
3. **No se puede corregir** un dato erróneo de forma quirúrgica.
4. **El modelo alucina**: cuando no sabe, genera algo plausible con la misma confianza.

Trabajos previos habían mostrado que los modelos de lenguaje almacenan cantidades sorprendentes
de conocimiento factual (Petroni et al., 2019), y a la vez que ese conocimiento es opaco y
difícil de mantener.

## 3. Propuesta

Combinar **memoria paramétrica** (los pesos del modelo generativo) con **memoria no
paramétrica** (un índice denso sobre un corpus de documentos):

1. Un **recuperador denso** (DPR) codifica la consulta y los documentos en el mismo espacio
   vectorial y devuelve los `k` pasajes más similares.
2. Un **generador seq2seq** (BART) produce la respuesta condicionada a la consulta **y** a los
   pasajes recuperados.
3. Ambos se entrenan de forma **conjunta**: la señal de la generación llega al codificador de
   la consulta (el índice de documentos se mantiene fijo, por coste).

El artículo propone dos variantes: **RAG-Sequence**, que usa el mismo documento para toda la
respuesta, y **RAG-Token**, que puede cambiar de documento en cada token generado.

## 4. Intuición sin fórmulas

Un examen a libro cerrado frente a uno a libro abierto. A libro cerrado, si no lo recuerdas, lo
inventas. A libro abierto, buscas la página, la citas y quien corrige puede verificarla.

**Dónde deja de funcionar la analogía:** en el examen a libro abierto, encontrar la página
garantiza casi la respuesta. Aquí no: el generador puede recuperar el documento correcto y aun
así contradecirlo. Recuperar y responder son dos fallos independientes.

## 5. Matemática mínima

```text
Recuperación densa:
    sim(x, z) = q(x)ᵀ · d(z)          →  top-k(x) por producto escalar

RAG-Sequence (un documento para toda la salida):
    p(y | x) ≈ Σ_{z ∈ top-k(x)}  p_η(z | x) · Π_t p_θ(y_t | x, z, y_<t)

RAG-Token (documento distinto por token):
    p(y | x) ≈ Π_t  Σ_{z ∈ top-k(x)}  p_η(z | x) · p_θ(y_t | x, z, y_<t)
```

- `p_η` — recuperador: memoria **no paramétrica**, sustituible sin reentrenar.
- `p_θ` — generador: memoria **paramétrica**.
- El documento latente `z` se **marginaliza**: no se elige uno y se descarta el resto.

<!-- puente:inicio -->
> [!TIP]
> **Puente matemático.** Esta sección da por sabido lo siguiente. Si algo no te suena,
> léelo primero: está explicado una sola vez, en un solo sitio, y sirve para todas las fichas.

| Dónde | Qué necesitas de ahí |
|---|---|
| [**A01 §2** · Norma y coseno](../../annexes/A01_ALGEBRA_Y_GEOMETRIA.md#2-norma-y-coseno) | recuperar es ordenar por coseno: sin esa métrica no hay recuperación |
<!-- puente:fin -->

## 6. Arquitectura o flujo

```text
   consulta x
       │
       ▼
  ┌──────────────┐        ┌─────────────────────────┐
  │ codificador  │───────►│  índice denso (MIPS)    │
  │ de consulta  │        │  corpus vectorizado     │
  └──────────────┘        └────────────┬────────────┘
                                       │ top-k pasajes z
                                       ▼
                        ┌──────────────────────────┐
       x ──────────────►│  generador seq2seq       │──► respuesta y
                        │  condicionado a (x, z)   │    + cita [z]
                        └──────────────────────────┘

  Actualizar conocimiento = reindexar documentos.  Sin tocar los pesos.
```

## 7. Qué observar en el paper original

- La **distinción entre RAG-Sequence y RAG-Token** y en qué tipo de pregunta gana cada una.
- La **marginalización sobre documentos**: es lo que diferencia RAG de «meter los documentos en
  el prompt». Los `k` documentos contribuyen a la vez, ponderados.
- El **experimento de actualización de conocimiento**: cambiar el índice cambia lo que el
  sistema responde, **sin reentrenar**. Es la demostración práctica de la tesis.
- La comparación contra modelos de **libro cerrado** (solo paramétricos) y contra sistemas
  extractivos.
- La discusión sobre **diversidad y especificidad** de las respuestas generadas frente a las
  extractivas.

## 8. Evidencia y resultados

Evaluación en tareas intensivas en conocimiento: **respuesta a preguntas de dominio abierto**
(Natural Questions, TriviaQA, WebQuestions, CuratedTrec), **generación de preguntas de Jeopardy**
y **verificación de hechos** (FEVER).

RAG establece nuevos máximos en varias de las tareas de respuesta a preguntas de libro abierto
del momento, y genera respuestas más específicas y factuales que los modelos puramente
paramétricos comparables. En verificación de hechos alcanza resultados cercanos a sistemas con
supervisión de evidencia mucho más rica.

> Las cifras por tarea (Exact Match, precisión) están en las tablas del artículo. Verificarlas
> allí antes de citarlas.

La miniatura de este eje aporta el mecanismo y un fallo real: con recuperación léxica, la
consulta correcta sitúa el documento pertinente en primer lugar (score 0,78); una consulta sin
respuesta en el corpus **también** devuelve un documento, con score bajo. De ahí la necesidad
de un umbral de abstención.

## 9. Impacto

- Da nombre a un patrón que hoy es la arquitectura por defecto de la mayoría de aplicaciones
  empresariales de IA generativa.
- Convierte la **base de datos vectorial** en pieza de infraestructura estándar.
- Introduce la exigencia de **atribución**: una respuesta sin fuente pasa a considerarse
  incompleta en dominios regulados.
- Reformula el mantenimiento: actualizar conocimiento se convierte en un problema de
  **ingeniería de datos**, no de entrenamiento.

## 10. Limitaciones

1. **Tres fallos independientes.** (a) el documento no está en el índice; (b) está y no se
   recupera; (c) se recupera y el generador lo contradice. Evaluar RAG exige medir los tres por
   separado.
2. **Alucinación con cita.** El caso más peligroso: la cita es real y relevante, pero la
   afirmación no está en ella. Difícil de detectar a simple vista.
3. **Calidad limitada por la del corpus.** Un índice con documentos obsoletos o contradictorios
   produce respuestas obsoletas o contradictorias, con toda la apariencia de rigor.
4. **Coste de latencia** añadido por la recuperación.
5. **El índice de documentos permanece fijo** durante el entrenamiento conjunto del paper: no
   se reentrena el codificador de documentos.
6. **Fragmentación (chunking) y granularidad** son decisiones de ingeniería con enorme impacto
   y ninguna respuesta universal.
7. **No sabe abstenerse.** El paper no incorpora un mecanismo de «no lo sé»; hay que añadirlo.

## 11. Errores comunes

| Error | Corrección |
|---|---|
| «RAG elimina las alucinaciones» | Las **reduce y las hace auditables**. Un modelo puede citar bien y afirmar mal. |
| «RAG es meter documentos en el prompt» | En el paper, el documento es una **variable latente marginalizada** y el sistema se entrena conjuntamente. Meter texto en el prompt es un caso particular, mucho más simple. |
| «Si la respuesta lleva cita, es correcta» | Hay que verificar que la afirmación **esté** en el documento citado. |
| «Recuperar bien basta» | Recuperación y generación fallan de forma independiente; hay que medir ambas. |
| «RAG usa búsqueda por palabras clave» | Usa recuperación **densa** (DPR). La léxica es una alternativa más simple, útil y a menudo complementaria. |
| «Con RAG el modelo ya no necesita saber nada» | La memoria paramétrica sigue haciendo el trabajo de comprender la consulta y redactar la respuesta. |

## 12. Relación con trabajos anteriores

- **[P05 Word2Vec](../P05_word2vec/README.md) (2013)** y **[P09 BERT](../P09_bert/README.md) (2018)**
  — la representación densa que hace posible la recuperación semántica.
- **Karpukhin et al. (2020), DPR** — el recuperador denso que RAG usa.
  [arXiv:2004.04906](https://arxiv.org/abs/2004.04906)
- **Lewis et al. (2019), BART** — el generador seq2seq.
  [arXiv:1910.13461](https://arxiv.org/abs/1910.13461)
- **Petroni et al. (2019)** — cuánto conocimiento factual almacenan los modelos de lenguaje.
  [arXiv:1909.01066](https://arxiv.org/abs/1909.01066)
- **REALM (Guu et al., 2020)** — trabajo contemporáneo con preentrenamiento aumentado por
  recuperación. [arXiv:2002.08909](https://arxiv.org/abs/2002.08909)

## 13. Relación con trabajos posteriores

- **FiD (2021)** — fusión en el decodificador de muchos pasajes.
- **Self-RAG, RAG con reordenamiento y RAG con verificación (2023+)** — añaden crítica y
  abstención.
- **GraphRAG y RAG sobre grafos de conocimiento** — estructura explícita sobre el corpus.
- **[P13 ReAct](../P13_react/README.md) (2022)** — la recuperación deja de ser un paso fijo y se
  convierte en una **acción** que el modelo decide ejecutar.

## 14. Notebook asociado

[`P11_rag.ipynb`](../../../notebooks/papers/P11_rag.ipynb)

**Qué implementa:** recuperación por similitud de coseno sobre frecuencias de términos,
generación con citas explícitas, el contraste con la respuesta sin recuperación, un caso de
**alucinación con cita** y un mecanismo de abstención por umbral.

**Qué NO implementa:** DPR, entrenamiento conjunto, marginalización sobre documentos ni BART.
La recuperación es léxica, no densa: ilustra el patrón, no el método del paper.

```bash
ai-evolution paper-lab P11 --seed 7
```

## 15. Actividades Bloom

| Nivel | Actividad |
|---|---|
| **Recordar** | Escribe la fórmula de RAG-Sequence e identifica qué representa `z`. |
| **Explicar** | Explica la diferencia entre memoria paramétrica y no paramétrica con un ejemplo de mantenimiento. |
| **Aplicar** | Ejecuta el notebook y ajusta el umbral de abstención hasta que la consulta sin respuesta se rechace. |
| **Analizar** | Diseña tres consultas que provoquen cada uno de los tres modos de fallo. |
| **Evaluar** | Te presentan un sistema con «95 % de respuestas con cita». ¿Qué métricas pides antes de aceptarlo? |
| **Crear** | Diseña un protocolo de evaluación con tres métricas separadas (recuperación, fidelidad, abstención) y define cómo medir cada una. |

## 16. Autoevaluación

1. ¿Qué significa marginalizar sobre el documento latente y por qué no es lo mismo que elegir el mejor?
2. ¿Cuál es la diferencia práctica entre RAG-Sequence y RAG-Token?
3. Nombra los tres modos de fallo de un sistema RAG y una métrica para cada uno.
4. ¿Por qué una alucinación con cita es más peligrosa que una sin cita?
5. ¿Qué se necesita para actualizar el conocimiento de un sistema RAG?
6. ¿Por qué hace falta un umbral de abstención y qué se rompe sin él?
7. ¿Qué parte del sistema sigue dependiendo de la memoria paramétrica del modelo?

## 17. Respuestas esperadas

1. Sumar sobre los `k` documentos ponderando por su probabilidad de recuperación, en vez de
   condicionar solo al mejor. Así la respuesta agrega evidencia de varios pasajes y es más
   robusta a un error del recuperador en la primera posición.
2. RAG-Sequence usa el mismo documento para toda la respuesta (mejor cuando la respuesta viene
   de una fuente única); RAG-Token puede cambiar de documento en cada token (mejor cuando la
   respuesta combina hechos de varias fuentes).
3. (a) cobertura del índice → recall del corpus; (b) recuperación → recall@k / MRR;
   (c) fidelidad → proporción de afirmaciones verificables en el contexto recuperado.
4. Porque la cita aporta una señal de credibilidad que el lector usa como atajo. Verificarla
   exige leer la fuente, y la mayoría no lo hace.
5. Reindexar los documentos. No hace falta tocar los pesos del modelo.
6. Porque el recuperador **siempre** devuelve algo: sin umbral, una consulta fuera del dominio
   recibe el documento «menos malo» y el generador construirá una respuesta sobre él.
7. Comprender la consulta, integrar los pasajes y redactar una respuesta coherente. RAG cambia
   de dónde vienen los hechos, no quién los redacta.

## 18. Fuentes primarias

- Lewis, P. et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*.
  **NeurIPS 2020**.
  [arXiv:2005.11401](https://arxiv.org/abs/2005.11401) · consultado 2026-08-16.
- Karpukhin, V. et al. (2020). *Dense Passage Retrieval for Open-Domain Question Answering*.
  **EMNLP 2020**.
  [arXiv:2004.04906](https://arxiv.org/abs/2004.04906) · consultado 2026-08-16.
- Guu, K. et al. (2020). *REALM: Retrieval-Augmented Language Model Pre-Training*.
  [arXiv:2002.08909](https://arxiv.org/abs/2002.08909) · consultado 2026-08-16.

---

[⬅️ Anterior: P10 GPT-3](../P10_gpt3/README.md) ·
[📇 Índice](../../catalog/PAPERS_INDEX.md) ·
[📝 Evaluación](../../../assessments/papers/P11_rag.md) ·
[🏫 Clase 105 del programa](../../../classes/part-08-retrieval-context-memory-and-knowledge/105-rag-basico-con-citas/README.md) ·
[➡️ Siguiente: P12 InstructGPT](../P12_instructgpt_rlhf/README.md)
