# 👩‍🏫 Guía docente — P147 · Los modelos recurrentes del mundo facilitan la evolución de políticas

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Recurrent World Models Facilitate Policy Evolution* (2018, NeurIPS 2018 · arXiv:1803.10122)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Aprender por refuerzo exige millones de interacciones con el entorno. En simulación es caro; en un robot, inviable. Y el agente pasa la mayor parte de esas interacciones reaprendiendo cómo funciona el mundo, no cómo actuar en él.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Separar el problema en tres piezas: un codificador que comprime la observación, un modelo recurrente que predice el futuro en ese espacio comprimido, y una política diminuta entrenada **dentro** del modelo, sin tocar el entorno.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P147_world_models.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P147_world_models`](../../papers/foundational/P147_world_models/README.md)
- Notebook: [`P147_world_models.ipynb`](../../notebooks/papers/P147_world_models.ipynb)
- Evaluación: [`P147_world_models.md`](../../assessments/papers/P147_world_models.md)
- Clases del programa relacionadas:
- [174-world-models-y-simulacion-interna](../../classes/part-14-frontier-research-and-capstones/174-world-models-y-simulacion-interna/README.md)

---

[⬅️ Guías docentes del eje](README.md)
