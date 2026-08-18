# 👩‍🏫 Guía docente — P77 · Contracción y selección en regresión mediante el lasso

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Regression Shrinkage and Selection via the Lasso* (1996, Journal of the Royal Statistical Society, Series B, 58(1), 267–288)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La regresión por mínimos cuadrados con muchas variables sobreajusta y produce modelos imposibles de interpretar. La selección por subconjuntos es inestable y la penalización de cresta encoge todos los coeficientes pero no elimina ninguno.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Penalizar la suma de los valores absolutos de los coeficientes. La geometría de esa restricción tiene esquinas sobre los ejes, y el óptimo tiende a caer en ellas: los coeficientes irrelevantes quedan exactamente en cero.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P77_lasso.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P77_lasso`](../../papers/foundational/P77_lasso/README.md)
- Notebook: [`P77_lasso.ipynb`](../../notebooks/papers/P77_lasso.ipynb)
- Evaluación: [`P77_lasso.md`](../../assessments/papers/P77_lasso.md)
- Clases del programa relacionadas:
- [038-regresion-lineal-regularizacion-y-diagnostico](../../classes/part-03-classical-machine-learning/038-regresion-lineal-regularizacion-y-diagnostico/README.md)

---

[⬅️ Guías docentes del eje](README.md)
