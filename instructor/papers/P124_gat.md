# 👩‍🏫 Guía docente — P124 · Redes de atención sobre grafos

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Graph Attention Networks* (2018, ICLR 2018 · arXiv:1710.10903)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La convolución de grafo promedia a todos los vecinos por igual y normaliza por el grado. Eso supone que todos los vecinos importan lo mismo y exige conocer el grafo completo, lo que impide aplicar el modelo a nodos que no se vieron al entrenar.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Calcular un coeficiente de atención para cada pareja de nodos vecinos, normalizarlo con softmax sobre el vecindario y agregar con esos pesos. Varias cabezas en paralelo, como en el Transformer.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P124_gat.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P124_gat`](../../papers/foundational/P124_gat/README.md)
- Notebook: [`P124_gat.ipynb`](../../notebooks/papers/P124_gat.ipynb)
- Evaluación: [`P124_gat.md`](../../assessments/papers/P124_gat.md)
- Clases del programa relacionadas:
- [056-graph-neural-networks](../../classes/part-04-neural-networks-and-deep-learning/056-graph-neural-networks/README.md)

---

[⬅️ Guías docentes del eje](README.md)
