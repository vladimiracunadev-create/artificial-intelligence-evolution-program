# 👩‍🏫 Guía docente — P07 · Traducción automática neuronal aprendiendo conjuntamente a alinear y traducir

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Neural Machine Translation by Jointly Learning to Align and Translate* (2014, arXiv:1409.0473 · ICLR 2015)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Comprimir una frase entera en un vector fijo degrada la traducción de frases largas: es un cuello de botella de información.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Un vector de contexto distinto por paso de salida, calculado como suma ponderada de los estados del codificador con pesos aprendidos (atención aditiva).* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P07_attention_bahdanau.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P07_attention_bahdanau`](../../papers/foundational/P07_attention_bahdanau/README.md)
- Notebook: [`P07_attention_bahdanau.ipynb`](../../notebooks/papers/P07_attention_bahdanau.ipynb)
- Evaluación: [`P07_attention_bahdanau.md`](../../assessments/papers/P07_attention_bahdanau.md)
- Clases del programa relacionadas:
- [054-rnn-lstm-y-secuencias](../../classes/part-04-neural-networks-and-deep-learning/054-rnn-lstm-y-secuencias/README.md)
- [055-atencion-y-arquitectura-transformer](../../classes/part-04-neural-networks-and-deep-learning/055-atencion-y-arquitectura-transformer/README.md)

---

[⬅️ Guías docentes del eje](README.md)
