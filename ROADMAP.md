# 🗺️ Roadmap

> Lo entregado se contrasta contra el [CHANGELOG](CHANGELOG.md) y contra el
> repositorio, no contra la memoria. Los conteos de cada versión son los que había
> **en esa versión**, no los de hoy.

## 📌 Estado actual

| Superficie | Verdad verificable |
|---|---|
| Versión | **0.9.1** (`pyproject.toml`, sincronizada en los cinco manifests) |
| Programa | 15 partes · 183 clases · 549 notebooks de clase |
| Eje de papers | 52 fichas · 60 notebooks · 52 motores · 5 anexos · 52 PDFs |
| Motores didácticos | 20 de clases + 52 de papers |
| PDFs | 69: 17 del programa (15 partes + completo + eje) y 52 individuales, uno por paper |
| Tests | 39 |

## ✅ 0.1.0 — Programa maestro inicial (entregado)

- [x] 15 partes y **180 clases**.
- [x] **540 notebooks** diferenciados: recorrido, estudiante y solución.
- [x] 180 entrypoints de laboratorio sobre 20 motores didácticos.
- [x] CLI, PWA, visor de escritorio y Docker.
- [x] Tests de estructura, contratos y motores.
- [x] Catálogo de datasets, especializaciones y frontera.

## ✅ 0.2.0 — Profundización pedagógica (entregado)

- [x] Materia completa en las 180 clases dentro del README de cada clase.
- [x] 540 notebooks con ejercicios y soluciones verificadas por ejecución.
- [x] Sitio de GitHub Pages con las clases navegables en HTML.
- [x] PDFs por parte y programa completo en `docs/pdf/`.
- [x] `theory.md` eliminado del contrato: la teoría vive en el README de la clase.

## ✅ 0.2.1 — Vocabulario 2026 (entregado)

- [x] Mapa de disciplinas: harness, loop, context, graph/flow, memory, eval
      engineering, SDD y AgentOps.
- [x] Glosario del programa con ~120 términos enlazados a su clase.

## ✅ 0.3.0 — Hardware de IA (entregado)

- [x] Tres clases nuevas en la parte 06: aceleradores y roofline, dimensionado
      de hardware, y ecosistema del cómputo.
- [x] Renumeración 081–183 y regeneración de sitio, PDFs, catálogo y app.
- [x] El programa pasa a **183 clases · 549 notebooks**.

## ✅ 0.4.x — Eje de papers fundacionales (entregado)

- [x] 16 fichas de 18 secciones, de Rosenblatt (1958) a los sistemas agentic.
- [x] 24 notebooks ejecutables, con 8 miniaturas que desmontan el Transformer.
- [x] 16 motores deterministas en Python estándar.
- [x] 5 guías de lectura crítica y 4 prompts reutilizables.
- [x] Guía docente, ficha de estudio y evaluación con rúbrica por paper.
- [x] 24 páginas del eje en el sitio y PDF imprimible de 155 páginas.
- [x] Contrato verificado por código: 18 secciones por ficha, 17 momentos por
      notebook, manifiesto con hash independiente del sistema operativo.

## ✅ 0.5.0 — Ampliación del eje de papers (entregado)

- [x] Ruta ampliada P17–P22: difusión, CLIP, leyes de escalado, Mamba, Mixtral y DeepSeek-R1.
- [x] 5 anexos matemáticos con ejemplos resueltos a mano.
- [x] Enlaces de vuelta clase → paper en 27 clases, generados y verificados.
- [x] Diagramas mermaid en las fichas nuevas y en el hub del eje.

## 🤖 Pendiente — Track agéntico aplicado

- [ ] Integraciones DEMO/LIVE con proveedores intercambiables.
- [ ] MCP server educativo de solo lectura.
- [ ] Persistencia SQLite/PostgreSQL para checkpoints.
- [ ] Evaluación de trayectorias y tool calls.
- [ ] Capstone con router, handoff, supervisor y aprobación humana.

## ✅ 0.6.0 — Representación y agentes (entregado)

- [x] Ruta de representación: GloVe, ELMo y T5.
- [x] Ruta de agentes: DQN, AlphaGo, Chain-of-Thought, Tree of Thoughts, Reflexion,
      Generative Agents, Voyager y AutoGen — incluido el hueco de refuerzo y el de multiagente.

## ✅ 0.7.0 — Memoria y contexto (entregado)

- [x] Bloque de memoria y contexto: RoPE, FlashAttention, *Lost in the Middle* y MemGPT.
- [x] P38 VAE abre el bloque de arquitectura y entrenamiento.
- [x] Índice unificado del eje: una tabla maestra por año, más vista temática.
- [x] Un PDF por paper, con portada que declara que no es el artículo original.

## ✅ 0.8.0 — El eje completo en 52 papers (entregado)

- [x] Las 14 fichas restantes (P39–P52): arquitectura y entrenamiento, evaluación y seguridad.
- [x] Rutas `ruta_arquitectura` (P38–P49) y `ruta_evaluacion` (P50–P52), cronológicas.
- [x] La sección de rutas de `papers/README.md` pasa a ser **generada**: ya no puede
      quedarse atrás respecto al catálogo.
- [x] Los anexos matemáticos entran en el PDF del eje, que su portada ya prometía.
- [x] Barrido de coherencia de toda la documentación, el sitio, los PDFs y el About.

## ✅ 0.9.0 — El eje conectado (entregado)

- [x] Puente matemático en las 52 fichas: apartados concretos de los anexos, con anclas verificadas.
- [x] Cobertura clase → paper de 50 a 81 clases (45 enlaces nuevos).
- [x] Enlaces del sitio a las fichas, que apuntaban a blobs de GitHub inexistentes.
- [x] La clase 010 enlaza el eje de papers y sus guías de lectura.

## 📦 Pendiente — Distribución

- [ ] Release de Windows firmado.
- [ ] App macOS y Linux empaquetada.
- [ ] PWA offline completa con bundles seleccionables.
- [ ] Material PPTX generado por parte y clase.

## 🧪 Sin versión asignada

- [ ] Reproducción parcial guiada de una figura real del Transformer.
- [ ] Traducción de las fichas al inglés.
- [ ] Rúbricas automáticas por familia de laboratorios.
- [ ] Quizzes pre/post y exportación de progreso.
- [ ] Ejecutar en CI una muestra rotativa de notebooks de clase.
- [ ] Glosario bilingüe ES/EN.

## 🧭 Principio

No se incorporará una tecnología a la ruta estable solo por popularidad. Debe
tener fuente primaria, propósito pedagógico, laboratorio o evidencia, límites
y fecha de revisión.
