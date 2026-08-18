# 👩‍🏫 Guía docente — P125 · LayoutLM: preentrenamiento de texto y disposición para comprensión de documentos

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *LayoutLM: Pre-training of Text and Layout for Document Image Understanding* (2020, KDD 2020, 1192–1200)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Un documento no es una secuencia de texto: es texto colocado. Al linealizar una factura de dos columnas, el OCR intercala campos que no se relacionan, y un modelo que solo ve la cadena no puede emparejar cada etiqueta con su valor.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Preentrenar sobre millones de documentos escaneados un modelo que recibe, para cada token, su texto y las coordenadas de su caja delimitadora, con objetivos de enmascarado que obligan a usar las dos señales.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P125_layoutlm.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P125_layoutlm`](../../papers/foundational/P125_layoutlm/README.md)
- Notebook: [`P125_layoutlm.ipynb`](../../notebooks/papers/P125_layoutlm.ipynb)
- Evaluación: [`P125_layoutlm.md`](../../assessments/papers/P125_layoutlm.md)
- Clases del programa relacionadas:
- [063-ocr-y-comprension-de-documentos](../../classes/part-05-language-vision-audio-and-multimodal-ai/063-ocr-y-comprension-de-documentos/README.md)

---

[⬅️ Guías docentes del eje](README.md)
