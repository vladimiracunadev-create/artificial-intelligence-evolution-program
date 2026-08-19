
# 001 — Qué es inteligencia artificial y qué no es

> Inicio del programa · [Índice de la parte](../README.md) · [Clase siguiente →](../../../classes/part-00-foundations-history-and-scientific-method/002-de-turing-a-dartmouth-nacimiento-formal-del-campo/README.md)

**Parte:** 00 — Fundamentos, historia y método científico  
**Nivel:** fundamentos · **Horas estimadas:** 4  
**Laboratorio:** `frontier` · **Estado:** `EXECUTABLE_CORE`

## 🎯 Propósito

Comprender **qué es inteligencia artificial y qué no es** dentro de la evolución de la inteligencia
artificial, implementar un experimento mínimo verificable y distinguir qué parte
constituye evidencia frente a una afirmación todavía no comprobada.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. Explicar qué es inteligencia artificial y qué no es usando los conceptos `IA estrecha`, `IA general`, `automatización`, `autonomía`.
2. Ejecutar el laboratorio con una semilla explícita y revisar su contrato JSON.
3. Identificar al menos un supuesto, una limitación y un riesgo de aplicación.
4. Comparar el enfoque con la etapa anterior de la ruta de aprendizaje.
5. Producir una evidencia reproducible y una conclusión que no exceda los datos.

## 🧩 Conceptos centrales

`IA estrecha`, `IA general`, `automatización`, `autonomía`

## 🗺️ Ubicación en el mapa de la IA

Esta clase es el punto cero del programa: antes de estudiar algoritmos concretos hay que
acotar el objeto de estudio. La definición operativa de IA que se adopte aquí determina cómo
se leerán los hitos históricos (clase 002), los ciclos de expectativas (clase 003) y el marco
de agentes racionales (clase 004). Sin esta demarcación, cualquier sistema con un `if` puede
venderse como "inteligente" y cualquier promesa de "IA general" puede pasar sin escrutinio.

## 📖 Fundamentos

### 🎯 Cuatro definiciones clásicas de IA

Russell y Norvig (AIMA 4e, cap. 1) organizan las definiciones históricas de IA en una matriz
de dos ejes: **pensar vs. actuar** y **como humanos vs. racionalmente**:

| | Como humanos | Racionalmente |
|---|---|---|
| **Pensar** | Ciencia cognitiva: modelar la mente humana | Leyes del pensamiento: lógica formal |
| **Actuar** | Test de Turing: conducta indistinguible | Agente racional: maximizar una medida de desempeño |

El enfoque dominante hoy es el del **agente racional**: un sistema que percibe su entorno y
actúa para maximizar el valor esperado de una medida de desempeño, dadas las percepciones
disponibles y su conocimiento previo. Esta definición es *operativa*: no exige conciencia
ni "entendimiento", exige desempeño medible.

### 🔬 IA estrecha vs. IA general

- **IA estrecha (narrow AI / weak AI):** sistemas competentes en una tarea o dominio acotado
  (clasificar imágenes, traducir, jugar Go, completar texto). Todo sistema desplegado
  comercialmente hasta hoy pertenece a esta categoría. Su competencia **no transfiere**
  automáticamente fuera de la distribución de datos para la que fue construido.
- **IA general (AGI):** sistema hipotético con competencia comparable a la humana en la
  mayoría de tareas cognitivas económicamente relevantes, incluyendo transferencia entre
  dominios y aprendizaje con pocos datos. Es un objetivo de investigación, no un artefacto
  existente; cualquier afirmación de que un sistema actual "es AGI" debe tratarse como un
  claim extraordinario que exige evidencia extraordinaria.

Un error de categoría frecuente: la fluidez lingüística de un modelo generativo se percibe
como generalidad. Fluidez ≠ generalidad: la competencia debe evaluarse por tarea, con
distribuciones de prueba distintas a las de entrenamiento.

### ⚙️ Automatización vs. autonomía

Dos conceptos que el marketing mezcla y la ingeniería debe separar:

- **Automatización:** ejecutar sin intervención humana un procedimiento *especificado de
  antemano*. Una macro, un cron job o un pipeline ETL son automatización sin IA. El
  comportamiento es trazable a reglas escritas por personas.
- **Autonomía:** capacidad de un sistema para *seleccionar sus propias acciones* ante
  situaciones no enumeradas explícitamente por el diseñador, usando percepción y algún
  criterio de decisión. La autonomía admite grados (los niveles de conducción autónoma
  SAE 0-5 son el ejemplo canónico) y siempre está acotada por el dominio de operación
  diseñado (ODD, *operational design domain*).

Una prueba práctica de demarcación en tres preguntas:

```text
1. ¿El mapeo entrada→salida fue escrito a mano?        → automatización clásica
2. ¿El mapeo se indujo desde datos u optimización?     → aprendizaje automático (IA estrecha)
3. ¿El sistema decide qué acción tomar en situaciones
   no enumeradas, bajo una medida de desempeño?        → agente con autonomía (acotada)
```

### 🚫 Qué NO es IA (hoy)

- No es magia estadística sin supuestos: todo modelo hereda los sesgos y la cobertura de sus datos.
- No es conciencia ni intencionalidad: optimizar una función de pérdida no implica "querer".
- No es infalibilidad: los sistemas de IA fallan de formas distintas (y a veces más silenciosas)
  que el software clásico, porque su especificación es implícita en los datos.
- No es un sustituto de la especificación del problema: si la medida de desempeño está mal
  elegida, el sistema optimizará lo incorrecto con gran eficacia (ley de Goodhart).

## 🧮 Ejemplo trabajado

Clasifiquemos cuatro sistemas con la prueba de demarcación:

| Sistema | ¿Reglas a mano? | ¿Inducido de datos? | ¿Decide acciones? | Veredicto |
|---|---|---|---|---|
| Termostato on/off a 22 °C | Sí (umbral fijo) | No | No | Automatización, no IA |
| Filtro de spam bayesiano | No | Sí (frecuencias de palabras) | No (solo etiqueta) | IA estrecha (clasificador) |
| Robot aspirador que mapea la casa | Parcial | Sí (SLAM, percepción) | Sí (ruta, dentro de un ODD) | Agente con autonomía acotada |
| "Asistente AGI" anunciado en una demo | ? | ? | ? | Claim sin evidencia: exigir evaluación por tarea |

Traza numérica para el filtro de spam: con un corpus de 1 000 correos (200 spam), la palabra
"gratis" aparece en 120 spam y 40 legítimos. P("gratis") = 160/1000 = 0.16 y
P("gratis"|spam)·P(spam) = (120/200)·(200/1000) = 0.12. Por Bayes,
P(spam|"gratis") = 0.12/0.16 = **0.75**. El sistema no "entiende" el correo: computa
frecuencias. Eso es IA estrecha funcionando exactamente como fue diseñada — y también su límite.

## 📊 Propiedades y comparación

| Dimensión | Automatización clásica | IA estrecha | IA general (hipotética) |
|---|---|---|---|
| Origen del comportamiento | Reglas explícitas | Inducción desde datos | Transferencia entre dominios |
| Fallo típico | Caso no previsto → excepción | Cambio de distribución → error silencioso | — (no existe artefacto) |
| Auditabilidad | Alta (código legible) | Media-baja (pesos opacos) | Desconocida |
| Evidencia exigible | Tests unitarios | Evaluación fuera de distribución, baselines | Claim extraordinario |
| Estado en 2026 | Ubicua | Ubicua | Objetivo de investigación |

```mermaid
flowchart TD
    S["Sistema que 'parece inteligente'"] --> Q1{"¿Mapeo entrada→salida<br/>escrito a mano?"}
    Q1 -- "Sí" --> A["Automatización clásica<br/>(no es IA)"]
    Q1 -- "No" --> Q2{"¿Comportamiento inducido<br/>desde datos/optimización?"}
    Q2 -- "Sí" --> Q3{"¿Selecciona acciones en<br/>situaciones no enumeradas?"}
    Q2 -- "No" --> A
    Q3 -- "No" --> B["IA estrecha<br/>(percepción/predicción)"]
    Q3 -- "Sí" --> C["Agente con autonomía acotada<br/>(dentro de su ODD)"]
    C --> D{"¿Competencia transferible a<br/>la mayoría de dominios?"}
    D -- "Nadie lo ha demostrado" --> E["Claim de AGI:<br/>exigir evidencia por tarea"]
```

## ⚠️ Errores conceptuales frecuentes

1. **"Si usa un modelo grande, es inteligente en general."** La escala mejora el desempeño
   dentro de la distribución de entrenamiento; la generalidad se demuestra con evaluaciones
   por tarea fuera de esa distribución, no con fluidez aparente.
2. **"Automatizar con reglas ya es IA."** Un árbol de `if/else` escrito a mano es software
   determinista clásico; llamarlo IA infla expectativas y confunde la auditoría.
3. **"El sistema decidió solo, nadie es responsable."** La autonomía es siempre delegada y
   acotada por diseño; la responsabilidad permanece en quien define la medida de desempeño
   y el dominio de operación.
4. **"Pasar una conversación convincente demuestra pensamiento."** El propio Turing (1950)
   propuso el juego de imitación como *sustituto operativo* de la pregunta "¿pueden pensar
   las máquinas?", que consideró demasiado ambigua — no como prueba de conciencia.
5. **"La IA elimina el sesgo humano."** Un modelo entrenado con decisiones humanas históricas
   reproduce y a veces amplifica esos sesgos, con la agravante de parecer objetivo.

## 🚀 Del aprendizaje a la operación

Entre esta taxonomía y un sistema real median: la especificación formal del dominio de
operación (qué entradas son válidas y cuáles se rechazan), la medición continua del cambio
de distribución en producción, un baseline no-IA contra el cual justificar la complejidad
añadida, y un protocolo de escalamiento a revisión humana cuando la confianza del sistema
cae. Clasificar correctamente el sistema (automatización / IA estrecha / agente) determina
qué régimen de pruebas y auditoría le corresponde.

## 🧪 Laboratorio

```bash
python lab.py
```

El laboratorio llama a `ai_evolution.labs.run_lab("frontier")`. Esta
decisión evita 183 implementaciones divergentes: cada clase tiene un entrypoint
propio, pero los motores didácticos se prueban como una biblioteca común.

### 🔍 Evidencia esperada

- tipo de laboratorio y semilla;
- entradas o decisiones observables;
- resultado estructurado;
- lista `evidence` con hechos que pueden inspeccionarse;
- lista `limitations` que impide presentar la demo como producción.

## 📓 Notebooks

- [📓 `notebook.ipynb`](notebook.ipynb): recorrido guiado con la materia resumida.
- [✍️ `notebook_student.ipynb`](notebook_student.ipynb): ejercicios para resolver.
- [✅ `notebook_solution.ipynb`](notebook_solution.ipynb): solución de referencia explicada.

## 📝 Evaluación

| Criterio | Peso |
|---|---:|
| Comprensión conceptual | 25 % |
| Ejecución reproducible | 25 % |
| Interpretación basada en evidencia | 25 % |
| Riesgos, límites y mejora propuesta | 25 % |

Consulta [assessment.md](assessment.md) para preguntas y criterio de aceptación.

## ⚠️ Errores comunes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El código corre, pero no hay conclusión | Se confundió ejecución con aprendizaje | Explica qué demuestra y qué no demuestra |
| El resultado cambia sin explicación | No se registró semilla o configuración | Conserva semilla, versión y parámetros |
| Se promete uso real | Se extrapoló desde una demo educativa | Declara entorno, datos, límites y revisión humana |
| Se copia una métrica aislada | No existe baseline ni costo de error | Añade comparación y criterio de decisión |

## ❓ Preguntas frecuentes

**¿Debo usar una API comercial?**  
No. El núcleo funciona localmente. Las extensiones LIVE se documentan por separado.

**¿El laboratorio representa una implementación industrial?**  
No por sí solo. Enseña el contrato y el patrón; producción exige integración,
seguridad, observabilidad, pruebas y operación.

**¿Dónde profundizo?**  
Revisa las especializaciones enlazadas en el README raíz y la ruta siguiente.

## 🔗 Referencias

- [Turing, A. M. (1950). Computing Machinery and Intelligence. *Mind*, LIX(236)](https://doi.org/10.1093/mind/LIX.236.433) — uso: fuente primaria del mecanismo estudiado
- [McCarthy, Minsky, Rochester & Shannon (1955). A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence](http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf) — uso: referencia consultada en su fuente original
- [McCarthy, J. What is Artificial Intelligence?](http://jmc.stanford.edu/artificial-intelligence/what-is-ai/index.html) — uso: referencia consultada en su fuente original
- [Russell, S. & Norvig, P. *Artificial Intelligence: A Modern Approach*, 4.ª ed., cap. 1](https://aima.cs.berkeley.edu/) — uso: desarrollo extendido del tema
- [Nilsson, N. (2010). *The Quest for Artificial Intelligence* (PDF oficial gratuito)](https://ai.stanford.edu/~nilsson/QAI/qai.pdf) — uso: referencia consultada en su fuente original

<!-- papers:inicio -->

---

## 📜 Papers que fundamentan esta clase

> Bloque generado por `python scripts/link_papers_to_classes.py`. La fuente es [`papers/catalog/papers.json`](../../../papers/catalog/papers.json).

| Paper | Año | Qué desbloqueó | Miniatura |
|---|---:|---|---|
| [P54 · Un cálculo lógico de las ideas inmanentes en la actividad nerviosa](../../../papers/foundational/P54_mcculloch_pitts/README.md) | 1943 | Establece que una red de neuronas de umbral puede calcular cualquier función lógica: el puente entre biología y computación. | [notebook](../../../notebooks/papers/P54_mcculloch_pitts.ipynb) |
| [P56 · Maquinaria computacional e inteligencia](../../../papers/foundational/P56_turing/README.md) | 1950 | Cambia una pregunta metafísica —¿pueden pensar las máquinas?— por un procedimiento que se puede ejecutar y discutir. | [notebook](../../../notebooks/papers/P56_turing.ipynb) |

Cada ficha explica el problema anterior, la matemática mínima, los límites y los errores de atribución más frecuentes. Para leerlas con método: [cómo leer un paper de IA](../../../papers/guides/COMO_LEER_UN_PAPER_DE_IA.md) · [anexos matemáticos](../../../papers/annexes/README.md).
<!-- papers:fin -->
<!-- bibliografia:inicio -->

---

## 📚 Bibliografía de apoyo

> Bloque generado por `python scripts/link_sources_to_classes.py`. Cada obra lleva su localizador verificado en [`sources/bibliography.json`](../../../sources/bibliography.json).

Los papers dicen **de dónde salió** el mecanismo. Estas obras lo **desarrollan** con el espacio que una clase no tiene: teoría completa, demostraciones y ejercicios.

| Obra | Edición | Localizador | Papel en esta clase |
|---|---|---|---|
| Russell, Stuart J. y Norvig, Peter — *Artificial Intelligence: A Modern Approach* | 4.ª · 2020 | [ISBN 9780134610993](https://openlibrary.org/isbn/9780134610993) · [web de la obra](https://aima.cs.berkeley.edu/) | citada en las referencias de esta clase · cap. 1 · obra de referencia de la parte 00 |
<!-- bibliografia:fin -->

---

## ⬅️ Clase anterior

Esta es la primera clase del programa.

## ➡️ Siguiente clase

[002 — De Turing a Dartmouth: nacimiento formal del campo](../../part-00-foundations-history-and-scientific-method/002-de-turing-a-dartmouth-nacimiento-formal-del-campo/README.md)
