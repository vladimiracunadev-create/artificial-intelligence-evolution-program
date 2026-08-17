# 👩‍🏫 Guía docente — P24 · Representaciones profundas de palabras dependientes del contexto

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Deep Contextualized Word Representations* (2018, NAACL 2018 · ACL Anthology N18-1202)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Un embedding estático da el mismo vector a «banco del parque» y «banco central»: el sentido se pierde antes de que el modelo empiece a trabajar.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Usar los estados internos de un modelo de lenguaje bidireccional profundo y combinar sus capas con pesos aprendidos por tarea.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P24_elmo.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P24_elmo`](../../papers/foundational/P24_elmo/README.md)
- Notebook: [`P24_elmo.ipynb`](../../notebooks/papers/P24_elmo.ipynb)
- Evaluación: [`P24_elmo.md`](../../assessments/papers/P24_elmo.md)
- Clases del programa relacionadas:
- [065-clasificacion-extraccion-y-generacion-de-texto](../../classes/part-05-language-vision-audio-and-multimodal-ai/065-clasificacion-extraccion-y-generacion-de-texto/README.md)
- [066-embeddings-semanticos-y-similitud](../../classes/part-05-language-vision-audio-and-multimodal-ai/066-embeddings-semanticos-y-similitud/README.md)

---

[⬅️ Guías docentes del eje](README.md)
