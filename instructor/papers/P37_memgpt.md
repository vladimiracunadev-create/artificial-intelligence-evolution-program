# 👩‍🏫 Guía docente — P37 · MemGPT: modelos de lenguaje como sistemas operativos

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *MemGPT: Towards LLMs as Operating Systems* (2023, arXiv:2310.08560)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La ventana de contexto es un límite duro. Ampliarla es caro y, como muestra P36, no garantiza que se use bien.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Gestionar el contexto como un sistema operativo gestiona la memoria: un contexto principal pequeño, un almacén externo grande, y el propio modelo decidiendo qué paginar mediante llamadas de función.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P37_memgpt.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P37_memgpt`](../../papers/foundational/P37_memgpt/README.md)
- Notebook: [`P37_memgpt.ipynb`](../../notebooks/papers/P37_memgpt.ipynb)
- Evaluación: [`P37_memgpt.md`](../../assessments/papers/P37_memgpt.md)
- Clases del programa relacionadas:
- [108-memoria-de-corto-y-largo-plazo](../../classes/part-08-retrieval-context-memory-and-knowledge/108-memoria-de-corto-y-largo-plazo/README.md)
- [109-compresion-de-contexto-y-caches-semanticos](../../classes/part-08-retrieval-context-memory-and-knowledge/109-compresion-de-contexto-y-caches-semanticos/README.md)

---

[⬅️ Guías docentes del eje](README.md)
