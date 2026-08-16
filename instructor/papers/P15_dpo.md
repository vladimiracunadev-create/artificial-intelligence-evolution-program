# 👩‍🏫 Guía docente — P15 · Optimización directa de preferencias: tu modelo de lenguaje ya es un modelo de recompensa

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Direct Preference Optimization: Your Language Model is Secretly a Reward Model* (2023, arXiv:2305.18290 · NeurIPS 2023)
**Nivel:** L4 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *El pipeline RLHF es frágil y caro: entrena un modelo extra, requiere muestreo on-policy y ajustar PPO es delicado.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Derivar la solución óptima del objetivo RLHF con restricción KL y reescribirlo como una pérdida de clasificación binaria sobre pares de preferencias.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P15_dpo.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P15_dpo`](../../papers/foundational/P15_dpo/README.md)
- Notebook: [`P15_dpo.ipynb`](../../notebooks/papers/P15_dpo.ipynb)
- Evaluación: [`P15_dpo.md`](../../assessments/papers/P15_dpo.md)
- Clases del programa relacionadas:
- [078-rlhf-rlaif-y-dpo](../../classes/part-06-foundation-models-and-llm-engineering/078-rlhf-rlaif-y-dpo/README.md)

---

[⬅️ Guías docentes del eje](README.md)
