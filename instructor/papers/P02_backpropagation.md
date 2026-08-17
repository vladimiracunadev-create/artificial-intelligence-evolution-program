# 👩‍🏫 Guía docente — P02 · Aprender representaciones retropropagando errores

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Learning representations by back-propagating errors* (1986, Nature, 323, 533–536)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Sin capas ocultas el perceptrón no resuelve XOR; con capas ocultas no se sabía cómo asignar el error a cada peso interno.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Aplicar la regla de la cadena hacia atrás por el grafo de cómputo para obtener el gradiente de la pérdida respecto de cada peso.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P02_backpropagation.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P02_backpropagation`](../../papers/foundational/P02_backpropagation/README.md)
- Notebook: [`P02_backpropagation.ipynb`](../../notebooks/papers/P02_backpropagation.ipynb)
- Evaluación: [`P02_backpropagation.md`](../../assessments/papers/P02_backpropagation.md)
- Clases del programa relacionadas:
- [050-mlp-y-backpropagation](../../classes/part-04-neural-networks-and-deep-learning/050-mlp-y-backpropagation/README.md)
- [051-activaciones-inicializacion-y-normalizacion](../../classes/part-04-neural-networks-and-deep-learning/051-activaciones-inicializacion-y-normalizacion/README.md)

---

[⬅️ Guías docentes del eje](README.md)
