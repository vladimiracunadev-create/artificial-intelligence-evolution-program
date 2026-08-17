# 👩‍🏫 Guía docente — P12 · Entrenar modelos de lenguaje para seguir instrucciones con retroalimentación humana

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Training language models to follow instructions with human feedback* (2022, arXiv:2203.02155 · NeurIPS 2022)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Maximizar la verosimilitud del texto de internet no es lo mismo que ser útil, honesto e inocuo; el objetivo de entrenamiento está desalineado con la intención del usuario.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Tres etapas: ajuste supervisado con demostraciones, modelo de recompensa entrenado con comparaciones humanas y optimización por PPO con penalización KL.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P12_instructgpt_rlhf.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P12_instructgpt_rlhf`](../../papers/foundational/P12_instructgpt_rlhf/README.md)
- Notebook: [`P12_instructgpt_rlhf.ipynb`](../../notebooks/papers/P12_instructgpt_rlhf.ipynb)
- Evaluación: [`P12_instructgpt_rlhf.md`](../../assessments/papers/P12_instructgpt_rlhf.md)
- Clases del programa relacionadas:
- [076-instruction-tuning-y-datos-de-instrucciones](../../classes/part-06-foundation-models-and-llm-engineering/076-instruction-tuning-y-datos-de-instrucciones/README.md)
- [078-rlhf-rlaif-y-dpo](../../classes/part-06-foundation-models-and-llm-engineering/078-rlhf-rlaif-y-dpo/README.md)

---

[⬅️ Guías docentes del eje](README.md)
