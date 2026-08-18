# 👩‍🏫 Guía docente — P70 · Consistencia en redes de relaciones

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Consistency in Networks of Relations* (1977, Artificial Intelligence, 8(1), 99–118)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *El retroceso cronológico repetía una y otra vez el mismo descubrimiento: que cierto valor era incompatible con sus vecinos. La información se hallaba y se tiraba en cada rama.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Hacer la red consistente de arco antes de asignar nada: eliminar de cada dominio los valores sin compañero legal en algún vecino, y repropagar en cascada. Los algoritmos AC-1, AC-2 y AC-3 formalizan el procedimiento.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P70_arco_consistencia.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P70_arco_consistencia`](../../papers/foundational/P70_arco_consistencia/README.md)
- Notebook: [`P70_arco_consistencia.ipynb`](../../notebooks/papers/P70_arco_consistencia.ipynb)
- Evaluación: [`P70_arco_consistencia.md`](../../assessments/papers/P70_arco_consistencia.md)
- Clases del programa relacionadas:
- [018-problemas-de-satisfaccion-de-restricciones](../../classes/part-01-symbolic-ai-search-logic-and-planning/018-problemas-de-satisfaccion-de-restricciones/README.md)

---

[⬅️ Guías docentes del eje](README.md)
