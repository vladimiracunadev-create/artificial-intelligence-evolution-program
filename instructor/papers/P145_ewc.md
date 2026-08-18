# 👩‍🏫 Guía docente — P145 · Superar el olvido catastrófico en redes neuronales

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Overcoming catastrophic forgetting in neural networks* (2017, PNAS, 114(13), 3521–3526)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *El olvido catastrófico llevaba treinta años documentado y sin remedio práctico. Reentrenar con todos los datos anteriores resuelve el problema y exige conservarlos, que es justo lo que no siempre se puede.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Estimar cuánto importa cada peso para lo ya aprendido —aproximando la información de Fisher— y añadir a la pérdida una penalización elástica que tira de esos pesos hacia su valor anterior, con fuerza proporcional a su importancia.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P145_ewc.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P145_ewc`](../../papers/foundational/P145_ewc/README.md)
- Notebook: [`P145_ewc.ipynb`](../../notebooks/papers/P145_ewc.ipynb)
- Evaluación: [`P145_ewc.md`](../../assessments/papers/P145_ewc.md)
- Clases del programa relacionadas:
- [176-aprendizaje-continuo-y-adaptacion](../../classes/part-14-frontier-research-and-capstones/176-aprendizaje-continuo-y-adaptacion/README.md)

---

[⬅️ Guías docentes del eje](README.md)
