# 👩‍🏫 Guía docente — P108 · CAP doce años después: cómo han cambiado las «reglas»

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *CAP Twelve Years Later: How the «Rules» Have Changed* (2012, IEEE Computer, 45(2), 23–29)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *El teorema CAP se citaba como «elige dos de consistencia, disponibilidad y tolerancia a particiones», y eso llevó a decisiones de arquitectura globales y rígidas: sistemas enteros declarados AP o CP.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Reformularlo con precisión: la tolerancia a particiones no es opcional, y la elección entre consistencia y disponibilidad solo aplica **durante** una partición. Se decide por operación, y hay que diseñar explícitamente la detección de la partición, el modo degradado y la reconciliación posterior.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P108_cap.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P108_cap`](../../papers/foundational/P108_cap/README.md)
- Notebook: [`P108_cap.ipynb`](../../notebooks/papers/P108_cap.ipynb)
- Evaluación: [`P108_cap.md`](../../assessments/papers/P108_cap.md)
- Clases del programa relacionadas:
- [158-resiliencia-idempotencia-rollback-y-recuperacion](../../classes/part-12-ai-engineering-mlops-llmops-and-agentops/158-resiliencia-idempotencia-rollback-y-recuperacion/README.md)

---

[⬅️ Guías docentes del eje](README.md)
