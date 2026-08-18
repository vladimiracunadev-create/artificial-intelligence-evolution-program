# 👩‍🏫 Guía docente — P67 · Una base formal para la determinación heurística de caminos de coste mínimo

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *A Formal Basis for the Heuristic Determination of Minimum Cost Paths* (1968, IEEE Transactions on Systems Science and Cybernetics, 4(2), 100–107)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La búsqueda guiada por heurística era rápida pero no garantizaba nada. La búsqueda exhaustiva garantizaba optimalidad y no escalaba. No había teoría que uniera las dos.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Evaluar cada nodo por `f(n) = g(n) + h(n)` —coste acumulado más estimación restante— y demostrar que si `h` es admisible (nunca sobrestima), el algoritmo devuelve el camino de coste mínimo, y que es óptimamente eficiente entre los que usan la misma información.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P67_a_estrella.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P67_a_estrella`](../../papers/foundational/P67_a_estrella/README.md)
- Notebook: [`P67_a_estrella.ipynb`](../../notebooks/papers/P67_a_estrella.ipynb)
- Evaluación: [`P67_a_estrella.md`](../../assessments/papers/P67_a_estrella.md)
- Clases del programa relacionadas:
- [015-costo-uniforme-busqueda-voraz-y-a](../../classes/part-01-symbolic-ai-search-logic-and-planning/015-costo-uniforme-busqueda-voraz-y-a/README.md)

---

[⬅️ Guías docentes del eje](README.md)
