# 👩‍🏫 Guía docente — P06 · Aprendizaje de secuencia a secuencia con redes neuronales

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Sequence to Sequence Learning with Neural Networks* (2014, arXiv:1409.3215 · NeurIPS (NIPS) 2014)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Las redes profundas requerían entradas y salidas de dimensión fija; la traducción automática dependía de sistemas estadísticos con muchas piezas separadas.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Un LSTM codifica la entrada en un vector de tamaño fijo y otro LSTM lo decodifica token a token; invertir la secuencia fuente mejora el resultado.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P06_seq2seq.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P06_seq2seq`](../../papers/foundational/P06_seq2seq/README.md)
- Notebook: [`P06_seq2seq.ipynb`](../../notebooks/papers/P06_seq2seq.ipynb)
- Evaluación: [`P06_seq2seq.md`](../../assessments/papers/P06_seq2seq.md)
- Clases del programa relacionadas:
- [054-rnn-lstm-y-secuencias](../../classes/part-04-neural-networks-and-deep-learning/054-rnn-lstm-y-secuencias/README.md)
- [055-atencion-y-arquitectura-transformer](../../classes/part-04-neural-networks-and-deep-learning/055-atencion-y-arquitectura-transformer/README.md)
- [067-reconocimiento-automatico-del-habla](../../classes/part-05-language-vision-audio-and-multimodal-ai/067-reconocimiento-automatico-del-habla/README.md)

---

[⬅️ Guías docentes del eje](README.md)
