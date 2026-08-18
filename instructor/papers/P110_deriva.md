# 👩‍🏫 Guía docente — P110 · Una revisión sobre adaptación a la deriva de concepto

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *A Survey on Concept Drift Adaptation* (2014, ACM Computing Surveys, 46(4), 1–37)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Un modelo se entrena con datos de un momento y se despliega sobre un flujo que cambia. La relación entre entradas y etiquetas puede cambiar sin que cambien las entradas, así que vigilar la distribución de entrada no basta y el modelo se degrada en silencio.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Una taxonomía de tipos de deriva —abrupta, gradual, incremental, recurrente— y de estrategias: detectores estadísticos sobre la tasa de error, ventanas adaptativas, conjuntos con reemplazo de miembros y reentrenamiento programado.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P110_deriva.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P110_deriva`](../../papers/foundational/P110_deriva/README.md)
- Notebook: [`P110_deriva.ipynb`](../../notebooks/papers/P110_deriva.ipynb)
- Evaluación: [`P110_deriva.md`](../../assessments/papers/P110_deriva.md)
- Clases del programa relacionadas:
- [154-deriva-feedback-y-evaluacion-continua](../../classes/part-12-ai-engineering-mlops-llmops-and-agentops/154-deriva-feedback-y-evaluacion-continua/README.md)

---

[⬅️ Guías docentes del eje](README.md)
