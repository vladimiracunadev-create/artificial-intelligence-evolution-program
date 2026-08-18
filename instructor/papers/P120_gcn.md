# 👩‍🏫 Guía docente — P120 · Clasificación semisupervisada con redes convolucionales de grafo

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Semi-Supervised Classification with Graph Convolutional Networks* (2017, ICLR 2017 · arXiv:1609.02907)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Muchos datos son grafos —citas, redes sociales, moléculas— donde etiquetar es caro y solo se tiene una fracción diminuta. Los métodos previos o eran costosos en el dominio espectral, o ignoraban la estructura y solo usaban los rasgos.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Una aproximación de primer orden de la convolución espectral que se reduce a promediar los rasgos de cada nodo con los de sus vecinos, normalizado por el grado, y apilar dos o tres de esas capas. Nada más.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P120_gcn.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P120_gcn`](../../papers/foundational/P120_gcn/README.md)
- Notebook: [`P120_gcn.ipynb`](../../notebooks/papers/P120_gcn.ipynb)
- Evaluación: [`P120_gcn.md`](../../assessments/papers/P120_gcn.md)
- Clases del programa relacionadas:
- [056-graph-neural-networks](../../classes/part-04-neural-networks-and-deep-learning/056-graph-neural-networks/README.md)

---

[⬅️ Guías docentes del eje](README.md)
