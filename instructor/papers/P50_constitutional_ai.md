# 👩‍🏫 Guía docente — P50 · IA constitucional: inocuidad a partir de retroalimentación de IA

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Constitutional AI: Harmlessness from AI Feedback* (2022, arXiv:2212.08073)
**Nivel:** L4 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *RLHF depende de miles de comparaciones humanas: es caro, expone a los anotadores a contenido dañino, y los criterios quedan implícitos en los datos, sin poder inspeccionarse ni discutirse.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Escribir los principios de forma explícita, hacer que el modelo critique y revise sus propias respuestas contra ellos, y usar preferencias generadas por IA para la fase de refuerzo.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P50_constitutional_ai.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P50_constitutional_ai`](../../papers/foundational/P50_constitutional_ai/README.md)
- Notebook: [`P50_constitutional_ai.ipynb`](../../notebooks/papers/P50_constitutional_ai.ipynb)
- Evaluación: [`P50_constitutional_ai.md`](../../assessments/papers/P50_constitutional_ai.md)
- Clases del programa relacionadas:
- [078-rlhf-rlaif-y-dpo](../../classes/part-06-foundation-models-and-llm-engineering/078-rlhf-rlaif-y-dpo/README.md)

---

[⬅️ Guías docentes del eje](README.md)
