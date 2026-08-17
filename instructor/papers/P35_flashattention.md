# 👩‍🏫 Guía docente — P35 · FlashAttention: atención exacta, rápida y eficiente en memoria, consciente de la E/S

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness* (2022, arXiv:2205.14135 · NeurIPS 2022)
**Nivel:** L4 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Durante años se atacó el coste O(n²) de la atención con aproximaciones (dispersa, lineal), que perdían calidad y a menudo ni siquiera eran más rápidas en la práctica.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Reorganizar el cálculo por bloques que caben en la memoria rápida del chip, evitando materializar la matriz de atención completa en la memoria lenta.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P35_flashattention.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P35_flashattention`](../../papers/foundational/P35_flashattention/README.md)
- Notebook: [`P35_flashattention.ipynb`](../../notebooks/papers/P35_flashattention.ipynb)
- Evaluación: [`P35_flashattention.md`](../../assessments/papers/P35_flashattention.md)
- Clases del programa relacionadas:
- [081-aceleradores-memoria-y-el-limite-real-del-computo](../../classes/part-06-foundation-models-and-llm-engineering/081-aceleradores-memoria-y-el-limite-real-del-computo/README.md)
- [085-cuantizacion-e-inferencia-local](../../classes/part-06-foundation-models-and-llm-engineering/085-cuantizacion-e-inferencia-local/README.md)

---

[⬅️ Guías docentes del eje](README.md)
