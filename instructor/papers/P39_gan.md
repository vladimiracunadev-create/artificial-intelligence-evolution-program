# 👩‍🏫 Guía docente — P39 · Redes generativas adversarias

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Generative Adversarial Networks* (2014, arXiv:1406.2661 · NeurIPS 2014)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Los modelos generativos exigían definir y optimizar una verosimilitud, lo que obligaba a aproximaciones costosas o producía muestras borrosas.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Entrenar un generador contra un discriminador en un juego minimax: el generador gana cuando el discriminador ya no distingue lo real de lo sintético.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P39_gan.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P39_gan`](../../papers/foundational/P39_gan/README.md)
- Notebook: [`P39_gan.ipynb`](../../notebooks/papers/P39_gan.ipynb)
- Evaluación: [`P39_gan.md`](../../assessments/papers/P39_gan.md)
- Clases del programa relacionadas:
- [089-gan-y-entrenamiento-adversarial](../../classes/part-07-generative-ai-across-media/089-gan-y-entrenamiento-adversarial/README.md)
- [058-autoencoders-gan-y-difusion](../../classes/part-04-neural-networks-and-deep-learning/058-autoencoders-gan-y-difusion/README.md)

---

[⬅️ Guías docentes del eje](README.md)
