
<div align="center">

# 🧠 Artificial Intelligence Evolution Program

## **15 partes · 183 clases · 52 papers fundacionales · de la IA simbólica a los sistemas agénticos**

**Programa evolutivo y verificable para comprender e implementar la historia completa
de la inteligencia artificial: lógica, búsqueda, sistemas expertos, probabilidad,
machine learning, redes neuronales, modelos fundacionales, IA generativa, RAG,
agentes, multiagentes, robótica, MLOps, seguridad y frontera.**

[![CI](https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program/actions/workflows/ci.yml)
[![Security](https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program/actions/workflows/security.yml/badge.svg?branch=main)](https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program/actions/workflows/security.yml)
[![Pages](https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program/actions/workflows/pages.yml/badge.svg?branch=main)](https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program/actions/workflows/pages.yml)

[![Version](https://img.shields.io/badge/version-0.10.0-orange?style=for-the-badge)](CHANGELOG.md)
[![Classes](https://img.shields.io/badge/classes-183%20·%2015%20partes-7c5cff?style=for-the-badge)](classes/)
[![Papers](https://img.shields.io/badge/papers-52%20fundacionales-c9184a?style=for-the-badge)](papers/README.md)
[![Notebooks](https://img.shields.io/badge/notebooks-609-2e8b57?style=for-the-badge)](classes/)
[![Nivel](https://img.shields.io/badge/nivel-fundamentos%20→%20frontera-8957e5?style=for-the-badge)](docs/LEARNING_PATH.md)
[![Idioma](https://img.shields.io/badge/idioma-español-1f6feb?style=for-the-badge)](classes/)
[![License](https://img.shields.io/badge/license-MIT-3fb950?style=for-the-badge)](LICENSE)

[![Python](https://img.shields.io/badge/Python-3.11%20·%203.12%20·%203.13-3776AB?style=flat-square&logo=python&logoColor=white)](pyproject.toml)
[![Jupyter](https://img.shields.io/badge/Jupyter-595%20notebooks-F37626?style=flat-square&logo=jupyter&logoColor=white)](classes/)
[![Docker](https://img.shields.io/badge/Docker-compose%20listo-2496ED?style=flat-square&logo=docker&logoColor=white)](compose.yaml)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-sitio%20vivo-222?style=flat-square&logo=githubpages&logoColor=white)](https://vladimiracunadev-create.github.io/artificial-intelligence-evolution-program/)

[🌐 **Sitio de estudio (vivo)**](https://vladimiracunadev-create.github.io/artificial-intelligence-evolution-program/) ·
[📜 Papers fundacionales](papers/README.md) ·
[🧭 Ruta](docs/LEARNING_PATH.md) ·
[🤖 Especialización en agentes](docs/AGENTIC_SYSTEMS_TRACK.md) ·
[📖 Glosario](docs/GLOSSARY.md) ·
[📕 PDFs](docs/pdf/) ·
[🏗️ Arquitectura](docs/ARCHITECTURE.md) ·
[🗺️ Roadmap](ROADMAP.md) ·
[🤝 Contribuir](CONTRIBUTING.md) ·
[🔐 Seguridad](SECURITY.md)

<br>

| 📘 Clases | 📓 Notebooks | 🧪 Laboratorios | 🧩 Partes | 📜 Papers | 🧰 Motores didácticos | 📕 PDFs |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **183** | **549 + 46** | **183** | **15** | **38** | **20 + 52** | **17 + 38** |

</div>

---

> [!IMPORTANT]
> Este repositorio **no reemplaza** los programas especializados. Es el mapa maestro
> de la evolución de la IA. `python-data-science-program`,
> `neural-network-training-labs`, `langgraph-realworld` y
> `claude-skills-toolkit` aparecen como rutas oficiales de profundización, sin copiar
> ni falsear su contenido.

## ✅ Estado verificable

| Superficie | Estado |
|---|---|
| Currículo | ✅ 183/183 clases documentadas |
| Papers | ✅ 52 fichas de 18 secciones + 60 notebooks + 52 motores + 5 anexos + un PDF por paper + enlaces de vuelta en 86 clases |
| Notebooks | ✅ 183 recorridos + 183 estudiantes + 183 soluciones |
| Laboratorios | ✅ 183 entrypoints que reutilizan 20 motores didácticos ejecutables |
| Datasets | ✅ catálogo de fuentes públicas reales; sin fallback sintético silencioso |
| CLI | ✅ `ai-evolution catalog`, `run`, `validate`, `frontier`, `progress`, `papers`, `paper`, `paper-lab` |
| Sitio | ✅ PWA estática, búsqueda, filtros, progreso local y 67 páginas del eje de papers |
| Escritorio | ✅ visor Tkinter local; workflow opcional para `.exe` |
| CI | ✅ estructura, notebooks, tests, compilación y seguridad básica |
| GPU / APIs pagadas | ⚪ extensiones opcionales; no se finge ejecución en CI |

## 🌟 Qué hace diferente a este programa

- Presenta los agentes como una etapa de la evolución de la IA, no como el inicio.
- Mantiene un **núcleo estable** y una **frontera revisable** con fecha y fuente.
- Cada clase incluye teoría, laboratorio, evaluación, errores comunes, FAQ y referencias.
- Diferencia claramente modelo, prompt, resource, tool, skill, workflow y agente.
- Usa código local y determinista para enseñar contratos antes de depender de APIs.
- No declara “producción” sin evidencia operativa, métricas y revisión humana.

## 🧬 El mapa evolutivo

```mermaid
flowchart LR
    A["📜 00 Fundamentos<br/>e historia"] --> B["♟️ 01 IA simbólica<br/>y búsqueda"]
    B --> C["🎲 02 Probabilística<br/>y evolutiva"]
    C --> D["📊 03 ML<br/>clásico"]
    D --> E["🧠 04 Deep<br/>learning"]
    E --> F["👁️ 05 Lenguaje, visión<br/>y multimodal"]
    F --> G["⚙️ 06 Modelos<br/>fundacionales"]
    G --> H["🎨 07 IA<br/>generativa"]
    G --> I["🔎 08 RAG, memoria<br/>y conocimiento"]
    H --> J["🤖 09 Agentes"]
    I --> J
    J --> K["🕸️ 10 Multiagentes<br/>e interop"]
    K --> L["🦾 11 Robótica y<br/>computer use"]
    K --> M["🛠️ 12 MLOps, LLMOps<br/>y AgentOps"]
    L --> N["🛡️ 13 Evaluación, seguridad<br/>y gobernanza"]
    M --> N
    N --> O["🔭 14 Frontera<br/>y capstones"]
```

## 🗂️ Las 15 partes, en 6 etapas evolutivas

Cada parte tiene su **propio README** con la secuencia de sus clases —12 en
todas, salvo la parte 06 que tiene 15. Las etapas siguen la evolución histórica
del campo: lo que cada una enseña es el prerrequisito real de la siguiente.

### 🟢 Etapa 1 — Fundamentos e IA clásica

La base que el resto del programa asume: método científico, búsqueda, lógica e
incertidumbre. **Salida: leer el campo con criterio, no con hype.**

| # | Parte | Clases | Nivel | Duración |
|---:|---|---:|---|---|
| 00 | [📜 Fundamentos, historia y método científico](classes/part-00-foundations-history-and-scientific-method/README.md) | 12 | fundamentos | 3–4 |
| 01 | [♟️ IA simbólica, búsqueda, lógica y planificación](classes/part-01-symbolic-ai-search-logic-and-planning/README.md) | 12 | fundamentos | 4–5 |
| 02 | [🎲 IA probabilística, evolutiva y de decisión](classes/part-02-probabilistic-evolutionary-and-decision-ai/README.md) | 12 | intermedio | 4–5 |

### 🔵 Etapa 2 — Aprendizaje automático y percepción

De las reglas escritas a los patrones aprendidos, y de los vectores a los
sentidos. **Salida: entrenar, diagnosticar y evaluar modelos con evidencia.**

| # | Parte | Clases | Nivel | Duración |
|---:|---|---:|---|---|
| 03 | [📊 Machine learning clásico](classes/part-03-classical-machine-learning/README.md) | 12 | intermedio | 5–6 |
| 04 | [🧠 Redes neuronales y deep learning](classes/part-04-neural-networks-and-deep-learning/README.md) | 12 | intermedio-avanzado | 6–8 |
| 05 | [👁️ Lenguaje, visión, audio e IA multimodal](classes/part-05-language-vision-audio-and-multimodal-ai/README.md) | 12 | avanzado | 5–6 |

### 🟣 Etapa 3 — Modelos fundacionales, generativa y conocimiento

El giro de 2020s: modelos preentrenados adaptables, generación en todos los
medios y sistemas que citan evidencia. **Salida: dimensionar el hardware que los
sostiene y construir servicios LLM con contratos, RAG auditable y memoria.**

| # | Parte | Clases | Nivel | Duración |
|---:|---|---:|---|---|
| 06 | [⚙️ Modelos fundacionales e ingeniería de LLM](classes/part-06-foundation-models-and-llm-engineering/README.md) | 15 | avanzado | 6–7 |
| 07 | [🎨 IA generativa para texto, imagen, audio, video y 3D](classes/part-07-generative-ai-across-media/README.md) | 12 | avanzado | 5–6 |
| 08 | [🔎 Recuperación, contexto, memoria y conocimiento](classes/part-08-retrieval-context-memory-and-knowledge/README.md) | 12 | avanzado | 5–6 |

### 🟠 Etapa 4 — Agentes: del modelo que responde al sistema que actúa

El modelo se convierte en componente de decisión de un sistema con
herramientas, permisos y presupuesto. **Salida: dominar las ingenierías de
agentes (harness, loop, graph, context) y la orquestación multiagente.**

| # | Parte | Clases | Nivel | Duración |
|---:|---|---:|---|---|
| 09 | [🤖 Ingeniería de agentes de IA](classes/part-09-ai-agent-engineering/README.md) | 12 | avanzado | 6–7 |
| 10 | [🕸️ Sistemas multiagente e interoperabilidad](classes/part-10-multi-agent-systems-and-interoperability/README.md) | 12 | experto | 6–7 |
| 11 | [🦾 IA encarnada, robótica y uso de computadores](classes/part-11-embodied-ai-robotics-and-computer-use/README.md) | 12 | experto | 5–6 |

### 🔴 Etapa 5 — Operación, evaluación y gobernanza

Lo que separa la demo del sistema en producción: observabilidad, evals como
gate, seguridad y cumplimiento. **Salida: operar IA con evidencia y responder
por ella.**

| # | Parte | Clases | Nivel | Duración |
|---:|---|---:|---|---|
| 12 | [🛠️ Ingeniería de IA, MLOps, LLMOps y AgentOps](classes/part-12-ai-engineering-mlops-llmops-and-agentops/README.md) | 12 | experto | 6–7 |
| 13 | [🛡️ Evaluación, seguridad y gobernanza](classes/part-13-evaluation-safety-security-and-governance/README.md) | 12 | experto | 6–7 |

### ⚫ Etapa 6 — Frontera y capstones

Investigación abierta con fecha y fuente, y el proyecto integrador que une las
14 partes anteriores. **Salida: vigilar la frontera sin perseguir modas.**

| # | Parte | Clases | Nivel | Duración |
|---:|---|---:|---|---|
| 14 | [🔭 Frontera, investigación y proyectos integradores](classes/part-14-frontier-research-and-capstones/README.md) | 12 | frontera | 8–12 |

## 📜 Eje de papers fundacionales

Las clases enseñan **qué** sabe hoy el campo. El [eje de papers](papers/README.md) enseña
**cómo llegó a saberlo**, leyendo las fuentes primarias y ejecutando una miniatura de cada
mecanismo. No es una colección de PDFs: cada hito sigue la misma secuencia.

```text
problema histórico → propuesta → intuición → matemática mínima →
implementación → experimento → interpretación → limitaciones → siguiente hito
```

La última flecha es la clave: **cada paper existe porque el anterior dejó algo sin resolver.**

```mermaid
flowchart LR
    A["🔵 1958-1986<br/>Perceptrón · Backprop"] --> B["🟢 1997-2014<br/>LSTM · AlexNet<br/>Word2Vec · Seq2Seq"]
    B --> C["🟡 2014-2017<br/>Attention · Transformer"]
    C --> D["🟠 2018-2020<br/>BERT · GPT-3 · RAG"]
    D --> E["🔴 2022-2023<br/>InstructGPT · ReAct<br/>Toolformer · DPO"]
    E --> F["⚫ 2023+<br/>Sistemas agentic"]
```

| Qué incluye | Detalle |
|---|---|
| 📄 **52 fichas** | 18 secciones obligatorias cada una: problema anterior, matemática mínima, qué observar en el paper original, límites, errores comunes, actividades Bloom y fuentes primarias con fecha de consulta |
| 📓 **60 notebooks** | 52 miniaturas + 8 que desmontan *Attention Is All You Need* pieza por pieza (Q/K/V, √d_k, máscara causal, multi-head, positional encoding, residual + layer norm, encoder–decoder) |
| 🧪 **52 motores** | Implementaciones deterministas en Python estándar: sin GPU, sin dependencias, sin APIs pagadas |
| 🧮 **5 anexos** | Toda la matemática del eje explicada una vez, con ejemplo resuelto a mano y su error común |
| 🔁 **Ida y vuelta** | Las 86 clases enlazadas llevan un bloque generado con sus papers: el circuito se cierra en ambos sentidos |
| 📚 **5 guías** | [Cómo leer un paper](papers/guides/COMO_LEER_UN_PAPER_DE_IA.md) · [método en 5 pasadas](papers/guides/METODO_DE_LECTURA_EN_5_PASADAS.md) · [dónde vive la investigación](papers/guides/FUENTES_Y_VENUES.md) · [plantilla de ficha](papers/guides/PLANTILLA_FICHA_PAPER.md) · [glosario](papers/guides/GLOSARIO_PAPERS_IA.md) |
| 🎓 **Niveles L0–L5** | De orientar sobre qué es un paper a leer la frontera con fecha y fuente |
| 👩‍🏫 **Aula completa** | [Guías docentes](instructor/papers/README.md), [fichas de estudio](student/papers/README.md) y [evaluaciones con rúbrica](assessments/papers/README.md) |

Reglas que el repositorio **verifica automáticamente**: no atribuir a un paper ideas
posteriores, no inventar autores, fechas, datasets ni métricas, registrar siempre venue y fecha
de consulta, y no redistribuir material con copyright — solo enlazar.

> [!TIP]
> La guía [dónde vive la investigación](papers/guides/FUENTES_Y_VENUES.md) explica la
> diferencia entre **dónde se publica** (arXiv, NeurIPS, ICML, ICLR, ACL Anthology) y **dónde
> se busca** (Google Scholar, Semantic Scholar), y por qué OpenReview es el sitio más
> infravalorado para aprender a leer con criterio.

## 🚀 Inicio rápido

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .

ai-evolution catalog
ai-evolution validate
ai-evolution run 001
ai-evolution frontier

ai-evolution papers              # los 16 hitos de la ruta
ai-evolution paper P08           # ficha de Attention Is All You Need
ai-evolution paper-lab P08       # ejecuta su miniatura
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

## 📕 PDFs del programa

El mismo contenido de las clases, listo para imprimir o leer offline
(generado desde la fuente markdown con `python scripts/generate_pdfs.py`):

- [📕 Programa completo (1 159 páginas)](docs/pdf/programa-completo.pdf)
- [📜 Papers fundacionales (451 páginas)](docs/pdf/papers-fundacionales.pdf) — las 52 fichas,
  las 5 guías, los 5 anexos matemáticos, la matriz clase ↔ paper y las 52 evaluaciones del eje
  (`python scripts/generate_pdfs.py --papers`)
- Por parte: [00](docs/pdf/parte-00.pdf) · [01](docs/pdf/parte-01.pdf) ·
  [02](docs/pdf/parte-02.pdf) · [03](docs/pdf/parte-03.pdf) ·
  [04](docs/pdf/parte-04.pdf) · [05](docs/pdf/parte-05.pdf) ·
  [06](docs/pdf/parte-06.pdf) · [07](docs/pdf/parte-07.pdf) ·
  [08](docs/pdf/parte-08.pdf) · [09](docs/pdf/parte-09.pdf) ·
  [10](docs/pdf/parte-10.pdf) · [11](docs/pdf/parte-11.pdf) ·
  [12](docs/pdf/parte-12.pdf) · [13](docs/pdf/parte-13.pdf) ·
  [14](docs/pdf/parte-14.pdf)

## 📦 Contrato de una clase

```text
classes/part-XX-slug/NNN-topic/
├── README.md        ← incluye la teoría completa de la clase
├── assessment.md
├── lesson.yaml
├── lab.py
├── notebook.ipynb
├── notebook_student.ipynb
└── notebook_solution.ipynb
```

## 📦 Contrato de un paper

```text
papers/
├── catalog/papers.json          ← fuente de verdad (16 entradas validadas)
├── catalog/sources.yaml         ← venues y repositorios primarios
├── foundational/PXX_slug/       ← ficha de 18 secciones
├── guides/                      ← cómo leer, 5 pasadas, plantilla, glosario, fuentes
└── manifest.json                ← inventario con SHA-256 (generado)

notebooks/papers/PXX_slug.ipynb  ← 17 momentos, del contexto al desafío autónomo
instructor/papers/PXX_slug.md    ← plan de sesión de 90 minutos
student/papers/PXX_slug.md       ← ruta de estudio y checklist
assessments/papers/PXX_slug.md   ← evaluación con rúbrica A/B/C
```

Regenerar y verificar el eje completo:

```bash
python scripts/generate_papers.py
python scripts/generate_papers.py --check
```

## 🔗 Especializaciones conectadas

| Especialización | Rol |
|---|---|
| [Python Data Science Program](https://github.com/vladimiracunadev-create/python-data-science-program) | Python, ML, estadística, MLOps y datos |
| [Neural Network Training Labs](https://github.com/vladimiracunadev-create/neural-network-training-labs) | Entrenamiento y despliegue profundo de redes neuronales |
| [LangGraph Realworld](https://github.com/vladimiracunadev-create/langgraph-realworld) | Casos empresariales de orquestación |
| [Claude Skills Toolkit](https://github.com/vladimiracunadev-create/claude-skills-toolkit) | Skills operativos reutilizables |

## ⚖️ Qué es y qué no es este programa

<table>
<tr>
<td valign="top" width="50%">

### ✅ Lo que sí es

- 🧬 un **mapa evolutivo completo** de la IA: 183 clases de la lógica simbólica a los sistemas agénticos, donde cada etapa explica la siguiente;
- 📜 un **eje de 52 papers fundacionales** que ancla ese mapa en sus fuentes primarias, de Rosenblatt (1958) a DeepSeek-R1 (2025), con bloques de representación, agentes y multiagente, con fichas verificables, miniaturas ejecutables y anexos matemáticos;
- 🧪 material **ejecutable y verificable**: 595 notebooks (549 de clase + 46 de papers), 183 laboratorios locales y 72 motores deterministas con contratos JSON que declaran `evidence` y `limitations`;
- 📖 contenido **abierto y gratuito en español**, legible en GitHub, en un sitio PWA instalable o en 69 PDFs imprimibles;
- 🗣️ un temario **alineado al vocabulario 2026** de la industria: harness, loop, graph, context engineering y compañía, con glosario propio;
- 🔍 material **honesto sobre sus límites**: cada laboratorio declara qué demuestra y qué no.

</td>
<td valign="top" width="50%">

### ❌ Lo que no es

- 🚫 una certificación: completar clases no acredita competencia clínica, financiera, legal ni de seguridad;
- 🚫 un curso de una sola API: los laboratorios base corren con Python estándar, sin claves ni servicios pagados;
- 🚫 entrenamiento a gran escala: los entrenamientos grandes, robots físicos y APIs comerciales exigen entornos externos;
- 🚫 conocimiento congelado: la carpeta `frontier/` registra lo emergente con fecha y fuente, sin presentarlo como estable;
- 🚫 un sustituto de la verificación: las licencias de datasets se revisan de nuevo al descargar cada versión concreta.

</td>
</tr>
</table>

## 💡 Idea fuerza

> El valor de este programa no está en acumular técnicas de IA, sino en
> **recorrer su evolución con evidencia**: cada clase produce un resultado
> reproducible, declara sus límites, y prepara exactamente lo que la siguiente
> etapa asume. Los agentes no son el inicio de la historia — son el capítulo
> que solo se entiende con los trece anteriores.

## 🧪 Calidad

```bash
python -m unittest discover -s tests -v
python -m compileall -q src scripts classes apps
python scripts/validate_repository.py --strict
```

## 📄 Licencia

Código y documentación original bajo [MIT](LICENSE). Datasets, papers, modelos y
servicios externos conservan sus propias licencias y términos.

---

<div align="center">

**Hecho para quien quiere entender la IA completa, no solo la última ola.**

[⬆️ Empezar por la clase 001](classes/part-00-foundations-history-and-scientific-method/001-que-es-inteligencia-artificial-y-que-no-es/README.md) ·
[🌐 Sitio de estudio](https://vladimiracunadev-create.github.io/artificial-intelligence-evolution-program/) ·
[📖 Glosario](docs/GLOSSARY.md) ·
[📕 Programa completo en PDF](docs/pdf/programa-completo.pdf) ·
[🗺️ Roadmap](ROADMAP.md)

<br>

**¿Te resulta útil? ⭐ Dale una estrella al repo.**

[![GitHub stars](https://img.shields.io/github/stars/vladimiracunadev-create/artificial-intelligence-evolution-program?style=social)](https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/vladimiracunadev-create/artificial-intelligence-evolution-program?style=social)](https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program/network/members)
[![Follow](https://img.shields.io/github/followers/vladimiracunadev-create?style=social&label=Follow)](https://github.com/vladimiracunadev-create)

Hecho con 🧠 y ☕ por [Vladimir Acuña](https://github.com/vladimiracunadev-create)

</div>
