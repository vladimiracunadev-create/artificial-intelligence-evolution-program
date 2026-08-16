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
