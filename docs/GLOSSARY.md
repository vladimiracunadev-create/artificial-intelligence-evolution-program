# 📖 Glosario del programa

Vocabulario de trabajo de las 15 partes, organizado por etapa evolutiva. Cada término
enlaza a la clase donde se desarrolla. La primera sección reúne las **ingenierías de IA**
— el vocabulario 2026 de la industria — y el resto sigue el orden del programa.

**Índice:** [Ingenierías de IA](#-ingenierías-de-ia-el-vocabulario-2026) ·
[Fundamentos](#-fundamentos-y-método-parte-00) · [IA simbólica](#%EF%B8%8F-ia-simbólica-parte-01) ·
[Probabilística](#-ia-probabilística-y-evolutiva-parte-02) · [ML clásico](#-machine-learning-clásico-parte-03) ·
[Deep learning](#-redes-neuronales-y-deep-learning-parte-04) · [Lenguaje y multimodal](#%EF%B8%8F-lenguaje-visión-audio-y-multimodal-parte-05) ·
[Modelos fundacionales](#%EF%B8%8F-modelos-fundacionales-y-llm-engineering-parte-06) · [IA generativa](#-ia-generativa-parte-07) ·
[RAG y memoria](#-recuperación-contexto-memoria-y-conocimiento-parte-08) · [Agentes](#-ingeniería-de-agentes-parte-09) ·
[Multiagentes](#%EF%B8%8F-sistemas-multiagente-e-interoperabilidad-parte-10) · [IA encarnada](#-ia-encarnada-robótica-y-computer-use-parte-11) ·
[MLOps/AgentOps](#%EF%B8%8F-mlops-llmops-y-agentops-parte-12) · [Evaluación y seguridad](#%EF%B8%8F-evaluación-seguridad-y-gobernanza-parte-13) ·
[Frontera](#-frontera-parte-14)

---

## 🧰 Ingenierías de IA (el vocabulario 2026)

Disciplinas con nombre propio que la industria consolidó alrededor de los agentes. El
mapa completo, con su correspondencia clase a clase, está en la
[clase 109](../classes/part-09-ai-agent-engineering/109-de-modelo-y-automatizacion-a-agente/README.md).

- **Agent engineering:** disciplina paraguas — diseñar, construir, evaluar y operar
  agentes de forma fiable en producción. Cubre las demás entradas de esta sección.
- **Agent persona:** identidad operativa de un agente en un gateway empresarial: su rol
  atado a modelo, herramientas y guardrails como configuración auditable
  ([clase 150](../classes/part-12-ai-engineering-mlops-llmops-and-agentops/150-observabilidad-logs-metricas-y-trazas/README.md)).
- **Context engineering:** decidir qué tokens *ganan* lugar en la ventana en cada paso:
  el menor conjunto de alta señal que maximiza el resultado
  ([clase 106](../classes/part-08-retrieval-context-memory-and-knowledge/106-compresion-de-contexto-y-caches-semanticos/README.md),
  [115](../classes/part-09-ai-agent-engineering/115-memoria-contexto-y-continuidad/README.md)).
- **Context rot:** degradación de la atención del modelo sobre información enterrada en
  contextos largos; hoy medible con benchmarks dedicados
  ([clase 115](../classes/part-09-ai-agent-engineering/115-memoria-contexto-y-continuidad/README.md)).
- **Evaluation-driven development (EDD):** el eval en CI como *gate* de despliegue; el
  eval se escribe antes del cambio, como TDD hizo con los tests
  ([clase 119](../classes/part-09-ai-agent-engineering/119-evaluacion-y-depuracion-de-agentes/README.md)).
- **Graph / flow engineering:** formalizar el sistema como grafo explícito de estados —
  nodos, aristas condicionales, estado tipado, checkpoints — en vez de bucle imperativo
  ([clase 121](../classes/part-10-multi-agent-systems-and-interoperability/121-workflow-subagente-y-sistema-multiagente/README.md)).
- **Harness engineering:** diseñar la capa determinista que valida, autoriza, ejecuta y
  registra cada acción propuesta por el modelo. Ecuación: **Agente = Modelo + Harness**
  ([clase 110](../classes/part-09-ai-agent-engineering/110-anatomia-instrucciones-herramientas-estado-y-salida/README.md)).
- **Loop engineering:** diseñar el bucle — descubrimiento, descomposición, orquestación,
  verificación, memoria — y no solo el prompt
  ([clase 111](../classes/part-09-ai-agent-engineering/111-ciclo-react-y-observacion-del-entorno/README.md)).
- **Memory engineering:** decidir qué persiste entre sesiones, cómo se recupera y cómo
  se mide, con benchmarks estandarizados de recuerdo
  ([clase 105](../classes/part-08-retrieval-context-memory-and-knowledge/105-memoria-de-corto-y-largo-plazo/README.md)).
- **Patrones agénticos:** catálogo canónico de la industria — Reflection, Tool use,
  Planning, Multi-agent (Ng) y los cinco workflows de Anthropic
  ([clase 121](../classes/part-10-multi-agent-systems-and-interoperability/121-workflow-subagente-y-sistema-multiagente/README.md)).
- **Prompt engineering:** diseñar la instrucción de una llamada individual
  ([clase 079](../classes/part-06-foundation-models-and-llm-engineering/079-prompting-contexto-y-resultados-estructurados/README.md)).
- **Spec-driven development (SDD):** la especificación con criterios de aceptación
  verificables como contrato entre humano y agente de código
  ([clase 175](../classes/part-14-frontier-research-and-capstones/175-ia-para-programacion-y-modernizacion/README.md)).

## 🧭 Fundamentos y método (parte 00)

- **Agente racional:** entidad que percibe y actúa maximizando una medida de desempeño
  ([clase 004](../classes/part-00-foundations-history-and-scientific-method/004-agentes-racionales-entornos-y-medidas-de-desempeno/README.md)).
- **Baseline:** referencia mínima contra la que se compara cualquier mejora declarada
  ([clase 008](../classes/part-00-foundations-history-and-scientific-method/008-datos-evidencia-hipotesis-y-falsabilidad/README.md)).
- **Benchmark:** conjunto de tareas estandarizado para comparar sistemas; leerlo con
  criterio es una habilidad ([clase 010](../classes/part-00-foundations-history-and-scientific-method/010-como-leer-papers-benchmarks-y-claims-de-ia/README.md)).
- **Falsabilidad:** propiedad de una afirmación que puede refutarse con evidencia; base
  del método experimental del programa
  ([clase 008](../classes/part-00-foundations-history-and-scientific-method/008-datos-evidencia-hipotesis-y-falsabilidad/README.md)).
- **Invierno de la IA:** ciclo histórico de expectativas infladas y recortes
  ([clase 003](../classes/part-00-foundations-history-and-scientific-method/003-inviernos-resurgimientos-y-ciclos-de-expectativas/README.md)).
- **Medida de desempeño:** criterio externo que define el éxito de un agente
  ([clase 004](../classes/part-00-foundations-history-and-scientific-method/004-agentes-racionales-entornos-y-medidas-de-desempeno/README.md)).
- **Reproducibilidad:** capacidad de re-obtener un resultado con semilla, versión y
  datos fijos ([clase 009](../classes/part-00-foundations-history-and-scientific-method/009-entornos-python-git-y-experimentos-reproducibles/README.md)).
- **Test de Turing:** criterio conductual de inteligencia propuesto en 1950
  ([clase 002](../classes/part-00-foundations-history-and-scientific-method/002-de-turing-a-dartmouth-nacimiento-formal-del-campo/README.md)).

## ♟️ IA simbólica (parte 01)

- **A\*:** búsqueda informada óptima con heurística admisible
  ([clase 015](../classes/part-01-symbolic-ai-search-logic-and-planning/015-costo-uniforme-busqueda-voraz-y-a/README.md)).
- **CSP:** problema de satisfacción de restricciones — variables, dominios, restricciones
  ([clase 018](../classes/part-01-symbolic-ai-search-logic-and-planning/018-problemas-de-satisfaccion-de-restricciones/README.md)).
- **Espacio de estados:** formulación de un problema como estados y operadores
  ([clase 013](../classes/part-01-symbolic-ai-search-logic-and-planning/013-espacios-de-estados-y-formulacion-de-problemas/README.md)).
- **Heurística:** estimación del costo restante que guía la búsqueda; se diseña y valida
  ([clase 016](../classes/part-01-symbolic-ai-search-logic-and-planning/016-diseno-y-validacion-de-heuristicas/README.md)).
- **Minimax / poda alfa-beta:** decisión adversarial en juegos de suma cero
  ([clase 017](../classes/part-01-symbolic-ai-search-logic-and-planning/017-juegos-minimax-y-poda-alfa-beta/README.md)).
- **Ontología:** especificación formal de conceptos y relaciones de un dominio
  ([clase 021](../classes/part-01-symbolic-ai-search-logic-and-planning/021-representacion-del-conocimiento-y-ontologias/README.md)).
- **Sistema experto:** motor de reglas + base de conocimiento con explicación de
  inferencias ([clase 022](../classes/part-01-symbolic-ai-search-logic-and-planning/022-sistemas-expertos-y-motores-de-reglas/README.md)).
- **STRIPS / PDDL:** lenguajes de planificación clásica por precondiciones y efectos
  ([clase 023](../classes/part-01-symbolic-ai-search-logic-and-planning/023-planificacion-clasica-con-strips-y-pddl/README.md)).
- **Unificación:** emparejamiento de términos lógicos que habilita la inferencia de
  primer orden ([clase 020](../classes/part-01-symbolic-ai-search-logic-and-planning/020-logica-de-primer-orden-y-unificacion/README.md)).

## 🎲 IA probabilística y evolutiva (parte 02)

- **Algoritmo genético:** optimización por selección, cruce y mutación de poblaciones
  ([clase 033](../classes/part-02-probabilistic-evolutionary-and-decision-ai/033-algoritmos-geneticos/README.md)).
- **Causalidad:** distinción entre correlación e intervención; modelos causales
  ([clase 035](../classes/part-02-probabilistic-evolutionary-and-decision-ai/035-programacion-probabilistica-y-causalidad/README.md)).
- **HMM:** modelo oculto de Markov — estados latentes con observaciones ruidosas
  ([clase 028](../classes/part-02-probabilistic-evolutionary-and-decision-ai/028-modelos-ocultos-de-markov/README.md)).
- **Lógica difusa:** pertenencia gradual y control aproximado
  ([clase 032](../classes/part-02-probabilistic-evolutionary-and-decision-ai/032-logica-difusa-y-control-aproximado/README.md)).
- **MDP:** proceso de decisión de Markov — estados, acciones, recompensas, política
  ([clase 029](../classes/part-02-probabilistic-evolutionary-and-decision-ai/029-procesos-de-decision-de-markov/README.md)).
- **Monte Carlo:** estimación por muestreo aleatorio repetido
  ([clase 031](../classes/part-02-probabilistic-evolutionary-and-decision-ai/031-metodos-monte-carlo-y-simulacion/README.md)).
- **Red bayesiana:** grafo dirigido de dependencias probabilísticas
  ([clase 027](../classes/part-02-probabilistic-evolutionary-and-decision-ai/027-redes-bayesianas-e-independencia-condicional/README.md)).
- **Teorema de Bayes:** actualización de creencias con evidencia nueva
  ([clase 026](../classes/part-02-probabilistic-evolutionary-and-decision-ai/026-teorema-de-bayes-y-actualizacion-de-creencias/README.md)).
- **Utilidad esperada:** criterio de decisión bajo incertidumbre
  ([clase 030](../classes/part-02-probabilistic-evolutionary-and-decision-ai/030-teoria-de-decision-y-utilidad-esperada/README.md)).

## 📊 Machine learning clásico (parte 03)

- **Backtesting:** evaluación temporal sin fuga de futuro en series
  ([clase 045](../classes/part-03-classical-machine-learning/045-series-temporales-y-backtesting/README.md)).
- **Boosting / ensemble:** combinación de modelos débiles en uno fuerte
  ([clase 041](../classes/part-03-classical-machine-learning/041-random-forest-boosting-y-ensembles/README.md)).
- **Calibración:** que las probabilidades predichas coincidan con las frecuencias reales
  ([clase 047](../classes/part-03-classical-machine-learning/047-metricas-calibracion-sesgo-y-costo-de-error/README.md)).
- **Clustering:** agrupación no supervisada por similitud
  ([clase 043](../classes/part-03-classical-machine-learning/043-clustering-y-reduccion-de-dimensionalidad/README.md)).
- **Detección de anomalías:** identificar observaciones que no siguen el patrón
  ([clase 044](../classes/part-03-classical-machine-learning/044-deteccion-de-anomalias/README.md)).
- **Feature engineering:** construcción y selección de variables predictivas
  ([clase 042](../classes/part-03-classical-machine-learning/042-ingenieria-y-seleccion-de-caracteristicas/README.md)).
- **Overfitting / regularización:** memorizar el train vs. penalizar la complejidad
  ([clase 038](../classes/part-03-classical-machine-learning/038-regresion-lineal-regularizacion-y-diagnostico/README.md)).
- **Train/validation/test:** partición que separa ajuste, selección y estimación honesta
  ([clase 037](../classes/part-03-classical-machine-learning/037-flujo-supervisado-y-particion-train-validation-test/README.md)).

## 🧠 Redes neuronales y deep learning (parte 04)

- **Atención / Transformer:** pesado dinámico de relaciones entre tokens; la arquitectura
  dominante ([clase 055](../classes/part-04-neural-networks-and-deep-learning/055-atencion-y-arquitectura-transformer/README.md)).
- **Backpropagation:** cálculo del gradiente por regla de la cadena hacia atrás
  ([clase 050](../classes/part-04-neural-networks-and-deep-learning/050-mlp-y-backpropagation/README.md)).
- **CNN:** red convolucional para estructura espacial
  ([clase 053](../classes/part-04-neural-networks-and-deep-learning/053-cnn-y-aprendizaje-espacial/README.md)).
- **Difusión:** generación por des-ruido iterativo
  ([clase 058](../classes/part-04-neural-networks-and-deep-learning/058-autoencoders-gan-y-difusion/README.md)).
- **Fine-tuning / destilación:** adaptar un modelo preentrenado o comprimirlo en otro
  menor ([clase 059](../classes/part-04-neural-networks-and-deep-learning/059-transferencia-fine-tuning-y-destilacion/README.md)).
- **GNN:** red neuronal sobre grafos
  ([clase 056](../classes/part-04-neural-networks-and-deep-learning/056-graph-neural-networks/README.md)).
- **LSTM / RNN:** redes recurrentes para secuencias
  ([clase 054](../classes/part-04-neural-networks-and-deep-learning/054-rnn-lstm-y-secuencias/README.md)).
- **Perceptrón:** neurona lineal con umbral; el límite de separabilidad que motivó todo
  lo demás ([clase 049](../classes/part-04-neural-networks-and-deep-learning/049-perceptron-y-limites-de-separabilidad/README.md)).
- **RL profundo:** aprendizaje por refuerzo con aproximadores neuronales
  ([clase 057](../classes/part-04-neural-networks-and-deep-learning/057-aprendizaje-por-refuerzo-profundo/README.md)).

## 👁️ Lenguaje, visión, audio y multimodal (parte 05)

- **ASR:** reconocimiento automático del habla
  ([clase 067](../classes/part-05-language-vision-audio-and-multimodal-ai/067-reconocimiento-automatico-del-habla/README.md)).
- **Embedding semántico:** vector que captura similitud de significado
  ([clase 066](../classes/part-05-language-vision-audio-and-multimodal-ai/066-embeddings-semanticos-y-similitud/README.md)).
- **Fusión multimodal:** representación conjunta de texto, imagen y audio
  ([clase 070](../classes/part-05-language-vision-audio-and-multimodal-ai/070-fusion-multimodal-y-representacion-conjunta/README.md)).
- **OCR:** extracción de texto desde imágenes y documentos
  ([clase 063](../classes/part-05-language-vision-audio-and-multimodal-ai/063-ocr-y-comprension-de-documentos/README.md)).
- **Segmentación / pose:** localización a nivel de píxel y esqueleto
  ([clase 062](../classes/part-05-language-vision-audio-and-multimodal-ai/062-deteccion-segmentacion-y-pose/README.md)).
- **Tokenización:** partir texto en unidades que el modelo procesa
  ([clase 064](../classes/part-05-language-vision-audio-and-multimodal-ai/064-tokenizacion-y-representacion-del-lenguaje/README.md)).
- **VLM:** modelo visión-lenguaje
  ([clase 069](../classes/part-05-language-vision-audio-and-multimodal-ai/069-modelos-vision-lenguaje/README.md)).

## ⚙️ Modelos fundacionales y LLM engineering (parte 06)

- **Instruction tuning:** ajuste con pares instrucción-respuesta para seguir órdenes
  ([clase 076](../classes/part-06-foundation-models-and-llm-engineering/076-instruction-tuning-y-datos-de-instrucciones/README.md)).
- **Leyes de escalamiento:** relaciones empíricas entre cómputo, datos y calidad
  ([clase 075](../classes/part-06-foundation-models-and-llm-engineering/075-escalamiento-computo-y-leyes-empiricas/README.md)).
- **LoRA / QLoRA:** adaptación eficiente con matrices de bajo rango
  ([clase 077](../classes/part-06-foundation-models-and-llm-engineering/077-lora-qlora-y-adaptacion-eficiente/README.md)).
- **Modelo fundacional:** modelo preentrenado a gran escala adaptable a múltiples tareas
  ([clase 074](../classes/part-06-foundation-models-and-llm-engineering/074-objetivos-de-preentrenamiento/README.md)).
- **Prompting estructurado:** instrucciones + contexto + contrato de salida
  ([clase 079](../classes/part-06-foundation-models-and-llm-engineering/079-prompting-contexto-y-resultados-estructurados/README.md)).
- **Cuantización:** reducir la precisión numérica para inferencia local barata
  ([clase 082](../classes/part-06-foundation-models-and-llm-engineering/082-cuantizacion-e-inferencia-local/README.md)).
- **RLHF / DPO:** alineación con preferencias humanas
  ([clase 078](../classes/part-06-foundation-models-and-llm-engineering/078-rlhf-rlaif-y-dpo/README.md)).
- **Serving / batching:** infraestructura de inferencia con caches y lotes
  ([clase 081](../classes/part-06-foundation-models-and-llm-engineering/081-serving-batching-y-caches/README.md)).
- **Tool calling:** el modelo emite intenciones de llamada que un runtime ejecuta
  ([clase 080](../classes/part-06-foundation-models-and-llm-engineering/080-tool-calling-y-ejecucion-controlada/README.md)).

## 🎨 IA generativa (parte 07)

- **Datos sintéticos:** datos generados; útiles y a la vez riesgo de contaminación
  ([clase 094](../classes/part-07-generative-ai-across-media/094-datos-sinteticos-utilidad-y-contaminacion/README.md)).
- **Espacio latente:** representación comprimida donde se interpola y edita
  ([clase 085](../classes/part-07-generative-ai-across-media/085-espacios-latentes-y-autoencoders-variacionales/README.md)).
- **GAN:** generador y discriminador en entrenamiento adversarial
  ([clase 086](../classes/part-07-generative-ai-across-media/086-gan-y-entrenamiento-adversarial/README.md)).
- **Modelo de difusión:** generación por des-ruido; el estándar de imagen
  ([clase 087](../classes/part-07-generative-ai-across-media/087-modelos-de-difusion/README.md)).
- **Procedencia / watermarking:** marcas y metadatos de autenticidad del contenido
  generado ([clase 095](../classes/part-07-generative-ai-across-media/095-procedencia-marcas-y-autenticidad/README.md)).
- **Text-to-image / condicionamiento:** guiar la generación con texto u otras señales
  ([clase 088](../classes/part-07-generative-ai-across-media/088-texto-a-imagen-y-condicionamiento/README.md)).

## 🔎 Recuperación, contexto, memoria y conocimiento (parte 08)

- **BM25:** ranking léxico clásico; complemento del vectorial
  ([clase 099](../classes/part-08-retrieval-context-memory-and-knowledge/099-busqueda-lexica-y-bm25/README.md)).
- **Búsqueda híbrida:** fusión de rankings léxico y vectorial
  ([clase 100](../classes/part-08-retrieval-context-memory-and-knowledge/100-busqueda-hibrida-y-fusion-de-rankings/README.md)).
- **Chunking:** segmentación de documentos con metadatos y ventanas
  ([clase 098](../classes/part-08-retrieval-context-memory-and-knowledge/098-segmentacion-metadatos-y-ventanas/README.md)).
- **Compactación:** resumir con pérdida lo viejo del contexto conservando el rumbo
  ([clase 105](../classes/part-08-retrieval-context-memory-and-knowledge/105-memoria-de-corto-y-largo-plazo/README.md),
  [115](../classes/part-09-ai-agent-engineering/115-memoria-contexto-y-continuidad/README.md)).
- **GraphRAG / knowledge graph:** recuperación sobre grafos de entidades y relaciones
  ([clase 104](../classes/part-08-retrieval-context-memory-and-knowledge/104-knowledge-graphs-y-graphrag/README.md)).
- **Memoria episódica / semántica / procedimental:** qué pasó / hechos destilados / cómo
  actuar ([clase 105](../classes/part-08-retrieval-context-memory-and-knowledge/105-memoria-de-corto-y-largo-plazo/README.md)).
- **RAG:** generación aumentada con recuperación de evidencia citable
  ([clase 102](../classes/part-08-retrieval-context-memory-and-knowledge/102-rag-basico-con-citas/README.md)).
- **Re-ranking:** reordenar candidatos con un modelo más caro y preciso
  ([clase 101](../classes/part-08-retrieval-context-memory-and-knowledge/101-re-ranking-y-filtros-de-evidencia/README.md)).
- **Caché semántico:** reutilizar respuestas de consultas equivalentes
  ([clase 106](../classes/part-08-retrieval-context-memory-and-knowledge/106-compresion-de-contexto-y-caches-semanticos/README.md)).

## 🤖 Ingeniería de agentes (parte 09)

- **Agente:** LLM que, en un bucle, decide qué acción ejecutar, observa el resultado real
  y decide el siguiente paso bajo límites explícitos
  ([clase 109](../classes/part-09-ai-agent-engineering/109-de-modelo-y-automatizacion-a-agente/README.md)).
- **Checkpoint:** instantánea del estado del bucle para reanudar sin repetir efectos
  ([clase 115](../classes/part-09-ai-agent-engineering/115-memoria-contexto-y-continuidad/README.md)).
- **Ciclo ReAct:** thought → action → observation; la observación ancla al mundo real
  ([clase 111](../classes/part-09-ai-agent-engineering/111-ciclo-react-y-observacion-del-entorno/README.md)).
- **Espectro de autonomía:** dial L0-L5, de modelo puro a autonomía extendida
  ([clase 109](../classes/part-09-ai-agent-engineering/109-de-modelo-y-automatizacion-a-agente/README.md)).
- **Guardrail:** control que valida o limita entradas, salidas o acciones
  ([clase 116](../classes/part-09-ai-agent-engineering/116-permisos-sandbox-y-minimo-privilegio/README.md)).
- **Harness:** capa determinista que valida, autoriza, ejecuta y registra las acciones
  del modelo ([clase 110](../classes/part-09-ai-agent-engineering/110-anatomia-instrucciones-herramientas-estado-y-salida/README.md)).
- **Human-in-the-loop:** aprobación humana interpuesta ante acciones de riesgo
  ([clase 117](../classes/part-09-ai-agent-engineering/117-human-in-the-loop-y-aprobaciones/README.md)).
- **Idempotencia:** ejecutar dos veces produce el mismo efecto que una; requisito para
  reintentos seguros ([clase 113](../classes/part-09-ai-agent-engineering/113-herramientas-tipadas-y-efectos-laterales/README.md)).
- **Mínimo privilegio:** cada herramienta con los permisos estrictamente necesarios
  ([clase 116](../classes/part-09-ai-agent-engineering/116-permisos-sandbox-y-minimo-privilegio/README.md)).
- **Presupuesto:** límites duros de pasos, tokens, costo y tiempo por tarea
  ([clase 118](../classes/part-09-ai-agent-engineering/118-presupuestos-de-pasos-tokens-costo-y-tiempo/README.md)).
- **Salida estructurada:** contrato de resultado con `evidence` y `limitations`
  obligatorios ([clase 110](../classes/part-09-ai-agent-engineering/110-anatomia-instrucciones-herramientas-estado-y-salida/README.md)).
- **Tool:** operación invocable con contrato (nombre, esquema, retorno); lectura o efecto
  ([clase 113](../classes/part-09-ai-agent-engineering/113-herramientas-tipadas-y-efectos-laterales/README.md)).
- **Trayectoria:** secuencia auditable de decisiones y observaciones de un run
  ([clase 119](../classes/part-09-ai-agent-engineering/119-evaluacion-y-depuracion-de-agentes/README.md)).

## 🕸️ Sistemas multiagente e interoperabilidad (parte 10)

- **A2A:** protocolo de descubrimiento e interoperabilidad entre agentes
  ([clase 131](../classes/part-10-multi-agent-systems-and-interoperability/131-a2a-descubrimiento-e-interoperabilidad/README.md)).
- **Blackboard:** memoria compartida donde los agentes leen y publican
  ([clase 127](../classes/part-10-multi-agent-systems-and-interoperability/127-blackboard-y-memoria-compartida/README.md)).
- **Fan-out / map-reduce:** paralelizar subtareas y consolidar resultados
  ([clase 125](../classes/part-10-multi-agent-systems-and-interoperability/125-paralelismo-fan-out-y-map-reduce/README.md)).
- **Handoff:** transferencia de responsabilidad y contexto entre agentes
  ([clase 123](../classes/part-10-multi-agent-systems-and-interoperability/123-handoffs-y-transferencia-de-contexto/README.md)).
- **MCP:** Model Context Protocol — contratos estándar de tools, resources y prompts
  ([clase 129](../classes/part-10-multi-agent-systems-and-interoperability/129-mcp-tools-resources-y-prompts/README.md)).
- **Router:** clasificador que dirige cada tarea al especialista adecuado
  ([clase 122](../classes/part-10-multi-agent-systems-and-interoperability/122-router-y-especialistas/README.md)).
- **Skill:** instrucciones y recursos portables que empaquetan una capacidad
  ([clase 130](../classes/part-10-multi-agent-systems-and-interoperability/130-agent-skills-como-capacidades-portables/README.md)).
- **Subagente:** agente invocado por otro como herramienta, con contexto aislado y
  retorno resumido ([clase 121](../classes/part-10-multi-agent-systems-and-interoperability/121-workflow-subagente-y-sistema-multiagente/README.md)).
- **Supervisor-workers:** orquestador que delega en trabajadores y consolida
  ([clase 124](../classes/part-10-multi-agent-systems-and-interoperability/124-supervisor-workers/README.md)).
- **Workflow:** secuencia de pasos definida por código donde el LLM rellena casillas
  ([clase 121](../classes/part-10-multi-agent-systems-and-interoperability/121-workflow-subagente-y-sistema-multiagente/README.md)).

## 🦾 IA encarnada, robótica y computer use (parte 11)

- **Computer use:** agente que opera interfaces gráficas por visión y acciones de
  teclado/ratón ([clase 141](../classes/part-11-embodied-ai-robotics-and-computer-use/141-computer-use-basado-en-vision/README.md)).
- **Digital twin / sim-to-real:** entrenar en simulación y transferir al mundo físico
  ([clase 139](../classes/part-11-embodied-ai-robotics-and-computer-use/139-simulacion-sim-to-real-y-digital-twins/README.md)).
- **Percepción-planificación-acción:** la arquitectura clásica de robótica
  ([clase 133](../classes/part-11-embodied-ai-robotics-and-computer-use/133-arquitectura-percepcion-planificacion-accion/README.md)).
- **RPA agéntica:** automatización de escritorio con decisión del modelo
  ([clase 143](../classes/part-11-embodied-ai-robotics-and-computer-use/143-automatizacion-de-escritorio-y-rpa-agentica/README.md)).
- **SLAM:** localización y mapeo simultáneos
  ([clase 135](../classes/part-11-embodied-ai-robotics-and-computer-use/135-localizacion-mapeo-y-slam/README.md)).

## ⚙️ MLOps, LLMOps y AgentOps (parte 12)

- **AgentOps:** operación de agentes — análisis de trayectorias, costos por rol,
  incidentes ([clase 153](../classes/part-12-ai-engineering-mlops-llmops-and-agentops/153-agentops-y-analisis-de-trayectorias/README.md)).
- **AI gateway:** proxy único de acceso a modelos y agentes: trazas, costos, límites,
  registros y personas ([clase 150](../classes/part-12-ai-engineering-mlops-llmops-and-agentops/150-observabilidad-logs-metricas-y-trazas/README.md)).
- **Champion-challenger:** promoción de modelos por comparación controlada
  ([clase 147](../classes/part-12-ai-engineering-mlops-llmops-and-agentops/147-registro-y-promocion-champion-challenger/README.md)).
- **Deriva (drift):** cambio en los datos o el comportamiento que degrada el sistema
  ([clase 151](../classes/part-12-ai-engineering-mlops-llmops-and-agentops/151-deriva-feedback-y-evaluacion-continua/README.md)).
- **Observabilidad:** inferir el estado interno desde logs, métricas y trazas
  ([clase 150](../classes/part-12-ai-engineering-mlops-llmops-and-agentops/150-observabilidad-logs-metricas-y-trazas/README.md)).
- **OpenTelemetry / span:** estándar de trazas; cada span es una operación medida
  ([clase 150](../classes/part-12-ai-engineering-mlops-llmops-and-agentops/150-observabilidad-logs-metricas-y-trazas/README.md)).
- **Rollback:** volver a un estado bueno conocido tras un despliegue fallido
  ([clase 155](../classes/part-12-ai-engineering-mlops-llmops-and-agentops/155-resiliencia-idempotencia-rollback-y-recuperacion/README.md)).
- **SLO:** objetivo de nivel de servicio medible (latencia, error, fallback)
  ([clase 150](../classes/part-12-ai-engineering-mlops-llmops-and-agentops/150-observabilidad-logs-metricas-y-trazas/README.md)).

## 🛡️ Evaluación, seguridad y gobernanza (parte 13)

- **Abstención:** que el sistema diga "no sé" cuando la evidencia no alcanza
  ([clase 165](../classes/part-13-evaluation-safety-security-and-governance/165-alucinacion-grounding-y-abstencion/README.md)).
- **Alucinación:** afirmación fluida sin anclaje en evidencia
  ([clase 165](../classes/part-13-evaluation-safety-security-and-governance/165-alucinacion-grounding-y-abstencion/README.md)).
- **Eval:** prueba estructurada de comportamiento con criterio de éxito ejecutable
  ([clase 157](../classes/part-13-evaluation-safety-security-and-governance/157-diseno-de-evaluaciones-y-criterios-de-exito/README.md)).
- **Fairness:** análisis de sesgo por grupos afectados
  ([clase 163](../classes/part-13-evaluation-safety-security-and-governance/163-sesgo-fairness-y-grupos-afectados/README.md)).
- **Golden dataset:** conjunto curado de referencia para regresión
  ([clase 158](../classes/part-13-evaluation-safety-security-and-governance/158-golden-datasets-regresion-y-llm-as-judge/README.md)).
- **Grounding:** anclar cada afirmación a una observación o fuente verificable
  ([clase 165](../classes/part-13-evaluation-safety-security-and-governance/165-alucinacion-grounding-y-abstencion/README.md)).
- **LLM-as-judge:** usar un LLM con rúbrica como evaluador; requiere calibración humana
  ([clase 158](../classes/part-13-evaluation-safety-security-and-governance/158-golden-datasets-regresion-y-llm-as-judge/README.md)).
- **Prompt injection:** instrucciones maliciosas dentro de datos observados
  ([clase 160](../classes/part-13-evaluation-safety-security-and-governance/160-prompt-injection-e-instrucciones-no-confiables/README.md)).
- **Red teaming:** ataque deliberado y sistemático para encontrar fallos antes que el
  adversario ([clase 159](../classes/part-13-evaluation-safety-security-and-governance/159-red-teaming-y-abuso/README.md)).
- **Supply chain de tools:** riesgo de herramientas y servidores MCP de terceros
  ([clase 161](../classes/part-13-evaluation-safety-security-and-governance/161-seguridad-de-tools-mcp-y-supply-chain/README.md)).

## 🔭 Frontera (parte 14)

- **Aprendizaje continuo:** adaptarse sin olvidar catastróficamente
  ([clase 173](../classes/part-14-frontier-research-and-capstones/173-aprendizaje-continuo-y-adaptacion/README.md)).
- **Causal AI:** descubrimiento y uso de estructura causal
  ([clase 170](../classes/part-14-frontier-research-and-capstones/170-causal-ai-y-descubrimiento-cientifico/README.md)).
- **Cómputo en tiempo de inferencia:** razonar más muestreando/verificando más
  ([clase 172](../classes/part-14-frontier-research-and-capstones/172-razonamiento-y-computo-en-tiempo-de-inferencia/README.md)).
- **IA neuro-simbólica:** combinar aprendizaje neuronal con razonamiento simbólico
  ([clase 169](../classes/part-14-frontier-research-and-capstones/169-ia-neuro-simbolica/README.md)).
- **pass@k:** probabilidad de que alguna de k muestras pase todos los tests
  ([clase 175](../classes/part-14-frontier-research-and-capstones/175-ia-para-programacion-y-modernizacion/README.md)).
- **Privacidad diferencial / federado:** aprender sin centralizar ni exponer datos
  individuales ([clase 174](../classes/part-14-frontier-research-and-capstones/174-privacidad-diferencial-y-aprendizaje-federado/README.md)).
- **SWE-bench:** benchmark de agentes de código sobre issues reales de GitHub
  ([clase 175](../classes/part-14-frontier-research-and-capstones/175-ia-para-programacion-y-modernizacion/README.md)).
- **Tests de caracterización:** tests que fijan el comportamiento actual antes de migrar
  legado ([clase 175](../classes/part-14-frontier-research-and-capstones/175-ia-para-programacion-y-modernizacion/README.md)).
- **World model:** modelo interno del entorno que permite simular antes de actuar
  ([clase 171](../classes/part-14-frontier-research-and-capstones/171-world-models-y-simulacion-interna/README.md)).
