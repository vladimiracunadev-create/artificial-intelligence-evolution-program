# 👩‍🏫 Guía docente — P26 · Control a nivel humano mediante aprendizaje por refuerzo profundo

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Human-level control through deep reinforcement learning* (2015, Nature 518, 529–533 (2015))
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Combinar aprendizaje por refuerzo con aproximación de función no lineal era notoriamente inestable: las muestras consecutivas están correlacionadas y el objetivo se mueve mientras se aprende.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Q-learning con una red convolucional, estabilizado con repetición de experiencia (rompe la correlación) y una red objetivo congelada (fija el blanco).* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P26_dqn.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P26_dqn`](../../papers/foundational/P26_dqn/README.md)
- Notebook: [`P26_dqn.ipynb`](../../notebooks/papers/P26_dqn.ipynb)
- Evaluación: [`P26_dqn.md`](../../assessments/papers/P26_dqn.md)
- Clases del programa relacionadas:
- [029-procesos-de-decision-de-markov](../../classes/part-02-probabilistic-evolutionary-and-decision-ai/029-procesos-de-decision-de-markov/README.md)
- [030-teoria-de-decision-y-utilidad-esperada](../../classes/part-02-probabilistic-evolutionary-and-decision-ai/030-teoria-de-decision-y-utilidad-esperada/README.md)
- [057-aprendizaje-por-refuerzo-profundo](../../classes/part-04-neural-networks-and-deep-learning/057-aprendizaje-por-refuerzo-profundo/README.md)

---

[⬅️ Guías docentes del eje](README.md)
