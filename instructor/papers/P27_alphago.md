# 👩‍🏫 Guía docente — P27 · Dominar el go con redes neuronales profundas y búsqueda en árbol

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Mastering the game of Go with deep neural networks and tree search* (2016, Nature 529, 484–489 (2016))
**Nivel:** L4 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *El go tiene un espacio de estados y un factor de ramificación que hacen inviable la búsqueda exhaustiva, y no existía una función de evaluación de posiciones suficientemente buena.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Una red de políticas que propone jugadas plausibles y una red de valor que evalúa posiciones, usadas para guiar y truncar una búsqueda de Monte Carlo en árbol.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P27_alphago.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P27_alphago`](../../papers/foundational/P27_alphago/README.md)
- Notebook: [`P27_alphago.ipynb`](../../notebooks/papers/P27_alphago.ipynb)
- Evaluación: [`P27_alphago.md`](../../assessments/papers/P27_alphago.md)
- Clases del programa relacionadas:
- [017-juegos-minimax-y-poda-alfa-beta](../../classes/part-01-symbolic-ai-search-logic-and-planning/017-juegos-minimax-y-poda-alfa-beta/README.md)
- [031-metodos-monte-carlo-y-simulacion](../../classes/part-02-probabilistic-evolutionary-and-decision-ai/031-metodos-monte-carlo-y-simulacion/README.md)

---

[⬅️ Guías docentes del eje](README.md)
