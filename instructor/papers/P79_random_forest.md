# 👩‍🏫 Guía docente — P79 · Bosques aleatorios

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Random Forests* (2001, Machine Learning, 45(1), 5–32)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *El bagging reducía la varianza promediando árboles entrenados sobre remuestreos, pero los árboles seguían pareciéndose demasiado: ante los mismos datos elegían casi siempre las mismas variables.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Añadir una segunda fuente de azar: en cada nodo, considerar solo un subconjunto aleatorio de variables. Los árboles empeoran individualmente y se descorrelacionan, y la cota del error del bosque mejora.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P79_random_forest.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P79_random_forest`](../../papers/foundational/P79_random_forest/README.md)
- Notebook: [`P79_random_forest.ipynb`](../../notebooks/papers/P79_random_forest.ipynb)
- Evaluación: [`P79_random_forest.md`](../../assessments/papers/P79_random_forest.md)
- Clases del programa relacionadas:
- [041-random-forest-boosting-y-ensembles](../../classes/part-03-classical-machine-learning/041-random-forest-boosting-y-ensembles/README.md)

---

[⬅️ Guías docentes del eje](README.md)
