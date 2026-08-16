# 👩‍🏫 Guía docente — P20 · Mamba: modelado de secuencias en tiempo lineal con espacios de estados selectivos

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Mamba: Linear-Time Sequence Modeling with Selective State Spaces* (2023, arXiv:2312.00752 · COLM 2024 (Outstanding Paper Award))
**Nivel:** L4 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La atención cuesta O(n²) y su memoria crece con la secuencia; las alternativas subcuadráticas previas no alcanzaban a la atención en lenguaje.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Hacer que los parámetros del espacio de estados dependan de la ENTRADA (selección), y compensar la pérdida de la convolución eficiente con un algoritmo paralelo consciente del hardware.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P20_mamba.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P20_mamba`](../../papers/foundational/P20_mamba/README.md)
- Notebook: [`P20_mamba.ipynb`](../../notebooks/papers/P20_mamba.ipynb)
- Evaluación: [`P20_mamba.md`](../../assessments/papers/P20_mamba.md)
- Clases del programa relacionadas:
- [055-atencion-y-arquitectura-transformer](../../classes/part-04-neural-networks-and-deep-learning/055-atencion-y-arquitectura-transformer/README.md)
- [054-rnn-lstm-y-secuencias](../../classes/part-04-neural-networks-and-deep-learning/054-rnn-lstm-y-secuencias/README.md)

---

[⬅️ Guías docentes del eje](README.md)
