# 👩‍🏫 Guía docente — P73 · Cuantización por mínimos cuadrados en PCM

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Least Squares Quantization in PCM* (1982, IEEE Transactions on Information Theory, 28(2), 129–137)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Resumir un conjunto de puntos con k representantes exige elegirlos minimizando el error cuadrático. El problema es combinatorio y su solución exacta, inabordable.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Alternar dos pasos que cada uno reduce el error: asignar cada punto a su representante más cercano, y recolocar cada representante en el centro de los puntos que le tocaron.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P73_kmeans.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P73_kmeans`](../../papers/foundational/P73_kmeans/README.md)
- Notebook: [`P73_kmeans.ipynb`](../../notebooks/papers/P73_kmeans.ipynb)
- Evaluación: [`P73_kmeans.md`](../../assessments/papers/P73_kmeans.md)
- Clases del programa relacionadas:
- [043-clustering-y-reduccion-de-dimensionalidad](../../classes/part-03-classical-machine-learning/043-clustering-y-reduccion-de-dimensionalidad/README.md)

---

[⬅️ Guías docentes del eje](README.md)
