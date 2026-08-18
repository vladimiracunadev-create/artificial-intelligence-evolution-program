# 👩‍🏫 Guía docente — P94 · Stan: un lenguaje de programación probabilística

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Stan: A Probabilistic Programming Language* (2017, Journal of Statistical Software, 76(1))
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Cada modelo bayesiano nuevo exigía escribir a mano su propio muestreador, con la matemática y los errores que eso trae. El coste de probar una variante del modelo era el de reimplementar el algoritmo.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Un lenguaje declarativo para especificar el modelo —previas y verosimilitud— y un motor de inferencia general basado en Monte Carlo hamiltoniano con NUTS, más diagnósticos de convergencia integrados.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P94_programacion_probabilistica.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P94_programacion_probabilistica`](../../papers/foundational/P94_programacion_probabilistica/README.md)
- Notebook: [`P94_programacion_probabilistica.ipynb`](../../notebooks/papers/P94_programacion_probabilistica.ipynb)
- Evaluación: [`P94_programacion_probabilistica.md`](../../assessments/papers/P94_programacion_probabilistica.md)
- Clases del programa relacionadas:
- [035-programacion-probabilistica-y-causalidad](../../classes/part-02-probabilistic-evolutionary-and-decision-ai/035-programacion-probabilistica-y-causalidad/README.md)

---

[⬅️ Guías docentes del eje](README.md)
