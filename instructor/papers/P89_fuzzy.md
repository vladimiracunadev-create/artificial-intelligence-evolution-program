# 👩‍🏫 Guía docente — P89 · Conjuntos difusos

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Fuzzy Sets* (1965, Information and Control, 8(3), 338–353)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La teoría de conjuntos es binaria: algo pertenece o no pertenece. Pero «alto», «caliente» o «cerca» no tienen frontera nítida, y forzarlos a un umbral produce sistemas que cambian de decisión ante una diferencia irrelevante.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Sustituir la función característica {0,1} por una función de pertenencia a [0,1], y definir sobre ella unión, intersección y complemento con máximo, mínimo y complemento a uno.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P89_fuzzy.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P89_fuzzy`](../../papers/foundational/P89_fuzzy/README.md)
- Notebook: [`P89_fuzzy.ipynb`](../../notebooks/papers/P89_fuzzy.ipynb)
- Evaluación: [`P89_fuzzy.md`](../../assessments/papers/P89_fuzzy.md)
- Clases del programa relacionadas:
- [032-logica-difusa-y-control-aproximado](../../classes/part-02-probabilistic-evolutionary-and-decision-ai/032-logica-difusa-y-control-aproximado/README.md)

---

[⬅️ Guías docentes del eje](README.md)
