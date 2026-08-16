# P10 — GPT-3 y el aprendizaje en contexto

> La tarea deja de especificarse con un dataset etiquetado y pasa a especificarse **en el
> prompt**. Ningún peso cambia: cambia lo que hay escrito antes de la pregunta.

**Nivel:** L3 · **Motor:** `gpt3_icl` · **Notebook:** [`P10_gpt3.ipynb`](../../../notebooks/papers/P10_gpt3.ipynb)

## 1. Identificación

| Campo | Valor |
|---|---|
| **Título original** | *Language Models are Few-Shot Learners* |
| **Autoría** | Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah y otros (OpenAI) |
| **Año** | 2020 |
| **Venue** | arXiv:2005.14165 · NeurIPS 2020 |
| **Fuente primaria** | [arXiv:2005.14165](https://arxiv.org/abs/2005.14165) |
| **Acceso** | Abierto (el modelo, no) |
| **Fecha de consulta** | 2026-08-16 |

## 2. Problema anterior

El patrón que [BERT](../P09_bert/README.md) consolidó exigía, para cada tarea nueva, un
conjunto etiquetado y un ajuste fino que producía una copia entera del modelo. Eso tiene tres
costes: **datos** anotados, **cómputo** de ajuste y **almacenamiento** por tarea.

Además, ese patrón no se parece a cómo una persona recibe una tarea: a un humano se le explica
con una instrucción y dos ejemplos, no con diez mil casos etiquetados.

GPT-2 (2019) ya había mostrado indicios de resolver tareas sin ajuste fino. La pregunta abierta
era si eso era una curiosidad o una **tendencia con el tamaño**.

## 3. Propuesta

Escalar la rama **decoder** del Transformer hasta 175 000 millones de parámetros, entrenarla
con el objetivo autorregresivo de siempre sobre un corpus masivo, y evaluar sin ninguna
actualización de gradiente en tres regímenes:

- **zero-shot** — solo la instrucción;
- **one-shot** — la instrucción y un ejemplo;
- **few-shot** — la instrucción y `k` ejemplos, con `k` limitado por la ventana de contexto.

El artículo mide sistemáticamente el rendimiento frente al **tamaño del modelo** en decenas de
tareas, y documenta que la ventaja del régimen few-shot sobre el zero-shot **crece con la
escala**.

## 4. Intuición sin fórmulas

En lugar de reentrenar a un empleado para cada tarea nueva, le dejas una nota con dos ejemplos
resueltos y la tarea pendiente. Lo que hace es **seguir el patrón que ve en la nota**.

**Dónde deja de funcionar la analogía:** el empleado recuerda mañana lo que aprendió hoy. El
modelo no. Cierras la sesión y no queda rastro: no hubo aprendizaje, hubo condicionamiento.

## 5. Matemática mínima

El objetivo de entrenamiento es exactamente el de siempre:

```text
L = − Σ_t log p_θ(x_t | x_<t)
```

Lo nuevo es el **protocolo de evaluación**, no la matemática:

```text
zero-shot : p(y | instrucción, x)
one-shot  : p(y | instrucción, (x₁,y₁), x)
few-shot  : p(y | instrucción, (x₁,y₁)…(x_k,y_k), x)

θ NO cambia en ninguno de los tres casos.
```

**Escala del modelo mayor:** 175 000 millones de parámetros, 96 capas, `d_model = 12 288`,
96 cabezas de atención, ventana de contexto de 2 048 tokens.

## 6. Arquitectura o flujo

```text
   ┌────────────────────────── PROMPT ──────────────────────────┐
   │ Traduce al francés:                          ← instrucción │
   │ mar → mer                                    ← ejemplo 1   │
   │ cielo → ciel                                 ← ejemplo 2   │
   │ montaña →                                    ← consulta    │
   └────────────────────────────┬───────────────────────────────┘
                                ▼
            DECODER TRANSFORMER × 96  (self-attention causal)
                                │
                                ▼
                    p(siguiente token) → "montagne"

   Pesos actualizados: 0.   Memoria entre llamadas: ninguna.
```

## 7. Qué observar en el paper original

- La **figura de las curvas de escala**: rendimiento frente a tamaño del modelo, con una curva
  por régimen (zero, one, few-shot). La separación entre curvas creciendo con el tamaño es el
  resultado principal.
- La **tabla de composición del corpus** de entrenamiento (Common Crawl filtrado, WebText2,
  libros, Wikipedia) y sus pesos de muestreo.
- La **sección sobre contaminación de datos**: los autores analizan explícitamente el
  solapamiento entre los benchmarks y el corpus de entrenamiento, y reconocen limitaciones en
  ese análisis. Leerla es obligatorio antes de citar cualquier cifra.
- La **sección de impactos más amplios**: desinformación, sesgo y consumo energético. Es
  inusualmente extensa para la época.
- Las tareas donde el modelo **falla**: razonamiento aritmético de varios dígitos, inferencia
  en algunos conjuntos, comparaciones que requieren varios pasos.
- El artículo tiene decenas de páginas: casi todo es apéndice de evaluación.

## 8. Evidencia y resultados

Evaluación en más de veinte conjuntos de datos: modelado de lenguaje, respuesta a preguntas de
libro cerrado, traducción, razonamiento de sentido común, comprensión lectora, SuperGLUE y
tareas sintéticas (aritmética, uso de palabras nuevas, corrección gramatical).

Resultado central: **en varias tareas el régimen few-shot se aproxima a métodos ajustados
específicamente**, y la brecha se estrecha conforme crece el modelo. En otras, sigue muy por
detrás.

> Las cifras por tarea y régimen están en las tablas del artículo. Verificarlas allí, y leer
> antes la sección de contaminación: parte del rendimiento en algunos conjuntos podría estar
> afectado por solapamiento con el corpus de entrenamiento.

La miniatura de este eje **no reproduce nada de esto**. Simula el fenómeno con inducción
explícita de hipótesis para mostrar cómo cada ejemplo del prompt restringe el espacio de tareas
compatibles.

## 9. Impacto

- Desplaza el centro de gravedad del PLN del **ajuste fino** al **diseño de prompts**, y crea
  de facto la práctica que hoy se llama ingeniería de prompts y de contexto.
- Hace del **tamaño** una variable de primer orden y motiva el estudio sistemático de las
  leyes de escalado.
- Populariza el acceso a modelos por **API** en lugar de por pesos, con las consecuencias de
  reproducibilidad que eso implica.
- Es el punto de partida de [InstructGPT](../P12_instructgpt_rlhf/README.md): un modelo
  potente que **no** hace lo que se le pide de forma fiable necesita alineación.

## 10. Limitaciones

1. **El contexto se paga en cada llamada.** Los ejemplos ocupan tokens, cuestan latencia y
   dinero, y compiten con el resto del contexto.
2. **Sensibilidad al prompt.** El orden de los ejemplos, el formato y hasta los separadores
   alteran el resultado. Eso convierte muchas comparaciones en poco fiables.
3. **Sin memoria entre llamadas.** No hay aprendizaje persistente de ningún tipo.
4. **Contaminación de benchmarks**, reconocida por los propios autores.
5. **Aritmética y razonamiento de varios pasos** siguen siendo débiles.
6. **Alucinación**: genera afirmaciones plausibles y falsas, sin forma de citar fuente. Es el
   problema que ataca [RAG](../P11_rag/README.md).
7. **Modelo cerrado**: sin pesos públicos, la replicación independiente es imposible.
8. **Coste energético y económico** del entrenamiento, no repetible por la mayoría de equipos.
9. **No sigue instrucciones de forma fiable.** Completa texto; que eso coincida con lo que
   quería el usuario es otra cosa.

## 11. Errores comunes

| Error | Corrección |
|---|---|
| «Con los ejemplos del prompt, el modelo aprende» | Se **condiciona**. No hay gradiente, ni actualización, ni persistencia. Llamar «aprendizaje» a esto es la fuente de la mayoría de los malentendidos. |
| «GPT-3 inventó el prompting» | El artículo lo sistematiza y lo mide a escala. La idea de condicionar con instrucciones es anterior (GPT-2, 2019). |
| «GPT-3 es ChatGPT» | ChatGPT deriva de modelos **alineados con instrucciones** ([P12](../P12_instructgpt_rlhf/README.md)). GPT-3 base no está ajustado para dialogar ni para obedecer. |
| «Few-shot supera al ajuste fino» | En **algunas** tareas se acerca. En muchas otras el ajuste fino sigue ganando claramente. |
| «El modelo razona» | Produce continuaciones estadísticamente plausibles. Que a veces coincidan con un razonamiento correcto no autoriza la afirmación. |
| «Los benchmarks del paper son limpios» | Los propios autores documentan solapamiento con el corpus y las limitaciones de su análisis. |

## 12. Relación con trabajos anteriores

- **[P08 Transformer](../P08_transformer/README.md) (2017)** — la rama decoder.
- **GPT-1 (Radford et al., 2018)** — preentrenar y ajustar con decoder. Informe técnico de OpenAI.
- **GPT-2 (Radford et al., 2019)** — primeros indicios de tareas resueltas sin ajuste fino.
- **Kaplan et al. (2020)** — leyes de escalado, del mismo equipo y meses antes.
  [arXiv:2001.08361](https://arxiv.org/abs/2001.08361)
- **[P09 BERT](../P09_bert/README.md) (2018)** — el paradigma que este trabajo cuestiona.

## 13. Relación con trabajos posteriores

- **[P11 RAG](../P11_rag/README.md) (2020)** — ataca la alucinación y el conocimiento congelado.
- **[P12 InstructGPT](../P12_instructgpt_rlhf/README.md) (2022)** — alineación con instrucciones.
- **Wei et al. (2022), Chain-of-Thought** — razonamiento paso a paso inducido en el prompt.
  [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)
- **Hoffmann et al. (2022), Chinchilla** — corrige el reparto entre parámetros y datos.
  [arXiv:2203.15556](https://arxiv.org/abs/2203.15556)
- **[P13 ReAct](../P13_react/README.md) (2022)** — el modelo pasa a controlar un bucle.

## 14. Notebook asociado

[`P10_gpt3.ipynb`](../../../notebooks/papers/P10_gpt3.ipynb)

**Qué implementa:** una maqueta del aprendizaje en contexto mediante eliminación explícita de
hipótesis: con 0 ejemplos hay cuatro tareas compatibles; con 2, queda una sola. La precisión en
casos no vistos sube en consecuencia.

**Qué NO implementa —y esto es lo importante—:** nada de GPT-3. No hay modelo de lenguaje, ni
175 000 millones de parámetros, ni corpus. GPT-3 **no enumera hipótesis**: condiciona una
distribución aprendida. La maqueta sirve para razonar sobre el mecanismo, no para afirmar nada
sobre el modelo real.

```bash
ai-evolution paper-lab P10 --seed 7
```

## 15. Actividades Bloom

| Nivel | Actividad |
|---|---|
| **Recordar** | Define zero-shot, one-shot y few-shot con precisión. |
| **Explicar** | Explica por qué el aprendizaje en contexto no es aprendizaje, usando tres propiedades ausentes. |
| **Aplicar** | Cambia la tarea latente del notebook y mide cuántos ejemplos hacen falta para desambiguar. |
| **Analizar** | Diseña dos prompts con el mismo contenido y distinto orden de ejemplos. ¿Qué implicación tiene para comparar modelos? |
| **Evaluar** | Lee la sección de contaminación del paper y decide qué cifras aceptarías sin reservas. |
| **Crear** | Diseña un benchmark resistente a la contaminación y justifica cada decisión de diseño. |

## 16. Autoevaluación

1. ¿Qué cambia exactamente en el modelo entre zero-shot y few-shot?
2. ¿Por qué el aprendizaje en contexto no es aprendizaje?
3. ¿Qué limita el número de ejemplos que puedes poner en el prompt?
4. ¿Qué es la contaminación de benchmark y por qué es crítica en este paper concreto?
5. ¿Por qué la sensibilidad al orden de los ejemplos es un problema metodológico serio?
6. ¿Qué diferencia hay entre GPT-3 y un asistente conversacional actual?
7. ¿Qué tres problemas de GPT-3 atacan directamente los tres papers siguientes de la ruta?

## 17. Respuestas esperadas

1. Nada en el modelo. Cambia únicamente el texto de entrada. Los pesos son idénticos.
2. Porque no hay actualización de parámetros, no hay persistencia entre llamadas y no hay
   generalización acumulativa: cada llamada parte de cero.
3. La ventana de contexto (2 048 tokens en el modelo del paper) y el coste por token.
4. Que ejemplos de test aparezcan en el corpus de preentrenamiento. Es crítico aquí porque el
   corpus es Common Crawl a gran escala, donde es probable que estén muchos benchmarks
   públicos; los autores lo analizan y reconocen que su análisis es imperfecto.
5. Porque si reordenar los mismos ejemplos cambia el resultado, la métrica no mide solo la
   capacidad del modelo: mide también una elección arbitraria del evaluador. Sin reportar la
   varianza sobre órdenes, las comparaciones son frágiles.
6. El asistente está **alineado** con instrucciones mediante ajuste supervisado y aprendizaje
   con preferencias humanas. GPT-3 base solo continúa texto.
7. Conocimiento congelado y no citable → RAG. No seguir instrucciones → InstructGPT.
   No poder consultar el mundo ni actuar → ReAct.

## 18. Fuentes primarias

- Brown, T. B. et al. (2020). *Language Models are Few-Shot Learners*. **NeurIPS 2020**.
  [arXiv:2005.14165](https://arxiv.org/abs/2005.14165) · consultado 2026-08-16.
- Kaplan, J. et al. (2020). *Scaling Laws for Neural Language Models*.
  [arXiv:2001.08361](https://arxiv.org/abs/2001.08361) · consultado 2026-08-16.
- Bender, E. M., Gebru, T., McMillan-Major, A. y Shmitchell, S. (2021). *On the Dangers of
  Stochastic Parrots*. **FAccT 2021**.
  [doi.org/10.1145/3442188.3445922](https://doi.org/10.1145/3442188.3445922) · consultado 2026-08-16.

---

[⬅️ Anterior: P09 BERT](../P09_bert/README.md) ·
[📇 Índice](../../catalog/PAPERS_INDEX.md) ·
[📝 Evaluación](../../../assessments/papers/P10_gpt3.md) ·
[🏫 Clase 074 del programa](../../../classes/part-06-foundation-models-and-llm-engineering/074-objetivos-de-preentrenamiento/README.md) ·
[➡️ Siguiente: P11 RAG](../P11_rag/README.md)
