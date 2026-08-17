# 👩‍🏫 Guía docente — P18 · Aprender modelos visuales transferibles con supervisión de lenguaje natural

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Learning Transferable Visual Models From Natural Language Supervision* (2021, arXiv:2103.00020 · ICML 2021)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La visión dependía de conjuntos etiquetados con categorías fijas; cambiar de tarea exigía volver a anotar y volver a entrenar.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Entrenar de forma contrastiva sobre 400 millones de pares (imagen, texto) de internet, alineando ambos espacios, y clasificar comparando la imagen con el texto de cada clase.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P18_clip.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P18_clip`](../../papers/foundational/P18_clip/README.md)
- Notebook: [`P18_clip.ipynb`](../../notebooks/papers/P18_clip.ipynb)
- Evaluación: [`P18_clip.md`](../../assessments/papers/P18_clip.md)
- Clases del programa relacionadas:
- [062-deteccion-segmentacion-y-pose](../../classes/part-05-language-vision-audio-and-multimodal-ai/062-deteccion-segmentacion-y-pose/README.md)
- [069-modelos-vision-lenguaje](../../classes/part-05-language-vision-audio-and-multimodal-ai/069-modelos-vision-lenguaje/README.md)
- [070-fusion-multimodal-y-representacion-conjunta](../../classes/part-05-language-vision-audio-and-multimodal-ai/070-fusion-multimodal-y-representacion-conjunta/README.md)

---

[⬅️ Guías docentes del eje](README.md)
