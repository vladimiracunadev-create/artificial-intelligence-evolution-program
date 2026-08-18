# 👩‍🏫 Guía docente — P123 · SentencePiece: un tokenizador y detokenizador de subpalabras simple e independiente del idioma

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing* (2018, EMNLP 2018 (demos), 66–71)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *BPE suponía texto ya partido por espacios, y eso no es universal: el japonés y el chino no los usan. Además cada implementación normalizaba a su manera, así que reconstruir el texto original era imposible y los resultados no eran comparables.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Tratar la entrada como un flujo de caracteres crudo, codificar el espacio como un símbolo más del vocabulario, y ofrecer también un modelo unigrama donde la segmentación es inferencia probabilística y se puede muestrear para regularizar.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P123_sentencepiece.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P123_sentencepiece`](../../papers/foundational/P123_sentencepiece/README.md)
- Notebook: [`P123_sentencepiece.ipynb`](../../notebooks/papers/P123_sentencepiece.ipynb)
- Evaluación: [`P123_sentencepiece.md`](../../assessments/papers/P123_sentencepiece.md)
- Clases del programa relacionadas:
- [073-tokenizacion-moderna-y-vocabularios](../../classes/part-06-foundation-models-and-llm-engineering/073-tokenizacion-moderna-y-vocabularios/README.md)

---

[⬅️ Guías docentes del eje](README.md)
