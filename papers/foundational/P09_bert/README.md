# P09 — BERT

> El preentrenamiento deja de ser un truco y se convierte en la norma: un modelo base, muchas
> tareas, un ajuste pequeño para cada una.

**Nivel:** L3 · **Motor:** `bert_mlm` · **Notebook:** [`P09_bert.ipynb`](../../../notebooks/papers/P09_bert.ipynb)
· **Anexo:** [probabilidad y verosimilitud](../../annexes/A02_PROBABILIDAD_Y_VEROSIMILITUD.md)

## 1. Identificación

| Campo | Valor |
|---|---|
| **Título original** | *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding* |
| **Autoría** | Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova |
| **Año** | 2018 (arXiv) · 2019 (NAACL) |
| **Venue** | arXiv:1810.04805 · NAACL-HLT 2019 |
| **Fuente primaria** | [arXiv:1810.04805](https://arxiv.org/abs/1810.04805) · [ACL Anthology](https://aclanthology.org/N19-1423/) |
| **Acceso** | Abierto |
| **Fecha de consulta** | 2026-08-16 |

## 2. Problema anterior

Con el [Transformer](../P08_transformer/README.md) disponible, la pregunta pasó a ser **cómo
preentrenarlo**. Los modelos de lenguaje predicen el token siguiente y son, por construcción,
**unidireccionales**: solo ven el pasado.

Para tareas de comprensión —responder preguntas, clasificar, extraer entidades— eso es un
desperdicio: para interpretar una palabra hace falta lo que hay antes **y** después. ELMo
(2018) lo había abordado concatenando dos LSTM entrenadas en direcciones opuestas, pero cada
una seguía viendo un solo lado; la fusión era superficial.

El obstáculo técnico era real: **no se puede entrenar un modelo profundo y bidireccional con
el objetivo de predecir el token siguiente**, porque a través de las capas cada token acabaría
viéndose a sí mismo. La predicción sería trivial.

## 3. Propuesta

Cambiar el objetivo de preentrenamiento:

1. **Masked Language Modeling (MLM).** Se enmascara un porcentaje de los tokens (≈15 %) y el
   modelo predice cada uno usando **todo** el contexto, a ambos lados. Enmascarar es lo que
   hace legítima la bidireccionalidad.
2. **Next Sentence Prediction (NSP).** Dado un par de segmentos, predecir si el segundo sigue
   realmente al primero. Pensado para tareas que relacionan dos frases.

Y un procedimiento uniforme: **preentrenar una vez, ajustar todo el modelo** para cada tarea
añadiendo una capa de salida mínima. La misma arquitectura sirve para clasificación,
etiquetado y respuesta a preguntas.

Detalle importante del MLM: los tokens seleccionados no siempre se sustituyen por `[MASK]`.
Se reparten entre `[MASK]`, una palabra aleatoria y la palabra original, para que el modelo no
aprenda a ignorar las posiciones sin máscara durante el ajuste fino, donde `[MASK]` no aparece.

## 4. Intuición sin fórmulas

Un examen de rellenar huecos. Para adivinar la palabra tapada lees toda la frase, no solo la
mitad izquierda. Un modelo que renuncia al lado derecho está tirando la mitad de la evidencia.

**Dónde deja de funcionar la analogía:** rellenar huecos no es lo mismo que escribir un texto.
BERT es excelente **comprendiendo** y no es un generador: su objetivo nunca fue producir texto
token a token.

## 5. Matemática mínima

```text
MLM:
    L_MLM = − Σ_{t ∈ M} log p(x_t | x_\M)

    M    = conjunto de posiciones enmascaradas
    x_\M = la secuencia con esas posiciones ocultas (contexto completo a ambos lados)

NSP:
    L_NSP = − log p(esSiguiente | segmentoA, segmentoB)

Objetivo total:
    L = L_MLM + L_NSP
```

Entrada: `[CLS] tokens_A [SEP] tokens_B [SEP]`, con tres embeddings sumados por posición
(token + segmento + posición). El vector de `[CLS]` se usa como representación agregada de la
secuencia para clasificación.

**Escala del modelo:** BERT-base con 12 capas, `d_model=768`, 12 cabezas, ≈110 M de parámetros;
BERT-large con 24 capas, `d_model=1024`, 16 cabezas, ≈340 M.

<!-- puente:inicio -->
> [!TIP]
> **Puente matemático.** Esta sección da por sabido lo siguiente. Si algo no te suena,
> léelo primero: está explicado una sola vez, en un solo sitio, y sirve para todas las fichas.

| Dónde | Qué necesitas de ahí |
|---|---|
| [**A02 §3** · Verosimilitud y entropía cruzada](../../annexes/A02_PROBABILIDAD_Y_VEROSIMILITUD.md#3-verosimilitud-y-entropía-cruzada) | predecir la palabra oculta es maximizar una verosimilitud, medida con entropía cruzada |
<!-- puente:fin -->

## 6. Arquitectura o flujo

```text
PREENTRENAMIENTO (no supervisado, corpus masivo)
   [CLS] el banco [MASK] estaba mojado [SEP] llovió toda la noche [SEP]
      │                    ▲                                    │
      │                    │                                    │
      ▼          ENCODER TRANSFORMER × N (bidireccional)        ▼
   NSP: ¿siguiente?              MLM: predecir el token enmascarado

AJUSTE FINO (supervisado, pocos datos por tarea)
   mismo modelo  +  una capa de salida  →  clasificación / QA / etiquetado
   se actualizan TODOS los parámetros
```

## 7. Qué observar en el paper original

- La **figura comparativa** entre BERT, GPT y ELMo: muestra visualmente qué significa
  «bidireccional profundo» frente a «unidireccional» y «bidireccional superficial».
- La **justificación de por qué no se puede usar el objetivo autorregresivo** para entrenar
  bidireccionalmente. Es el argumento central y suele resumirse mal.
- El detalle del **80/10/10** en el enmascarado y su motivación (la discrepancia entre
  preentrenamiento y ajuste fino).
- Los **estudios de ablación**: qué aporta NSP, qué aporta el número de pasos de
  preentrenamiento y qué pasa al usar el modelo como extractor de características congelado.
- La tabla de **GLUE** y las de SQuAD.

## 8. Evidencia y resultados

Evaluación sobre **GLUE** (once tareas de comprensión), **SQuAD v1.1 y v2.0** (respuesta a
preguntas extractiva) y **SWAG** (inferencia de sentido común).

BERT establece nuevos máximos en las tres familias de tareas con el mismo procedimiento de
ajuste, y el artículo reporta una mejora agregada en GLUE que llevó la puntuación por encima
del 80 %. Las ablaciones muestran que **la bidireccionalidad es el factor dominante** y que la
contribución de NSP es menor.

> Las cifras exactas por tarea, para base y large, están en las tablas del artículo.
> Verificarlas allí antes de citarlas.

La miniatura de este eje aporta el argumento estructural, no las cifras: contando candidatos
compatibles en un corpus de juguete, añadir el contexto derecho **nunca amplía** el conjunto de
candidatos y en general lo reduce.

## 9. Impacto

- Convierte **preentrenar y ajustar** en el procedimiento estándar del PLN, desplazando a los
  modelos entrenados desde cero por tarea.
- Genera una familia enorme de descendientes: RoBERTa, ALBERT, DistilBERT, ELECTRA, DeBERTa y
  variantes por idioma y dominio.
- Sus embeddings contextuales son la base de los **recuperadores densos** que sostienen
  [RAG](../P11_rag/README.md).
- Instala la idea de **modelo fundacional**: un artefacto costoso de entrenar y barato de
  adaptar.

## 10. Limitaciones

1. **No genera texto.** El objetivo MLM no define una distribución autorregresiva utilizable
   para generación libre.
2. **Discrepancia preentrenamiento/ajuste.** `[MASK]` aparece en el preentrenamiento y nunca en
   el uso real; el reparto 80/10/10 mitiga el problema sin eliminarlo.
3. **Ineficiencia del MLM.** Solo se aprende de ≈15 % de los tokens por paso (ELECTRA atacó
   exactamente esto).
4. **NSP resultó de valor dudoso**: RoBERTa (2019) mostró que quitarlo no perjudica.
5. **Longitud de contexto limitada** (512 tokens en las configuraciones del paper).
6. **Coste de ajuste fino por tarea**: hay que guardar una copia completa del modelo por cada
   tarea, lo que motivó después los métodos de ajuste eficiente en parámetros.
7. **Sesgos del corpus** heredados y amplificados.

## 11. Errores comunes

| Error | Corrección |
|---|---|
| «BERT es un LLM generativo» | Es un **encoder** para comprensión. La familia generativa viene de la rama decoder ([P10](../P10_gpt3/README.md)). |
| «BERT fue el primer modelo bidireccional» | ELMo (2018) ya combinaba dos direcciones. BERT fue el primero **profundamente** bidireccional en todas las capas. |
| «MLM es lo mismo que predecir el token siguiente» | Son objetivos distintos y producen modelos con capacidades distintas. |
| «NSP es esencial en BERT» | Las ablaciones posteriores (RoBERTa) mostraron que se puede eliminar sin pérdida. |
| «BERT entiende el lenguaje» | Obtiene buenas puntuaciones en GLUE y SQuAD. Trabajos posteriores mostraron que parte de ese rendimiento se apoya en atajos estadísticos del dataset. |
| «Se enmascara siempre con `[MASK]`» | 80 % `[MASK]`, 10 % palabra aleatoria, 10 % palabra original. |

## 12. Relación con trabajos anteriores

- **[P08 Transformer](../P08_transformer/README.md) (2017)** — la arquitectura (solo el encoder).
- **ELMo (Peters et al., 2018)** — embeddings contextuales con LSTM bidireccionales.
  [ACL Anthology](https://aclanthology.org/N18-1202/)
- **GPT-1 (Radford et al., 2018)** — preentrenar y ajustar con un decoder unidireccional; el
  trabajo con el que BERT se compara directamente.
- **ULMFiT (Howard y Ruder, 2018)** — transferencia en PLN con LSTM.
  [arXiv:1801.06146](https://arxiv.org/abs/1801.06146)
- **[P05 Word2Vec](../P05_word2vec/README.md) (2013)** — el antecesor estático de la idea de
  representación reutilizable.

## 13. Relación con trabajos posteriores

- **RoBERTa (2019)** — mismo modelo, mejor entrenado, sin NSP.
  [arXiv:1907.11692](https://arxiv.org/abs/1907.11692)
- **ELECTRA (2020)** — objetivo más eficiente que MLM.
  [arXiv:2003.10555](https://arxiv.org/abs/2003.10555)
- **Sentence-BERT (2019)** y los recuperadores densos → [P11 RAG](../P11_rag/README.md).
- **[P10 GPT-3](../P10_gpt3/README.md) (2020)** — la rama alternativa, que acabó dominando la
  conversación pública.

## 14. Notebook asociado

[`P09_bert.ipynb`](../../../notebooks/papers/P09_bert.ipynb)

**Qué implementa:** el argumento de la bidireccionalidad, mediante conteo de candidatos
compatibles con contexto izquierdo frente a contexto completo sobre un corpus de juguete con
polisemia («banco»).

**Qué NO implementa:** ningún Transformer, ningún preentrenamiento, ni NSP, ni el reparto
80/10/10, ni evaluación GLUE. Es un modelo de conteo que ilustra **por qué** el contexto
derecho aporta información, no **cómo** lo aprovecha BERT.

```bash
ai-evolution paper-lab P09 --seed 7
```

## 15. Actividades Bloom

| Nivel | Actividad |
|---|---|
| **Recordar** | Escribe los dos objetivos de preentrenamiento y qué predice cada uno. |
| **Explicar** | Explica por qué predecir el token siguiente impide entrenar bidireccionalmente en profundidad. |
| **Aplicar** | Añade frases al corpus del notebook y observa cómo cambia la ambigüedad del hueco. |
| **Analizar** | Compara las tres familias (encoder, decoder, encoder-decoder) por objetivo y tareas idóneas. |
| **Evaluar** | RoBERTa quitó NSP sin pérdida. ¿Qué dice eso sobre las ablaciones del paper original? |
| **Crear** | Diseña un objetivo de preentrenamiento alternativo y argumenta qué capacidad induciría. |

## 16. Autoevaluación

1. ¿Por qué enmascarar hace legítima la bidireccionalidad?
2. ¿Qué problema resuelve el reparto 80/10/10?
3. ¿Por qué el MLM es menos eficiente por token que el objetivo autorregresivo?
4. ¿Para qué sirve el token `[CLS]`?
5. ¿Por qué no conviene usar BERT para generar texto libre?
6. ¿Qué mostró RoBERTa sobre NSP, y qué implicación metodológica tiene?
7. ¿Qué significa exactamente una puntuación alta en GLUE, y qué no significa?

## 17. Respuestas esperadas

1. Porque el token objetivo se oculta de la entrada. Sin ocultarlo, la información fluiría por
   las capas y el modelo se vería a sí mismo: la predicción sería trivial.
2. La discrepancia entre preentrenamiento y uso: `[MASK]` nunca aparece en el ajuste fino ni en
   inferencia. Manteniendo a veces la palabra original o una aleatoria, el modelo debe construir
   una representación útil de **todas** las posiciones, no solo de las marcadas.
3. Porque solo aporta señal de aprendizaje el ≈15 % de posiciones enmascaradas, mientras que el
   objetivo autorregresivo produce una predicción por cada token de la secuencia.
4. Es una posición fija cuya representación final se usa como resumen de toda la secuencia para
   tareas de clasificación.
5. Porque su objetivo no define `p(x_t | x_<t)`. Puede rellenar huecos, no continuar un texto
   de forma coherente token a token.
6. Que su aportación era prescindible. Implicación: una ablación del propio paper puede ser
   insuficiente si el resto de la configuración no está bien ajustada; la replicación
   independiente importa.
7. Que el modelo acierta un conjunto de tareas de comprensión con sus datasets y métricas.
   No significa comprensión general: parte del rendimiento puede provenir de correlaciones
   superficiales de esos datasets.

## 18. Fuentes primarias

- Devlin, J., Chang, M.-W., Lee, K. y Toutanova, K. (2019). *BERT: Pre-training of Deep
  Bidirectional Transformers for Language Understanding*. **NAACL-HLT 2019**.
  [arXiv:1810.04805](https://arxiv.org/abs/1810.04805) ·
  [ACL Anthology](https://aclanthology.org/N19-1423/) · consultado 2026-08-16.
- Peters, M. et al. (2018). *Deep Contextualized Word Representations* (ELMo). **NAACL 2018**.
  [ACL Anthology](https://aclanthology.org/N18-1202/) · consultado 2026-08-16.
- Liu, Y. et al. (2019). *RoBERTa: A Robustly Optimized BERT Pretraining Approach*.
  [arXiv:1907.11692](https://arxiv.org/abs/1907.11692) · consultado 2026-08-16.

---

[⬅️ Anterior: P08 Transformer](../P08_transformer/README.md) ·
[📇 Índice](../../catalog/PAPERS_INDEX.md) ·
[📝 Evaluación](../../../assessments/papers/P09_bert.md) ·
[🏫 Clase 074 del programa](../../../classes/part-06-foundation-models-and-llm-engineering/074-objetivos-de-preentrenamiento/README.md) ·
[➡️ Siguiente: P10 GPT-3](../P10_gpt3/README.md)
