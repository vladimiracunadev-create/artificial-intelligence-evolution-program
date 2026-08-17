# 👩‍🏫 Guía docente — P49 · QLoRA: ajuste fino eficiente de modelos cuantizados

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *QLoRA: Efficient Finetuning of Quantized LLMs* (2023, arXiv:2305.14314 · NeurIPS 2023)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *LoRA reduce los parámetros entrenables, pero el modelo base seguía teniendo que caber en memoria en precisión alta: eso dejaba fuera a casi todo el mundo.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Cuantizar el modelo base congelado a 4 bits con un formato adaptado a la distribución de los pesos, y entrenar encima adaptadores LoRA en precisión alta.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P49_qlora.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P49_qlora`](../../papers/foundational/P49_qlora/README.md)
- Notebook: [`P49_qlora.ipynb`](../../notebooks/papers/P49_qlora.ipynb)
- Evaluación: [`P49_qlora.md`](../../assessments/papers/P49_qlora.md)
- Clases del programa relacionadas:
- [077-lora-qlora-y-adaptacion-eficiente](../../classes/part-06-foundation-models-and-llm-engineering/077-lora-qlora-y-adaptacion-eficiente/README.md)
- [082-dimensionar-hardware-de-la-laptop-al-cluster](../../classes/part-06-foundation-models-and-llm-engineering/082-dimensionar-hardware-de-la-laptop-al-cluster/README.md)
- [085-cuantizacion-e-inferencia-local](../../classes/part-06-foundation-models-and-llm-engineering/085-cuantizacion-e-inferencia-local/README.md)

---

[⬅️ Guías docentes del eje](README.md)
