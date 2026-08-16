# 📇 Índice de papers fundacionales

> Generado por `python scripts/generate_papers.py`. No editar a mano.

**Papers:** 16 · **Actualizado:** 2026-08-16 · **Ruta mínima:** P01 → P02 → P03 → P04 → P05 → P06 → P07 → P08 → P09 → P10 → P11 → P12 → P13 → P14 → P15 → P16

## Tabla maestra

| # | Paper | Año | Venue | Nivel | Motor | Ficha | Notebook |
|---|---|---:|---|:---:|---|---|---|
| P01 | El perceptrón: un modelo probabilístico de almacenamiento y organización de información en el cerebro | 1958 | revista | L1 | `perceptron` | [ficha](../foundational/P01_perceptron/README.md) | [notebook](../../notebooks/papers/P01_perceptron.ipynb) |
| P02 | Aprender representaciones retropropagando errores | 1986 | revista | L2 | `backprop` | [ficha](../foundational/P02_backpropagation/README.md) | [notebook](../../notebooks/papers/P02_backpropagation.ipynb) |
| P03 | Memoria larga de corto plazo | 1997 | revista | L2 | `lstm` | [ficha](../foundational/P03_lstm/README.md) | [notebook](../../notebooks/papers/P03_lstm.ipynb) |
| P04 | Clasificación de ImageNet con redes neuronales convolucionales profundas | 2012 | conferencia | L3 | `convnet` | [ficha](../foundational/P04_alexnet/README.md) | [notebook](../../notebooks/papers/P04_alexnet.ipynb) |
| P05 | Estimación eficiente de representaciones de palabras en un espacio vectorial | 2013 | preprint + taller | L2 | `word2vec` | [ficha](../foundational/P05_word2vec/README.md) | [notebook](../../notebooks/papers/P05_word2vec.ipynb) |
| P06 | Aprendizaje de secuencia a secuencia con redes neuronales | 2014 | preprint + conferencia | L3 | `seq2seq` | [ficha](../foundational/P06_seq2seq/README.md) | [notebook](../../notebooks/papers/P06_seq2seq.ipynb) |
| P07 | Traducción automática neuronal aprendiendo conjuntamente a alinear y traducir | 2014 | preprint + conferencia | L3 | `bahdanau` | [ficha](../foundational/P07_attention_bahdanau/README.md) | [notebook](../../notebooks/papers/P07_attention_bahdanau.ipynb) |
| P08 | La atención es todo lo que necesitas | 2017 | preprint + conferencia | L4 | `transformer` | [ficha](../foundational/P08_transformer/README.md) | [notebook](../../notebooks/papers/P08_transformer.ipynb) |
| P09 | BERT: preentrenamiento de Transformers bidireccionales profundos para comprensión del lenguaje | 2018 | preprint + conferencia | L3 | `bert_mlm` | [ficha](../foundational/P09_bert/README.md) | [notebook](../../notebooks/papers/P09_bert.ipynb) |
| P10 | Los modelos de lenguaje son aprendices con pocos ejemplos | 2020 | preprint + conferencia | L3 | `gpt3_icl` | [ficha](../foundational/P10_gpt3/README.md) | [notebook](../../notebooks/papers/P10_gpt3.ipynb) |
| P11 | Generación aumentada por recuperación para tareas de PLN intensivas en conocimiento | 2020 | preprint + conferencia | L3 | `rag` | [ficha](../foundational/P11_rag/README.md) | [notebook](../../notebooks/papers/P11_rag.ipynb) |
| P12 | Entrenar modelos de lenguaje para seguir instrucciones con retroalimentación humana | 2022 | preprint + conferencia | L3 | `rlhf` | [ficha](../foundational/P12_instructgpt_rlhf/README.md) | [notebook](../../notebooks/papers/P12_instructgpt_rlhf.ipynb) |
| P13 | ReAct: sinergia entre razonar y actuar en modelos de lenguaje | 2022 | preprint + conferencia | L2 | `react` | [ficha](../foundational/P13_react/README.md) | [notebook](../../notebooks/papers/P13_react.ipynb) |
| P14 | Toolformer: los modelos de lenguaje pueden enseñarse a sí mismos a usar herramientas | 2023 | preprint + conferencia | L3 | `toolformer` | [ficha](../foundational/P14_toolformer/README.md) | [notebook](../../notebooks/papers/P14_toolformer.ipynb) |
| P15 | Optimización directa de preferencias: tu modelo de lenguaje ya es un modelo de recompensa | 2023 | preprint + conferencia | L4 | `dpo` | [ficha](../foundational/P15_dpo/README.md) | [notebook](../../notebooks/papers/P15_dpo.ipynb) |
| P16 | Sistemas agentic contemporáneos: memoria, reflexión, multiagente e interoperabilidad | 2023 | cluster revisable | L5 | `agentic` | [ficha](../foundational/P16_agentic_systems/README.md) | [notebook](../../notebooks/papers/P16_agentic_systems.ipynb) |

## Qué resolvió cada uno

### P01 · The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain (1958)

- **Autoría:** Frank Rosenblatt
- **Problema anterior:** La IA de los años 50 programaba reglas a mano; no existía un procedimiento para que un sistema ajustara su comportamiento observando datos.
- **Propuesta:** Una unidad de decisión lineal con umbral y una regla de corrección de error que solo actúa cuando la predicción falla.
- **Hito:** Primera máquina que aprende sus propios pesos a partir de ejemplos en lugar de ejecutar reglas escritas por una persona.
- **Conceptos:** perceptrón, clasificador lineal, regla de aprendizaje, separabilidad, conexionismo
- **Clases del programa:** [049](../../classes/part-04-neural-networks-and-deep-learning/049-perceptron-y-limites-de-separabilidad/README.md)
- **Fuentes primarias:** [DOI (Psychological Review)](https://doi.org/10.1037/h0042519)

### P02 · Learning representations by back-propagating errors (1986)

- **Autoría:** David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams
- **Problema anterior:** Sin capas ocultas el perceptrón no resuelve XOR; con capas ocultas no se sabía cómo asignar el error a cada peso interno.
- **Propuesta:** Aplicar la regla de la cadena hacia atrás por el grafo de cómputo para obtener el gradiente de la pérdida respecto de cada peso.
- **Hito:** Un procedimiento práctico para entrenar capas ocultas: la red descubre representaciones intermedias que nadie diseñó.
- **Conceptos:** retropropagación, regla de la cadena, capas ocultas, gradiente, representaciones internas
- **Clases del programa:** [050](../../classes/part-04-neural-networks-and-deep-learning/050-mlp-y-backpropagation/README.md)
- **Fuentes primarias:** [DOI (Nature)](https://doi.org/10.1038/323533a0)

### P03 · Long Short-Term Memory (1997)

- **Autoría:** Sepp Hochreiter, Jürgen Schmidhuber
- **Problema anterior:** En un RNN el gradiente se multiplica en cada paso temporal: se desvanece o explota, y la red no aprende dependencias largas.
- **Propuesta:** Una celda con estado aditivo (carrusel de error constante) y puertas multiplicativas que deciden qué entra y qué sale.
- **Hito:** Primera arquitectura recurrente capaz de mantener información a través de cientos de pasos sin que el gradiente se desvanezca.
- **Conceptos:** LSTM, gradiente desvaneciente, puertas, estado de celda, dependencias largas
- **Clases del programa:** [054](../../classes/part-04-neural-networks-and-deep-learning/054-rnn-lstm-y-secuencias/README.md)
- **Fuentes primarias:** [DOI (Neural Computation)](https://doi.org/10.1162/neco.1997.9.8.1735)

### P04 · ImageNet Classification with Deep Convolutional Neural Networks (2012)

- **Autoría:** Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton
- **Problema anterior:** La visión por computador dependía de descriptores diseñados manualmente; escalar el aprendizaje de features a millones de imágenes era inviable.
- **Propuesta:** Una CNN profunda entrenada en GPU con ReLU, dropout, aumento de datos y solapamiento de pooling sobre ILSVRC-2012.
- **Hito:** El resultado que convirtió el deep learning en la corriente principal: margen amplio sobre los métodos de visión hechos a mano.
- **Conceptos:** CNN, ImageNet, ReLU, dropout, GPU, aumento de datos
- **Clases del programa:** [053](../../classes/part-04-neural-networks-and-deep-learning/053-cnn-y-aprendizaje-espacial/README.md)
- **Fuentes primarias:** [NeurIPS 2012 (proceedings)](https://papers.nips.cc/paper_files/paper/2012) · [DOI (versión Communications of the ACM, 2017)](https://doi.org/10.1145/3065386)

### P05 · Efficient Estimation of Word Representations in Vector Space (2013)

- **Autoría:** Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean
- **Problema anterior:** Representar palabras como identificadores dispersos (one-hot) impide medir similitud; los modelos neuronales de lenguaje previos eran demasiado costosos.
- **Propuesta:** Dos arquitecturas log-lineales sin capa oculta —CBOW y skip-gram— que predicen contexto y producen vectores con estructura lineal.
- **Hito:** El significado distribucional se vuelve barato: vectores densos entrenables sobre miles de millones de palabras.
- **Conceptos:** embeddings, skip-gram, CBOW, muestreo negativo, hipótesis distribucional, analogías
- **Clases del programa:** [066](../../classes/part-05-language-vision-audio-and-multimodal-ai/066-embeddings-semanticos-y-similitud/README.md), [100](../../classes/part-08-retrieval-context-memory-and-knowledge/100-embeddings-y-busqueda-vectorial/README.md)
- **Fuentes primarias:** [arXiv:1301.3781](https://arxiv.org/abs/1301.3781) · [arXiv:1310.4546 (muestreo negativo y frases)](https://arxiv.org/abs/1310.4546)

### P06 · Sequence to Sequence Learning with Neural Networks (2014)

- **Autoría:** Ilya Sutskever, Oriol Vinyals, Quoc V. Le
- **Problema anterior:** Las redes profundas requerían entradas y salidas de dimensión fija; la traducción automática dependía de sistemas estadísticos con muchas piezas separadas.
- **Propuesta:** Un LSTM codifica la entrada en un vector de tamaño fijo y otro LSTM lo decodifica token a token; invertir la secuencia fuente mejora el resultado.
- **Hito:** Una única red aprende a mapear secuencias de longitud variable a secuencias de longitud variable, de extremo a extremo.
- **Conceptos:** encoder-decoder, vector de contexto, traducción automática neuronal, cuello de botella, BLEU
- **Clases del programa:** [054](../../classes/part-04-neural-networks-and-deep-learning/054-rnn-lstm-y-secuencias/README.md)
- **Fuentes primarias:** [arXiv:1409.3215](https://arxiv.org/abs/1409.3215)

### P07 · Neural Machine Translation by Jointly Learning to Align and Translate (2014)

- **Autoría:** Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio
- **Problema anterior:** Comprimir una frase entera en un vector fijo degrada la traducción de frases largas: es un cuello de botella de información.
- **Propuesta:** Un vector de contexto distinto por paso de salida, calculado como suma ponderada de los estados del codificador con pesos aprendidos (atención aditiva).
- **Hito:** Nace la atención: el decodificador deja de depender de un único vector y consulta toda la entrada en cada paso.
- **Conceptos:** atención, alineación, vector de contexto dinámico, softmax, atención aditiva
- **Clases del programa:** [055](../../classes/part-04-neural-networks-and-deep-learning/055-atencion-y-arquitectura-transformer/README.md)
- **Fuentes primarias:** [arXiv:1409.0473](https://arxiv.org/abs/1409.0473)

### P08 · Attention Is All You Need (2017)

- **Autoría:** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin
- **Problema anterior:** La recurrencia impone un cómputo secuencial en la longitud de la secuencia y camina O(n) pasos entre posiciones distantes; eso limita el entrenamiento a gran escala.
- **Propuesta:** Un encoder–decoder compuesto solo de self-attention multi-cabeza, redes feed-forward por posición, conexiones residuales, layer normalization y codificación posicional.
- **Hito:** Elimina la recurrencia y la convolución del modelado de secuencias: todo el cómputo de una capa se paraleliza.
- **Conceptos:** Transformer, self-attention, multi-head, scaled dot-product, codificación posicional, máscara causal, paralelización
- **Clases del programa:** [055](../../classes/part-04-neural-networks-and-deep-learning/055-atencion-y-arquitectura-transformer/README.md), [074](../../classes/part-06-foundation-models-and-llm-engineering/074-objetivos-de-preentrenamiento/README.md)
- **Fuentes primarias:** [arXiv:1706.03762](https://arxiv.org/abs/1706.03762) · [NeurIPS 2017 (proceedings)](https://papers.nips.cc/paper_files/paper/2017)

### P09 · BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (2018)

- **Autoría:** Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova
- **Problema anterior:** Los modelos de lenguaje eran unidireccionales; para comprender una palabra hace falta el contexto de ambos lados, y entrenar bidireccionalmente con predicción del siguiente token es trivialmente degenerado.
- **Propuesta:** Modelado de lenguaje enmascarado (MLM) más predicción de la siguiente oración (NSP), y ajuste fino de todo el modelo por tarea.
- **Hito:** Consolida el patrón preentrenar-y-ajustar: un mismo modelo base sirve para muchas tareas con un ajuste pequeño.
- **Conceptos:** BERT, MLM, bidireccional, preentrenamiento, fine-tuning, GLUE
- **Clases del programa:** [074](../../classes/part-06-foundation-models-and-llm-engineering/074-objetivos-de-preentrenamiento/README.md)
- **Fuentes primarias:** [arXiv:1810.04805](https://arxiv.org/abs/1810.04805) · [ACL Anthology (NAACL 2019)](https://aclanthology.org/N19-1423/)

### P10 · Language Models are Few-Shot Learners (2020)

- **Autoría:** Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, y otros (OpenAI)
- **Problema anterior:** El patrón de BERT exigía un conjunto etiquetado y un ajuste fino por cada tarea nueva; eso no escala a la variedad de tareas reales.
- **Propuesta:** Escalar un Transformer autorregresivo hasta 175 000 millones de parámetros y evaluar en modo zero-shot, one-shot y few-shot mediante condicionamiento en el prompt.
- **Hito:** El aprendizaje en contexto: la tarea se especifica en el prompt y el modelo se adapta sin actualizar ningún peso.
- **Conceptos:** GPT-3, aprendizaje en contexto, few-shot, escalado, modelo autorregresivo, prompt
- **Clases del programa:** [074](../../classes/part-06-foundation-models-and-llm-engineering/074-objetivos-de-preentrenamiento/README.md), [086](../../classes/part-06-foundation-models-and-llm-engineering/086-seleccion-de-modelo-costo-latencia-y-privacidad/README.md)
- **Fuentes primarias:** [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)

### P11 · Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (2020)

- **Autoría:** Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, y otros
- **Problema anterior:** Todo lo que un modelo sabe está congelado en sus pesos: no se puede actualizar sin reentrenar, ni auditar de dónde salió una afirmación.
- **Propuesta:** Combinar un recuperador denso (DPR) sobre un índice de Wikipedia con un generador seq2seq (BART), entrenados de forma conjunta.
- **Hito:** Separa el conocimiento (índice consultable y actualizable) del razonamiento (parámetros del modelo).
- **Conceptos:** RAG, recuperación densa, memoria no paramétrica, citas, atribución, conocimiento actualizable
- **Clases del programa:** [105](../../classes/part-08-retrieval-context-memory-and-knowledge/105-rag-basico-con-citas/README.md), [110](../../classes/part-08-retrieval-context-memory-and-knowledge/110-evaluacion-de-fidelidad-cobertura-y-atribucion/README.md), [111](../../classes/part-08-retrieval-context-memory-and-knowledge/111-proyecto-rag-productivo-y-auditable/README.md)
- **Fuentes primarias:** [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)

### P12 · Training language models to follow instructions with human feedback (2022)

- **Autoría:** Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, y otros (OpenAI)
- **Problema anterior:** Maximizar la verosimilitud del texto de internet no es lo mismo que ser útil, honesto e inocuo; el objetivo de entrenamiento está desalineado con la intención del usuario.
- **Propuesta:** Tres etapas: ajuste supervisado con demostraciones, modelo de recompensa entrenado con comparaciones humanas y optimización por PPO con penalización KL.
- **Hito:** El salto de «modelo que completa texto» a «asistente que sigue instrucciones»: alineación con preferencias humanas.
- **Conceptos:** RLHF, alineación, modelo de recompensa, PPO, preferencias, instrucciones
- **Clases del programa:** [078](../../classes/part-06-foundation-models-and-llm-engineering/078-rlhf-rlaif-y-dpo/README.md)
- **Fuentes primarias:** [arXiv:2203.02155](https://arxiv.org/abs/2203.02155)

### P13 · ReAct: Synergizing Reasoning and Acting in Language Models (2022)

- **Autoría:** Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
- **Problema anterior:** El razonamiento en cadena (CoT) no consulta el mundo y alucina hechos; actuar sin razonar no descompone problemas de varios pasos.
- **Propuesta:** Intercalar trazas de pensamiento y acciones sobre un entorno, de modo que cada observación real condicione el siguiente razonamiento.
- **Hito:** El modelo deja de ser solo un generador de texto y pasa a ser el controlador de un bucle que observa y actúa.
- **Conceptos:** ReAct, agente, bucle pensamiento-acción-observación, herramientas, traza auditable
- **Clases del programa:** [114](../../classes/part-09-ai-agent-engineering/114-ciclo-react-y-observacion-del-entorno/README.md), [112](../../classes/part-09-ai-agent-engineering/112-de-modelo-y-automatizacion-a-agente/README.md)
- **Fuentes primarias:** [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)

### P14 · Toolformer: Language Models Can Teach Themselves to Use Tools (2023)

- **Autoría:** Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, y otros
- **Problema anterior:** Enseñar a un modelo a llamar APIs requería datos anotados por humanos, caros y limitados a las herramientas anotadas.
- **Propuesta:** Generar llamadas candidatas, ejecutarlas y conservar solo las que reducen la pérdida de predecir el texto siguiente; reentrenar con ese corpus filtrado.
- **Hito:** El uso de herramientas se aprende de forma autosupervisada: el criterio de utilidad es la propia pérdida del modelo.
- **Conceptos:** Toolformer, tool use, autosupervisión, filtrado por pérdida, API calls
- **Clases del programa:** [080](../../classes/part-06-foundation-models-and-llm-engineering/080-tool-calling-y-ejecucion-controlada/README.md), [113](../../classes/part-09-ai-agent-engineering/113-anatomia-instrucciones-herramientas-estado-y-salida/README.md)
- **Fuentes primarias:** [arXiv:2302.04761](https://arxiv.org/abs/2302.04761)

### P15 · Direct Preference Optimization: Your Language Model is Secretly a Reward Model (2023)

- **Autoría:** Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, Chelsea Finn
- **Problema anterior:** El pipeline RLHF es frágil y caro: entrena un modelo extra, requiere muestreo on-policy y ajustar PPO es delicado.
- **Propuesta:** Derivar la solución óptima del objetivo RLHF con restricción KL y reescribirlo como una pérdida de clasificación binaria sobre pares de preferencias.
- **Hito:** Alinear un modelo con preferencias humanas sin modelo de recompensa explícito ni bucle de aprendizaje por refuerzo.
- **Conceptos:** DPO, preferencias, recompensa implícita, KL, alineación, pérdida de clasificación
- **Clases del programa:** [078](../../classes/part-06-foundation-models-and-llm-engineering/078-rlhf-rlaif-y-dpo/README.md)
- **Fuentes primarias:** [arXiv:2305.18290](https://arxiv.org/abs/2305.18290)

### P16 · Sistemas agentic contemporáneos (nodo de frontera, revisable) (2023)

- **Autoría:** Varios (nodo compuesto)
- **Problema anterior:** Un bucle ReAct sin memoria, sin criterio de parada ni presupuesto no sobrevive a tareas largas ni a fallos de herramienta.
- **Propuesta:** No hay una única propuesta: hay una familia de trabajos que añaden autocrítica, memoria episódica, currículo autónomo, orquestación multiagente y estándares de acceso a herramientas.
- **Hito:** El agente deja de ser un bucle y pasa a ser un sistema: memoria, reflexión, planificación, presupuesto, múltiples agentes y protocolos de interoperabilidad.
- **Conceptos:** agentic, reflexión, memoria, multiagente, MCP, presupuesto, criterio de parada
- **Clases del programa:** [117](../../classes/part-09-ai-agent-engineering/117-prompt-recurso-tool-skill-workflow-y-agente/README.md), [122](../../classes/part-09-ai-agent-engineering/122-evaluacion-y-depuracion-de-agentes/README.md), [124](../../classes/part-10-multi-agent-systems-and-interoperability/124-workflow-subagente-y-sistema-multiagente/README.md), [132](../../classes/part-10-multi-agent-systems-and-interoperability/132-mcp-tools-resources-y-prompts/README.md), [164](../../classes/part-13-evaluation-safety-security-and-governance/164-seguridad-de-tools-mcp-y-supply-chain/README.md)
- **Fuentes primarias:** [Shinn et al. (2023), Reflexion](https://arxiv.org/abs/2303.11366) · [Park et al. (2023), Generative Agents](https://arxiv.org/abs/2304.03442) · [Wang et al. (2023), Voyager](https://arxiv.org/abs/2305.16291) · [Wu et al. (2023), AutoGen](https://arxiv.org/abs/2308.08155) · [Model Context Protocol (especificación)](https://modelcontextprotocol.io)

## Miniaturas del Transformer

El tratamiento especial de *Attention Is All You Need* se reparte en ocho notebooks:

| Miniatura | Foco |
|---|---|
| [T01 — Por qué había que quitar la recurrencia](../../notebooks/papers/T01_recurrencia_vs_paralelismo.ipynb) | el problema que motiva el paper |
| [T02 — Q, K, V y el producto escalar escalado](../../notebooks/papers/T02_qkv_scaled_dot_product.ipynb) | la ecuación 1 del paper |
| [T03 — Softmax, escala y saturación](../../notebooks/papers/T03_softmax_y_temperatura.ipynb) | por qué √d_k no es cosmética |
| [T04 — Self-attention y máscara causal](../../notebooks/papers/T04_self_attention_y_mascara_causal.ipynb) | atender a la propia secuencia, y no atender al futuro |
| [T05 — Multi-head attention](../../notebooks/papers/T05_multi_head_attention.ipynb) | varias relaciones a la vez, sin coste extra |
| [T06 — Codificación posicional](../../notebooks/papers/T06_positional_encoding.ipynb) | la atención es permutación-equivariante y eso es un problema |
| [T07 — Residual, layer norm y feed-forward](../../notebooks/papers/T07_residual_layernorm_ffn.ipynb) | el andamiaje sin el que la atención no entrena |
| [T08 — Encoder, decoder, complejidad y qué NO dice el título](../../notebooks/papers/T08_encoder_decoder_y_limites.ipynb) | el modelo completo y su lectura honesta |

---

[⬅️ Volver al eje de papers](../README.md) · [🗺️ Ruta](../ROADMAP.md) · [🌐 Fuentes y venues](../guides/FUENTES_Y_VENUES.md)
