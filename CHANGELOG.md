# 📜 Changelog

Este proyecto sigue Versionado Semántico y conserva hechos históricos.

## 🏷️ Política de versiones y releases

- **Fuente canónica de la versión:** `pyproject.toml`. Los otros cuatro
  marcadores —`curriculum.yaml`, `src/ai_evolution/__init__.py`,
  `apps/android/package.json` y el badge del README— deben coincidir con él;
  `tests/test_program.py::VersionCoherenceTests` falla en CI si divergen.
- **Cada versión de este changelog tiene su tag** `vX.Y.Z` apuntando al commit
  que la introdujo. Los tags anteriores a 0.4.3 se crearon retroactivamente en
  esa fecha, sobre sus commits reales.
- **No toda versión tiene una release publicada en GitHub.** Las releases marcan
  hitos que valen la pena descargar; los tags marcan todas las versiones.
- Los conteos que aparecen en cada entrada son los de **esa** versión. Para el
  estado actual, mira el [roadmap](ROADMAP.md) o ejecuta `ai-evolution validate`.

## 0.8.1 — 2026-08-16

Correcciones de coherencia encontradas con una auditoría **exhaustiva**: en vez de buscar los
valores que uno ya sospecha, se extrajo cada par (número, sustantivo) de los **903 ficheros**
`.md` y `.html` del repositorio y se contrastó contra los conteos reales.

- **El PDF del eje no contenía los anexos matemáticos** que su propia descripción prometía. Ahora
  los incluye, entre las guías y las fichas: 434 páginas frente a las 413 anteriores.
- **La sección de rutas de `papers/README.md` pasa a ser generada.** Estaba escrita a mano,
  anunciaba «seis rutas» cuando ya había siete y sus tablas paraban en P33: faltaban 19 papers.
  Ahora se genera desde `papers.json` entre marcadores, y `generate_papers.py --check` la vigila
  en CI, así que no puede volver a quedarse atrás.
- **El roadmap listaba como pendiente lo que ya se había entregado.** La sección «0.7 — Camino a
  50 papers» tenía sin marcar memoria y contexto, arquitectura y entrenamiento, y evaluación y
  seguridad, entregados en 0.7.0 y 0.8.0. Se sustituye por las secciones reales de esas dos
  versiones, y los planes que siguen pendientes dejan de llevar un número de versión que ya se
  usó para otra cosa.
- **Conteos corregidos**: el PDF del eje decía «201 páginas · 22 fichas · 22 evaluaciones»
  (`README.md`, `papers/ROADMAP.md`), los anexos hablaban de «22 fichas», los enlaces de vuelta
  de «27 clases», la clase 182 de «178» y «180 clases», y el total de PDFs imprimibles omitía los
  52 individuales.

## 0.8.0 — 2026-08-16

- **Las 14 fichas que faltaban (P39–P52)**, con lo que el eje queda **completo en 52 papers** y sin
  ninguna entrada pendiente en el catálogo. Cada una con sus 18 secciones, diagrama, fuentes
  primarias verificadas con fecha de consulta y una sección honesta de límites:
  - **Arquitectura y entrenamiento**: GAN (2014), Dropout (2014), Adam (2014), ejemplos adversarios
    (2014), BatchNorm (2015), ResNet (2015), destilación (2015), Vision Transformer (2020),
    AlphaFold 2 (2021), LoRA (2021) y QLoRA (2023).
  - **Evaluación y seguridad**: IA constitucional (2022), SWE-bench (2023) y superposición con
    autoencoders dispersos (2022–2023).
- **Dos rutas nuevas** en el catálogo: `ruta_arquitectura` (P38–P49) y `ruta_evaluacion`
  (P50–P52), ambas en orden cronológico y validadas por el mismo contrato que las anteriores.
- **Dos afirmaciones de motor corregidas** porque su propia salida las contradecía:
  - `constitutional_ai` evaluaba cada principio contra un texto que la revisión anterior ya había
    cambiado, así que la traza decía «un principio violado» mientras la evidencia decía dos. Ahora
    la crítica se hace contra la respuesta **original** y ambas coinciden.
  - `superposition` presentaba el solape **medio** como prueba de interferencia, pero ese valor
    depende de la dimensión y no del número de conceptos. Ahora cita el solape **máximo**, que sí
    crece: de 0,734 con 8 conceptos a 0,925 con 80.
- **Barrido de coherencia de toda la documentación**: se sincronizaron los conteos de papers,
  notebooks, motores, páginas del sitio y clases enlazadas en `README.md`, `ROADMAP.md`,
  `INSTALL.md`, `RECRUITER.md`, `papers/README.md`, `papers/ROADMAP.md`, `docs/ARCHITECTURE.md`,
  `docs/STUDENT_GUIDE.md`, `site/index.html`, los badges y el About de GitHub. Las referencias
  históricas del changelog y del roadmap por versión se conservan intactas.
- **52 PDFs individuales** regenerados (uno por paper) y el PDF completo del eje.
- **66 páginas del eje** en el sitio, con enlaces de vuelta en **50 clases**.

## 0.7.0 — 2026-08-16

- **Bloque de memoria y contexto (P34–P37)**, que faltaba por completo: RoPE (2021),
  FlashAttention (2022), *Lost in the Middle* (2023) y MemGPT (2023). Cubre cómo se codifica la
  posición, por qué el contexto largo es viable, por qué tenerlo **no basta** —la curva en U— y
  cómo se gestiona como memoria jerárquica. Los cuatro verificados contra su fuente primaria.
- **P38 VAE** abre el bloque de arquitectura y entrenamiento con el truco de reparametrización.
- **Índice unificado y ordenado por año.** La documentación mostraba una tabla por bloque, lo que
  se leía como un listado de «lo nuevo». Ahora `PAPERS_INDEX.md` tiene **una tabla maestra
  cronológica** con todos los papers y una columna de bloque, más una vista temática aparte. Se
  documenta explícitamente que los identificadores `PXX` son **estables** y su orden es de
  incorporación, no de lectura.
- **Un PDF por paper**: `python scripts/generate_pdfs.py --por-paper` genera 38 PDFs en
  `docs/pdf/papers/`, cada uno con la ficha completa y su evaluación, y una portada que deja
  claro que **no es el paper original** sino la ficha pedagógica en español que enlaza a la fuente.
- **19 motores deterministas nuevos** ya implementados y probados (RoPE, FlashAttention, curva en
  U, paginación de memoria, VAE, GAN, dropout, Adam, adversarios, batch norm, ResNet, destilación,
  ViT, AlphaFold, LoRA, cuantización, IA constitucional, SWE-bench y superposición), con sus 19
  notebooks generados y ejecutados sin error.
- **14 papers en construcción** (P39–P52). Sus motores y notebooks están listos y probados; les
  falta la ficha de 18 secciones. Se declaran en `pendientes_de_ficha` dentro del catálogo y
  aparecen como «en construcción» en el índice, **fuera** de la tabla maestra, para que el
  contrato del eje siga siendo verificable en todo momento.

## 0.6.0 — 2026-08-16

- **El eje pasa de 22 a 33 papers, con dos bloques nuevos.** El detonante fue una observación
  correcta: el eje tenía ReAct y Toolformer, pero Reflexion, Generative Agents, Voyager y AutoGen
  vivían **dentro** de P16 como cluster, sin ficha propia, y multiagente no tenía ninguna. Al
  revisarlo apareció un hueco mayor todavía: **no había un solo paper de aprendizaje por
  refuerzo**, que es de donde viene la idea de agente.
  - **Ruta de representación (P23–P25)**: GloVe (2014), ELMo (2018) y T5 (2019). Completa la
    historia de cómo el lenguaje pasó de vectores estáticos a representaciones contextuales y de
    ahí a un formato único texto → texto.
  - **Ruta de agentes (P26–P33)**: DQN (2015), AlphaGo (2016), Chain-of-Thought (2022),
    Tree of Thoughts (2023), Reflexion (2023), Generative Agents (2023), Voyager (2023) y
    AutoGen (2023). Empieza en el refuerzo profundo y la búsqueda guiada, y llega al multiagente.
  - Los identificadores P01–P22 **no se tocan**. El catálogo pasa a declarar cuatro rutas y la
    validación comprueba que cada bloque esté en orden cronológico y que ningún paper quede fuera.
- **11 motores deterministas nuevos**, todos en Python estándar: factorización de co-ocurrencias,
  representación contextual, formato texto → texto, Q-learning con repetición de experiencia y
  red objetivo, búsqueda guiada por prior, aritmética de la cadena de pensamiento, búsqueda en
  árbol con poda, bucle de reflexión, recuperación de memoria puntuada, biblioteca de habilidades
  y conversación multiagente con crítico.
- **Tres afirmaciones corregidas antes de publicar**, porque no se sostenían contra su propia
  salida: el motor de cadena de pensamiento anunciaba un cruce en el número de pasos que con sus
  constantes no existía (el cruce real está en la fiabilidad **por paso**); el de AlphaGo
  insinuaba que el prior fallaba cuando también acertaba; y el de ELMo daba una separación de
  sentidos demasiado débil para la afirmación que hacía.
- **Frontera**: se documenta explícitamente que el criterio de ascenso (12 meses) es lo que fija
  el final del eje en 2025, y que lo posterior vive en `frontier/` con fecha.

## 0.5.0 — 2026-08-16

- **El eje de papers se amplía de 16 a 22 hitos y llega hasta 2025.** El eje se cortaba en 2023
  sin que ninguna regla lo justificara: el propio criterio de ascenso admite hasta 12 meses
  antes de la fecha de revisión. Se añaden dos cosas distintas —cobertura que faltaba y
  continuación temporal— organizadas en **dos rutas**:
  - **Ruta mínima (P01–P16)**, sin cambios: la cadena canónica donde cada paper resuelve lo que
    el anterior dejó abierto. Se estudia en orden. **No se renumeró nada**, para no romper
    enlaces, notebooks ni evaluaciones existentes.
  - **Ruta ampliada (P17–P22)**, nueva y ordenada por año:
    **P17 Difusión/DDPM** (Ho, Jain y Abbeel, 2020) cubre generativa, que el eje no tocaba;
    **P18 CLIP** (Radford et al., 2021) cubre multimodal;
    **P19 Leyes de escalado/Chinchilla** (Hoffmann et al., 2022) cubre la economía del cómputo;
    **P20 Mamba** (Gu y Dao, 2023 · COLM 2024) ataca el O(n²) que dejó abierto el Transformer;
    **P21 Mixtral** (Jiang et al., 2024) desacopla capacidad de cómputo;
    **P22 DeepSeek-R1** (DeepSeek-AI, 2025 · **Nature** 645, 633–638) cierra en el primer LLM de
    pesos abiertos publicado tras revisión por pares.
  - Los seis papers se verificaron **contra sus fuentes primarias** antes de escribir las fichas:
    título exacto, autoría, fecha de la v1 y afirmación central del resumen. Donde el resumen no
    nombraba un detalle —el algoritmo de refuerzo de P22, por ejemplo— la ficha dice «verificar
    en el cuerpo del artículo» en lugar de rellenarlo de memoria.
- **6 motores deterministas nuevos** (`diffusion`, `clip`, `scaling_laws`, `ssm`, `moe`,
  `rl_reasoning`), todos en Python estándar, y 6 notebooks con el contrato de 17 momentos.
  Cada afirmación pedagógica de sus salidas está comprobada por un test: que el SSM selectivo
  separe más que el invariante, que el balanceo baje el CV del router, que la política de RL
  suba exactitud **y** coste, que la difusión reconstruya con error < 1e-9.
- **5 anexos matemáticos** en [`papers/annexes/`](papers/annexes/README.md): álgebra y geometría,
  probabilidad y verosimilitud, cálculo y gradientes, la atención paso a paso con números, y
  complejidad/coste/escalado. Cada uno explica **qué es**, **por qué aparece**, **dónde se usa**,
  trae un **ejemplo resuelto a mano** y termina en el **error común**. Existen porque la sección 5
  de cada ficha es deliberadamente corta y las mismas herramientas reaparecen en todos los papers.
- **Ida y vuelta con las clases.** Las fichas ya enlazaban hacia las clases; ahora
  [`scripts/link_papers_to_classes.py`](scripts/link_papers_to_classes.py) inserta en las **27
  clases enlazadas** un bloque generado con sus papers, el año, qué desbloqueó cada uno y su
  notebook. Es idempotente, se regenera desde `papers.json` y `--check` lo verifica en CI, así
  que no puede desincronizarse.
- **Diagramas mermaid** en las seis fichas nuevas (proceso directo/inverso de difusión, el
  contraste imagen-texto de CLIP, el reparto de presupuesto de Chinchilla, puerta fija frente a
  selectiva en Mamba, el router top-2 de Mixtral, el bucle de recompensa verificable de
  DeepSeek-R1), en el hub del eje y en el anexo de gradientes.
- **Sitio**: 36 páginas del eje (antes 24), incluidas las de los anexos, y los enlaces de vuelta
  de las clases resueltos a sus páginas correspondientes. 235 páginas totales, 0 enlaces rotos.
- **Frontera**: tres entradas de investigación nuevas y fechadas —híbridos atención+SSM, escalar
  cómputo en inferencia y recompensas verificables fuera de código— que documentan explícitamente
  por qué **no** están en `foundational/`.

## 0.4.3 — 2026-08-16

- **Reparación de coherencia**: la versión se declaraba en cinco sitios y decían
  tres cosas distintas. `src/ai_evolution/__init__.py` y `apps/android/package.json`
  seguían en `0.3.0` mientras `pyproject.toml` iba por `0.4.2`, y el «About» de
  GitHub anunciaba `v0.3.0` con la última release publicada en `v0.2.0`. Todos
  sincronizados a `0.4.3`, y `VersionCoherenceTests` convierte la próxima
  divergencia en un fallo de CI en vez de en un hallazgo casual.
- **Corregidas afirmaciones falsas de la documentación:**
  - `ROADMAP.md` atribuía a 0.1.0 «15 partes y 183 clases · 549 notebooks»,
    cuando 0.1.0 entregó **180 clases y 540 notebooks** —las 183 y los 549
    llegaron en 0.3.0—. Reescrito con los conteos reales de cada versión.
  - El mismo roadmap planificaba «0.3 — track agéntico» y «0.4 — distribución»
    como futuro **no empezado**, cuando 0.3.0 y 0.4.x ya estaban publicadas con
    otro contenido. El trabajo pendiente se renumeró a 0.5, 0.6 y 0.7.
  - `docs/STUDENT_GUIDE.md` mandaba «leer README y theory», pero `theory.md` se
    eliminó del contrato en 0.2.0 y no existe en ninguna de las 183 clases.
  - `RECRUITER.md` y `docs/ARCHITECTURE.md` afirmaban «20 motores didácticos»:
    son **36** desde 0.4.0 (20 de clases + 16 de papers).
  - README y sitio decían «16 PDFs» y «549 notebooks»: son **17 PDFs** y
    **573 notebooks** (549 de clase + 24 de papers).
- **Documentación que faltaba**: ninguno de los ficheros de `docs/` mencionaba el
  eje de papers pese a llevar tres versiones en el repositorio.
  - `docs/ARCHITECTURE.md` documenta ahora las **dos** fuentes de verdad
    (`curriculum.yaml` y `papers/catalog/papers.json`), los módulos `papers.py` y
    `papers_lab.py`, la tabla de generadores y la regla de que lo generado no se
    edita a mano.
  - `docs/STUDENT_GUIDE.md` y `docs/INSTRUCTOR_GUIDE.md` incorporan la ruta de
    trabajo de un paper y la sesión de 90 minutos del eje.
  - `INSTALL.md` documenta los comandos del eje y cómo regenerar los PDFs;
    `CONTRIBUTING.md`, los criterios para proponer un paper nuevo.
  - `Makefile`: nuevos objetivos `papers`, `papers-check`, `pdf`, `pdf-papers` y
    `all-checks`; `site` ahora regenera antes de servir.

## 0.4.2 — 2026-08-16

- **Corrige el manifiesto del eje de papers, que dependía del sistema operativo.**
  El CI de 0.4.1 falló en los nueve trabajos de la matriz —Linux, macOS y Windows, tres
  versiones de Python— con 79 fallos, todos del mismo origen: los generadores escribían
  los artefactos con el salto de línea por defecto (CRLF en Windows), git los versionaba
  con LF y el hash del fichero crudo daba dos valores distintos para el mismo contenido.
  El contrato pasaba en la máquina donde se generó y fallaba en todas las demás.
  - `sha256_of()` normaliza CRLF a LF antes de hashear: el manifiesto certifica el
    **contenido**, no el fichero en un sistema operativo concreto. La clave pasa de
    `sha256` a **`sha256_lf`** para que nadie espere que `sha256sum` coincida sobre un
    fichero en CRLF, y el propio manifiesto lo documenta en el campo `hash`.
  - `scripts/generate_papers.py` y `scripts/generate_site.py` escriben siempre con LF
    (`newline="\n"`), de modo que el mismo comando produce el mismo artefacto en
    cualquier sistema.
  - Nuevo `.gitattributes` que fija LF en el repositorio y marca los binarios para que no
    se conviertan nunca.
  - Dos pruebas nuevas que habrían atrapado el fallo antes del push:
    `test_hash_does_not_depend_on_the_operating_system` comprueba que el mismo contenido
    en CRLF y en LF da el mismo hash, y `test_generated_artefacts_use_lf` verifica que
    ningún artefacto generado se versiona con CRLF.

## 0.4.1 — 2026-08-16

- **El eje de papers se publica**, no solo se versiona:
  - `scripts/generate_site.py` genera **24 páginas HTML** en `site/papers/` (hub, ruta,
    índice, 5 guías y 16 fichas) reescribiendo cada enlace relativo del repositorio a su
    equivalente del sitio; lo que no tiene página propia —notebooks, evaluaciones,
    `frontier/`— apunta al repositorio en lugar de romperse. Verificado: 0 enlaces locales
    rotos en las 24 páginas.
  - Nueva sección **📜 Papers fundacionales** en la portada del sitio, con 16 tarjetas
    generadas desde `site/data/papers.json` y alcanzables por el buscador existente.
  - `scripts/generate_pdfs.py --papers` produce
    **`docs/pdf/papers-fundacionales.pdf`** (155 páginas): portada con la ruta completa,
    las 5 guías, las 16 fichas y sus 16 evaluaciones, con los enlaces relativos convertidos
    a texto porque en papel no funcionan.
  - `pages.yml` comprueba `site/data/papers.json`, el hub, la ficha de P08 y una guía antes
    de desplegar; `service-worker.js` sube a `v4` y cachea `papers.json`.

## 0.4.0 — 2026-08-16

- **Eje de papers fundacionales** (`papers/`), la pieza que faltaba para que el mapa
  evolutivo se apoyara en fuentes primarias y no en narrativa retrospectiva. 16 hitos,
  de Rosenblatt (1958) a los sistemas agentic, cada uno con la misma secuencia:
  problema histórico → propuesta → intuición → matemática mínima → implementación →
  experimento → interpretación → limitaciones → siguiente hito.
  - **16 fichas** de 18 secciones obligatorias en `papers/foundational/`, con
    identificación completa (autoría, año, venue, URL y fecha de consulta), qué observar
    en el paper original con número de tabla o sección, límites que el paper admite y
    límites que no admite, errores comunes —incluidas las atribuciones anacrónicas—,
    actividades Bloom, autoevaluación y respuestas esperadas.
  - **24 notebooks ejecutables** en `notebooks/papers/`: uno por hito más **ocho
    miniaturas que desmontan *Attention Is All You Need*** pieza por pieza (recurrencia
    vs paralelismo, Q/K/V y producto escalar escalado, softmax y saturación,
    self-attention y máscara causal, multi-head, codificación posicional, residual +
    layer norm + feed-forward, y encoder–decoder con sus límites). Cada notebook cumple
    un contrato de 17 momentos que incluye **predicción antes de ejecutar**, anti-patrón
    deliberado y su corrección.
  - **16 motores deterministas** en `src/ai_evolution/papers_lab.py`: perceptrón,
    backpropagation con verificación numérica del gradiente, carrusel de error constante
    de la LSTM, convolución y equivarianza, skip-gram con muestreo negativo, cuello de
    botella del vector fijo, atención aditiva entrenada, atención escalada multi-cabeza,
    MLM bidireccional, aprendizaje en contexto, recuperación con citas, modelo de
    recompensa Bradley-Terry, bucle ReAct, filtrado por reducción de pérdida, pérdida
    DPO y bucle agentic con presupuesto. Python estándar: sin GPU, sin dependencias
    nuevas, sin APIs pagadas.
  - **5 guías** en `papers/guides/`: cómo leer un paper de IA, método de lectura en 5
    pasadas, plantilla de ficha, glosario del eje y **dónde vive la investigación**
    (arXiv y sus categorías, NeurIPS, ICML, ICLR, ACL Anthology, OpenReview, Semantic
    Scholar y Google Scholar), con la distinción explícita entre dónde se publica y
    dónde se busca.
  - **Aula completa generada**: guía docente con sesión de 90 minutos, ficha de estudio
    con checklist y bitácora, y evaluación con rúbrica A/B/C por paper, en
    `instructor/papers/`, `student/papers/` y `assessments/papers/`.
  - **4 prompts reutilizables** en `prompts/`: prompt maestro del eje, lectura crítica de
    un paper, verificación de claims y vigilancia de frontera.
- **Contrato verificado, no declarado**: `ai_evolution.papers.validate_papers()` comprueba
  las 18 secciones de cada ficha y su orden, los 17 momentos de cada notebook, `nbformat`,
  la existencia del motor, que cada paper tenga fuente primaria con URL, que las clases
  enlazadas existan y que los SHA-256 de `papers/manifest.json` estén al día. Se integra en
  `scripts/validate_repository.py --strict`.
- **Nuevos comandos**: `ai-evolution papers`, `ai-evolution paper <id>` y
  `ai-evolution paper-lab <id> --seed`.
- **Nuevo generador**: `scripts/generate_papers.py` (con `--check` para CI) produce índice,
  notebooks, artefactos de aula y manifiesto con SHA-256 a partir de `papers/catalog/papers.json`.
- **Tests**: `tests/test_papers.py` añade 24 pruebas, entre ellas un smoke test que **ejecuta
  todas las celdas de código de los 24 notebooks** y comprobaciones de que las afirmaciones
  pedagógicas se sostienen (la analogía `rey − hombre + mujer → reina` es estable en tres
  semillas; la atención escalada tiene más entropía que la no escalada; la máscara causal deja
  masa 0 sobre el futuro; el agente escala en vez de responder ante un fallo de herramienta).

## 0.3.0 — 2026-08-14

- **Tres clases nuevas de hardware en la parte 06**, el hueco que el programa
  arrastraba desde el inicio: se enseñaba a elegir y servir modelos sin explicar
  la máquina que fija el techo.
  - `081 Aceleradores, memoria y el límite real del cómputo`: jerarquía de
    memoria, intensidad aritmética y modelo roofline; por qué el decode con lote
    1 usa el 0,34 % del pico de cómputo de una H100; densa vs dispersa; MFU/MBU.
  - `082 Dimensionar hardware: de la laptop al clúster`: la ecuación
    `pesos + KV cache + activaciones + overhead`, bytes por parámetro por
    formato, coste real del fine-tuning frente a QLoRA, y los tres escalones de
    máquina — con IA local (llama.cpp, Ollama, LM Studio, MLX) como opción de
    primera clase.
  - `083 El ecosistema del cómputo: fabricantes, nubes y laboratorios`: las
    cuatro capas de la cadena de valor, CUDA como foso de software, apuestas
    alternativas (TPU, Trainium, MTIA, Maia, Groq, Cerebras), controles de
    exportación y residencia de datos, y el protocolo de cinco preguntas para
    leer una cifra de rendimiento.
- **Renumeración**: las clases 081–180 pasaron a 084–183 para abrir los tres
  huecos en su lugar pedagógico (antes de serving y cuantización). Las
  referencias de las versiones anteriores de este changelog conservan la
  numeración vigente entonces: para traducirlas, súmales 3 si son ≥ 081.
- Programa: **183 clases · 549 notebooks · 15 partes**; la parte 06 pasa de 12 a
  15 clases.
- Glosario ampliado con 8 términos de hardware (ancho de banda de memoria,
  cadena de valor del cómputo, CUDA/ROCm, HBM, intensidad aritmética, MFU/MBU,
  memoria unificada, presupuesto de memoria, roofline).
- Sitio, PDFs, catálogo JSON y app Android regenerados sobre la numeración nueva.

## 0.2.1 — 2026-08-13

- Actualización al vocabulario 2026 de ingenierías de IA: mapa de disciplinas
  (harness, loop, context, graph/flow, memory, eval engineering, SDD, AgentOps)
  en la clase 109 con correspondencia clase a clase.
- Harness engineering y la ecuación Agente = Modelo + Harness (clase 110);
  loop engineering con la arquitectura de cinco partes (clase 111).
- Context engineering como disciplina, context rot medible y LOCA-bench
  (clases 106 y 115); memory engineering y benchmarks de memoria (clase 105).
- Graph engineering (grafo explícito de estados) y catálogo canónico de
  patrones agénticos Ng/Anthropic (clase 121).
- Spec-driven development como contrato humano-agente (clase 175);
  evaluation-driven development nombrado (clase 119); AI gateways, registros
  y agent personas (clase 150).
- Glosario del programa reescrito: ~120 términos organizados por parte con
  enlace a la clase donde se desarrollan, enlazado desde el README raíz.
- Versión unificada en 0.2.1 (curriculum.yaml y ai_evolution.__version__
  arrastraban 0.1.0 frente a pyproject/README en 0.2.0).

## 0.2.0 — 2026-08-01

- Materia completa en las 180 clases: fundamentos, ejemplo trabajado a mano,
  tabla comparativa, diagrama mermaid del tema, errores conceptuales y
  referencias primarias verificables (libros canónicos, papers con DOI/arXiv
  y documentación oficial) integrados en el README de cada clase.
- 540 notebooks didácticos: resumen de materia, ejercicios concretos por tema
  y soluciones explicadas verificadas por ejecución.
- La teoría vive en el README de la clase (theory.md eliminado del contrato).
- GitHub Pages publica las 180 clases y 15 partes como páginas HTML con
  navegación anterior/siguiente, mermaid renderizado y evaluación integrada.
- PDFs imprimibles en docs/pdf/: uno por parte (15) y el programa completo
  (~1 100 páginas), generados desde la misma fuente markdown.
- Navegación anterior/siguiente con títulos completos en las 180 clases e
  iconos y diagramas en toda la documentación.

## 0.1.0 — 2026-07-29

- Programa maestro inicial con 15 partes y 180 clases.
- 540 notebooks diferenciados: recorrido, estudiante y solución.
- 180 entrypoints de laboratorios sobre 20 motores didácticos comprobables.
- PWA de estudio con búsqueda, filtros y progreso local.
- CLI, visor de escritorio, Docker, CI, seguridad y validación estructural.
- Catálogo de datasets públicos, especializaciones y frontera revisada por fecha.
- Trayectoria completa de agentes: fundamentos, tools, skills, MCP, A2A,
  multiagente, human-in-the-loop, evaluación, seguridad y AgentOps.
