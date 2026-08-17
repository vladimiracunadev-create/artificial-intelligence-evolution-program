# 👩‍🏫 Guía docente — P40 · Dropout: una forma simple de evitar el sobreajuste en redes neuronales

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Dropout: A Simple Way to Prevent Neural Networks from Overfitting* (2014, JMLR 15(56):1929–1958)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Las redes grandes memorizaban el conjunto de entrenamiento, y las unidades desarrollaban co-adaptaciones frágiles: una función solo servía si su 'socia' estaba presente.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *En cada paso, poner a cero cada unidad con probabilidad p. Ninguna función puede depender de una unidad concreta, así que la red aprende representaciones redundantes.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P40_dropout.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P40_dropout`](../../papers/foundational/P40_dropout/README.md)
- Notebook: [`P40_dropout.ipynb`](../../notebooks/papers/P40_dropout.ipynb)
- Evaluación: [`P40_dropout.md`](../../assessments/papers/P40_dropout.md)
- Clases del programa relacionadas:
- [051-activaciones-inicializacion-y-normalizacion](../../classes/part-04-neural-networks-and-deep-learning/051-activaciones-inicializacion-y-normalizacion/README.md)
- [052-optimizadores-regularizacion-y-schedulers](../../classes/part-04-neural-networks-and-deep-learning/052-optimizadores-regularizacion-y-schedulers/README.md)

---

[⬅️ Guías docentes del eje](README.md)
