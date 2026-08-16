# 👩‍🏫 Guía docente — P29 · Árbol de pensamientos: resolución deliberada de problemas con modelos de lenguaje grandes

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Tree of Thoughts: Deliberate Problem Solving with Large Language Models* (2023, arXiv:2305.10601 · NeurIPS 2023)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Una cadena de pensamiento decide de izquierda a derecha y sin vuelta atrás: un paso localmente razonable y globalmente equivocado condena toda la solución.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Tratar los pasos de razonamiento como nodos de un árbol, hacer que el modelo evalúe estados parciales y aplicar búsqueda con poda y retroceso.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P29_tree_of_thoughts.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P29_tree_of_thoughts`](../../papers/foundational/P29_tree_of_thoughts/README.md)
- Notebook: [`P29_tree_of_thoughts.ipynb`](../../notebooks/papers/P29_tree_of_thoughts.ipynb)
- Evaluación: [`P29_tree_of_thoughts.md`](../../assessments/papers/P29_tree_of_thoughts.md)
- Clases del programa relacionadas:
- [014-busqueda-en-anchura-y-profundidad](../../classes/part-01-symbolic-ai-search-logic-and-planning/014-busqueda-en-anchura-y-profundidad/README.md)
- [016-diseno-y-validacion-de-heuristicas](../../classes/part-01-symbolic-ai-search-logic-and-planning/016-diseno-y-validacion-de-heuristicas/README.md)

---

[⬅️ Guías docentes del eje](README.md)
