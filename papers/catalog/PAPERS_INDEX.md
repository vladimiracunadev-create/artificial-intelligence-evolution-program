# 📇 Índice de papers fundacionales

> Generado por `python scripts/generate_papers.py`. No editar a mano.

**Papers:** 52 · **Actualizado:** 2026-08-16 · **Cobertura:** 1958–2025

> [!NOTE]
> Los identificadores `PXX` son **estables**: se asignan al incorporar cada paper y no
> se renumeran nunca, para no romper enlaces, notebooks ni evaluaciones. Por eso su orden
> es de incorporación y **no significa nada**. Para estudiar, usa el orden cronológico de
> esta tabla o la [vista temática](#vista-tematica).

## 📅 Tabla maestra — todos los papers, por año

| Año | # | Paper | Bloque | Nivel | Motor | Ficha | Notebook |
|---:|---|---|---|:---:|---|---|---|
| **1958** | P01 | El perceptrón: un modelo probabilístico de almacenamiento y organización de información en el cerebro | 🔗 cadena | L1 | `perceptron` | [ficha](../foundational/P01_perceptron/README.md) | [nb](../../notebooks/papers/P01_perceptron.ipynb) |
| **1986** | P02 | Aprender representaciones retropropagando errores | 🔗 cadena | L2 | `backprop` | [ficha](../foundational/P02_backpropagation/README.md) | [nb](../../notebooks/papers/P02_backpropagation.ipynb) |
| **1997** | P03 | Memoria larga de corto plazo | 🔗 cadena | L2 | `lstm` | [ficha](../foundational/P03_lstm/README.md) | [nb](../../notebooks/papers/P03_lstm.ipynb) |
| **2012** | P04 | Clasificación de ImageNet con redes neuronales convolucionales profundas | 🔗 cadena | L3 | `convnet` | [ficha](../foundational/P04_alexnet/README.md) | [nb](../../notebooks/papers/P04_alexnet.ipynb) |
| **2013** | P05 | Estimación eficiente de representaciones de palabras en un espacio vectorial | 🔗 cadena | L2 | `word2vec` | [ficha](../foundational/P05_word2vec/README.md) | [nb](../../notebooks/papers/P05_word2vec.ipynb) |
| **2013** | P38 | Bayes variacional con autocodificación | 🏗️ arquitectura | L3 | `vae` | [ficha](../foundational/P38_vae/README.md) | [nb](../../notebooks/papers/P38_vae.ipynb) |
| **2014** | P06 | Aprendizaje de secuencia a secuencia con redes neuronales | 🔗 cadena | L3 | `seq2seq` | [ficha](../foundational/P06_seq2seq/README.md) | [nb](../../notebooks/papers/P06_seq2seq.ipynb) |
| **2014** | P07 | Traducción automática neuronal aprendiendo conjuntamente a alinear y traducir | 🔗 cadena | L3 | `bahdanau` | [ficha](../foundational/P07_attention_bahdanau/README.md) | [nb](../../notebooks/papers/P07_attention_bahdanau.ipynb) |
| **2014** | P23 | GloVe: vectores globales para representación de palabras | 🔤 representación | L2 | `glove` | [ficha](../foundational/P23_glove/README.md) | [nb](../../notebooks/papers/P23_glove.ipynb) |
| **2014** | P39 | Redes generativas adversarias | 🏗️ arquitectura | L3 | `gan` | [ficha](../foundational/P39_gan/README.md) | [nb](../../notebooks/papers/P39_gan.ipynb) |
| **2014** | P40 | Dropout: una forma simple de evitar el sobreajuste en redes neuronales | 🏗️ arquitectura | L2 | `dropout` | [ficha](../foundational/P40_dropout/README.md) | [nb](../../notebooks/papers/P40_dropout.ipynb) |
| **2014** | P41 | Adam: un método de optimización estocástica | 🏗️ arquitectura | L2 | `adam` | [ficha](../foundational/P41_adam/README.md) | [nb](../../notebooks/papers/P41_adam.ipynb) |
| **2014** | P42 | Explicar y aprovechar los ejemplos adversarios | 🏗️ arquitectura | L3 | `adversarial` | [ficha](../foundational/P42_adversarial/README.md) | [nb](../../notebooks/papers/P42_adversarial.ipynb) |
| **2015** | P26 | Control a nivel humano mediante aprendizaje por refuerzo profundo | 🤖 agentes | L3 | `dqn` | [ficha](../foundational/P26_dqn/README.md) | [nb](../../notebooks/papers/P26_dqn.ipynb) |
| **2015** | P43 | Normalización por lotes: acelerar el entrenamiento profundo | 🏗️ arquitectura | L2 | `batchnorm` | [ficha](../foundational/P43_batchnorm/README.md) | [nb](../../notebooks/papers/P43_batchnorm.ipynb) |
| **2015** | P44 | Aprendizaje residual profundo para reconocimiento de imágenes | 🏗️ arquitectura | L3 | `resnet` | [ficha](../foundational/P44_resnet/README.md) | [nb](../../notebooks/papers/P44_resnet.ipynb) |
| **2015** | P45 | Destilar el conocimiento de una red neuronal | 🏗️ arquitectura | L2 | `distillation` | [ficha](../foundational/P45_distillation/README.md) | [nb](../../notebooks/papers/P45_distillation.ipynb) |
| **2016** | P27 | Dominar el go con redes neuronales profundas y búsqueda en árbol | 🤖 agentes | L4 | `alphago` | [ficha](../foundational/P27_alphago/README.md) | [nb](../../notebooks/papers/P27_alphago.ipynb) |
| **2017** | P08 | La atención es todo lo que necesitas | 🔗 cadena | L4 | `transformer` | [ficha](../foundational/P08_transformer/README.md) | [nb](../../notebooks/papers/P08_transformer.ipynb) |
| **2018** | P09 | BERT: preentrenamiento de Transformers bidireccionales profundos para comprensión del lenguaje | 🔗 cadena | L3 | `bert_mlm` | [ficha](../foundational/P09_bert/README.md) | [nb](../../notebooks/papers/P09_bert.ipynb) |
| **2018** | P24 | Representaciones profundas de palabras dependientes del contexto | 🔤 representación | L3 | `elmo` | [ficha](../foundational/P24_elmo/README.md) | [nb](../../notebooks/papers/P24_elmo.ipynb) |
| **2019** | P25 | Explorar los límites del aprendizaje por transferencia con un Transformer unificado texto a texto | 🔤 representación | L3 | `t5` | [ficha](../foundational/P25_t5/README.md) | [nb](../../notebooks/papers/P25_t5.ipynb) |
| **2020** | P10 | Los modelos de lenguaje son aprendices con pocos ejemplos | 🔗 cadena | L3 | `gpt3_icl` | [ficha](../foundational/P10_gpt3/README.md) | [nb](../../notebooks/papers/P10_gpt3.ipynb) |
| **2020** | P11 | Generación aumentada por recuperación para tareas de PLN intensivas en conocimiento | 🔗 cadena | L3 | `rag` | [ficha](../foundational/P11_rag/README.md) | [nb](../../notebooks/papers/P11_rag.ipynb) |
| **2020** | P17 | Modelos probabilísticos de difusión con eliminación de ruido | 📚 ampliada | L3 | `diffusion` | [ficha](../foundational/P17_diffusion/README.md) | [nb](../../notebooks/papers/P17_diffusion.ipynb) |
| **2020** | P46 | Una imagen vale 16x16 palabras: Transformers para reconocimiento de imágenes a escala | 🏗️ arquitectura | L3 | `vit` | [ficha](../foundational/P46_vit/README.md) | [nb](../../notebooks/papers/P46_vit.ipynb) |
| **2021** | P18 | Aprender modelos visuales transferibles con supervisión de lenguaje natural | 📚 ampliada | L3 | `clip` | [ficha](../foundational/P18_clip/README.md) | [nb](../../notebooks/papers/P18_clip.ipynb) |
| **2021** | P34 | RoFormer: Transformer mejorado con codificación posicional rotatoria | 🧠 memoria | L3 | `rope` | [ficha](../foundational/P34_rope/README.md) | [nb](../../notebooks/papers/P34_rope.ipynb) |
| **2021** | P47 | Predicción de estructura de proteínas de alta precisión con AlphaFold | 🏗️ arquitectura | L4 | `alphafold` | [ficha](../foundational/P47_alphafold/README.md) | [nb](../../notebooks/papers/P47_alphafold.ipynb) |
| **2021** | P48 | LoRA: adaptación de rango bajo de modelos de lenguaje grandes | 🏗️ arquitectura | L3 | `lora` | [ficha](../foundational/P48_lora/README.md) | [nb](../../notebooks/papers/P48_lora.ipynb) |
| **2022** | P12 | Entrenar modelos de lenguaje para seguir instrucciones con retroalimentación humana | 🔗 cadena | L3 | `rlhf` | [ficha](../foundational/P12_instructgpt_rlhf/README.md) | [nb](../../notebooks/papers/P12_instructgpt_rlhf.ipynb) |
| **2022** | P13 | ReAct: sinergia entre razonar y actuar en modelos de lenguaje | 🔗 cadena | L2 | `react` | [ficha](../foundational/P13_react/README.md) | [nb](../../notebooks/papers/P13_react.ipynb) |
| **2022** | P19 | Entrenar modelos de lenguaje grandes con cómputo óptimo | 📚 ampliada | L4 | `scaling_laws` | [ficha](../foundational/P19_scaling_laws/README.md) | [nb](../../notebooks/papers/P19_scaling_laws.ipynb) |
| **2022** | P28 | El prompting de cadena de pensamiento provoca razonamiento en modelos de lenguaje grandes | 🤖 agentes | L2 | `cot` | [ficha](../foundational/P28_chain_of_thought/README.md) | [nb](../../notebooks/papers/P28_chain_of_thought.ipynb) |
| **2022** | P35 | FlashAttention: atención exacta, rápida y eficiente en memoria, consciente de la E/S | 🧠 memoria | L4 | `flashattention` | [ficha](../foundational/P35_flashattention/README.md) | [nb](../../notebooks/papers/P35_flashattention.ipynb) |
| **2022** | P50 | IA constitucional: inocuidad a partir de retroalimentación de IA | 🛡️ evaluación | L4 | `constitutional_ai` | [ficha](../foundational/P50_constitutional_ai/README.md) | [nb](../../notebooks/papers/P50_constitutional_ai.ipynb) |
| **2023** | P14 | Toolformer: los modelos de lenguaje pueden enseñarse a sí mismos a usar herramientas | 🔗 cadena | L3 | `toolformer` | [ficha](../foundational/P14_toolformer/README.md) | [nb](../../notebooks/papers/P14_toolformer.ipynb) |
| **2023** | P15 | Optimización directa de preferencias: tu modelo de lenguaje ya es un modelo de recompensa | 🔗 cadena | L4 | `dpo` | [ficha](../foundational/P15_dpo/README.md) | [nb](../../notebooks/papers/P15_dpo.ipynb) |
| **2023** | P16 | Sistemas agentic contemporáneos: memoria, reflexión, multiagente e interoperabilidad | 🔗 cadena | L5 | `agentic` | [ficha](../foundational/P16_agentic_systems/README.md) | [nb](../../notebooks/papers/P16_agentic_systems.ipynb) |
| **2023** | P20 | Mamba: modelado de secuencias en tiempo lineal con espacios de estados selectivos | 📚 ampliada | L4 | `ssm` | [ficha](../foundational/P20_mamba/README.md) | [nb](../../notebooks/papers/P20_mamba.ipynb) |
| **2023** | P29 | Árbol de pensamientos: resolución deliberada de problemas con modelos de lenguaje grandes | 🤖 agentes | L3 | `tot` | [ficha](../foundational/P29_tree_of_thoughts/README.md) | [nb](../../notebooks/papers/P29_tree_of_thoughts.ipynb) |
| **2023** | P30 | Reflexion: agentes de lenguaje con refuerzo verbal | 🤖 agentes | L2 | `reflexion` | [ficha](../foundational/P30_reflexion/README.md) | [nb](../../notebooks/papers/P30_reflexion.ipynb) |
| **2023** | P31 | Agentes generativos: simulacros interactivos de comportamiento humano | 🤖 agentes | L3 | `generative_agents` | [ficha](../foundational/P31_generative_agents/README.md) | [nb](../../notebooks/papers/P31_generative_agents.ipynb) |
| **2023** | P32 | Voyager: un agente encarnado de final abierto con modelos de lenguaje grandes | 🤖 agentes | L3 | `voyager` | [ficha](../foundational/P32_voyager/README.md) | [nb](../../notebooks/papers/P32_voyager.ipynb) |
| **2023** | P33 | AutoGen: aplicaciones de nueva generación mediante conversación multiagente | 🤖 agentes | L4 | `autogen` | [ficha](../foundational/P33_autogen/README.md) | [nb](../../notebooks/papers/P33_autogen.ipynb) |
| **2023** | P36 | Perdidos en el medio: cómo usan los modelos de lenguaje los contextos largos | 🧠 memoria | L3 | `lost_in_middle` | [ficha](../foundational/P36_lost_in_middle/README.md) | [nb](../../notebooks/papers/P36_lost_in_middle.ipynb) |
| **2023** | P37 | MemGPT: modelos de lenguaje como sistemas operativos | 🧠 memoria | L3 | `memgpt` | [ficha](../foundational/P37_memgpt/README.md) | [nb](../../notebooks/papers/P37_memgpt.ipynb) |
| **2023** | P49 | QLoRA: ajuste fino eficiente de modelos cuantizados | 🏗️ arquitectura | L3 | `quantization` | [ficha](../foundational/P49_qlora/README.md) | [nb](../../notebooks/papers/P49_qlora.ipynb) |
| **2023** | P51 | SWE-bench: ¿pueden los modelos resolver incidencias reales de GitHub? | 🛡️ evaluación | L3 | `swebench` | [ficha](../foundational/P51_swebench/README.md) | [nb](../../notebooks/papers/P51_swebench.ipynb) |
| **2023** | P52 | Hacia la monosemanticidad: descomponer modelos de lenguaje con aprendizaje de diccionario | 🛡️ evaluación | L5 | `superposition` | [ficha](../foundational/P52_superposition/README.md) | [nb](../../notebooks/papers/P52_superposition.ipynb) |
| **2024** | P21 | Mixtral: mezcla dispersa de expertos | 📚 ampliada | L3 | `moe` | [ficha](../foundational/P21_moe/README.md) | [nb](../../notebooks/papers/P21_moe.ipynb) |
| **2025** | P22 | DeepSeek-R1: incentivar la capacidad de razonamiento mediante aprendizaje por refuerzo | 📚 ampliada | L5 | `rl_reasoning` | [ficha](../foundational/P22_deepseek_r1/README.md) | [nb](../../notebooks/papers/P22_deepseek_r1.ipynb) |

<a id="vista-tematica"></a>

## 🧭 Vista temática — por bloque

### 🔗 cadena

P01–P16: la cadena canónica donde cada paper resuelve lo que el anterior dejó abierto. Se estudia en orden.

- **1958** · [P01 · El perceptrón: un modelo probabilístico de almacenamiento y organización de información en el cerebro](../foundational/P01_perceptron/README.md) — Primera máquina que aprende sus propios pesos a partir de ejemplos en lugar de ejecutar reglas escritas por una persona.
- **1986** · [P02 · Aprender representaciones retropropagando errores](../foundational/P02_backpropagation/README.md) — Un procedimiento práctico para entrenar capas ocultas: la red descubre representaciones intermedias que nadie diseñó.
- **1997** · [P03 · Memoria larga de corto plazo](../foundational/P03_lstm/README.md) — Primera arquitectura recurrente capaz de mantener información a través de cientos de pasos sin que el gradiente se desvanezca.
- **2012** · [P04 · Clasificación de ImageNet con redes neuronales convolucionales profundas](../foundational/P04_alexnet/README.md) — El resultado que convirtió el deep learning en la corriente principal: margen amplio sobre los métodos de visión hechos a mano.
- **2013** · [P05 · Estimación eficiente de representaciones de palabras en un espacio vectorial](../foundational/P05_word2vec/README.md) — El significado distribucional se vuelve barato: vectores densos entrenables sobre miles de millones de palabras.
- **2014** · [P06 · Aprendizaje de secuencia a secuencia con redes neuronales](../foundational/P06_seq2seq/README.md) — Una única red aprende a mapear secuencias de longitud variable a secuencias de longitud variable, de extremo a extremo.
- **2014** · [P07 · Traducción automática neuronal aprendiendo conjuntamente a alinear y traducir](../foundational/P07_attention_bahdanau/README.md) — Nace la atención: el decodificador deja de depender de un único vector y consulta toda la entrada en cada paso.
- **2017** · [P08 · La atención es todo lo que necesitas](../foundational/P08_transformer/README.md) — Elimina la recurrencia y la convolución del modelado de secuencias: todo el cómputo de una capa se paraleliza.
- **2018** · [P09 · BERT: preentrenamiento de Transformers bidireccionales profundos para comprensión del lenguaje](../foundational/P09_bert/README.md) — Consolida el patrón preentrenar-y-ajustar: un mismo modelo base sirve para muchas tareas con un ajuste pequeño.
- **2020** · [P10 · Los modelos de lenguaje son aprendices con pocos ejemplos](../foundational/P10_gpt3/README.md) — El aprendizaje en contexto: la tarea se especifica en el prompt y el modelo se adapta sin actualizar ningún peso.
- **2020** · [P11 · Generación aumentada por recuperación para tareas de PLN intensivas en conocimiento](../foundational/P11_rag/README.md) — Separa el conocimiento (índice consultable y actualizable) del razonamiento (parámetros del modelo).
- **2022** · [P12 · Entrenar modelos de lenguaje para seguir instrucciones con retroalimentación humana](../foundational/P12_instructgpt_rlhf/README.md) — El salto de «modelo que completa texto» a «asistente que sigue instrucciones»: alineación con preferencias humanas.
- **2022** · [P13 · ReAct: sinergia entre razonar y actuar en modelos de lenguaje](../foundational/P13_react/README.md) — El modelo deja de ser solo un generador de texto y pasa a ser el controlador de un bucle que observa y actúa.
- **2023** · [P14 · Toolformer: los modelos de lenguaje pueden enseñarse a sí mismos a usar herramientas](../foundational/P14_toolformer/README.md) — El uso de herramientas se aprende de forma autosupervisada: el criterio de utilidad es la propia pérdida del modelo.
- **2023** · [P15 · Optimización directa de preferencias: tu modelo de lenguaje ya es un modelo de recompensa](../foundational/P15_dpo/README.md) — Alinear un modelo con preferencias humanas sin modelo de recompensa explícito ni bucle de aprendizaje por refuerzo.
- **2023** · [P16 · Sistemas agentic contemporáneos: memoria, reflexión, multiagente e interoperabilidad](../foundational/P16_agentic_systems/README.md) — El agente deja de ser un bucle y pasa a ser un sistema: memoria, reflexión, planificación, presupuesto, múltiples agentes y protocolos de interoperabilidad.

### 📚 ampliada

P17–P22: cobertura que la cadena mínima no da (generativa, multimodal, escalado) y continuación hasta 2025. Ordenada por año.

- **2020** · [P17 · Modelos probabilísticos de difusión con eliminación de ruido](../foundational/P17_diffusion/README.md) — La generación deja de ser un salto en la oscuridad: se aprende a deshacer, paso a paso, un proceso de ruido conocido.
- **2021** · [P18 · Aprender modelos visuales transferibles con supervisión de lenguaje natural](../foundational/P18_clip/README.md) — El texto se convierte en la etiqueta: un solo modelo clasifica categorías que nadie anotó, describiéndolas con palabras.
- **2022** · [P19 · Entrenar modelos de lenguaje grandes con cómputo óptimo](../foundational/P19_scaling_laws/README.md) — Corrige la carrera por el tamaño: a cómputo fijo, los modelos de la época estaban infraentrenados en datos.
- **2023** · [P20 · Mamba: modelado de secuencias en tiempo lineal con espacios de estados selectivos](../foundational/P20_mamba/README.md) — El primer competidor serio del Transformer en lenguaje: tiempo lineal y estado de tamaño fijo, sin atención.
- **2024** · [P21 · Mixtral: mezcla dispersa de expertos](../foundational/P21_moe/README.md) — Desacopla capacidad de cómputo: 47 000 millones de parámetros totales, 13 000 millones activos por token.
- **2025** · [P22 · DeepSeek-R1: incentivar la capacidad de razonamiento mediante aprendizaje por refuerzo](../foundational/P22_deepseek_r1/README.md) — El razonamiento se incentiva con refuerzo puro, sin trazas humanas anotadas; y es el primer LLM de pesos abiertos publicado tras revisión por pares.

### 🔤 representación

P23–P25: cómo el lenguaje pasó de vectores estáticos a representaciones contextuales y de ahí a un formato único texto → texto. Ordenada por año.

- **2014** · [P23 · GloVe: vectores globales para representación de palabras](../foundational/P23_glove/README.md) — Unifica las dos familias de embeddings: factorizar estadísticas globales de co-ocurrencia con la ventaja de los métodos predictivos.
- **2018** · [P24 · Representaciones profundas de palabras dependientes del contexto](../foundational/P24_elmo/README.md) — Un vector por APARICIÓN y no por palabra: la polisemia deja de colapsar en un único punto del espacio.
- **2019** · [P25 · Explorar los límites del aprendizaje por transferencia con un Transformer unificado texto a texto](../foundational/P25_t5/README.md) — Todo problema de texto se reescribe como texto → texto: un solo modelo, una sola pérdida, cero cabezas específicas.

### 🤖 agentes

P26–P33: decisión secuencial y agentes. Empieza en el refuerzo profundo y la búsqueda guiada —de donde viene la idea de agente— y llega al razonamiento deliberado, la memoria, las habilidades reutilizables y el multiagente. Ordenada por año.

- **2015** · [P26 · Control a nivel humano mediante aprendizaje por refuerzo profundo](../foundational/P26_dqn/README.md) — El primer agente que aprende a actuar directamente desde píxeles, con la misma arquitectura y los mismos hiperparámetros en decenas de juegos.
- **2016** · [P27 · Dominar el go con redes neuronales profundas y búsqueda en árbol](../foundational/P27_alphago/README.md) — Une las dos tradiciones de la IA: la búsqueda simbólica de la parte 01 y el aprendizaje profundo de la parte 04, en un solo sistema.
- **2022** · [P28 · El prompting de cadena de pensamiento provoca razonamiento en modelos de lenguaje grandes](../foundational/P28_chain_of_thought/README.md) — Descomponer en pasos intermedios desbloquea tareas que el mismo modelo fallaba respondiendo de una vez.
- **2023** · [P29 · Árbol de pensamientos: resolución deliberada de problemas con modelos de lenguaje grandes](../foundational/P29_tree_of_thoughts/README.md) — Devuelve la búsqueda clásica al razonamiento: explorar varias ramas, evaluarlas y poder retroceder.
- **2023** · [P30 · Reflexion: agentes de lenguaje con refuerzo verbal](../foundational/P30_reflexion/README.md) — El agente aprende entre intentos sin tocar un solo peso: el refuerzo ocurre en el contexto, en lenguaje natural.
- **2023** · [P31 · Agentes generativos: simulacros interactivos de comportamiento humano](../foundational/P31_generative_agents/README.md) — Resuelve la memoria de un agente que vive mucho tiempo: qué recordar, cuándo y por qué, cuando el contexto no da para todo.
- **2023** · [P32 · Voyager: un agente encarnado de final abierto con modelos de lenguaje grandes](../foundational/P32_voyager/README.md) — El agente acumula habilidades reutilizables en vez de contexto: memoria procedimental que no se borra al terminar la tarea.
- **2023** · [P33 · AutoGen: aplicaciones de nueva generación mediante conversación multiagente](../foundational/P33_autogen/README.md) — El multiagente deja de ser una metáfora y pasa a ser un patrón de programación: agentes con rol que conversan hasta converger.

### 🧠 memoria

P34–P37: cómo se codifica la posición, por qué el contexto largo es viable, por qué tenerlo no basta y cómo se gestiona como memoria jerárquica.

- **2021** · [P34 · RoFormer: Transformer mejorado con codificación posicional rotatoria](../foundational/P34_rope/README.md) — La posición se codifica rotando, y la atención pasa a depender solo de la distancia relativa. Es la base de casi todo modelo actual.
- **2022** · [P35 · FlashAttention: atención exacta, rápida y eficiente en memoria, consciente de la E/S](../foundational/P35_flashattention/README.md) — El cuello de botella de la atención no eran los FLOPs sino las lecturas y escrituras a memoria. Y la solución es EXACTA, no aproximada.
- **2023** · [P36 · Perdidos en el medio: cómo usan los modelos de lenguaje los contextos largos](../foundational/P36_lost_in_middle/README.md) — Tener contexto largo no es usarlo: el rendimiento cae en forma de U cuando el dato relevante está en el medio.
- **2023** · [P37 · MemGPT: modelos de lenguaje como sistemas operativos](../foundational/P37_memgpt/README.md) — Aplica al contexto la idea de memoria virtual: una jerarquía que da la ilusión de memoria grande sobre una pequeña y rápida.

### 🏗️ arquitectura

P38–P49: el andamiaje que hace entrenable todo lo demás — generativa clásica, regularización, optimización, robustez, normalización, profundidad, compresión, visión con Transformer, ciencia aplicada y adaptación eficiente.

- **2013** · [P38 · Bayes variacional con autocodificación](../foundational/P38_vae/README.md) — Hace entrenable un modelo generativo latente: el truco de reparametrización deja pasar el gradiente a través del muestreo.
- **2014** · [P39 · Redes generativas adversarias](../foundational/P39_gan/README.md) — Convierte la generación en un juego: dos redes compiten y ninguna necesita una verosimilitud explícita.
- **2014** · [P40 · Dropout: una forma simple de evitar el sobreajuste en redes neuronales](../foundational/P40_dropout/README.md) — Apagar unidades al azar durante el entrenamiento equivale a entrenar un ensamblado exponencial de subredes que comparten pesos.
- **2014** · [P41 · Adam: un método de optimización estocástica](../foundational/P41_adam/README.md) — Un paso de aprendizaje por dimensión, adaptado a la escala de su propio gradiente. Es el optimizador por defecto de casi todo lo que vino después.
- **2014** · [P42 · Explicar y aprovechar los ejemplos adversarios](../foundational/P42_adversarial/README.md) — Una perturbación imperceptible cambia la predicción. Y la causa no es la profundidad: es la linealidad en dimensión alta.
- **2015** · [P43 · Normalización por lotes: acelerar el entrenamiento profundo](../foundational/P43_batchnorm/README.md) — Normalizar las activaciones dentro de la red permite tasas de aprendizaje mucho mayores y hace el entrenamiento profundo mucho menos frágil.
- **2015** · [P44 · Aprendizaje residual profundo para reconocimiento de imágenes](../foundational/P44_resnet/README.md) — El atajo identidad hace apilables cientos de capas. Es la misma idea aditiva de la LSTM, aplicada a la profundidad.
- **2015** · [P45 · Destilar el conocimiento de una red neuronal](../foundational/P45_distillation/README.md) — Las probabilidades del maestro contienen más información que la etiqueta correcta: el modelo pequeño aprende de esa estructura.
- **2020** · [P46 · Una imagen vale 16x16 palabras: Transformers para reconocimiento de imágenes a escala](../foundational/P46_vit/README.md) — Trata la imagen como una secuencia de parches y aplica un Transformer puro: la convolución deja de ser imprescindible en visión.
- **2021** · [P47 · Predicción de estructura de proteínas de alta precisión con AlphaFold](../foundational/P47_alphafold/README.md) — Resuelve en la práctica un problema abierto de cincuenta años en biología, y demuestra que la IA puede producir conocimiento científico, no solo productos.
- **2021** · [P48 · LoRA: adaptación de rango bajo de modelos de lenguaje grandes](../foundational/P48_lora/README.md) — Ajustar un modelo enorme entrenando una fracción diminuta de parámetros, sin coste añadido en inferencia.
- **2023** · [P49 · QLoRA: ajuste fino eficiente de modelos cuantizados](../foundational/P49_qlora/README.md) — Pone el ajuste fino de un modelo muy grande al alcance de una sola GPU de consumo.

### 🛡️ evaluación

P50–P52: cómo se decide que un modelo es aceptable — principios explícitos, criterios de evaluación verificables e interpretabilidad de lo que hay dentro.

- **2022** · [P50 · IA constitucional: inocuidad a partir de retroalimentación de IA](../foundational/P50_constitutional_ai/README.md) — Sustituye parte del juicio humano por un conjunto de principios explícitos y auditables, y por la autocrítica del modelo.
- **2023** · [P51 · SWE-bench: ¿pueden los modelos resolver incidencias reales de GitHub?](../foundational/P51_swebench/README.md) — Cambia el criterio de evaluación: no si el código parece bien, sino si los tests del repositorio real pasan.
- **2023** · [P52 · Hacia la monosemanticidad: descomponer modelos de lenguaje con aprendizaje de diccionario](../foundational/P52_superposition/README.md) — Explica por qué una neurona no significa una cosa, y propone una forma de descomponer las activaciones en características interpretables.

## 📖 Qué resolvió cada uno

### P01 · The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain (1958)

- **Autoría:** Frank Rosenblatt
- **Problema anterior:** La IA de los años 50 programaba reglas a mano; no existía un procedimiento para que un sistema ajustara su comportamiento observando datos.
- **Propuesta:** Una unidad de decisión lineal con umbral y una regla de corrección de error que solo actúa cuando la predicción falla.
- **Hito:** Primera máquina que aprende sus propios pesos a partir de ejemplos en lugar de ejecutar reglas escritas por una persona.
- **Conceptos:** perceptrón, clasificador lineal, regla de aprendizaje, separabilidad, conexionismo
- **Clases del programa:** [039](../../classes/part-03-classical-machine-learning/039-clasificacion-logistica-y-umbrales/README.md), [049](../../classes/part-04-neural-networks-and-deep-learning/049-perceptron-y-limites-de-separabilidad/README.md)
- **Fuentes primarias:** [DOI (Psychological Review)](https://doi.org/10.1037/h0042519)

### P02 · Learning representations by back-propagating errors (1986)

- **Autoría:** David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams
- **Problema anterior:** Sin capas ocultas el perceptrón no resuelve XOR; con capas ocultas no se sabía cómo asignar el error a cada peso interno.
- **Propuesta:** Aplicar la regla de la cadena hacia atrás por el grafo de cómputo para obtener el gradiente de la pérdida respecto de cada peso.
- **Hito:** Un procedimiento práctico para entrenar capas ocultas: la red descubre representaciones intermedias que nadie diseñó.
- **Conceptos:** retropropagación, regla de la cadena, capas ocultas, gradiente, representaciones internas
- **Clases del programa:** [050](../../classes/part-04-neural-networks-and-deep-learning/050-mlp-y-backpropagation/README.md), [051](../../classes/part-04-neural-networks-and-deep-learning/051-activaciones-inicializacion-y-normalizacion/README.md)
- **Fuentes primarias:** [DOI (Nature)](https://doi.org/10.1038/323533a0)

### P03 · Long Short-Term Memory (1997)

- **Autoría:** Sepp Hochreiter, Jürgen Schmidhuber
- **Problema anterior:** En un RNN el gradiente se multiplica en cada paso temporal: se desvanece o explota, y la red no aprende dependencias largas.
- **Propuesta:** Una celda con estado aditivo (carrusel de error constante) y puertas multiplicativas que deciden qué entra y qué sale.
- **Hito:** Primera arquitectura recurrente capaz de mantener información a través de cientos de pasos sin que el gradiente se desvanezca.
- **Conceptos:** LSTM, gradiente desvaneciente, puertas, estado de celda, dependencias largas
- **Clases del programa:** [028](../../classes/part-02-probabilistic-evolutionary-and-decision-ai/028-modelos-ocultos-de-markov/README.md), [054](../../classes/part-04-neural-networks-and-deep-learning/054-rnn-lstm-y-secuencias/README.md)
- **Fuentes primarias:** [DOI (Neural Computation)](https://doi.org/10.1162/neco.1997.9.8.1735)

### P04 · ImageNet Classification with Deep Convolutional Neural Networks (2012)

- **Autoría:** Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton
- **Problema anterior:** La visión por computador dependía de descriptores diseñados manualmente; escalar el aprendizaje de features a millones de imágenes era inviable.
- **Propuesta:** Una CNN profunda entrenada en GPU con ReLU, dropout, aumento de datos y solapamiento de pooling sobre ILSVRC-2012.
- **Hito:** El resultado que convirtió el deep learning en la corriente principal: margen amplio sobre los métodos de visión hechos a mano.
- **Conceptos:** CNN, ImageNet, ReLU, dropout, GPU, aumento de datos
- **Clases del programa:** [053](../../classes/part-04-neural-networks-and-deep-learning/053-cnn-y-aprendizaje-espacial/README.md), [061](../../classes/part-05-language-vision-audio-and-multimodal-ai/061-clasificacion-y-representacion-visual/README.md), [062](../../classes/part-05-language-vision-audio-and-multimodal-ai/062-deteccion-segmentacion-y-pose/README.md)
- **Fuentes primarias:** [NeurIPS 2012 (proceedings)](https://papers.nips.cc/paper_files/paper/2012) · [DOI (versión Communications of the ACM, 2017)](https://doi.org/10.1145/3065386)

### P05 · Efficient Estimation of Word Representations in Vector Space (2013)

- **Autoría:** Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean
- **Problema anterior:** Representar palabras como identificadores dispersos (one-hot) impide medir similitud; los modelos neuronales de lenguaje previos eran demasiado costosos.
- **Propuesta:** Dos arquitecturas log-lineales sin capa oculta —CBOW y skip-gram— que predicen contexto y producen vectores con estructura lineal.
- **Hito:** El significado distribucional se vuelve barato: vectores densos entrenables sobre miles de millones de palabras.
- **Conceptos:** embeddings, skip-gram, CBOW, muestreo negativo, hipótesis distribucional, analogías
- **Clases del programa:** [064](../../classes/part-05-language-vision-audio-and-multimodal-ai/064-tokenizacion-y-representacion-del-lenguaje/README.md), [066](../../classes/part-05-language-vision-audio-and-multimodal-ai/066-embeddings-semanticos-y-similitud/README.md), [100](../../classes/part-08-retrieval-context-memory-and-knowledge/100-embeddings-y-busqueda-vectorial/README.md), [166](../../classes/part-13-evaluation-safety-security-and-governance/166-sesgo-fairness-y-grupos-afectados/README.md)
- **Fuentes primarias:** [arXiv:1301.3781](https://arxiv.org/abs/1301.3781) · [arXiv:1310.4546 (muestreo negativo y frases)](https://arxiv.org/abs/1310.4546)

### P38 · Auto-Encoding Variational Bayes (2013)

- **Autoría:** Diederik P. Kingma, Max Welling
- **Problema anterior:** Un modelo generativo con variables latentes exige muestrear, y muestrear es un nodo estocástico que bloquea el gradiente: no se podía entrenar por retropropagación.
- **Propuesta:** Escribir la muestra como z = μ + σ·ε con ε de una normal fija: el azar queda fuera del camino del gradiente, y se optimiza una cota inferior de la verosimilitud (ELBO).
- **Hito:** Hace entrenable un modelo generativo latente: el truco de reparametrización deja pasar el gradiente a través del muestreo.
- **Conceptos:** VAE, reparametrización, ELBO, espacio latente, inferencia variacional
- **Clases del programa:** [058](../../classes/part-04-neural-networks-and-deep-learning/058-autoencoders-gan-y-difusion/README.md), [088](../../classes/part-07-generative-ai-across-media/088-espacios-latentes-y-autoencoders-variacionales/README.md)
- **Fuentes primarias:** [arXiv:1312.6114](https://arxiv.org/abs/1312.6114)

### P06 · Sequence to Sequence Learning with Neural Networks (2014)

- **Autoría:** Ilya Sutskever, Oriol Vinyals, Quoc V. Le
- **Problema anterior:** Las redes profundas requerían entradas y salidas de dimensión fija; la traducción automática dependía de sistemas estadísticos con muchas piezas separadas.
- **Propuesta:** Un LSTM codifica la entrada en un vector de tamaño fijo y otro LSTM lo decodifica token a token; invertir la secuencia fuente mejora el resultado.
- **Hito:** Una única red aprende a mapear secuencias de longitud variable a secuencias de longitud variable, de extremo a extremo.
- **Conceptos:** encoder-decoder, vector de contexto, traducción automática neuronal, cuello de botella, BLEU
- **Clases del programa:** [054](../../classes/part-04-neural-networks-and-deep-learning/054-rnn-lstm-y-secuencias/README.md), [055](../../classes/part-04-neural-networks-and-deep-learning/055-atencion-y-arquitectura-transformer/README.md), [067](../../classes/part-05-language-vision-audio-and-multimodal-ai/067-reconocimiento-automatico-del-habla/README.md)
- **Fuentes primarias:** [arXiv:1409.3215](https://arxiv.org/abs/1409.3215)

### P07 · Neural Machine Translation by Jointly Learning to Align and Translate (2014)

- **Autoría:** Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio
- **Problema anterior:** Comprimir una frase entera en un vector fijo degrada la traducción de frases largas: es un cuello de botella de información.
- **Propuesta:** Un vector de contexto distinto por paso de salida, calculado como suma ponderada de los estados del codificador con pesos aprendidos (atención aditiva).
- **Hito:** Nace la atención: el decodificador deja de depender de un único vector y consulta toda la entrada en cada paso.
- **Conceptos:** atención, alineación, vector de contexto dinámico, softmax, atención aditiva
- **Clases del programa:** [054](../../classes/part-04-neural-networks-and-deep-learning/054-rnn-lstm-y-secuencias/README.md), [055](../../classes/part-04-neural-networks-and-deep-learning/055-atencion-y-arquitectura-transformer/README.md)
- **Fuentes primarias:** [arXiv:1409.0473](https://arxiv.org/abs/1409.0473)

### P23 · GloVe: Global Vectors for Word Representation (2014)

- **Autoría:** Jeffrey Pennington, Richard Socher, Christopher D. Manning
- **Problema anterior:** Word2Vec aprendía de ventanas locales y desaprovechaba las estadísticas globales del corpus; los métodos de factorización usaban esas estadísticas pero producían peores analogías.
- **Propuesta:** Ajustar por mínimos cuadrados ponderados el producto de vectores al logaritmo de la co-ocurrencia, con el argumento de que lo informativo es la RAZÓN de co-ocurrencias, no su valor bruto.
- **Hito:** Unifica las dos familias de embeddings: factorizar estadísticas globales de co-ocurrencia con la ventaja de los métodos predictivos.
- **Conceptos:** GloVe, co-ocurrencia, factorización, mínimos cuadrados ponderados, razón de probabilidades
- **Clases del programa:** [064](../../classes/part-05-language-vision-audio-and-multimodal-ai/064-tokenizacion-y-representacion-del-lenguaje/README.md), [066](../../classes/part-05-language-vision-audio-and-multimodal-ai/066-embeddings-semanticos-y-similitud/README.md)
- **Fuentes primarias:** [ACL Anthology (EMNLP 2014)](https://aclanthology.org/D14-1162/) · [DOI](https://doi.org/10.3115/v1/D14-1162)

### P39 · Generative Adversarial Networks (2014)

- **Autoría:** Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, y otros
- **Problema anterior:** Los modelos generativos exigían definir y optimizar una verosimilitud, lo que obligaba a aproximaciones costosas o producía muestras borrosas.
- **Propuesta:** Entrenar un generador contra un discriminador en un juego minimax: el generador gana cuando el discriminador ya no distingue lo real de lo sintético.
- **Hito:** Convierte la generación en un juego: dos redes compiten y ninguna necesita una verosimilitud explícita.
- **Conceptos:** GAN, minimax, discriminador, colapso de modos, entrenamiento adversario
- **Clases del programa:** [058](../../classes/part-04-neural-networks-and-deep-learning/058-autoencoders-gan-y-difusion/README.md), [089](../../classes/part-07-generative-ai-across-media/089-gan-y-entrenamiento-adversarial/README.md)
- **Fuentes primarias:** [arXiv:1406.2661](https://arxiv.org/abs/1406.2661)

### P40 · Dropout: A Simple Way to Prevent Neural Networks from Overfitting (2014)

- **Autoría:** Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky, Ilya Sutskever, Ruslan Salakhutdinov
- **Problema anterior:** Las redes grandes memorizaban el conjunto de entrenamiento, y las unidades desarrollaban co-adaptaciones frágiles: una función solo servía si su 'socia' estaba presente.
- **Propuesta:** En cada paso, poner a cero cada unidad con probabilidad p. Ninguna función puede depender de una unidad concreta, así que la red aprende representaciones redundantes.
- **Hito:** Apagar unidades al azar durante el entrenamiento equivale a entrenar un ensamblado exponencial de subredes que comparten pesos.
- **Conceptos:** dropout, regularización, co-adaptación, ensamblado, sobreajuste
- **Clases del programa:** [051](../../classes/part-04-neural-networks-and-deep-learning/051-activaciones-inicializacion-y-normalizacion/README.md), [052](../../classes/part-04-neural-networks-and-deep-learning/052-optimizadores-regularizacion-y-schedulers/README.md)
- **Fuentes primarias:** [JMLR 15(56)](https://jmlr.org/papers/v15/srivastava14a.html)

### P41 · Adam: A Method for Stochastic Optimization (2014)

- **Autoría:** Diederik P. Kingma, Jimmy Ba
- **Problema anterior:** SGD usa la misma tasa de aprendizaje en todas las direcciones. En un problema mal condicionado, o oscila en las direcciones de mucha curvatura o se arrastra en las de poca.
- **Propuesta:** Mantener medias móviles del gradiente (primer momento) y de su cuadrado (segundo momento), con corrección de sesgo, y normalizar el paso de cada coordenada por su magnitud típica.
- **Hito:** Un paso de aprendizaje por dimensión, adaptado a la escala de su propio gradiente. Es el optimizador por defecto de casi todo lo que vino después.
- **Conceptos:** Adam, optimización adaptativa, momentos, corrección de sesgo, tasa de aprendizaje
- **Clases del programa:** [050](../../classes/part-04-neural-networks-and-deep-learning/050-mlp-y-backpropagation/README.md), [052](../../classes/part-04-neural-networks-and-deep-learning/052-optimizadores-regularizacion-y-schedulers/README.md)
- **Fuentes primarias:** [arXiv:1412.6980](https://arxiv.org/abs/1412.6980)

### P42 · Explaining and Harnessing Adversarial Examples (2014)

- **Autoría:** Ian J. Goodfellow, Jonathon Shlens, Christian Szegedy
- **Problema anterior:** Szegedy et al. (2013) habían descubierto que perturbaciones minúsculas engañaban a las redes, y se atribuía a la extrema no linealidad de los modelos profundos.
- **Propuesta:** Mostrar que la explicación es la contraria —el comportamiento demasiado LINEAL en alta dimensión— y derivar de ahí un ataque de un solo paso (FGSM) y una defensa por entrenamiento adversario.
- **Hito:** Una perturbación imperceptible cambia la predicción. Y la causa no es la profundidad: es la linealidad en dimensión alta.
- **Conceptos:** ejemplos adversarios, FGSM, robustez, linealidad, entrenamiento adversario
- **Clases del programa:** [053](../../classes/part-04-neural-networks-and-deep-learning/053-cnn-y-aprendizaje-espacial/README.md), [162](../../classes/part-13-evaluation-safety-security-and-governance/162-red-teaming-y-abuso/README.md), [163](../../classes/part-13-evaluation-safety-security-and-governance/163-prompt-injection-e-instrucciones-no-confiables/README.md)
- **Fuentes primarias:** [arXiv:1412.6572](https://arxiv.org/abs/1412.6572)

### P26 · Human-level control through deep reinforcement learning (2015)

- **Autoría:** Volodymyr Mnih, Koray Kavukcuoglu, David Silver, y otros (DeepMind)
- **Problema anterior:** Combinar aprendizaje por refuerzo con aproximación de función no lineal era notoriamente inestable: las muestras consecutivas están correlacionadas y el objetivo se mueve mientras se aprende.
- **Propuesta:** Q-learning con una red convolucional, estabilizado con repetición de experiencia (rompe la correlación) y una red objetivo congelada (fija el blanco).
- **Hito:** El primer agente que aprende a actuar directamente desde píxeles, con la misma arquitectura y los mismos hiperparámetros en decenas de juegos.
- **Conceptos:** DQN, Q-learning, repetición de experiencia, red objetivo, Atari, refuerzo profundo
- **Clases del programa:** [029](../../classes/part-02-probabilistic-evolutionary-and-decision-ai/029-procesos-de-decision-de-markov/README.md), [030](../../classes/part-02-probabilistic-evolutionary-and-decision-ai/030-teoria-de-decision-y-utilidad-esperada/README.md), [057](../../classes/part-04-neural-networks-and-deep-learning/057-aprendizaje-por-refuerzo-profundo/README.md)
- **Fuentes primarias:** [DOI (Nature 518, 529–533)](https://doi.org/10.1038/nature14236)

### P43 · Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift (2015)

- **Autoría:** Sergey Ioffe, Christian Szegedy
- **Problema anterior:** Entrenar redes profundas exigía inicializaciones cuidadosas y tasas de aprendizaje pequeñas: la distribución de las activaciones de cada capa se desplazaba durante el entrenamiento.
- **Propuesta:** Normalizar cada activación usando la media y la varianza del minilote, y añadir dos parámetros aprendidos (γ, β) para que la red pueda deshacer la normalización si le conviene.
- **Hito:** Normalizar las activaciones dentro de la red permite tasas de aprendizaje mucho mayores y hace el entrenamiento profundo mucho menos frágil.
- **Conceptos:** normalización por lotes, activaciones, tasa de aprendizaje, γ y β, estabilidad
- **Clases del programa:** [051](../../classes/part-04-neural-networks-and-deep-learning/051-activaciones-inicializacion-y-normalizacion/README.md), [052](../../classes/part-04-neural-networks-and-deep-learning/052-optimizadores-regularizacion-y-schedulers/README.md)
- **Fuentes primarias:** [arXiv:1502.03167](https://arxiv.org/abs/1502.03167)

### P44 · Deep Residual Learning for Image Recognition (2015)

- **Autoría:** Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun
- **Problema anterior:** Al pasar de 20 a 56 capas, el error de ENTRENAMIENTO subía. No era sobreajuste: era que las redes muy profundas se habían vuelto imposibles de optimizar.
- **Propuesta:** Que cada bloque aprenda un residuo F(x) y la salida sea F(x) + x. Si la capa no aporta, aprender F ≈ 0 es fácil, y el gradiente siempre tiene una ruta directa.
- **Hito:** El atajo identidad hace apilables cientos de capas. Es la misma idea aditiva de la LSTM, aplicada a la profundidad.
- **Conceptos:** ResNet, conexión residual, atajo identidad, degradación, profundidad
- **Clases del programa:** [051](../../classes/part-04-neural-networks-and-deep-learning/051-activaciones-inicializacion-y-normalizacion/README.md), [053](../../classes/part-04-neural-networks-and-deep-learning/053-cnn-y-aprendizaje-espacial/README.md), [061](../../classes/part-05-language-vision-audio-and-multimodal-ai/061-clasificacion-y-representacion-visual/README.md), [062](../../classes/part-05-language-vision-audio-and-multimodal-ai/062-deteccion-segmentacion-y-pose/README.md)
- **Fuentes primarias:** [arXiv:1512.03385](https://arxiv.org/abs/1512.03385)

### P45 · Distilling the Knowledge in a Neural Network (2015)

- **Autoría:** Geoffrey Hinton, Oriol Vinyals, Jeff Dean
- **Problema anterior:** Los modelos grandes o los conjuntos de modelos daban los mejores resultados pero eran caros de servir, y entrenar el modelo pequeño con las etiquetas duras daba mucho peor resultado.
- **Propuesta:** Entrenar el modelo pequeño para reproducir la distribución completa del maestro, suavizada con una temperatura que revela la estructura de similitud entre clases.
- **Hito:** Las probabilidades del maestro contienen más información que la etiqueta correcta: el modelo pequeño aprende de esa estructura.
- **Conceptos:** destilación, objetivos suaves, temperatura, conocimiento oscuro, compresión de modelos
- **Clases del programa:** [059](../../classes/part-04-neural-networks-and-deep-learning/059-transferencia-fine-tuning-y-destilacion/README.md), [086](../../classes/part-06-foundation-models-and-llm-engineering/086-seleccion-de-modelo-costo-latencia-y-privacidad/README.md), [157](../../classes/part-12-ai-engineering-mlops-llmops-and-agentops/157-costo-latencia-caching-y-capacidad/README.md)
- **Fuentes primarias:** [arXiv:1503.02531](https://arxiv.org/abs/1503.02531)

### P27 · Mastering the game of Go with deep neural networks and tree search (2016)

- **Autoría:** David Silver, Aja Huang, Chris J. Maddison, y otros (DeepMind)
- **Problema anterior:** El go tiene un espacio de estados y un factor de ramificación que hacen inviable la búsqueda exhaustiva, y no existía una función de evaluación de posiciones suficientemente buena.
- **Propuesta:** Una red de políticas que propone jugadas plausibles y una red de valor que evalúa posiciones, usadas para guiar y truncar una búsqueda de Monte Carlo en árbol.
- **Hito:** Une las dos tradiciones de la IA: la búsqueda simbólica de la parte 01 y el aprendizaje profundo de la parte 04, en un solo sistema.
- **Conceptos:** AlphaGo, MCTS, red de políticas, red de valor, autojuego, búsqueda guiada
- **Clases del programa:** [017](../../classes/part-01-symbolic-ai-search-logic-and-planning/017-juegos-minimax-y-poda-alfa-beta/README.md), [031](../../classes/part-02-probabilistic-evolutionary-and-decision-ai/031-metodos-monte-carlo-y-simulacion/README.md), [057](../../classes/part-04-neural-networks-and-deep-learning/057-aprendizaje-por-refuerzo-profundo/README.md), [172](../../classes/part-14-frontier-research-and-capstones/172-ia-neuro-simbolica/README.md)
- **Fuentes primarias:** [DOI (Nature 529, 484–489)](https://doi.org/10.1038/nature16961)

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
- **Clases del programa:** [065](../../classes/part-05-language-vision-audio-and-multimodal-ai/065-clasificacion-extraccion-y-generacion-de-texto/README.md), [074](../../classes/part-06-foundation-models-and-llm-engineering/074-objetivos-de-preentrenamiento/README.md)
- **Fuentes primarias:** [arXiv:1810.04805](https://arxiv.org/abs/1810.04805) · [ACL Anthology (NAACL 2019)](https://aclanthology.org/N19-1423/)

### P24 · Deep Contextualized Word Representations (2018)

- **Autoría:** Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, Luke Zettlemoyer
- **Problema anterior:** Un embedding estático da el mismo vector a «banco del parque» y «banco central»: el sentido se pierde antes de que el modelo empiece a trabajar.
- **Propuesta:** Usar los estados internos de un modelo de lenguaje bidireccional profundo y combinar sus capas con pesos aprendidos por tarea.
- **Hito:** Un vector por APARICIÓN y no por palabra: la polisemia deja de colapsar en un único punto del espacio.
- **Conceptos:** ELMo, embeddings contextuales, polisemia, modelo de lenguaje bidireccional, combinación de capas
- **Clases del programa:** [065](../../classes/part-05-language-vision-audio-and-multimodal-ai/065-clasificacion-extraccion-y-generacion-de-texto/README.md), [066](../../classes/part-05-language-vision-audio-and-multimodal-ai/066-embeddings-semanticos-y-similitud/README.md)
- **Fuentes primarias:** [ACL Anthology (NAACL 2018)](https://aclanthology.org/N18-1202/)

### P25 · Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (2019)

- **Autoría:** Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu
- **Problema anterior:** Cada tarea exigía su propia cabeza —clasificación, regresión, extracción, generación— lo que impedía comparar objetivos, arquitecturas y datos en igualdad de condiciones.
- **Propuesta:** Un marco unificado texto a texto, un estudio sistemático de todas las decisiones de diseño del preentrenamiento, y el corpus C4 (Colossal Clean Crawled Corpus).
- **Hito:** Todo problema de texto se reescribe como texto → texto: un solo modelo, una sola pérdida, cero cabezas específicas.
- **Conceptos:** T5, texto a texto, transferencia, C4, encoder-decoder, estudio sistemático
- **Clases del programa:** [065](../../classes/part-05-language-vision-audio-and-multimodal-ai/065-clasificacion-extraccion-y-generacion-de-texto/README.md), [074](../../classes/part-06-foundation-models-and-llm-engineering/074-objetivos-de-preentrenamiento/README.md)
- **Fuentes primarias:** [arXiv:1910.10683](https://arxiv.org/abs/1910.10683) · [JMLR 21(140)](https://jmlr.org/papers/v21/20-074.html)

### P10 · Language Models are Few-Shot Learners (2020)

- **Autoría:** Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, y otros (OpenAI)
- **Problema anterior:** El patrón de BERT exigía un conjunto etiquetado y un ajuste fino por cada tarea nueva; eso no escala a la variedad de tareas reales.
- **Propuesta:** Escalar un Transformer autorregresivo hasta 175 000 millones de parámetros y evaluar en modo zero-shot, one-shot y few-shot mediante condicionamiento en el prompt.
- **Hito:** El aprendizaje en contexto: la tarea se especifica en el prompt y el modelo se adapta sin actualizar ningún peso.
- **Conceptos:** GPT-3, aprendizaje en contexto, few-shot, escalado, modelo autorregresivo, prompt
- **Clases del programa:** [074](../../classes/part-06-foundation-models-and-llm-engineering/074-objetivos-de-preentrenamiento/README.md), [076](../../classes/part-06-foundation-models-and-llm-engineering/076-instruction-tuning-y-datos-de-instrucciones/README.md), [086](../../classes/part-06-foundation-models-and-llm-engineering/086-seleccion-de-modelo-costo-latencia-y-privacidad/README.md)
- **Fuentes primarias:** [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)

### P11 · Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (2020)

- **Autoría:** Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, y otros
- **Problema anterior:** Todo lo que un modelo sabe está congelado en sus pesos: no se puede actualizar sin reentrenar, ni auditar de dónde salió una afirmación.
- **Propuesta:** Combinar un recuperador denso (DPR) sobre un índice de Wikipedia con un generador seq2seq (BART), entrenados de forma conjunta.
- **Hito:** Separa el conocimiento (índice consultable y actualizable) del razonamiento (parámetros del modelo).
- **Conceptos:** RAG, recuperación densa, memoria no paramétrica, citas, atribución, conocimiento actualizable
- **Clases del programa:** [102](../../classes/part-08-retrieval-context-memory-and-knowledge/102-busqueda-lexica-y-bm25/README.md), [103](../../classes/part-08-retrieval-context-memory-and-knowledge/103-busqueda-hibrida-y-fusion-de-rankings/README.md), [104](../../classes/part-08-retrieval-context-memory-and-knowledge/104-re-ranking-y-filtros-de-evidencia/README.md), [105](../../classes/part-08-retrieval-context-memory-and-knowledge/105-rag-basico-con-citas/README.md), [106](../../classes/part-08-retrieval-context-memory-and-knowledge/106-transformacion-y-descomposicion-de-consultas/README.md), [110](../../classes/part-08-retrieval-context-memory-and-knowledge/110-evaluacion-de-fidelidad-cobertura-y-atribucion/README.md), [111](../../classes/part-08-retrieval-context-memory-and-knowledge/111-proyecto-rag-productivo-y-auditable/README.md), [168](../../classes/part-13-evaluation-safety-security-and-governance/168-alucinacion-grounding-y-abstencion/README.md)
- **Fuentes primarias:** [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)

### P17 · Denoising Diffusion Probabilistic Models (2020)

- **Autoría:** Jonathan Ho, Ajay Jain, Pieter Abbeel
- **Problema anterior:** Las GAN generaban imágenes de calidad pero eran inestables de entrenar y colapsaban la diversidad; los VAE eran estables y producían muestras borrosas.
- **Propuesta:** Un proceso directo que añade ruido gaussiano en T pasos con forma cerrada, y una red que aprende a predecir ese ruido para invertirlo.
- **Hito:** La generación deja de ser un salto en la oscuridad: se aprende a deshacer, paso a paso, un proceso de ruido conocido.
- **Conceptos:** difusión, DDPM, proceso directo, predicción de ruido, cota variacional, score matching
- **Clases del programa:** [090](../../classes/part-07-generative-ai-across-media/090-modelos-de-difusion/README.md), [091](../../classes/part-07-generative-ai-across-media/091-texto-a-imagen-y-condicionamiento/README.md), [092](../../classes/part-07-generative-ai-across-media/092-control-estructural-y-edicion-generativa/README.md), [095](../../classes/part-07-generative-ai-across-media/095-generacion-y-edicion-de-video/README.md)
- **Fuentes primarias:** [arXiv:2006.11239](https://arxiv.org/abs/2006.11239)

### P46 · An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (2020)

- **Autoría:** Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, y otros
- **Problema anterior:** La convolución traía de fábrica localidad y equivarianza a la traslación, y se asumía que sin esos sesgos inductivos la visión no funcionaría.
- **Propuesta:** Partir la imagen en parches, proyectarlos como si fueran tokens, añadir codificación posicional y aplicar el encoder del Transformer sin más.
- **Hito:** Trata la imagen como una secuencia de parches y aplica un Transformer puro: la convolución deja de ser imprescindible en visión.
- **Conceptos:** ViT, parches, sesgo inductivo, preentrenamiento a escala, visión
- **Clases del programa:** [053](../../classes/part-04-neural-networks-and-deep-learning/053-cnn-y-aprendizaje-espacial/README.md), [061](../../classes/part-05-language-vision-audio-and-multimodal-ai/061-clasificacion-y-representacion-visual/README.md), [069](../../classes/part-05-language-vision-audio-and-multimodal-ai/069-modelos-vision-lenguaje/README.md)
- **Fuentes primarias:** [arXiv:2010.11929](https://arxiv.org/abs/2010.11929)

### P18 · Learning Transferable Visual Models From Natural Language Supervision (2021)

- **Autoría:** Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, y otros (OpenAI)
- **Problema anterior:** La visión dependía de conjuntos etiquetados con categorías fijas; cambiar de tarea exigía volver a anotar y volver a entrenar.
- **Propuesta:** Entrenar de forma contrastiva sobre 400 millones de pares (imagen, texto) de internet, alineando ambos espacios, y clasificar comparando la imagen con el texto de cada clase.
- **Hito:** El texto se convierte en la etiqueta: un solo modelo clasifica categorías que nadie anotó, describiéndolas con palabras.
- **Conceptos:** CLIP, contrastivo, InfoNCE, zero-shot, multimodal, supervisión débil
- **Clases del programa:** [062](../../classes/part-05-language-vision-audio-and-multimodal-ai/062-deteccion-segmentacion-y-pose/README.md), [069](../../classes/part-05-language-vision-audio-and-multimodal-ai/069-modelos-vision-lenguaje/README.md), [070](../../classes/part-05-language-vision-audio-and-multimodal-ai/070-fusion-multimodal-y-representacion-conjunta/README.md)
- **Fuentes primarias:** [arXiv:2103.00020](https://arxiv.org/abs/2103.00020)

### P34 · RoFormer: Enhanced Transformer with Rotary Position Embedding (2021)

- **Autoría:** Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, Yunfeng Liu
- **Problema anterior:** La codificación sinusoidal del Transformer se SUMA al embedding y codifica posición absoluta; la atención no ve directamente la distancia entre dos tokens, que es lo que importa en lenguaje.
- **Propuesta:** Rotar los vectores de consulta y clave en función de su posición, de modo que el producto escalar entre dos posiciones dependa únicamente de su diferencia.
- **Hito:** La posición se codifica rotando, y la atención pasa a depender solo de la distancia relativa. Es la base de casi todo modelo actual.
- **Conceptos:** RoPE, posición relativa, rotación, contexto largo, decaimiento con la distancia
- **Clases del programa:** [055](../../classes/part-04-neural-networks-and-deep-learning/055-atencion-y-arquitectura-transformer/README.md), [079](../../classes/part-06-foundation-models-and-llm-engineering/079-prompting-contexto-y-resultados-estructurados/README.md)
- **Fuentes primarias:** [arXiv:2104.09864](https://arxiv.org/abs/2104.09864)

### P47 · Highly accurate protein structure prediction with AlphaFold (2021)

- **Autoría:** John Jumper, Richard Evans, Alexander Pritzel, y otros (DeepMind)
- **Problema anterior:** Predecir la estructura tridimensional de una proteína a partir de su secuencia de aminoácidos llevaba décadas sin resolverse, y determinarla experimentalmente cuesta meses o años por proteína.
- **Propuesta:** Una arquitectura que razona conjuntamente sobre alineamientos múltiples de secuencias y sobre representaciones de pares de residuos, con un módulo que produce coordenadas 3D directamente.
- **Hito:** Resuelve en la práctica un problema abierto de cincuenta años en biología, y demuestra que la IA puede producir conocimiento científico, no solo productos.
- **Conceptos:** AlphaFold, plegamiento de proteínas, estructura, atención sobre pares, IA para ciencia
- **Clases del programa:** [173](../../classes/part-14-frontier-research-and-capstones/173-causal-ai-y-descubrimiento-cientifico/README.md), [181](../../classes/part-14-frontier-research-and-capstones/181-ia-para-ciencia-clima-y-salud-responsable/README.md)
- **Fuentes primarias:** [DOI (Nature 596, 583–589)](https://doi.org/10.1038/s41586-021-03819-2)

### P48 · LoRA: Low-Rank Adaptation of Large Language Models (2021)

- **Autoría:** Edward J. Hu, Yelong Shen, Phillip Wallis, y otros
- **Problema anterior:** El ajuste fino completo exige una copia entera del modelo por tarea: inviable en almacenamiento y en memoria de entrenamiento cuando el modelo tiene miles de millones de parámetros.
- **Propuesta:** Congelar los pesos originales y aprender una actualización factorizada de rango bajo, W' = W + BA, que al desplegar se puede fusionar con W.
- **Hito:** Ajustar un modelo enorme entrenando una fracción diminuta de parámetros, sin coste añadido en inferencia.
- **Conceptos:** LoRA, rango bajo, adaptación eficiente, PEFT, adaptadores
- **Clases del programa:** [059](../../classes/part-04-neural-networks-and-deep-learning/059-transferencia-fine-tuning-y-destilacion/README.md), [077](../../classes/part-06-foundation-models-and-llm-engineering/077-lora-qlora-y-adaptacion-eficiente/README.md)
- **Fuentes primarias:** [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)

### P12 · Training language models to follow instructions with human feedback (2022)

- **Autoría:** Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, y otros (OpenAI)
- **Problema anterior:** Maximizar la verosimilitud del texto de internet no es lo mismo que ser útil, honesto e inocuo; el objetivo de entrenamiento está desalineado con la intención del usuario.
- **Propuesta:** Tres etapas: ajuste supervisado con demostraciones, modelo de recompensa entrenado con comparaciones humanas y optimización por PPO con penalización KL.
- **Hito:** El salto de «modelo que completa texto» a «asistente que sigue instrucciones»: alineación con preferencias humanas.
- **Conceptos:** RLHF, alineación, modelo de recompensa, PPO, preferencias, instrucciones
- **Clases del programa:** [076](../../classes/part-06-foundation-models-and-llm-engineering/076-instruction-tuning-y-datos-de-instrucciones/README.md), [078](../../classes/part-06-foundation-models-and-llm-engineering/078-rlhf-rlaif-y-dpo/README.md)
- **Fuentes primarias:** [arXiv:2203.02155](https://arxiv.org/abs/2203.02155)

### P13 · ReAct: Synergizing Reasoning and Acting in Language Models (2022)

- **Autoría:** Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
- **Problema anterior:** El razonamiento en cadena (CoT) no consulta el mundo y alucina hechos; actuar sin razonar no descompone problemas de varios pasos.
- **Propuesta:** Intercalar trazas de pensamiento y acciones sobre un entorno, de modo que cada observación real condicione el siguiente razonamiento.
- **Hito:** El modelo deja de ser solo un generador de texto y pasa a ser el controlador de un bucle que observa y actúa.
- **Conceptos:** ReAct, agente, bucle pensamiento-acción-observación, herramientas, traza auditable
- **Clases del programa:** [112](../../classes/part-09-ai-agent-engineering/112-de-modelo-y-automatizacion-a-agente/README.md), [114](../../classes/part-09-ai-agent-engineering/114-ciclo-react-y-observacion-del-entorno/README.md), [115](../../classes/part-09-ai-agent-engineering/115-planificacion-y-descomposicion-de-tareas/README.md), [116](../../classes/part-09-ai-agent-engineering/116-herramientas-tipadas-y-efectos-laterales/README.md)
- **Fuentes primarias:** [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)

### P19 · Training Compute-Optimal Large Language Models (2022)

- **Autoría:** Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, y otros (DeepMind)
- **Problema anterior:** Tras GPT-3 la industria escalaba parámetros asumiendo que era la variable dominante, sin medir el reparto óptimo entre parámetros y tokens a cómputo constante.
- **Propuesta:** Ajustar empíricamente L(N, D) y resolver el reparto que minimiza la pérdida bajo la restricción C = 6ND.
- **Hito:** Corrige la carrera por el tamaño: a cómputo fijo, los modelos de la época estaban infraentrenados en datos.
- **Conceptos:** leyes de escalado, cómputo óptimo, tokens por parámetro, FLOPs, infraentrenamiento
- **Clases del programa:** [074](../../classes/part-06-foundation-models-and-llm-engineering/074-objetivos-de-preentrenamiento/README.md), [075](../../classes/part-06-foundation-models-and-llm-engineering/075-escalamiento-computo-y-leyes-empiricas/README.md), [082](../../classes/part-06-foundation-models-and-llm-engineering/082-dimensionar-hardware-de-la-laptop-al-cluster/README.md), [086](../../classes/part-06-foundation-models-and-llm-engineering/086-seleccion-de-modelo-costo-latencia-y-privacidad/README.md)
- **Fuentes primarias:** [arXiv:2203.15556](https://arxiv.org/abs/2203.15556)

### P28 · Chain-of-Thought Prompting Elicits Reasoning in Large Language Models (2022)

- **Autoría:** Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, Denny Zhou
- **Problema anterior:** Los modelos grandes fallaban en aritmética y razonamiento de varios pasos aunque acertaran tareas aparentemente más difíciles: se les pedía el resultado sin dejarles espacio para llegar a él.
- **Propuesta:** Incluir en el prompt unos pocos ejemplos que muestren el razonamiento paso a paso, sin ajuste fino ni datos adicionales.
- **Hito:** Descomponer en pasos intermedios desbloquea tareas que el mismo modelo fallaba respondiendo de una vez.
- **Conceptos:** cadena de pensamiento, razonamiento, prompting, emergencia, pasos intermedios
- **Clases del programa:** [114](../../classes/part-09-ai-agent-engineering/114-ciclo-react-y-observacion-del-entorno/README.md), [115](../../classes/part-09-ai-agent-engineering/115-planificacion-y-descomposicion-de-tareas/README.md), [175](../../classes/part-14-frontier-research-and-capstones/175-razonamiento-y-computo-en-tiempo-de-inferencia/README.md)
- **Fuentes primarias:** [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)

### P35 · FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness (2022)

- **Autoría:** Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, Christopher Ré
- **Problema anterior:** Durante años se atacó el coste O(n²) de la atención con aproximaciones (dispersa, lineal), que perdían calidad y a menudo ni siquiera eran más rápidas en la práctica.
- **Propuesta:** Reorganizar el cálculo por bloques que caben en la memoria rápida del chip, evitando materializar la matriz de atención completa en la memoria lenta.
- **Hito:** El cuello de botella de la atención no eran los FLOPs sino las lecturas y escrituras a memoria. Y la solución es EXACTA, no aproximada.
- **Conceptos:** FlashAttention, consciencia de E/S, tiling, atención exacta, jerarquía de memoria, contexto largo
- **Clases del programa:** [081](../../classes/part-06-foundation-models-and-llm-engineering/081-aceleradores-memoria-y-el-limite-real-del-computo/README.md), [085](../../classes/part-06-foundation-models-and-llm-engineering/085-cuantizacion-e-inferencia-local/README.md)
- **Fuentes primarias:** [arXiv:2205.14135](https://arxiv.org/abs/2205.14135)

### P50 · Constitutional AI: Harmlessness from AI Feedback (2022)

- **Autoría:** Yuntao Bai, Saurav Kadavath, Sandipan Kundu, y otros (Anthropic)
- **Problema anterior:** RLHF depende de miles de comparaciones humanas: es caro, expone a los anotadores a contenido dañino, y los criterios quedan implícitos en los datos, sin poder inspeccionarse ni discutirse.
- **Propuesta:** Escribir los principios de forma explícita, hacer que el modelo critique y revise sus propias respuestas contra ellos, y usar preferencias generadas por IA para la fase de refuerzo.
- **Hito:** Sustituye parte del juicio humano por un conjunto de principios explícitos y auditables, y por la autocrítica del modelo.
- **Conceptos:** IA constitucional, RLAIF, autocrítica, principios explícitos, inocuidad
- **Clases del programa:** [078](../../classes/part-06-foundation-models-and-llm-engineering/078-rlhf-rlaif-y-dpo/README.md), [161](../../classes/part-13-evaluation-safety-security-and-governance/161-golden-datasets-regresion-y-llm-as-judge/README.md)
- **Fuentes primarias:** [arXiv:2212.08073](https://arxiv.org/abs/2212.08073)

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

### P20 · Mamba: Linear-Time Sequence Modeling with Selective State Spaces (2023)

- **Autoría:** Albert Gu, Tri Dao
- **Problema anterior:** La atención cuesta O(n²) y su memoria crece con la secuencia; las alternativas subcuadráticas previas no alcanzaban a la atención en lenguaje.
- **Propuesta:** Hacer que los parámetros del espacio de estados dependan de la ENTRADA (selección), y compensar la pérdida de la convolución eficiente con un algoritmo paralelo consciente del hardware.
- **Hito:** El primer competidor serio del Transformer en lenguaje: tiempo lineal y estado de tamaño fijo, sin atención.
- **Conceptos:** SSM, selección, tiempo lineal, estado de tamaño fijo, escaneo paralelo, contexto largo
- **Clases del programa:** [054](../../classes/part-04-neural-networks-and-deep-learning/054-rnn-lstm-y-secuencias/README.md), [055](../../classes/part-04-neural-networks-and-deep-learning/055-atencion-y-arquitectura-transformer/README.md)
- **Fuentes primarias:** [arXiv:2312.00752](https://arxiv.org/abs/2312.00752)

### P29 · Tree of Thoughts: Deliberate Problem Solving with Large Language Models (2023)

- **Autoría:** Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan
- **Problema anterior:** Una cadena de pensamiento decide de izquierda a derecha y sin vuelta atrás: un paso localmente razonable y globalmente equivocado condena toda la solución.
- **Propuesta:** Tratar los pasos de razonamiento como nodos de un árbol, hacer que el modelo evalúe estados parciales y aplicar búsqueda con poda y retroceso.
- **Hito:** Devuelve la búsqueda clásica al razonamiento: explorar varias ramas, evaluarlas y poder retroceder.
- **Conceptos:** árbol de pensamientos, búsqueda, autoevaluación, poda, retroceso, deliberación
- **Clases del programa:** [014](../../classes/part-01-symbolic-ai-search-logic-and-planning/014-busqueda-en-anchura-y-profundidad/README.md), [016](../../classes/part-01-symbolic-ai-search-logic-and-planning/016-diseno-y-validacion-de-heuristicas/README.md), [115](../../classes/part-09-ai-agent-engineering/115-planificacion-y-descomposicion-de-tareas/README.md), [175](../../classes/part-14-frontier-research-and-capstones/175-razonamiento-y-computo-en-tiempo-de-inferencia/README.md)
- **Fuentes primarias:** [arXiv:2305.10601](https://arxiv.org/abs/2305.10601)

### P30 · Reflexion: Language Agents with Verbal Reinforcement Learning (2023)

- **Autoría:** Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao
- **Problema anterior:** Un bucle ReAct que falla vuelve a empezar de cero y repite el mismo error, porque no conserva nada de lo aprendido en el intento anterior.
- **Propuesta:** Tras cada fallo, generar una reflexión verbal sobre qué salió mal y conservarla en una memoria episódica que condiciona el siguiente intento.
- **Hito:** El agente aprende entre intentos sin tocar un solo peso: el refuerzo ocurre en el contexto, en lenguaje natural.
- **Conceptos:** Reflexion, refuerzo verbal, memoria episódica, autocrítica, reintento
- **Clases del programa:** [122](../../classes/part-09-ai-agent-engineering/122-evaluacion-y-depuracion-de-agentes/README.md), [129](../../classes/part-10-multi-agent-systems-and-interoperability/129-critica-revision-y-debate-controlado/README.md)
- **Fuentes primarias:** [arXiv:2303.11366](https://arxiv.org/abs/2303.11366)

### P31 · Generative Agents: Interactive Simulacra of Human Behavior (2023)

- **Autoría:** Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein
- **Problema anterior:** Un agente con muchas horas de historia no cabe en su ventana de contexto, y un registro cronológico recupera lo reciente y trivial en vez de lo pertinente.
- **Propuesta:** Un flujo de memoria con recuperación puntuada por relevancia, recencia e importancia, más un proceso de reflexión que sintetiza recuerdos en conclusiones de nivel superior.
- **Hito:** Resuelve la memoria de un agente que vive mucho tiempo: qué recordar, cuándo y por qué, cuando el contexto no da para todo.
- **Conceptos:** memoria episódica, recuperación puntuada, reflexión, planificación, simulación social
- **Clases del programa:** [107](../../classes/part-08-retrieval-context-memory-and-knowledge/107-knowledge-graphs-y-graphrag/README.md), [118](../../classes/part-09-ai-agent-engineering/118-memoria-contexto-y-continuidad/README.md)
- **Fuentes primarias:** [arXiv:2304.03442](https://arxiv.org/abs/2304.03442)

### P32 · Voyager: An Open-Ended Embodied Agent with Large Language Models (2023)

- **Autoría:** Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, Anima Anandkumar
- **Problema anterior:** Un agente que resuelve tareas cada vez desde cero no mejora con la experiencia, y meter todo lo aprendido en el prompt no escala.
- **Propuesta:** Un currículo automático que propone la siguiente tarea alcanzable, una biblioteca de habilidades ejecutables indexada por nombre, y un bucle iterativo que depura el código con la retroalimentación del entorno.
- **Hito:** El agente acumula habilidades reutilizables en vez de contexto: memoria procedimental que no se borra al terminar la tarea.
- **Conceptos:** Voyager, biblioteca de habilidades, currículo automático, memoria procedimental, agente encarnado
- **Clases del programa:** [133](../../classes/part-10-multi-agent-systems-and-interoperability/133-agent-skills-como-capacidades-portables/README.md), [147](../../classes/part-11-embodied-ai-robotics-and-computer-use/147-proyecto-agente-que-actua-con-limites/README.md)
- **Fuentes primarias:** [arXiv:2305.16291](https://arxiv.org/abs/2305.16291)

### P33 · AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation (2023)

- **Autoría:** Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, y otros
- **Problema anterior:** Un solo agente escribe y juzga su propio trabajo, así que arrastra sus propios puntos ciegos; y no había forma estándar de componer varios agentes con humanos en el bucle.
- **Propuesta:** Agentes conversables y configurables —con o sin persona humana, con o sin ejecución de código— que se coordinan mediante mensajes, con patrones de conversación programables.
- **Hito:** El multiagente deja de ser una metáfora y pasa a ser un patrón de programación: agentes con rol que conversan hasta converger.
- **Conceptos:** multiagente, conversación, roles, crítico, human-in-the-loop, orquestación
- **Clases del programa:** [124](../../classes/part-10-multi-agent-systems-and-interoperability/124-workflow-subagente-y-sistema-multiagente/README.md), [127](../../classes/part-10-multi-agent-systems-and-interoperability/127-supervisor-workers/README.md), [131](../../classes/part-10-multi-agent-systems-and-interoperability/131-contratos-de-roles-capacidades-y-resultados/README.md)
- **Fuentes primarias:** [arXiv:2308.08155](https://arxiv.org/abs/2308.08155)

### P36 · Lost in the Middle: How Language Models Use Long Contexts (2023)

- **Autoría:** Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang
- **Problema anterior:** La industria competía por anunciar ventanas de contexto cada vez mayores, sin medir si los modelos aprovechaban de verdad todo ese espacio.
- **Propuesta:** Medirlo: colocar el mismo documento relevante en distintas posiciones del contexto y observar cómo cambia la exactitud.
- **Hito:** Tener contexto largo no es usarlo: el rendimiento cae en forma de U cuando el dato relevante está en el medio.
- **Conceptos:** contexto largo, curva en U, primacía, recencia, recuperación, posición
- **Clases del programa:** [101](../../classes/part-08-retrieval-context-memory-and-knowledge/101-segmentacion-metadatos-y-ventanas/README.md), [109](../../classes/part-08-retrieval-context-memory-and-knowledge/109-compresion-de-contexto-y-caches-semanticos/README.md), [110](../../classes/part-08-retrieval-context-memory-and-knowledge/110-evaluacion-de-fidelidad-cobertura-y-atribucion/README.md), [118](../../classes/part-09-ai-agent-engineering/118-memoria-contexto-y-continuidad/README.md)
- **Fuentes primarias:** [arXiv:2307.03172](https://arxiv.org/abs/2307.03172)

### P37 · MemGPT: Towards LLMs as Operating Systems (2023)

- **Autoría:** Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G. Patil, Ion Stoica, Joseph E. Gonzalez
- **Problema anterior:** La ventana de contexto es un límite duro. Ampliarla es caro y, como muestra P36, no garantiza que se use bien.
- **Propuesta:** Gestionar el contexto como un sistema operativo gestiona la memoria: un contexto principal pequeño, un almacén externo grande, y el propio modelo decidiendo qué paginar mediante llamadas de función.
- **Hito:** Aplica al contexto la idea de memoria virtual: una jerarquía que da la ilusión de memoria grande sobre una pequeña y rápida.
- **Conceptos:** MemGPT, memoria jerárquica, paginación, contexto virtual, llamadas de función, memoria de agente
- **Clases del programa:** [108](../../classes/part-08-retrieval-context-memory-and-knowledge/108-memoria-de-corto-y-largo-plazo/README.md), [109](../../classes/part-08-retrieval-context-memory-and-knowledge/109-compresion-de-contexto-y-caches-semanticos/README.md), [118](../../classes/part-09-ai-agent-engineering/118-memoria-contexto-y-continuidad/README.md)
- **Fuentes primarias:** [arXiv:2310.08560](https://arxiv.org/abs/2310.08560)

### P49 · QLoRA: Efficient Finetuning of Quantized LLMs (2023)

- **Autoría:** Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer
- **Problema anterior:** LoRA reduce los parámetros entrenables, pero el modelo base seguía teniendo que caber en memoria en precisión alta: eso dejaba fuera a casi todo el mundo.
- **Propuesta:** Cuantizar el modelo base congelado a 4 bits con un formato adaptado a la distribución de los pesos, y entrenar encima adaptadores LoRA en precisión alta.
- **Hito:** Pone el ajuste fino de un modelo muy grande al alcance de una sola GPU de consumo.
- **Conceptos:** QLoRA, cuantización de 4 bits, NF4, ajuste eficiente, memoria
- **Clases del programa:** [077](../../classes/part-06-foundation-models-and-llm-engineering/077-lora-qlora-y-adaptacion-eficiente/README.md), [082](../../classes/part-06-foundation-models-and-llm-engineering/082-dimensionar-hardware-de-la-laptop-al-cluster/README.md), [085](../../classes/part-06-foundation-models-and-llm-engineering/085-cuantizacion-e-inferencia-local/README.md)
- **Fuentes primarias:** [arXiv:2305.14314](https://arxiv.org/abs/2305.14314)

### P51 · SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (2023)

- **Autoría:** Carlos E. Jimenez, John Yang, Alexander Wettig, y otros
- **Problema anterior:** Los benchmarks de programación usaban problemas de juguete autocontenidos y se saturaban rápido; no medían nada parecido al trabajo real de mantener un repositorio.
- **Propuesta:** Construir el conjunto a partir de incidencias y parches reales de proyectos populares, y evaluar con un criterio objetivo: aplicar el parche generado y ejecutar los tests del propio repositorio.
- **Hito:** Cambia el criterio de evaluación: no si el código parece bien, sino si los tests del repositorio real pasan.
- **Conceptos:** SWE-bench, evaluación, tests como criterio, agentes de programación, contaminación
- **Clases del programa:** [122](../../classes/part-09-ai-agent-engineering/122-evaluacion-y-depuracion-de-agentes/README.md), [160](../../classes/part-13-evaluation-safety-security-and-governance/160-diseno-de-evaluaciones-y-criterios-de-exito/README.md), [178](../../classes/part-14-frontier-research-and-capstones/178-ia-para-programacion-y-modernizacion/README.md)
- **Fuentes primarias:** [arXiv:2310.06770](https://arxiv.org/abs/2310.06770)

### P52 · Towards Monosemanticity: Decomposing Language Models With Dictionary Learning (2023)

- **Autoría:** Trenton Bricken, Adly Templeton, Joshua Batson, y otros (Anthropic)
- **Problema anterior:** Al inspeccionar neuronas individuales de un modelo se encuentra que responden a conceptos no relacionados entre sí. La interpretabilidad neurona a neurona no funcionaba, y no se sabía por qué.
- **Propuesta:** La hipótesis de superposición: el modelo representa MÁS características que dimensiones tiene, como direcciones casi ortogonales con interferencia. Y un autoencoder disperso puede recuperar esas direcciones.
- **Hito:** Explica por qué una neurona no significa una cosa, y propone una forma de descomponer las activaciones en características interpretables.
- **Conceptos:** superposición, monosemanticidad, autoencoder disperso, interpretabilidad mecanicista, características
- **Clases del programa:** [160](../../classes/part-13-evaluation-safety-security-and-governance/160-diseno-de-evaluaciones-y-criterios-de-exito/README.md), [162](../../classes/part-13-evaluation-safety-security-and-governance/162-red-teaming-y-abuso/README.md), [167](../../classes/part-13-evaluation-safety-security-and-governance/167-explicabilidad-incertidumbre-y-calibracion/README.md)
- **Fuentes primarias:** [Transformer Circuits Thread (2023)](https://transformer-circuits.pub/2023/monosemantic-features)

### P21 · Mixtral of Experts (2024)

- **Autoría:** Albert Q. Jiang, y otros (Mistral AI)
- **Problema anterior:** En un modelo denso, cada token paga TODOS los parámetros. Crecer en capacidad implica crecer en coste de inferencia en la misma proporción.
- **Propuesta:** Sustituir la capa feed-forward por 8 expertos con un router que elige 2 por token, y publicar pesos y resultados bajo licencia abierta.
- **Hito:** Desacopla capacidad de cómputo: 47 000 millones de parámetros totales, 13 000 millones activos por token.
- **Conceptos:** mezcla de expertos, router, top-2, parámetros activos, balanceo de carga, Apache 2.0
- **Clases del programa:** [082](../../classes/part-06-foundation-models-and-llm-engineering/082-dimensionar-hardware-de-la-laptop-al-cluster/README.md), [084](../../classes/part-06-foundation-models-and-llm-engineering/084-serving-batching-y-caches/README.md), [086](../../classes/part-06-foundation-models-and-llm-engineering/086-seleccion-de-modelo-costo-latencia-y-privacidad/README.md), [125](../../classes/part-10-multi-agent-systems-and-interoperability/125-router-y-especialistas/README.md)
- **Fuentes primarias:** [arXiv:2401.04088](https://arxiv.org/abs/2401.04088)

### P22 · DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (2025)

- **Autoría:** DeepSeek-AI
- **Problema anterior:** La cadena de pensamiento dependía de demostraciones humanas caras, y esa supervisión limitaba la capacidad en problemas complejos.
- **Propuesta:** Recompensar únicamente el RESULTADO verificable y dejar que el comportamiento de razonamiento emerja del refuerzo, para luego transferirlo a modelos menores.
- **Hito:** El razonamiento se incentiva con refuerzo puro, sin trazas humanas anotadas; y es el primer LLM de pesos abiertos publicado tras revisión por pares.
- **Conceptos:** razonamiento, refuerzo, recompensa verificable, cómputo en inferencia, destilación, pesos abiertos
- **Clases del programa:** [078](../../classes/part-06-foundation-models-and-llm-engineering/078-rlhf-rlaif-y-dpo/README.md), [114](../../classes/part-09-ai-agent-engineering/114-ciclo-react-y-observacion-del-entorno/README.md), [175](../../classes/part-14-frontier-research-and-capstones/175-razonamiento-y-computo-en-tiempo-de-inferencia/README.md)
- **Fuentes primarias:** [arXiv:2501.12948](https://arxiv.org/abs/2501.12948) · [DOI (Nature 645, 633–638, 2025)](https://doi.org/10.1038/s41586-025-09422-z)

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
