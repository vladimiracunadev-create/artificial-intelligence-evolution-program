# 👩‍🏫 Guía docente — P65 · Un programa de máquina para demostración de teoremas

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *A Machine Program for Theorem-Proving* (1962, Communications of the ACM, 5(7), 394–397)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *El procedimiento de Davis y Putnam (1960) era correcto pero consumía memoria de forma impracticable al eliminar variables por resolución.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Sustituir la eliminación por una búsqueda en profundidad con retroceso, apoyada en dos reglas que no requieren elegir: propagación de cláusulas unitarias y literales puros.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P65_dpll.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P65_dpll`](../../papers/foundational/P65_dpll/README.md)
- Notebook: [`P65_dpll.ipynb`](../../notebooks/papers/P65_dpll.ipynb)
- Evaluación: [`P65_dpll.md`](../../assessments/papers/P65_dpll.md)
- Clases del programa relacionadas:
- [019-logica-proposicional-e-inferencia](../../classes/part-01-symbolic-ai-search-logic-and-planning/019-logica-proposicional-e-inferencia/README.md)

---

[⬅️ Guías docentes del eje](README.md)
