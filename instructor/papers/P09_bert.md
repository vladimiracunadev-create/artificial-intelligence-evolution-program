# 👩‍🏫 Guía docente — P09 · BERT: preentrenamiento de Transformers bidireccionales profundos para comprensión del lenguaje

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding* (2018, arXiv:1810.04805 · NAACL-HLT 2019)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Los modelos de lenguaje eran unidireccionales; para comprender una palabra hace falta el contexto de ambos lados, y entrenar bidireccionalmente con predicción del siguiente token es trivialmente degenerado.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Modelado de lenguaje enmascarado (MLM) más predicción de la siguiente oración (NSP), y ajuste fino de todo el modelo por tarea.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P09_bert.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P09_bert`](../../papers/foundational/P09_bert/README.md)
- Notebook: [`P09_bert.ipynb`](../../notebooks/papers/P09_bert.ipynb)
- Evaluación: [`P09_bert.md`](../../assessments/papers/P09_bert.md)
- Clases del programa relacionadas:
- [065-clasificacion-extraccion-y-generacion-de-texto](../../classes/part-05-language-vision-audio-and-multimodal-ai/065-clasificacion-extraccion-y-generacion-de-texto/README.md)
- [074-objetivos-de-preentrenamiento](../../classes/part-06-foundation-models-and-llm-engineering/074-objetivos-de-preentrenamiento/README.md)

---

[⬅️ Guías docentes del eje](README.md)
