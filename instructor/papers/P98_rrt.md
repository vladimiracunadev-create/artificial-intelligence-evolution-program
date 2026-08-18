# 👩‍🏫 Guía docente — P98 · RRT-Connect: un enfoque eficiente para planificación de caminos de consulta única

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *RRT-Connect: An Efficient Approach to Single-Query Path Planning* (2000, Proceedings of ICRA 2000, 995–1001)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Un brazo de siete articulaciones tiene un espacio de configuración de siete dimensiones. Discretizarlo para aplicar búsqueda en grafo produce un número de celdas astronómico, y los métodos de campos potenciales se quedan atrapados en mínimos locales.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Muestrear configuraciones al azar y extender el árbol desde el nodo más cercano hacia cada muestra. El árbol se sesga solo hacia las regiones no exploradas, y con dos árboles que crecen uno hacia el otro la convergencia es mucho más rápida.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P98_rrt.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P98_rrt`](../../papers/foundational/P98_rrt/README.md)
- Notebook: [`P98_rrt.ipynb`](../../notebooks/papers/P98_rrt.ipynb)
- Evaluación: [`P98_rrt.md`](../../assessments/papers/P98_rrt.md)
- Clases del programa relacionadas:
- [139-planificacion-de-movimiento-y-navegacion](../../classes/part-11-embodied-ai-robotics-and-computer-use/139-planificacion-de-movimiento-y-navegacion/README.md)

---

[⬅️ Guías docentes del eje](README.md)
