# 👩‍🏫 Guía docente — P05 · Estimación eficiente de representaciones de palabras en un espacio vectorial

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Efficient Estimation of Word Representations in Vector Space* (2013, arXiv:1301.3781 · ICLR 2013 (workshop))
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Representar palabras como identificadores dispersos (one-hot) impide medir similitud; los modelos neuronales de lenguaje previos eran demasiado costosos.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Dos arquitecturas log-lineales sin capa oculta —CBOW y skip-gram— que predicen contexto y producen vectores con estructura lineal.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P05_word2vec.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P05_word2vec`](../../papers/foundational/P05_word2vec/README.md)
- Notebook: [`P05_word2vec.ipynb`](../../notebooks/papers/P05_word2vec.ipynb)
- Evaluación: [`P05_word2vec.md`](../../assessments/papers/P05_word2vec.md)
- Clases del programa relacionadas:
- [064-tokenizacion-y-representacion-del-lenguaje](../../classes/part-05-language-vision-audio-and-multimodal-ai/064-tokenizacion-y-representacion-del-lenguaje/README.md)
- [066-embeddings-semanticos-y-similitud](../../classes/part-05-language-vision-audio-and-multimodal-ai/066-embeddings-semanticos-y-similitud/README.md)
- [100-embeddings-y-busqueda-vectorial](../../classes/part-08-retrieval-context-memory-and-knowledge/100-embeddings-y-busqueda-vectorial/README.md)
- [166-sesgo-fairness-y-grupos-afectados](../../classes/part-13-evaluation-safety-security-and-governance/166-sesgo-fairness-y-grupos-afectados/README.md)

---

[⬅️ Guías docentes del eje](README.md)
