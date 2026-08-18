# 👩‍🏫 Guía docente — P78 · Una generalización decisional del aprendizaje en línea y su aplicación al boosting

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting* (1997, Journal of Computer and System Sciences, 55(1), 119–139)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Kearns y Valiant habían preguntado si un aprendiz «débil» —apenas mejor que el azar— puede convertirse en uno «fuerte». La respuesta afirmativa existía pero era impracticable: exigía conocer de antemano la ventaja del aprendiz débil.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *AdaBoost: entrenar clasificadores en serie, subiendo el peso de los ejemplos que el anterior falló, y ponderar el voto de cada uno por su error. Se adapta solo a la calidad de cada aprendiz, sin conocerla de antemano.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P78_adaboost.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P78_adaboost`](../../papers/foundational/P78_adaboost/README.md)
- Notebook: [`P78_adaboost.ipynb`](../../notebooks/papers/P78_adaboost.ipynb)
- Evaluación: [`P78_adaboost.md`](../../assessments/papers/P78_adaboost.md)
- Clases del programa relacionadas:
- [041-random-forest-boosting-y-ensembles](../../classes/part-03-classical-machine-learning/041-random-forest-boosting-y-ensembles/README.md)

---

[⬅️ Guías docentes del eje](README.md)
