
<div align="center">

# 🧠 Artificial Intelligence Evolution Program

## **15 partes · 180 clases · 540 notebooks · de la IA simbólica a los sistemas agénticos**

**Programa evolutivo y verificable para comprender e implementar la historia completa
de la inteligencia artificial: lógica, búsqueda, sistemas expertos, probabilidad,
machine learning, redes neuronales, modelos fundacionales, IA generativa, RAG,
agentes, multiagentes, robótica, MLOps, seguridad y frontera.**

[![Version](https://img.shields.io/badge/version-0.1.0-orange?style=for-the-badge)](CHANGELOG.md)
[![Classes](https://img.shields.io/badge/classes-180-7c5cff?style=for-the-badge)](classes/)
[![Notebooks](https://img.shields.io/badge/notebooks-540-2e8b57?style=for-the-badge)](classes/)
[![Python](https://img.shields.io/badge/python-3.11%2B-3776ab?style=for-the-badge)](pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-3fb950?style=for-the-badge)](LICENSE)

[🌐 Sitio de estudio](site/index.html) · [🧭 Ruta](docs/LEARNING_PATH.md) ·
[🤖 Especialización en agentes](docs/AGENTIC_SYSTEMS_TRACK.md) ·
[🏗️ Arquitectura](docs/ARCHITECTURE.md) · [🗺️ Roadmap](ROADMAP.md)

</div>

---

> [!IMPORTANT]
> Este repositorio **no reemplaza** los programas especializados. Es el mapa maestro
> de la evolución de la IA. `python-data-science-program`,
> `neural-network-training-labs`, `langgraph-realworld` y
> `claude-skills-toolkit` aparecen como rutas oficiales de profundización, sin copiar
> ni falsear su contenido.

## Estado verificable

| Superficie | Estado |
|---|---|
| Currículo | ✅ 180/180 clases documentadas |
| Notebooks | ✅ 180 recorridos + 180 estudiantes + 180 soluciones |
| Laboratorios | ✅ 180 entrypoints que reutilizan 20 motores didácticos ejecutables |
| Datasets | ✅ catálogo de fuentes públicas reales; sin fallback sintético silencioso |
| CLI | ✅ `ai-evolution catalog`, `run`, `validate`, `frontier`, `progress` |
| Sitio | ✅ PWA estática, búsqueda, filtros y progreso local |
| Escritorio | ✅ visor Tkinter local; workflow opcional para `.exe` |
| CI | ✅ estructura, notebooks, tests, compilación y seguridad básica |
| GPU / APIs pagadas | ⚪ extensiones opcionales; no se finge ejecución en CI |

## Qué hace diferente a este programa

- Presenta los agentes como una etapa de la evolución de la IA, no como el inicio.
- Mantiene un **núcleo estable** y una **frontera revisable** con fecha y fuente.
- Cada clase incluye teoría, laboratorio, evaluación, errores comunes, FAQ y referencias.
- Diferencia claramente modelo, prompt, resource, tool, skill, workflow y agente.
- Usa código local y determinista para enseñar contratos antes de depender de APIs.
- No declara “producción” sin evidencia operativa, métricas y revisión humana.

## Partes del programa

| # | Parte | Clases | Nivel | Duración |
|---:|---|---:|---|---|
| 00 | [Fundamentos, historia y método científico](classes/part-00-foundations-history-and-scientific-method/README.md) | 12 | fundamentos | 3–4 |
| 01 | [IA simbólica, búsqueda, lógica y planificación](classes/part-01-symbolic-ai-search-logic-and-planning/README.md) | 12 | fundamentos | 4–5 |
| 02 | [IA probabilística, evolutiva y de decisión](classes/part-02-probabilistic-evolutionary-and-decision-ai/README.md) | 12 | intermedio | 4–5 |
| 03 | [Machine learning clásico](classes/part-03-classical-machine-learning/README.md) | 12 | intermedio | 5–6 |
| 04 | [Redes neuronales y deep learning](classes/part-04-neural-networks-and-deep-learning/README.md) | 12 | intermedio-avanzado | 6–8 |
| 05 | [Lenguaje, visión, audio e IA multimodal](classes/part-05-language-vision-audio-and-multimodal-ai/README.md) | 12 | avanzado | 5–6 |
| 06 | [Modelos fundacionales e ingeniería de LLM](classes/part-06-foundation-models-and-llm-engineering/README.md) | 12 | avanzado | 6–7 |
| 07 | [IA generativa para texto, imagen, audio, video y 3D](classes/part-07-generative-ai-across-media/README.md) | 12 | avanzado | 5–6 |
| 08 | [Recuperación, contexto, memoria y conocimiento](classes/part-08-retrieval-context-memory-and-knowledge/README.md) | 12 | avanzado | 5–6 |
| 09 | [Ingeniería de agentes de IA](classes/part-09-ai-agent-engineering/README.md) | 12 | avanzado | 6–7 |
| 10 | [Sistemas multiagente e interoperabilidad](classes/part-10-multi-agent-systems-and-interoperability/README.md) | 12 | experto | 6–7 |
| 11 | [IA encarnada, robótica y uso de computadores](classes/part-11-embodied-ai-robotics-and-computer-use/README.md) | 12 | experto | 5–6 |
| 12 | [Ingeniería de IA, MLOps, LLMOps y AgentOps](classes/part-12-ai-engineering-mlops-llmops-and-agentops/README.md) | 12 | experto | 6–7 |
| 13 | [Evaluación, seguridad y gobernanza](classes/part-13-evaluation-safety-security-and-governance/README.md) | 12 | experto | 6–7 |
| 14 | [Frontera, investigación y proyectos integradores](classes/part-14-frontier-research-and-capstones/README.md) | 12 | frontera | 8–12 |

## Inicio rápido

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .

ai-evolution catalog
ai-evolution validate
ai-evolution run 001
ai-evolution frontier
```

Sin instalar el paquete:

```bash
python scripts/validate_repository.py
python classes/part-01-symbolic-ai-search-logic-and-planning/013-espacios-de-estados-y-formulacion-de-problemas/lab.py
```

Sitio local:

```bash
python -m http.server 8080
```

Abre `http://localhost:8080/site/`.

## Contrato de una clase

```text
classes/part-XX-slug/NNN-topic/
├── README.md
├── theory.md
├── assessment.md
├── lesson.yaml
├── lab.py
├── notebook.ipynb
├── notebook_student.ipynb
└── notebook_solution.ipynb
```

## Especializaciones conectadas

| Especialización | Rol |
|---|---|
| [Python Data Science Program](https://github.com/vladimiracunadev-create/python-data-science-program) | Python, ML, estadística, MLOps y datos |
| [Neural Network Training Labs](https://github.com/vladimiracunadev-create/neural-network-training-labs) | Entrenamiento y despliegue profundo de redes neuronales |
| [LangGraph Realworld](https://github.com/vladimiracunadev-create/langgraph-realworld) | Casos empresariales de orquestación |
| [Claude Skills Toolkit](https://github.com/vladimiracunadev-create/claude-skills-toolkit) | Skills operativos reutilizables |

## Límites honestos

- Los laboratorios base priorizan ejecución reproducible con Python estándar.
- Los entrenamientos grandes, robots físicos y APIs comerciales requieren entornos externos.
- Un caso educativo no equivale a certificación clínica, financiera, legal o de seguridad.
- La carpeta `frontier/` registra tecnología emergente; no la presenta como conocimiento estable.
- Las licencias de datasets deben revisarse nuevamente al descargar una versión concreta.

## Calidad

```bash
python -m unittest discover -s tests -v
python -m compileall -q src scripts classes apps
python scripts/validate_repository.py --strict
```

## Licencia

Código y documentación original bajo [MIT](LICENSE). Datasets, papers, modelos y
servicios externos conservan sus propias licencias y términos.
