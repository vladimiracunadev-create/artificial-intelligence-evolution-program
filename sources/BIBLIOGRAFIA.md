# 📚 Bibliografía de apoyo del programa

> Fichero generado por `python scripts/verify-sources --write` desde
> [`bibliography.json`](bibliography.json) y [`support_map.json`](support_map.json).
> No se edita a mano.

Los [papers fundacionales](../papers/README.md) dicen **de dónde salió** cada idea.
Esta bibliografía dice **con qué se estudia**: la obra que desarrolla el contenido de
cada parte con el espacio que una clase no tiene.

## Obra de referencia por parte

### Parte 00 — Fundamentos, historia y método científico

- Russell, Stuart J. y Norvig, Peter — *Artificial Intelligence: A Modern Approach* · 4.ª · 2020 — [ISBN 9780134610993](https://openlibrary.org/isbn/9780134610993) · [web de la obra](https://aima.cs.berkeley.edu/)
  - **capítulos de introducción y de agentes racionales**: fija el objeto de estudio y el marco de agente, entorno y medida de desempeño con el que se lee todo el resto del programa

### Parte 01 — IA simbólica, búsqueda, lógica y planificación

- Russell, Stuart J. y Norvig, Peter — *Artificial Intelligence: A Modern Approach* · 4.ª · 2020 — [ISBN 9780134610993](https://openlibrary.org/isbn/9780134610993) · [web de la obra](https://aima.cs.berkeley.edu/)
  - **bloque de búsqueda, lógica y planificación**: desarrolla con demostraciones y ejercicios lo que aquí se implementa: espacios de estados, heurísticas admisibles, A*, CSP, lógica proposicional y de primer orden y planificación
- Nilsson, N. J. — *Principles of Artificial Intelligence* · 1980 — [ISBN 9780387113401](https://openlibrary.org/isbn/9780387113401)
  - **representación por espacios de estados**: el tratamiento clásico del que sale la formulación de problemas que usa la parte

### Parte 02 — IA probabilística, evolutiva y de decisión

- Russell, Stuart J. y Norvig, Peter — *Artificial Intelligence: A Modern Approach* · 4.ª · 2020 — [ISBN 9780134610993](https://openlibrary.org/isbn/9780134610993) · [web de la obra](https://aima.cs.berkeley.edu/)
  - **bloque de incertidumbre y decisión**: probabilidad, redes bayesianas, razonamiento temporal y teoría de la decisión con el nivel de detalle que la clase resume
- Koller, Daphne y Friedman, Nir — *Probabilistic Graphical Models: Principles and Techniques* · 2010 — [ISBN 9780262013192](https://openlibrary.org/isbn/9780262013192) · [web de la obra](https://mitpress.mit.edu/9780262013192/probabilistic-graphical-models/)
  - **modelos gráficos probabilísticos**: el tratado de referencia de representación, inferencia y aprendizaje en modelos gráficos
- Pearl, J. — *Probabilistic Reasoning in Intelligent Systems* · 1988 — [ISBN 9780080514895](https://openlibrary.org/isbn/9780080514895)
  - **redes de creencia**: la obra que introdujo las redes bayesianas y su propagación de evidencia

### Parte 03 — Machine learning clásico

- Hastie, Trevor, Tibshirani, Robert y Friedman, Jerome — *The Elements of Statistical Learning* · 2.ª · 2009 — [ISBN 9780387848570](https://openlibrary.org/isbn/9780387848570) · [web de la obra](https://hastie.su.domains/ElemStatLearn/)
  - **toda la parte**: el texto estándar de aprendizaje estadístico: sesgo-varianza, regularización, árboles, ensambles y validación
- James, Gareth et al. — *An Introduction to Statistical Learning* · 2021 — [ISBN 9783031387470](https://openlibrary.org/isbn/9783031387470) · [web de la obra](https://www.statlearning.com/)
  - **toda la parte, nivel introductorio**: la versión accesible del anterior, con ejercicios resueltos; sirve de entrada cuando la matemática de ESL pesa demasiado
- Murphy, Kevin P. — *Probabilistic Machine Learning* · 2022 — [ISBN 9780262046824](https://openlibrary.org/isbn/9780262046824) · [web de la obra](https://probml.github.io/pml-book/)
  - **fundamentos probabilísticos del aprendizaje**: unifica el ML clásico y el moderno bajo una misma notación probabilística

### Parte 04 — Redes neuronales y deep learning

- Goodfellow, Ian, Bengio, Yoshua y Courville, Aaron — *Deep Learning* · 2016 — [ISBN 9780262035613](https://openlibrary.org/isbn/9780262035613) · [web de la obra](https://www.deeplearningbook.org/)
  - **toda la parte**: el texto de referencia de redes neuronales: optimización, regularización, convolucionales, recurrentes y autoencoders
- Murphy, Kevin P. — *Probabilistic Machine Learning* · 2022 — [ISBN 9780262046824](https://openlibrary.org/isbn/9780262046824) · [web de la obra](https://probml.github.io/pml-book/)
  - **modelos profundos desde la probabilidad**: da el marco probabilístico de lo que el libro anterior presenta desde la optimización

### Parte 05 — Lenguaje, visión, audio e IA multimodal

- Jurafsky, Daniel y Martin, James H. — *Speech and Language Processing* · 2.ª (la 3.ª circula como borrador abierto sin ISBN) · 2009 — [ISBN 9780131873216](https://openlibrary.org/isbn/9780131873216) · [web de la obra](https://web.stanford.edu/~jurafsky/slp3/)
  - **lenguaje y habla**: el texto de referencia de procesamiento de lenguaje natural y voz, del n-grama al transformador

### Parte 06 — Modelos fundacionales e ingeniería de LLM

- Jurafsky, Daniel y Martin, James H. — *Speech and Language Processing* · 2.ª (la 3.ª circula como borrador abierto sin ISBN) · 2009 — [ISBN 9780131873216](https://openlibrary.org/isbn/9780131873216) · [web de la obra](https://web.stanford.edu/~jurafsky/slp3/)
  - **capítulos de modelos de lenguaje y transformadores**: desarrolla la mecánica de los modelos que esta parte pone a trabajar: tokenización, atención, preentrenamiento y ajuste
- Goodfellow, Ian, Bengio, Yoshua y Courville, Aaron — *Deep Learning* · 2016 — [ISBN 9780262035613](https://openlibrary.org/isbn/9780262035613) · [web de la obra](https://www.deeplearningbook.org/)
  - **optimización y entrenamiento a escala**: explica por qué el entrenamiento funciona —o no— cuando el modelo y los datos crecen

### Parte 07 — IA generativa para texto, imagen, audio, video y 3D

- Goodfellow, Ian, Bengio, Yoshua y Courville, Aaron — *Deep Learning* · 2016 — [ISBN 9780262035613](https://openlibrary.org/isbn/9780262035613) · [web de la obra](https://www.deeplearningbook.org/)
  - **capítulos de modelos generativos**: modelos generativos profundos, muestreo y evaluación de lo generado

### Parte 08 — Recuperación, contexto, memoria y conocimiento

- Manning, Christopher D., Raghavan, Prabhakar y Schütze, Hinrich — *Introduction to Information Retrieval* · 2008 — [ISBN 9780521865715](https://openlibrary.org/isbn/9780521865715) · [web de la obra](https://nlp.stanford.edu/IR-book/)
  - **toda la parte**: el texto de referencia de recuperación de información: índices, ponderación, evaluación y ranking, que es lo que hay debajo de cualquier RAG
- Jurafsky, Daniel y Martin, James H. — *Speech and Language Processing* · 2.ª (la 3.ª circula como borrador abierto sin ISBN) · 2009 — [ISBN 9780131873216](https://openlibrary.org/isbn/9780131873216) · [web de la obra](https://web.stanford.edu/~jurafsky/slp3/)
  - **representaciones vectoriales de significado**: de dónde salen los embeddings con los que se recupera

### Parte 09 — Ingeniería de agentes de IA

- Russell, Stuart J. y Norvig, Peter — *Artificial Intelligence: A Modern Approach* · 4.ª · 2020 — [ISBN 9780134610993](https://openlibrary.org/isbn/9780134610993) · [web de la obra](https://aima.cs.berkeley.edu/)
  - **capítulo de agentes racionales**: la definición de agente, entorno, sensores y actuadores que esta parte lleva a herramientas y bucles de ejecución
- Michael J. Wooldridge — *An Introduction to MultiAgent Systems* · 2009 — [ISBN 9780471496915](https://openlibrary.org/isbn/9780471496915)
  - **arquitecturas de agente**: arquitecturas deliberativas y reactivas, y qué compromete cada una

### Parte 10 — Sistemas multiagente e interoperabilidad

- Michael J. Wooldridge — *An Introduction to MultiAgent Systems* · 2009 — [ISBN 9780471496915](https://openlibrary.org/isbn/9780471496915)
  - **toda la parte**: el texto de referencia de sistemas multiagente: coordinación, negociación, protocolos y mecanismos
- Russell, Stuart J. y Norvig, Peter — *Artificial Intelligence: A Modern Approach* · 4.ª · 2020 — [ISBN 9780134610993](https://openlibrary.org/isbn/9780134610993) · [web de la obra](https://aima.cs.berkeley.edu/)
  - **decisión multiagente y teoría de juegos**: el marco formal de la interacción entre agentes con intereses propios

### Parte 11 — IA encarnada, robótica y uso de computadores

- Sebastian Thrun — *Probabilistic Robotics* · 2005 — [ISBN 9780262201629](https://openlibrary.org/isbn/9780262201629) · [web de la obra](https://mitpress.mit.edu/9780262201629/probabilistic-robotics/)
  - **toda la parte**: el texto de referencia de robótica probabilística: localización, mapeo y control bajo incertidumbre de sensores

### Parte 12 — Ingeniería de IA, MLOps, LLMOps y AgentOps

- Huyen, Chip — *Designing Machine Learning Systems* · 2022 — [ISBN 9781098107956](https://openlibrary.org/isbn/9781098107956) · [web de la obra](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) · _pendiente de confirmar en su catálogo_
  - **toda la parte**: el texto de referencia de sistemas de ML en producción: datos, despliegue, monitorización y deuda técnica

### Parte 13 — Evaluación, seguridad y gobernanza

- Huyen, Chip — *Designing Machine Learning Systems* · 2022 — [ISBN 9781098107956](https://openlibrary.org/isbn/9781098107956) · [web de la obra](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) · _pendiente de confirmar en su catálogo_
  - **capítulos de evaluación y monitorización**: cómo se mide un sistema en producción y qué se vigila cuando la distribución cambia
- Russell, Stuart J. y Norvig, Peter — *Artificial Intelligence: A Modern Approach* · 4.ª · 2020 — [ISBN 9780134610993](https://openlibrary.org/isbn/9780134610993) · [web de la obra](https://aima.cs.berkeley.edu/)
  - **capítulo de filosofía, ética y seguridad de la IA**: el tratamiento académico de los riesgos y límites que esta parte convierte en controles

### Parte 14 — Frontera, investigación y proyectos integradores

- Russell, Stuart J. y Norvig, Peter — *Artificial Intelligence: A Modern Approach* · 4.ª · 2020 — [ISBN 9780134610993](https://openlibrary.org/isbn/9780134610993) · [web de la obra](https://aima.cs.berkeley.edu/)
  - **capítulo sobre el futuro de la IA**: el marco con el que leer la frontera sin confundir promesa con resultado
- Goodfellow, Ian, Bengio, Yoshua y Courville, Aaron — *Deep Learning* · 2016 — [ISBN 9780262035613](https://openlibrary.org/isbn/9780262035613) · [web de la obra](https://www.deeplearningbook.org/)
  - **límites de los métodos actuales**: qué está resuelto y qué sigue abierto en el aprendizaje profundo

## Todas las obras que citan las clases

| Obra | Edición | Localizador | Clases |
|---|---|---|---:|
| Holland, J. H. — *Adaptation in Natural and Artificial Systems* | 1975 | [ISBN 9780262082136](https://openlibrary.org/isbn/9780262082136) | 1 |
| Michael J. Wooldridge — *An Introduction to MultiAgent Systems* | 2009 | [ISBN 9780471496915](https://openlibrary.org/isbn/9780471496915) | 4 |
| James, Gareth et al. — *An Introduction to Statistical Learning* | 2021 | [ISBN 9783031387470](https://openlibrary.org/isbn/9783031387470) · [web de la obra](https://www.statlearning.com/) | 5 |
| Dorigo, Marco y Stützle, Thomas — *Ant Colony Optimization (Bradford Books)* | 2004 | [ISBN 9780262042192](https://openlibrary.org/isbn/9780262042192) · [web de la obra](https://mitpress.mit.edu/9780262042192/ant-colony-optimization/) | 1 |
| Russell, Stuart J. y Norvig, Peter — *Artificial Intelligence: A Modern Approach* | 4.ª · 2020 | [ISBN 9780134610993](https://openlibrary.org/isbn/9780134610993) · [web de la obra](https://aima.cs.berkeley.edu/) | 39 |
| Spirtes, P., Glymour, C. y Scheines, R. — *Causation, Prediction, and Search* | 2000 | [ISBN 9781461227489](https://openlibrary.org/isbn/9781461227489) | 1 |
| Szeliski, Richard — *Computer Vision: Algorithms and Applications* | 2.ª · 2022 | [web de la obra](https://szeliski.org/Book/) · _pendiente de confirmar en su catálogo_ | 4 |
| Goodfellow, Ian, Bengio, Yoshua y Courville, Aaron — *Deep Learning* | 2016 | [ISBN 9780262035613](https://openlibrary.org/isbn/9780262035613) · [web de la obra](https://www.deeplearningbook.org/) | 15 |
| Huyen, Chip — *Designing Machine Learning Systems* | 2022 | [ISBN 9781098107956](https://openlibrary.org/isbn/9781098107956) · [web de la obra](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) · _pendiente de confirmar en su catálogo_ | 6 |
| Bellman, R. — *Dynamic Programming* | 1957 | [ISBN 9780691079516](https://openlibrary.org/isbn/9780691079516) | 1 |
| Peters, Jonas, Janzing, Dominik y Schölkopf, Bernhard — *Elements of Causal Inference* | 2017 | [ISBN 9780262037310](https://openlibrary.org/isbn/9780262037310) · [web de la obra](https://mitpress.mit.edu/9780262037310/elements-of-causal-inference/) | 1 |
| Ross, T. J. — *Fuzzy Logic with Engineering Applications* | 2010 | [ISBN 9780071136372](https://openlibrary.org/isbn/9780071136372) | 1 |
| Goldberg, D. E. — *Genetic Algorithms in Search, Optimization, and Machine Learning* | 1989 | [ISBN 9780201157673](https://openlibrary.org/isbn/9780201157673) | 1 |
| Rossi, F., van Beek, P. y Walsh, T. — *Handbook of Constraint Programming* | 2006 | [ISBN 9780444527264](https://openlibrary.org/isbn/9780444527264) | 1 |
| Biere, A. et al. — *Handbook of Satisfiability* | 2021 | [ISBN 9781643681603](https://openlibrary.org/isbn/9781643681603) | 1 |
| Pearl, J. — *Heuristics: Intelligent Search Strategies for Computer Problem Solving* | 1984 | _sin localizador verificado_ | 2 |
| Manning, Christopher D., Raghavan, Prabhakar y Schütze, Hinrich — *Introduction to Information Retrieval* | 2008 | [ISBN 9780521865715](https://openlibrary.org/isbn/9780521865715) · [web de la obra](https://nlp.stanford.edu/IR-book/) | 3 |
| Vygotsky, Lev S. — *Mind in society* | 1978 | [ISBN 9780674576292](https://openlibrary.org/isbn/9780674576292) · [web de la obra](https://www.hup.harvard.edu/books/9780674576292) | 1 |
| Meyer, Bertrand — *Object-Oriented Software Construction* | 1997 | [ISBN 9780136291558](https://openlibrary.org/isbn/9780136291558) | 1 |
| Nilsson, N. J. — *Principles of Artificial Intelligence* | 1980 | [ISBN 9780387113401](https://openlibrary.org/isbn/9780387113401) | 1 |
| Koller, Daphne y Friedman, Nir — *Probabilistic Graphical Models: Principles and Techniques* | 2010 | [ISBN 9780262013192](https://openlibrary.org/isbn/9780262013192) · [web de la obra](https://mitpress.mit.edu/9780262013192/probabilistic-graphical-models/) | 4 |
| Murphy, Kevin P. — *Probabilistic Machine Learning* | 2022 | [ISBN 9780262046824](https://openlibrary.org/isbn/9780262046824) · [web de la obra](https://probml.github.io/pml-book/) | 2 |
| Pearl, J. — *Probabilistic Reasoning in Intelligent Systems* | 1988 | [ISBN 9780080514895](https://openlibrary.org/isbn/9780080514895) | 2 |
| Sebastian Thrun — *Probabilistic Robotics* | 2005 | [ISBN 9780262201629](https://openlibrary.org/isbn/9780262201629) · [web de la obra](https://mitpress.mit.edu/9780262201629/probabilistic-robotics/) | 4 |
| Jaynes, E. T. — *Probability Theory: The Logic of Science* | 2003 | _sin localizador verificado_ | 1 |
| Sutton, Richard S. y Barto, Andrew G. — *Reinforcement Learning: An Introduction* | 2.ª · 2018 | [ISBN 9780262039246](https://openlibrary.org/isbn/9780262039246) · [web de la obra](http://incompleteideas.net/book/the-book-2nd.html) | 9 |
| Jurafsky, Daniel y Martin, James H. — *Speech and Language Processing* | 2.ª (la 3.ª circula como borrador abierto sin ISBN) · 2009 | [ISBN 9780131873216](https://openlibrary.org/isbn/9780131873216) · [web de la obra](https://web.stanford.edu/~jurafsky/slp3/) | 14 |
| Bonabeau, E., Dorigo, M. y Theraulaz, G. — *Swarm Intelligence: From Natural to Artificial Systems* | 1999 | _sin localizador verificado_ | 1 |
| Pearl, J. y Mackenzie, D. — *The Book of Why* | 2018 | [ISBN 9780465097609](https://openlibrary.org/isbn/9780465097609) | 2 |
| Baader y F. et al — *The Description Logic Handbook* | 2007 | [ISBN 9781280417993](https://openlibrary.org/isbn/9781280417993) | 1 |
| Hastie, Trevor, Tibshirani, Robert y Friedman, Jerome — *The Elements of Statistical Learning* | 2.ª · 2009 | [ISBN 9780387848570](https://openlibrary.org/isbn/9780387848570) · [web de la obra](https://hastie.su.domains/ElemStatLearn/) | 10 |
| Savage, L. J. — *The Foundations of Statistics* | 1954 | [ISBN 9780486623498](https://openlibrary.org/isbn/9780486623498) | 1 |
| von Neumann, J. y Morgenstern, O. — *Theory of Games and Economic Behavior* | 1944 | [ISBN 9781777257316](https://openlibrary.org/isbn/9781777257316) | 1 |
| Warden, P. y Situnayake, D. — *TinyML: Machine Learning with TensorFlow Lite on Arduino and Ultra-Low-Power Microcontrollers* | 2019 | _sin localizador verificado_ | 1 |

## Normas y especificaciones

| Norma | Versión | Fuente | Clases |
|---|---|---|---:|
| A2A Protocol | — | [A2A Protocol](https://a2a-protocol.org/latest/) | 3 |
| AI Risk Management Framework | 1.0 | [National Institute of Standards and Technology (NIST)](https://www.nist.gov/itl/ai-risk-management-framework) | 15 |
| c2pa.org/specifications | — | [Coalition for Content Provenance and Authenticity (C2PA)](https://c2pa.org/specifications/specifications/2.2/index.html) | 4 |
| Comisión Europea | — | [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | 1 |
| Computer Security Incident Handling Guide | 2 | [National Institute of Standards and Technology (NIST)](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final) | 1 |
| Especificación JSON Schema | — | [JSON Schema](https://json-schema.org) | 3 |
| Guidelines for Secure AI System Development | — | [Cybersecurity and Infrastructure Security Agency (CISA)](https://www.cisa.gov/resources-tools/resources/guidelines-secure-ai-system-development) | 1 |
| https://www.w3.org/TR/owl2-overview/ | — | [World Wide Web Consortium (W3C)](https://www.w3.org/TR/owl2-overview/) | 1 |
| https://www.w3.org/TR/rdf11-concepts/ | — | [World Wide Web Consortium (W3C)](https://www.w3.org/TR/rdf11-concepts/) | 1 |
| Idempotent Methods | — | [RFC Editor](https://www.rfc-editor.org/rfc/rfc9110.html#name-idempotent-methods) | 1 |
| ISO 10218-1:2025 | — | [International Organization for Standardization (ISO)](https://www.iso.org/standard/73933.html) | 1 |
| ISO 12100:2010 | — | [International Organization for Standardization (ISO)](https://www.iso.org/standard/51528.html) | 1 |
| ISO 31000:2018 | — | [International Organization for Standardization (ISO)](https://www.iso.org/standard/65694.html) | 1 |
| ISO/IEC 23894:2023 | 23894:2023 | [International Organization for Standardization (ISO)](https://www.iso.org/standard/77304.html) | 1 |
| ISO/TS 15066:2016 | — | [International Organization for Standardization (ISO)](https://www.iso.org/standard/62996.html) | 2 |
| JSON Schema | — | [JSON Schema](https://json-schema.org/specification) | 3 |
| MCP | 2025-06-18 | [Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18) | 1 |
| Model Context Protocol | — | [Model Context Protocol](https://modelcontextprotocol.io) | 12 |
| Model Context Protocol | — | [Model Context Protocol](https://modelcontextprotocol.io/specification) | 1 |
| Model Context Protocol | — | [Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18/server/tools) | 2 |
| NIST AI RMF 1.0 | 1.0 | [National Institute of Standards and Technology (NIST)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf) | 1 |
| nist.gov/cyberframework | — | [National Institute of Standards and Technology (NIST)](https://www.nist.gov/cyberframework) | 1 |
| NIST SP 800-218 / SBOM | — | [Cybersecurity and Infrastructure Security Agency (CISA)](https://www.cisa.gov/sbom) | 1 |
| OpenTelemetry | — | [OpenTelemetry (CNCF)](https://opentelemetry.io/docs/specs/semconv/gen-ai/) | 3 |
| OpenTelemetry Documentation | — | [OpenTelemetry (CNCF)](https://opentelemetry.io/docs/) | 5 |
| OWASP | — | [Open Worldwide Application Security Project (OWASP)](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) | 1 |
| OWASP Top 10 for LLM Applications | — | [Open Worldwide Application Security Project (OWASP)](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | 14 |
| Reglamento (UE) 2016/679 | 2016/679 | [Unión Europea — EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | 1 |
| Reglamento (UE) 2024/1689 | 2024/1689 | [Unión Europea — EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) | 3 |
| The OAuth 2.0 Authorization Framework | — | [RFC Editor](https://www.rfc-editor.org/rfc/rfc6749) | 1 |
| w3.org/TR/speech-synthesis11 | — | [World Wide Web Consortium (W3C)](https://www.w3.org/TR/speech-synthesis11/) | 1 |
| w3.org/TR/WCAG22 | — | [World Wide Web Consortium (W3C)](https://www.w3.org/TR/WCAG22/) | 1 |
| w3.org/WAI/fundamentals/accessibility-intro | — | [World Wide Web Consortium (W3C)](https://www.w3.org/WAI/fundamentals/accessibility-intro/) | 1 |
| W3C | — | [World Wide Web Consortium (W3C)](https://www.w3.org/TR/wai-aria-1.2/) | 1 |

## Estado del registro

- Obras registradas: **615** (34 libros, 344 artículos, 34 normas, 203 documentos de referencia).
- Con localizador resuelto contra su autoridad: **585**; pendientes con motivo declarado: **30**.
- Clases sin bibliografía de apoyo: **0**.
- Última resolución en red: **2026-08-19** (`python scripts/refresh-sources`).

El detalle por entrada, con el motivo de cada pendiente, está en
[`bibliography.json`](bibliography.json); el método, en [`README.md`](README.md).
