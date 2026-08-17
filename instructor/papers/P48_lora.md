# 👩‍🏫 Guía docente — P48 · LoRA: adaptación de rango bajo de modelos de lenguaje grandes

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *LoRA: Low-Rank Adaptation of Large Language Models* (2021, arXiv:2106.09685 · ICLR 2022)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *El ajuste fino completo exige una copia entera del modelo por tarea: inviable en almacenamiento y en memoria de entrenamiento cuando el modelo tiene miles de millones de parámetros.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Congelar los pesos originales y aprender una actualización factorizada de rango bajo, W' = W + BA, que al desplegar se puede fusionar con W.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P48_lora.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P48_lora`](../../papers/foundational/P48_lora/README.md)
- Notebook: [`P48_lora.ipynb`](../../notebooks/papers/P48_lora.ipynb)
- Evaluación: [`P48_lora.md`](../../assessments/papers/P48_lora.md)
- Clases del programa relacionadas:
- [077-lora-qlora-y-adaptacion-eficiente](../../classes/part-06-foundation-models-and-llm-engineering/077-lora-qlora-y-adaptacion-eficiente/README.md)

---

[⬅️ Guías docentes del eje](README.md)
