# 👩‍🏫 Guía docente — P76 · Un estudio de la validación cruzada y el bootstrap para estimar exactitud y seleccionar modelos

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection* (1995, IJCAI'95, 1137–1143)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Se reportaban exactitudes sin decir cómo se habían estimado. Holdout, validación cruzada y bootstrap dan números distintos sobre los mismos datos, y nadie había medido cuál era preferible ni por qué.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Comparar empíricamente los estimadores en sesgo y varianza sobre conjuntos reales, y recomendar validación cruzada estratificada de diez pliegues como compromiso entre ambos.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P76_validacion_cruzada.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P76_validacion_cruzada`](../../papers/foundational/P76_validacion_cruzada/README.md)
- Notebook: [`P76_validacion_cruzada.ipynb`](../../notebooks/papers/P76_validacion_cruzada.ipynb)
- Evaluación: [`P76_validacion_cruzada.md`](../../assessments/papers/P76_validacion_cruzada.md)
- Clases del programa relacionadas:
- [037-flujo-supervisado-y-particion-train-validation-test](../../classes/part-03-classical-machine-learning/037-flujo-supervisado-y-particion-train-validation-test/README.md)

---

[⬅️ Guías docentes del eje](README.md)
