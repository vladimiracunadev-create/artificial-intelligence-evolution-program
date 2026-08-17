# 👩‍🏫 Guía docente — P36 · Perdidos en el medio: cómo usan los modelos de lenguaje los contextos largos

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Lost in the Middle: How Language Models Use Long Contexts* (2023, arXiv:2307.03172 · TACL)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La industria competía por anunciar ventanas de contexto cada vez mayores, sin medir si los modelos aprovechaban de verdad todo ese espacio.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Medirlo: colocar el mismo documento relevante en distintas posiciones del contexto y observar cómo cambia la exactitud.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P36_lost_in_middle.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P36_lost_in_middle`](../../papers/foundational/P36_lost_in_middle/README.md)
- Notebook: [`P36_lost_in_middle.ipynb`](../../notebooks/papers/P36_lost_in_middle.ipynb)
- Evaluación: [`P36_lost_in_middle.md`](../../assessments/papers/P36_lost_in_middle.md)
- Clases del programa relacionadas:
- [109-compresion-de-contexto-y-caches-semanticos](../../classes/part-08-retrieval-context-memory-and-knowledge/109-compresion-de-contexto-y-caches-semanticos/README.md)
- [110-evaluacion-de-fidelidad-cobertura-y-atribucion](../../classes/part-08-retrieval-context-memory-and-knowledge/110-evaluacion-de-fidelidad-cobertura-y-atribucion/README.md)

---

[⬅️ Guías docentes del eje](README.md)
