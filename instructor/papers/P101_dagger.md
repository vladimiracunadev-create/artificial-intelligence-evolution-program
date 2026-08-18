# 👩‍🏫 Guía docente — P101 · Una reducción del aprendizaje por imitación al aprendizaje en línea sin arrepentimiento

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning* (2011, AISTATS 2011 · arXiv:1011.0686)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Al clonar el comportamiento de un experto, el modelo se entrena con los estados que visita el EXPERTO y se ejecuta sobre los estados que visita ÉL MISMO. Un error lo saca de la distribución de entrenamiento, donde comete más errores, y la desviación se realimenta.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *DAgger: ejecutar la política actual, recoger los estados que visita de verdad, pedir al experto la acción correcta **en esos estados**, y reentrenar sobre el conjunto acumulado. La distribución de entrenamiento converge a la de ejecución.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P101_dagger.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P101_dagger`](../../papers/foundational/P101_dagger/README.md)
- Notebook: [`P101_dagger.ipynb`](../../notebooks/papers/P101_dagger.ipynb)
- Evaluación: [`P101_dagger.md`](../../assessments/papers/P101_dagger.md)
- Clases del programa relacionadas:
- [141-aprendizaje-por-imitacion](../../classes/part-11-embodied-ai-robotics-and-computer-use/141-aprendizaje-por-imitacion/README.md)

---

[⬅️ Guías docentes del eje](README.md)
