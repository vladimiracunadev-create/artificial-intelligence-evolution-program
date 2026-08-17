# 👩‍🏫 Guía docente — P43 · Normalización por lotes: acelerar el entrenamiento profundo

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift* (2015, arXiv:1502.03167 · ICML 2015)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Entrenar redes profundas exigía inicializaciones cuidadosas y tasas de aprendizaje pequeñas: la distribución de las activaciones de cada capa se desplazaba durante el entrenamiento.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Normalizar cada activación usando la media y la varianza del minilote, y añadir dos parámetros aprendidos (γ, β) para que la red pueda deshacer la normalización si le conviene.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P43_batchnorm.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P43_batchnorm`](../../papers/foundational/P43_batchnorm/README.md)
- Notebook: [`P43_batchnorm.ipynb`](../../notebooks/papers/P43_batchnorm.ipynb)
- Evaluación: [`P43_batchnorm.md`](../../assessments/papers/P43_batchnorm.md)
- Clases del programa relacionadas:
- [051-activaciones-inicializacion-y-normalizacion](../../classes/part-04-neural-networks-and-deep-learning/051-activaciones-inicializacion-y-normalizacion/README.md)
- [052-optimizadores-regularizacion-y-schedulers](../../classes/part-04-neural-networks-and-deep-learning/052-optimizadores-regularizacion-y-schedulers/README.md)

---

[⬅️ Guías docentes del eje](README.md)
