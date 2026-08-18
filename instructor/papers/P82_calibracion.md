# 👩‍🏫 Guía docente — P82 · Predecir buenas probabilidades con aprendizaje supervisado

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Predicting Good Probabilities with Supervised Learning* (2005, ICML '05, 625–632)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Las salidas de un clasificador se usan como probabilidades para decidir con umbrales de coste o para combinarlas con otras. Pero un modelo puede tener un AUC excelente y probabilidades sistemáticamente sesgadas, y nadie lo estaba midiendo.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Medir la calibración con diagramas de fiabilidad y puntuaciones propias, caracterizar cómo se descalibra cada familia de modelos, y corregirla con escalado de Platt o regresión isotónica sin alterar el orden.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P82_calibracion.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P82_calibracion`](../../papers/foundational/P82_calibracion/README.md)
- Notebook: [`P82_calibracion.ipynb`](../../notebooks/papers/P82_calibracion.ipynb)
- Evaluación: [`P82_calibracion.md`](../../assessments/papers/P82_calibracion.md)
- Clases del programa relacionadas:
- [047-metricas-calibracion-sesgo-y-costo-de-error](../../classes/part-03-classical-machine-learning/047-metricas-calibracion-sesgo-y-costo-de-error/README.md)

---

[⬅️ Guías docentes del eje](README.md)
