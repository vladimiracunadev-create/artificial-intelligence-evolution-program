# 👩‍🏫 Guía docente — P03 · Memoria larga de corto plazo

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Long Short-Term Memory* (1997, Neural Computation, 9(8), 1735–1780)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *En un RNN el gradiente se multiplica en cada paso temporal: se desvanece o explota, y la red no aprende dependencias largas.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Una celda con estado aditivo (carrusel de error constante) y puertas multiplicativas que deciden qué entra y qué sale.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P03_lstm.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P03_lstm`](../../papers/foundational/P03_lstm/README.md)
- Notebook: [`P03_lstm.ipynb`](../../notebooks/papers/P03_lstm.ipynb)
- Evaluación: [`P03_lstm.md`](../../assessments/papers/P03_lstm.md)
- Clases del programa relacionadas:
- [028-modelos-ocultos-de-markov](../../classes/part-02-probabilistic-evolutionary-and-decision-ai/028-modelos-ocultos-de-markov/README.md)
- [054-rnn-lstm-y-secuencias](../../classes/part-04-neural-networks-and-deep-learning/054-rnn-lstm-y-secuencias/README.md)

---

[⬅️ Guías docentes del eje](README.md)
