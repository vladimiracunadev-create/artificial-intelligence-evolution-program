# 👩‍🏫 Guía docente — P87 · Ensayo para resolver un problema en la doctrina de las probabilidades

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *An Essay towards solving a Problem in the Doctrine of Chances* (1763, Philosophical Transactions of the Royal Society, 53, 370–418)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La probabilidad sabía calcular qué datos esperar dada una causa conocida. La pregunta inversa —qué causa es probable dados los datos observados— no tenía tratamiento, y es la que hace falta para aprender de la experiencia.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Tratar la causa desconocida como una cantidad con distribución previa, y actualizarla con la verosimilitud de lo observado. En forma de odds, la actualización es una multiplicación por la razón de verosimilitud.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P87_bayes.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P87_bayes`](../../papers/foundational/P87_bayes/README.md)
- Notebook: [`P87_bayes.ipynb`](../../notebooks/papers/P87_bayes.ipynb)
- Evaluación: [`P87_bayes.md`](../../assessments/papers/P87_bayes.md)
- Clases del programa relacionadas:
- [026-teorema-de-bayes-y-actualizacion-de-creencias](../../classes/part-02-probabilistic-evolutionary-and-decision-ai/026-teorema-de-bayes-y-actualizacion-de-creencias/README.md)

---

[⬅️ Guías docentes del eje](README.md)
