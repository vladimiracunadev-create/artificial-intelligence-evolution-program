# 📜 Changelog

Este proyecto sigue Versionado Semántico y conserva hechos históricos.

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
