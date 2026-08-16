# 👩‍🏫 Guía docente — P23 · GloVe: vectores globales para representación de palabras

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *GloVe: Global Vectors for Word Representation* (2014, EMNLP 2014 · ACL Anthology D14-1162)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Word2Vec aprendía de ventanas locales y desaprovechaba las estadísticas globales del corpus; los métodos de factorización usaban esas estadísticas pero producían peores analogías.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Ajustar por mínimos cuadrados ponderados el producto de vectores al logaritmo de la co-ocurrencia, con el argumento de que lo informativo es la RAZÓN de co-ocurrencias, no su valor bruto.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P23_glove.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P23_glove`](../../papers/foundational/P23_glove/README.md)
- Notebook: [`P23_glove.ipynb`](../../notebooks/papers/P23_glove.ipynb)
- Evaluación: [`P23_glove.md`](../../assessments/papers/P23_glove.md)
- Clases del programa relacionadas:
- [066-embeddings-semanticos-y-similitud](../../classes/part-05-language-vision-audio-and-multimodal-ai/066-embeddings-semanticos-y-similitud/README.md)

---

[⬅️ Guías docentes del eje](README.md)
