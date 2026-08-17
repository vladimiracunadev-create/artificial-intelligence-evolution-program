# 👩‍🏫 Guía docente — P38 · Bayes variacional con autocodificación

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Auto-Encoding Variational Bayes* (2013, arXiv:1312.6114 · ICLR 2014)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Un modelo generativo con variables latentes exige muestrear, y muestrear es un nodo estocástico que bloquea el gradiente: no se podía entrenar por retropropagación.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Escribir la muestra como z = μ + σ·ε con ε de una normal fija: el azar queda fuera del camino del gradiente, y se optimiza una cota inferior de la verosimilitud (ELBO).* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P38_vae.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P38_vae`](../../papers/foundational/P38_vae/README.md)
- Notebook: [`P38_vae.ipynb`](../../notebooks/papers/P38_vae.ipynb)
- Evaluación: [`P38_vae.md`](../../assessments/papers/P38_vae.md)
- Clases del programa relacionadas:
- [058-autoencoders-gan-y-difusion](../../classes/part-04-neural-networks-and-deep-learning/058-autoencoders-gan-y-difusion/README.md)
- [088-espacios-latentes-y-autoencoders-variacionales](../../classes/part-07-generative-ai-across-media/088-espacios-latentes-y-autoencoders-variacionales/README.md)

---

[⬅️ Guías docentes del eje](README.md)
