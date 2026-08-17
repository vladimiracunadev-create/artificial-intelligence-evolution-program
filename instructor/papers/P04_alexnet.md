# 👩‍🏫 Guía docente — P04 · Clasificación de ImageNet con redes neuronales convolucionales profundas

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *ImageNet Classification with Deep Convolutional Neural Networks* (2012, NeurIPS (NIPS) 2012)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La visión por computador dependía de descriptores diseñados manualmente; escalar el aprendizaje de features a millones de imágenes era inviable.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Una CNN profunda entrenada en GPU con ReLU, dropout, aumento de datos y solapamiento de pooling sobre ILSVRC-2012.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P04_alexnet.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P04_alexnet`](../../papers/foundational/P04_alexnet/README.md)
- Notebook: [`P04_alexnet.ipynb`](../../notebooks/papers/P04_alexnet.ipynb)
- Evaluación: [`P04_alexnet.md`](../../assessments/papers/P04_alexnet.md)
- Clases del programa relacionadas:
- [053-cnn-y-aprendizaje-espacial](../../classes/part-04-neural-networks-and-deep-learning/053-cnn-y-aprendizaje-espacial/README.md)
- [061-clasificacion-y-representacion-visual](../../classes/part-05-language-vision-audio-and-multimodal-ai/061-clasificacion-y-representacion-visual/README.md)
- [062-deteccion-segmentacion-y-pose](../../classes/part-05-language-vision-audio-and-multimodal-ai/062-deteccion-segmentacion-y-pose/README.md)

---

[⬅️ Guías docentes del eje](README.md)
