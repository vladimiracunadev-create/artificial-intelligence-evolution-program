# 👩‍🏫 Guía docente — P44 · Aprendizaje residual profundo para reconocimiento de imágenes

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Deep Residual Learning for Image Recognition* (2015, arXiv:1512.03385 · CVPR 2016)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Al pasar de 20 a 56 capas, el error de ENTRENAMIENTO subía. No era sobreajuste: era que las redes muy profundas se habían vuelto imposibles de optimizar.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Que cada bloque aprenda un residuo F(x) y la salida sea F(x) + x. Si la capa no aporta, aprender F ≈ 0 es fácil, y el gradiente siempre tiene una ruta directa.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P44_resnet.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P44_resnet`](../../papers/foundational/P44_resnet/README.md)
- Notebook: [`P44_resnet.ipynb`](../../notebooks/papers/P44_resnet.ipynb)
- Evaluación: [`P44_resnet.md`](../../assessments/papers/P44_resnet.md)
- Clases del programa relacionadas:
- [051-activaciones-inicializacion-y-normalizacion](../../classes/part-04-neural-networks-and-deep-learning/051-activaciones-inicializacion-y-normalizacion/README.md)
- [053-cnn-y-aprendizaje-espacial](../../classes/part-04-neural-networks-and-deep-learning/053-cnn-y-aprendizaje-espacial/README.md)
- [061-clasificacion-y-representacion-visual](../../classes/part-05-language-vision-audio-and-multimodal-ai/061-clasificacion-y-representacion-visual/README.md)
- [062-deteccion-segmentacion-y-pose](../../classes/part-05-language-vision-audio-and-multimodal-ai/062-deteccion-segmentacion-y-pose/README.md)

---

[⬅️ Guías docentes del eje](README.md)
