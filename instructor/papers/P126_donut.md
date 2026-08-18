# 👩‍🏫 Guía docente — P126 · Transformer de comprensión de documentos sin OCR

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *OCR-free Document Understanding Transformer* (2022, ECCV 2022, 498–517)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La tubería OCR más analizador arrastra dos costes: los errores del OCR llegan intactos al final y se componen carácter a carácter, y el OCR hay que licenciarlo y mantenerlo por idioma.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Un codificador de imagen y un decodificador que emite directamente la estructura —JSON, pares clave-valor—, preentrenado con la tarea de leer el documento completo. Sin etapa intermedia, no hay error que heredar.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P126_donut.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P126_donut`](../../papers/foundational/P126_donut/README.md)
- Notebook: [`P126_donut.ipynb`](../../notebooks/papers/P126_donut.ipynb)
- Evaluación: [`P126_donut.md`](../../assessments/papers/P126_donut.md)
- Clases del programa relacionadas:
- [063-ocr-y-comprension-de-documentos](../../classes/part-05-language-vision-audio-and-multimodal-ai/063-ocr-y-comprension-de-documentos/README.md)

---

[⬅️ Guías docentes del eje](README.md)
