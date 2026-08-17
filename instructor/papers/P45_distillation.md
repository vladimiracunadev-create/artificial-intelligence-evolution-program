# 👩‍🏫 Guía docente — P45 · Destilar el conocimiento de una red neuronal

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Distilling the Knowledge in a Neural Network* (2015, arXiv:1503.02531)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Los modelos grandes o los conjuntos de modelos daban los mejores resultados pero eran caros de servir, y entrenar el modelo pequeño con las etiquetas duras daba mucho peor resultado.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Entrenar el modelo pequeño para reproducir la distribución completa del maestro, suavizada con una temperatura que revela la estructura de similitud entre clases.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P45_distillation.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P45_distillation`](../../papers/foundational/P45_distillation/README.md)
- Notebook: [`P45_distillation.ipynb`](../../notebooks/papers/P45_distillation.ipynb)
- Evaluación: [`P45_distillation.md`](../../assessments/papers/P45_distillation.md)
- Clases del programa relacionadas:
- [059-transferencia-fine-tuning-y-destilacion](../../classes/part-04-neural-networks-and-deep-learning/059-transferencia-fine-tuning-y-destilacion/README.md)
- [086-seleccion-de-modelo-costo-latencia-y-privacidad](../../classes/part-06-foundation-models-and-llm-engineering/086-seleccion-de-modelo-costo-latencia-y-privacidad/README.md)
- [157-costo-latencia-caching-y-capacidad](../../classes/part-12-ai-engineering-mlops-llmops-and-agentops/157-costo-latencia-caching-y-capacidad/README.md)

---

[⬅️ Guías docentes del eje](README.md)
