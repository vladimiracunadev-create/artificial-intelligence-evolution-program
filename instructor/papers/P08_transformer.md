# 👩‍🏫 Guía docente — P08 · La atención es todo lo que necesitas

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Attention Is All You Need* (2017, arXiv:1706.03762 · NeurIPS (NIPS) 2017)
**Nivel:** L4 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La recurrencia impone un cómputo secuencial en la longitud de la secuencia y camina O(n) pasos entre posiciones distantes; eso limita el entrenamiento a gran escala.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Un encoder–decoder compuesto solo de self-attention multi-cabeza, redes feed-forward por posición, conexiones residuales, layer normalization y codificación posicional.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P08_transformer.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P08_transformer`](../../papers/foundational/P08_transformer/README.md)
- Notebook: [`P08_transformer.ipynb`](../../notebooks/papers/P08_transformer.ipynb)
- Evaluación: [`P08_transformer.md`](../../assessments/papers/P08_transformer.md)
- Clases del programa relacionadas:
- [055-atencion-y-arquitectura-transformer](../../classes/part-04-neural-networks-and-deep-learning/055-atencion-y-arquitectura-transformer/README.md)
- [074-objetivos-de-preentrenamiento](../../classes/part-06-foundation-models-and-llm-engineering/074-objetivos-de-preentrenamiento/README.md)

---

[⬅️ Guías docentes del eje](README.md)
