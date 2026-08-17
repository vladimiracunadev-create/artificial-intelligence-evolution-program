# 👩‍🏫 Guía docente — P46 · Una imagen vale 16x16 palabras: Transformers para reconocimiento de imágenes a escala

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale* (2020, arXiv:2010.11929 · ICLR 2021)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La convolución traía de fábrica localidad y equivarianza a la traslación, y se asumía que sin esos sesgos inductivos la visión no funcionaría.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Partir la imagen en parches, proyectarlos como si fueran tokens, añadir codificación posicional y aplicar el encoder del Transformer sin más.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P46_vit.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P46_vit`](../../papers/foundational/P46_vit/README.md)
- Notebook: [`P46_vit.ipynb`](../../notebooks/papers/P46_vit.ipynb)
- Evaluación: [`P46_vit.md`](../../assessments/papers/P46_vit.md)
- Clases del programa relacionadas:
- [053-cnn-y-aprendizaje-espacial](../../classes/part-04-neural-networks-and-deep-learning/053-cnn-y-aprendizaje-espacial/README.md)
- [061-clasificacion-y-representacion-visual](../../classes/part-05-language-vision-audio-and-multimodal-ai/061-clasificacion-y-representacion-visual/README.md)
- [069-modelos-vision-lenguaje](../../classes/part-05-language-vision-audio-and-multimodal-ai/069-modelos-vision-lenguaje/README.md)

---

[⬅️ Guías docentes del eje](README.md)
