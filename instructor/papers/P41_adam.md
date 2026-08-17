# 👩‍🏫 Guía docente — P41 · Adam: un método de optimización estocástica

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Adam: A Method for Stochastic Optimization* (2014, arXiv:1412.6980 · ICLR 2015)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *SGD usa la misma tasa de aprendizaje en todas las direcciones. En un problema mal condicionado, o oscila en las direcciones de mucha curvatura o se arrastra en las de poca.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Mantener medias móviles del gradiente (primer momento) y de su cuadrado (segundo momento), con corrección de sesgo, y normalizar el paso de cada coordenada por su magnitud típica.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P41_adam.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P41_adam`](../../papers/foundational/P41_adam/README.md)
- Notebook: [`P41_adam.ipynb`](../../notebooks/papers/P41_adam.ipynb)
- Evaluación: [`P41_adam.md`](../../assessments/papers/P41_adam.md)
- Clases del programa relacionadas:
- [052-optimizadores-regularizacion-y-schedulers](../../classes/part-04-neural-networks-and-deep-learning/052-optimizadores-regularizacion-y-schedulers/README.md)

---

[⬅️ Guías docentes del eje](README.md)
