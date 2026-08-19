# ⏱️ Guía rápida para evaluación técnica

Este repositorio demuestra:

- diseño curricular de 183 clases en 15 partes;
- comprensión de la evolución completa de la IA, anclada en 148 papers
  fundacionales leídos en su fuente primaria;
- separación entre modelos, tools, skills, workflows y agentes;
- 168 motores didácticos reutilizables con contratos uniformes (20 de clase + 148 de papers)
  (20 de clases + 16 de papers), deterministas y sin dependencias;
- contratos verificados por código, no declarados: 18 secciones por ficha,
  17 momentos por notebook y un manifiesto con hash por artefacto;
- pruebas de estructura, notebooks, CLI, PWA y aplicación local;
- documentación de seguridad, evaluación, datos y límites.

## 🚀 Ruta de 10 minutos

1. `README.md`
2. `docs/ARCHITECTURE.md`
3. `papers/foundational/P08_transformer/README.md` — la ficha del Transformer,
   incluida la sección «qué **no** significa el título»
4. `src/ai_evolution/papers_lab.py` — 16 mecanismos en Python estándar
5. `docs/AGENTIC_SYSTEMS_TRACK.md`
6. `src/ai_evolution/labs.py`
7. `tests/test_papers.py` — incluye un smoke test que ejecuta las celdas de los
   156 notebooks del eje
8. `site/index.html`

El repositorio no afirma que los ejemplos educativos sean despliegues
empresariales. Esa separación es deliberada.
