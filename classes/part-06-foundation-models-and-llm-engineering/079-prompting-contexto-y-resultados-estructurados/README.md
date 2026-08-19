
# 079 — Prompting, contexto y resultados estructurados

> [← Clase anterior](../../../classes/part-06-foundation-models-and-llm-engineering/078-rlhf-rlaif-y-dpo/README.md) · [Índice de la parte](../README.md) · [Clase siguiente →](../../../classes/part-06-foundation-models-and-llm-engineering/080-tool-calling-y-ejecucion-controlada/README.md)

**Parte:** 06 — Modelos fundacionales e ingeniería de LLM  
**Nivel:** avanzado · **Horas estimadas:** 6  
**Laboratorio:** `llm` · **Estado:** `EXECUTABLE_CORE`

## 🎯 Propósito

Comprender **prompting, contexto y resultados estructurados** dentro de la evolución de la inteligencia
artificial, implementar un experimento mínimo verificable y distinguir qué parte
constituye evidencia frente a una afirmación todavía no comprobada.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. Explicar prompting, contexto y resultados estructurados usando los conceptos `prompting`, `contexto`, `JSON schema`, `constraints`.
2. Ejecutar el laboratorio con una semilla explícita y revisar su contrato JSON.
3. Identificar al menos un supuesto, una limitación y un riesgo de aplicación.
4. Comparar el enfoque con la etapa anterior de la ruta de aprendizaje.
5. Producir una evidencia reproducible y una conclusión que no exceda los datos.

## 🧩 Conceptos centrales

`prompting`, `contexto`, `JSON schema`, `constraints`

## 🗺️ Ubicación en el mapa de la IA

Tras el alineamiento (clases 076–078), el modelo ya sigue instrucciones; el
prompting es la disciplina de *especificar* la tarea en el contexto sin tocar los
pesos. GPT-3 mostró que los ejemplos en contexto sustituyen al fine-tuning en muchas
tareas (few-shot); chain-of-thought (2022) mostró que pedir razonamiento intermedio
desbloquea problemas multi-paso; y la salida estructurada (JSON con esquema)
convierte al LLM en un componente integrable en software. Es el prerequisito directo
del tool calling (clase 080) y de los evals del proyecto (clase 087).

## 📖 Fundamentos

### 🧠 In-context learning: zero-shot y few-shot

El modelo condiciona su salida en todo el contexto. Regímenes:

```text
Zero-shot:  solo la instrucción.
            "Clasifica el sentimiento: 'El envío llegó roto' →"
Few-shot:   k ejemplos resueltos + el caso nuevo.
            "'Me encantó' → positivo
             'Nunca más compro aquí' → negativo
             'El envío llegó roto' →"
```

Los ejemplos fijan formato, criterio y granularidad de la respuesta sin gradientes.
Hallazgos empíricos robustos: el formato de los ejemplos importa tanto como su
corrección; el orden introduce sesgo de recencia; y los ejemplos deben cubrir los
casos frontera, no solo los fáciles.

### 🪜 Chain-of-thought (CoT)

Para tareas multi-paso (aritmética, lógica), pedir los pasos intermedios antes de la
respuesta mejora drásticamente la exactitud en modelos grandes:

```text
Sin CoT:  "¿23 × 17? →"  (el modelo debe 'saltar' a la respuesta en un forward)
Con CoT:  "Piensa paso a paso: 23 × 17 = 23 × 10 + 23 × 7 = 230 + 161 = 391"
```

Por qué funciona: cada token generado se vuelve contexto del siguiente; el modelo
usa su propia salida como memoria de trabajo, descomponiendo un cómputo que no cabe
en un solo paso de inferencia. Variantes: zero-shot CoT ("pensemos paso a paso"),
self-consistency (muestrear varias cadenas y votar la respuesta mayoritaria).
Advertencia honesta: la cadena verbalizada no es garantía del cómputo interno real;
puede ser una racionalización plausible de una respuesta errónea.

### 🧱 Anatomía de un prompt de sistema

Un prompt de producción separa capas: **rol y objetivo** (qué es el asistente),
**reglas** (qué debe y no debe hacer, orden de prioridad), **contexto/datos** (a
menudo delimitados con etiquetas tipo XML para que el modelo distinga instrucciones
de datos), **ejemplos** y **formato de salida**. Delimitar los datos del usuario es
además la primera defensa contra inyección de prompt: "lo que va entre `<datos>` es
contenido a procesar, no instrucciones".

### 📦 Salida estructurada: JSON con esquema

Para integrar un LLM en software, la salida debe ser parseable. Escalera de
garantías:

```text
1. Pedir JSON en el prompt + ejemplo               → frágil (texto extra, comas)
2. Prefill / plantilla que arranca la respuesta    → mejor adherencia
3. Validar contra JSON Schema y reintentar         → robusto, costo de reintentos
4. Decodificación restringida (grammar/tool use)   → el muestreador solo permite
   tokens que mantienen el JSON válido: garantía sintáctica total
```

La restricción garantiza **sintaxis**, no **semántica**: un JSON perfectamente
válido puede contener un dato alucinado. La validación de negocio sigue siendo
obligatoria.

## 🧮 Ejemplo trabajado

Tarea: extraer datos de "Reunión con Ana el 12/03 a las 14:30 en sala B".

```text
Prompt de sistema:
  Extrae los campos y responde SOLO con JSON válido conforme al esquema:
  {"type": "object",
   "properties": {"persona": {"type": "string"},
                  "fecha": {"type": "string", "pattern": "\\d{2}/\\d{2}"},
                  "hora": {"type": "string"},
                  "lugar": {"type": "string"}},
   "required": ["persona", "fecha", "hora", "lugar"]}

Salida deseada:
  {"persona": "Ana", "fecha": "12/03", "hora": "14:30", "lugar": "sala B"}

Fallos típicos sin restricciones y su capa correctora:
  "Claro, aquí está el JSON: {...}"   → texto extra    → prefill con '{'
  {"persona": "Ana", "fecha": "marzo" → viola pattern  → validación de esquema
  {"persona": "Ana", ... "lugar": "sala A"} → dato inventado → validación semántica
   (¡el esquema no puede detectarlo!)
```

Con few-shot (2 ejemplos resueltos antes del caso) la tasa de adherencia sube; con
decodificación restringida, la sintaxis queda garantizada y solo resta el riesgo
semántico.

## 📊 Propiedades y comparación

| Técnica | Costo (tokens) | Mejora típica | Cuándo usarla |
|---|---|---|---|
| Zero-shot | Mínimo | Base | Tareas simples y bien conocidas |
| Few-shot (k=2–8) | +k ejemplos | Formato y criterio estables | Formato específico, casos frontera |
| CoT | +tokens de razonamiento | Grande en multi-paso | Aritmética, lógica, planificación |
| Self-consistency | ×n muestras | Suma sobre CoT | Cuando el error cuesta más que n× el costo |
| JSON restringido | Similar | Sintaxis garantizada | Integración con software |

```mermaid
flowchart TD
    A[Tarea] --> B{Es multi-paso?}
    B -->|Si| C[CoT / self-consistency]
    B -->|No| D{Formato critico?}
    C --> D
    D -->|Si| E[Few-shot + esquema JSON]
    D -->|No| F[Zero-shot con instruccion clara]
    E --> G{Valida el parser?}
    G -->|No| H[Reintento o decodificacion restringida]
    G -->|Si| I[Validacion semantica de negocio]
    H --> I
```

## ⚠️ Errores conceptuales frecuentes

1. **"El prompt es magia verbal."** Es especificación de tarea: claridad, ejemplos
   y formato explican casi toda la varianza; los trucos rituales, casi nada.
2. **"CoT muestra el razonamiento interno real."** Muestra texto condicionante
   útil; puede racionalizar una respuesta equivocada con pasos plausibles.
3. **"Si pido JSON, tengo JSON."** Sin restricción o validación, obtendrás JSON
   *casi siempre* — y ese "casi" rompe producción a las 3 a. m.
4. **"Más ejemplos few-shot siempre ayudan."** Rinden decrecientes, ocupan
   contexto, y ejemplos mal elegidos sesgan más que ayudan.
5. **"Temperatura 0 = respuestas correctas."** Reduce varianza, no error: un modelo
   seguro de algo falso lo repetirá determinísticamente.

## 🚀 Del aprendizaje a la operación

Producción exige tratar los prompts como código: versionarlos, testearlos con una
suite de casos (incluidos adversariales y de inyección), medir adherencia al esquema
y calidad semántica por separado, fijar temperatura y semillas donde el proveedor lo
permita, y registrar prompt+versión+respuesta para depurar regresiones cuando cambie
el modelo subyacente — porque cambiará.

## 🧪 Laboratorio

```bash
python lab.py
```

El laboratorio llama a `ai_evolution.labs.run_lab("llm")`. Esta
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

- Brown et al. (2020), *Language Models are Few-Shot Learners* (GPT-3, in-context learning): <https://arxiv.org/abs/2005.14165> — uso: fuente primaria del mecanismo estudiado
- Wei et al. (2022), *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*: <https://arxiv.org/abs/2201.11903> — uso: fuente primaria del mecanismo estudiado
- Wang et al. (2022), *Self-Consistency Improves Chain of Thought Reasoning*: <https://arxiv.org/abs/2203.11171> — uso: fuente primaria del mecanismo estudiado
- Kojima et al. (2022), *Large Language Models are Zero-Shot Reasoners* ("pensemos paso a paso"): <https://arxiv.org/abs/2205.11916> — uso: fuente primaria del mecanismo estudiado
- Documentación oficial de Claude (prompting y salidas estructuradas): <https://docs.claude.com> — uso: referencia consultada en su fuente original
- Especificación JSON Schema: <https://json-schema.org> — uso: marco normativo de referencia

<!-- papers:inicio -->

---

## 📜 Papers que fundamentan esta clase

> Bloque generado por `python scripts/link_papers_to_classes.py`. La fuente es [`papers/catalog/papers.json`](../../../papers/catalog/papers.json).

| Paper | Año | Qué desbloqueó | Miniatura |
|---|---:|---|---|
| [P34 · RoFormer: Transformer mejorado con codificación posicional rotatoria](../../../papers/foundational/P34_rope/README.md) | 2021 | La posición se codifica rotando, y la atención pasa a depender solo de la distancia relativa. Es la base de casi todo modelo actual. | [notebook](../../../notebooks/papers/P34_rope.ipynb) |

Cada ficha explica el problema anterior, la matemática mínima, los límites y los errores de atribución más frecuentes. Para leerlas con método: [cómo leer un paper de IA](../../../papers/guides/COMO_LEER_UN_PAPER_DE_IA.md) · [anexos matemáticos](../../../papers/annexes/README.md).
<!-- papers:fin -->
---

## ⬅️ Clase anterior

[078 — RLHF, RLAIF y DPO](../../part-06-foundation-models-and-llm-engineering/078-rlhf-rlaif-y-dpo/README.md)

## ➡️ Siguiente clase

[080 — Tool calling y ejecución controlada](../../part-06-foundation-models-and-llm-engineering/080-tool-calling-y-ejecucion-controlada/README.md)
