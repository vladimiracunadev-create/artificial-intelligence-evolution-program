# 👩‍🏫 Guía docente — P81 · Introducción a la selección de variables y características

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *An Introduction to Variable and Feature Selection* (2003, Journal of Machine Learning Research, 3, 1157–1182)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Con miles de variables y pocas muestras hay que reducir. El método habitual —ordenar las variables por su correlación con la etiqueta y quedarse con las primeras— tiene modos de fallo que casi nadie enunciaba.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Un marco con tres familias —filtros, envolturas y métodos embebidos— y dos advertencias con contraejemplo: una variable inútil por separado puede ser imprescindible en compañía, y dos variables redundantes pueden ser mejores juntas que cualquiera sola.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P81_seleccion_de_caracteristicas.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P81_seleccion_de_caracteristicas`](../../papers/foundational/P81_seleccion_de_caracteristicas/README.md)
- Notebook: [`P81_seleccion_de_caracteristicas.ipynb`](../../notebooks/papers/P81_seleccion_de_caracteristicas.ipynb)
- Evaluación: [`P81_seleccion_de_caracteristicas.md`](../../assessments/papers/P81_seleccion_de_caracteristicas.md)
- Clases del programa relacionadas:
- [042-ingenieria-y-seleccion-de-caracteristicas](../../classes/part-03-classical-machine-learning/042-ingenieria-y-seleccion-de-caracteristicas/README.md)

---

[⬅️ Guías docentes del eje](README.md)
