# 👩‍🏫 Guía docente — P68 · STRIPS: un nuevo enfoque para aplicar la demostración de teoremas a la resolución de problemas

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *STRIPS: A New Approach to the Application of Theorem Proving to Problem Solving* (1971, Artificial Intelligence, 2(3–4), 189–208)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Describir en lógica qué cambia y qué no al ejecutar una acción exigía escribir un axioma por cada literal que permanece igual. Es el problema del marco, y hacía inviable planificar con un demostrador de teoremas.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Describir cada operador con tres listas —precondiciones, literales que añade y literales que borra— y adoptar el supuesto de que todo lo no mencionado persiste.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P68_strips.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P68_strips`](../../papers/foundational/P68_strips/README.md)
- Notebook: [`P68_strips.ipynb`](../../notebooks/papers/P68_strips.ipynb)
- Evaluación: [`P68_strips.md`](../../assessments/papers/P68_strips.md)
- Clases del programa relacionadas:
- [023-planificacion-clasica-con-strips-y-pddl](../../classes/part-01-symbolic-ai-search-logic-and-planning/023-planificacion-clasica-con-strips-y-pddl/README.md)

---

[⬅️ Guías docentes del eje](README.md)
