# P12 — InstructGPT y RLHF

> El salto de «modelo que completa texto» a «asistente que hace lo que se le pide». Y la
> constatación incómoda de que «mejor» es una decisión de quién etiqueta, no una propiedad del
> modelo.

**Nivel:** L3 · **Motor:** `rlhf` · **Notebook:** [`P12_instructgpt_rlhf.ipynb`](../../../notebooks/papers/P12_instructgpt_rlhf.ipynb)

## 1. Identificación

| Campo | Valor |
|---|---|
| **Título original** | *Training language models to follow instructions with human feedback* |
| **Autoría** | Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida y otros (OpenAI) |
| **Año** | 2022 |
| **Venue** | arXiv:2203.02155 · NeurIPS 2022 |
| **Fuente primaria** | [arXiv:2203.02155](https://arxiv.org/abs/2203.02155) |
| **Acceso** | Abierto |
| **Fecha de consulta** | 2026-08-16 |

## 2. Problema anterior

[GPT-3](../P10_gpt3/README.md) se entrena maximizando la verosimilitud del texto de internet.
Ese objetivo **no es** «sé útil, honesto e inocuo». Es «predice qué viene después».

La consecuencia práctica: el modelo continúa el texto de la forma más plausible, que a menudo
no es lo que el usuario quería. Ante «explícame X», puede generar más preguntas sobre X en
lugar de explicarlo, porque en internet eso también es una continuación plausible.

A esto se le llama **desalineación de objetivo**: el objetivo de entrenamiento y la intención
del usuario no coinciden. Y no se arregla con más escala, porque escalar mejora el objetivo
equivocado.

## 3. Propuesta

Tres etapas encadenadas:

1. **SFT (ajuste supervisado).** Etiquetadores escriben respuestas de demostración a prompts
   reales; el modelo se ajusta sobre ellas.
2. **Modelo de recompensa (RM).** Para cada prompt se muestrean varias respuestas y los
   etiquetadores las **ordenan por preferencia**. Con esas comparaciones se entrena un modelo
   que asigna un escalar `r(x, y)`.
3. **Optimización por refuerzo.** La política se optimiza con PPO para maximizar `r`, con una
   **penalización KL** que la mantiene cerca del modelo SFT.

La decisión metodológica clave: **pedir comparaciones, no puntuaciones**. Ordenar dos
respuestas es más fácil, más rápido y mucho más consistente entre anotadores que puntuar del
1 al 10.

## 4. Intuición sin fórmulas

Enseñar a alguien a cocinar sin darle recetas: le pones dos platos delante y le dices cuál está
mejor. Con suficientes comparaciones, aprende qué buscas — aunque tú nunca hayas sabido
formularlo con palabras.

**Dónde deja de funcionar la analogía:** el aprendiz humano entiende *por qué* un plato es
mejor. El modelo de recompensa solo aprende **qué correlaciona** con la preferencia. Si tus
platos preferidos resultan ser siempre los más grandes, aprenderá a servir raciones enormes.

## 5. Matemática mínima

### Modelo de recompensa (Bradley-Terry)

```text
p(y_w ≻ y_l | x) = σ( r(x, y_w) − r(x, y_l) )

L_RM = − E[ log σ( r(x, y_w) − r(x, y_l) ) ]
```

`y_w` = respuesta preferida, `y_l` = rechazada. Solo importa la **diferencia**: la escala
absoluta de `r` no está determinada.

### Optimización con restricción

```text
max_π  E_{y ~ π(·|x)} [ r(x, y) ]  −  β · KL( π(·|x) ‖ π_SFT(·|x) )
```

El término KL es imprescindible: sin él la política deriva hacia texto degenerado que engaña al
modelo de recompensa. `β` fija el precio de alejarse del modelo base.

## 6. Arquitectura o flujo

```text
   ┌── ETAPA 1: SFT ────────────────────────────────────────┐
   │  prompts reales + demostraciones humanas               │
   │  modelo base ──ajuste supervisado──► π_SFT             │
   └────────────────────────┬───────────────────────────────┘
                            ▼
   ┌── ETAPA 2: modelo de recompensa ───────────────────────┐
   │  prompt → π_SFT genera k respuestas                    │
   │  etiquetadores las ORDENAN por preferencia             │
   │  comparaciones ──Bradley-Terry──► r(x, y)              │
   └────────────────────────┬───────────────────────────────┘
                            ▼
   ┌── ETAPA 3: refuerzo (PPO) ─────────────────────────────┐
   │  π genera → r puntúa → PPO actualiza π                 │
   │  penalización β·KL(π ‖ π_SFT) como ancla               │
   └────────────────────────────────────────────────────────┘
```

## 7. Qué observar en el paper original

- El **resultado más citado**: los etiquetadores prefieren las salidas del modelo InstructGPT
  de **1 300 millones** de parámetros sobre las de GPT-3 de **175 000 millones**. Alinear
  resultó más rentable que escalar dos órdenes de magnitud.
- La sección sobre **quién etiquetó**: perfil demográfico de los anotadores, criterios de
  selección y guía de anotación. Es una de las secciones más honestas y menos leídas del
  artículo, y determina qué significa «mejor» en todo el trabajo.
- El **impuesto de alineación** (*alignment tax*): la caída de rendimiento en algunos
  benchmarks académicos, y la mezcla de gradientes de preentrenamiento que usan para mitigarla.
- Las secciones sobre **límites**: el modelo sigue alucinando, sigue siendo sensible al prompt y
  puede obedecer instrucciones dañinas si están bien formuladas.

## 8. Evidencia y resultados

Evaluación principal por **preferencia humana**: se comparan salidas de distintos modelos sobre
la distribución de prompts real de la API y sobre conjuntos públicos.

- InstructGPT es preferido a GPT-3 por un margen amplio, **incluso con modelos mucho más
  pequeños**.
- Mejora en veracidad (TruthfulQA) y reducción de generación tóxica frente al modelo base.
- Generaliza a instrucciones y a idiomas poco representados en los datos de ajuste.
- Se documenta un retroceso en algunos benchmarks académicos, mitigado parcialmente.

> Las proporciones exactas de preferencia y los resultados por benchmark están en las figuras y
> tablas del artículo. Verificarlos allí antes de citarlos.

La miniatura de este eje muestra el mecanismo del modelo de recompensa: cinco comparaciones
bastan para que un `r` lineal ordene cuatro respuestas candidatas, situando arriba la útil y
honesta y abajo la peligrosa.

## 9. Impacto

- Es la técnica que hizo posibles los asistentes conversacionales de uso masivo. **ChatGPT
  desciende directamente de este trabajo**, no de GPT-3 base.
- Convierte la **alineación** en una disciplina de ingeniería con etapas, datos y métricas, no
  solo en una discusión conceptual.
- Instala la **preferencia humana como métrica**, con todo lo que eso implica: la evaluación
  deja de ser puramente automática.
- Abre la línea de trabajo sobre reward hacking, RLAIF y alineación con principios explícitos
  (Constitutional AI, 2022).

## 10. Limitaciones

1. **Reward hacking.** Si una característica superficial correlaciona con la preferencia (por
   ejemplo, la longitud), la política aprende a explotarla.
2. **Los valores son los de los anotadores.** El modelo de recompensa no descubre qué es mejor:
   reproduce el criterio de un grupo concreto de personas con una guía concreta.
3. **Pipeline complejo y caro**: tres modelos, datos humanos y un bucle de RL delicado de
   estabilizar. Este es el problema que ataca [DPO](../P15_dpo/README.md).
4. **Impuesto de alineación**: caída en algunos benchmarks académicos.
5. **Sigue alucinando.** La alineación cambia el estilo y la obediencia, no añade conocimiento
   ni verificación.
6. **Sicofancia**: si a los anotadores les gustan las respuestas que les dan la razón, el modelo
   aprende a darla.
7. **PPO es sensible** a hiperparámetros; reproducirlo requiere mucho oficio no documentado.

## 11. Errores comunes

| Error | Corrección |
|---|---|
| «RLHF hace que el modelo diga la verdad» | Hace que produzca respuestas **preferidas por los anotadores**. La correlación con la verdad es parcial y no está garantizada. |
| «RLHF añade conocimiento al modelo» | No. Reorganiza el comportamiento sobre el conocimiento que ya tenía. |
| «El modelo de recompensa es objetivo por ser un modelo» | Es un resumen estadístico de juicios humanos concretos, con sus sesgos. |
| «InstructGPT es GPT-3 con más datos» | Son tres etapas y dos modelos adicionales. La diferencia es de procedimiento, no de escala. |
| «Este paper inventó RLHF» | Christiano et al. (2017) ya lo aplicaba a control con preferencias humanas. Este trabajo lo lleva a modelos de lenguaje a escala. |
| «El término KL es un detalle de regularización» | Sin él la política colapsa hacia texto degenerado con recompensa alta. Es estructural. |

## 12. Relación con trabajos anteriores

- **[P10 GPT-3](../P10_gpt3/README.md) (2020)** — el modelo base y el problema.
- **Christiano et al. (2017)** — RL a partir de preferencias humanas.
  [arXiv:1706.03741](https://arxiv.org/abs/1706.03741)
- **Stiennon et al. (2020)** — RLHF aplicado a resumen; el precedente directo.
  [arXiv:2009.01325](https://arxiv.org/abs/2009.01325)
- **Schulman et al. (2017), PPO** — el algoritmo de optimización.
  [arXiv:1707.06347](https://arxiv.org/abs/1707.06347)
- **Bradley y Terry (1952)** — el modelo de comparaciones por pares.

## 13. Relación con trabajos posteriores

- **Bai et al. (2022), Constitutional AI** — reemplazar parte del juicio humano por principios
  explícitos y crítica del propio modelo.
  [arXiv:2212.08073](https://arxiv.org/abs/2212.08073)
- **[P15 DPO](../P15_dpo/README.md) (2023)** — el mismo objetivo sin modelo de recompensa ni RL.
- **RLAIF (2023)** — retroalimentación generada por IA.
- **Trabajo sobre sicofancia y reward hacking (2023+)** — el estudio sistemático de los fallos
  que este pipeline induce.

## 14. Notebook asociado

[`P12_instructgpt_rlhf.ipynb`](../../../notebooks/papers/P12_instructgpt_rlhf.ipynb)

**Qué implementa:** el modelo de recompensa Bradley-Terry entrenado por descenso de gradiente
sobre comparaciones por pares, el ranking resultante, una selección best-of-n, y una
demostración numérica de cómo el término KL penaliza alejarse del modelo base.

**Qué NO implementa:** SFT, PPO, generación de texto, ni etiquetadores humanos. Las
«respuestas» son cuatro vectores de características escritos a mano.

```bash
ai-evolution paper-lab P12 --seed 7
```

## 15. Actividades Bloom

| Nivel | Actividad |
|---|---|
| **Recordar** | Enumera las tres etapas y qué produce cada una. |
| **Explicar** | Explica por qué se piden comparaciones en vez de puntuaciones absolutas. |
| **Aplicar** | Cambia una comparación en el notebook y observa cómo se reordena el ranking. |
| **Analizar** | Construye un conjunto de preferencias donde el modelo aprenda a premiar la longitud. |
| **Evaluar** | ¿Un modelo alineado es más seguro o solo lo parece? Argumenta con dos límites del propio paper. |
| **Crear** | Diseña una guía de anotación de una página para un dominio que conozcas, y explica qué sesgo introduce cada regla. |

## 16. Autoevaluación

1. ¿Qué significa exactamente «desalineación de objetivo» en este contexto?
2. ¿Por qué las comparaciones son mejores datos que las puntuaciones?
3. ¿Qué ocurre si se elimina el término KL del objetivo?
4. ¿Qué es el reward hacking y cómo lo detectarías en un sistema propio?
5. ¿Por qué un modelo de 1 300 millones alineado puede preferirse a uno de 175 000 millones sin alinear?
6. ¿Qué es el impuesto de alineación?
7. ¿Qué **no** arregla RLHF?

## 17. Respuestas esperadas

1. Que el objetivo optimizado (verosimilitud del texto) difiere de lo que el usuario quiere
   (una respuesta útil). Escalar mejora el primero sin acercar el segundo.
2. Porque son más consistentes entre anotadores: una escala numérica se interpreta de forma
   distinta por cada persona y deriva con el tiempo, mientras que «cuál prefieres» es estable.
3. La política deriva libremente hacia regiones donde el modelo de recompensa da valores altos
   pero el texto es degenerado. El KL ancla la política al modelo SFT.
4. Explotar una característica que correlaciona con la recompensa sin mejorar la calidad real.
   Se detecta evaluando con humanos independientes del modelo de recompensa y controlando por
   variables superficiales como la longitud.
5. Porque el modelo grande optimiza un objetivo distinto del que el usuario quiere. La
   alineación reorganiza el comportamiento, y eso vale más que capacidad bruta mal dirigida.
6. La pérdida de rendimiento en algunos benchmarks académicos que aparece al alinear, y que el
   paper mitiga mezclando gradientes de preentrenamiento.
7. La alucinación, la falta de conocimiento actualizado, la sensibilidad al prompt y el sesgo
   heredado del corpus. Cambia el comportamiento, no lo que el modelo sabe.

## 18. Fuentes primarias

- Ouyang, L. et al. (2022). *Training language models to follow instructions with human
  feedback*. **NeurIPS 2022**.
  [arXiv:2203.02155](https://arxiv.org/abs/2203.02155) · consultado 2026-08-16.
- Christiano, P. et al. (2017). *Deep Reinforcement Learning from Human Preferences*.
  [arXiv:1706.03741](https://arxiv.org/abs/1706.03741) · consultado 2026-08-16.
- Stiennon, N. et al. (2020). *Learning to summarize with human feedback*.
  [arXiv:2009.01325](https://arxiv.org/abs/2009.01325) · consultado 2026-08-16.
- Bai, Y. et al. (2022). *Constitutional AI: Harmlessness from AI Feedback*.
  [arXiv:2212.08073](https://arxiv.org/abs/2212.08073) · consultado 2026-08-16.

---

[⬅️ Anterior: P11 RAG](../P11_rag/README.md) ·
[📇 Índice](../../catalog/PAPERS_INDEX.md) ·
[📝 Evaluación](../../../assessments/papers/P12_instructgpt_rlhf.md) ·
[🏫 Clase 078 del programa](../../../classes/part-06-foundation-models-and-llm-engineering/078-rlhf-rlaif-y-dpo/README.md) ·
[➡️ Siguiente: P13 ReAct](../P13_react/README.md)
