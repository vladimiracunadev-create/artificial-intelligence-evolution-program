# 👩‍🏫 Guía docente — P10 · Los modelos de lenguaje son aprendices con pocos ejemplos

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Language Models are Few-Shot Learners* (2020, arXiv:2005.14165 · NeurIPS 2020)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *El patrón de BERT exigía un conjunto etiquetado y un ajuste fino por cada tarea nueva; eso no escala a la variedad de tareas reales.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Escalar un Transformer autorregresivo hasta 175 000 millones de parámetros y evaluar en modo zero-shot, one-shot y few-shot mediante condicionamiento en el prompt.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P10_gpt3.ipynb`, secciones 6–9 | Salida del experimento controlado |
| Interpretación | 15 | Contraste predicción/resultado y anti-patrón (secciones 11–12) | Corrección argumentada |
| Límites y cierre | 15 | Qué NO demuestra la miniatura, qué NO dice el paper | Una limitación por estudiante |

## Errores que aparecerán en clase

1. Atribuir al paper ideas posteriores (revisar la sección 12 de la ficha antes de la sesión).
2. Confundir la miniatura del notebook con una reproducción del experimento original.
3. Aceptar una métrica sin preguntar por tarea, dataset, línea base y protocolo.

## Preguntas para dinamizar

- ¿Qué habría que observar para considerar refutada la propuesta del paper?
- ¿Qué parte del resultado depende de los datos y qué parte del método?
- Si este paper no existiera, ¿qué habría bloqueado el hito siguiente?

## Enlaces de aula

- Ficha completa: [`P10_gpt3`](../../papers/foundational/P10_gpt3/README.md)
- Notebook: [`P10_gpt3.ipynb`](../../notebooks/papers/P10_gpt3.ipynb)
- Evaluación: [`P10_gpt3.md`](../../assessments/papers/P10_gpt3.md)
- Clases del programa relacionadas:
- [074-objetivos-de-preentrenamiento](../../classes/part-06-foundation-models-and-llm-engineering/074-objetivos-de-preentrenamiento/README.md)
- [086-seleccion-de-modelo-costo-latencia-y-privacidad](../../classes/part-06-foundation-models-and-llm-engineering/086-seleccion-de-modelo-costo-latencia-y-privacidad/README.md)

---

[⬅️ Guías docentes del eje](README.md)
