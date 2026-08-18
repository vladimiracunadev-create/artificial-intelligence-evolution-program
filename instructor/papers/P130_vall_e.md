# 👩‍🏫 Guía docente — P130 · Los modelos de lenguaje sobre códecs neuronales sintetizan voz sin ejemplos previos

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Neural Codec Language Models are Zero-Shot Text to Speech Synthesizers* (2023, arXiv:2301.02111)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Adaptar un sintetizador a una voz nueva exigía media hora o más de grabaciones y un ajuste fino del modelo. Eso limitaba la personalización a quien tuviera estudio, y de paso actuaba como barrera práctica frente al uso indebido.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Tratar los códigos de un códec neuronal como un vocabulario y la síntesis como predicción del siguiente token, con la voz objetivo entrada como aviso en contexto. Sin entrenamiento por hablante: tres segundos bastan.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P130_vall_e.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P130_vall_e`](../../papers/foundational/P130_vall_e/README.md)
- Notebook: [`P130_vall_e.ipynb`](../../notebooks/papers/P130_vall_e.ipynb)
- Evaluación: [`P130_vall_e.md`](../../assessments/papers/P130_vall_e.md)
- Clases del programa relacionadas:
- [094-sintesis-de-voz-y-derechos-de-identidad](../../classes/part-07-generative-ai-across-media/094-sintesis-de-voz-y-derechos-de-identidad/README.md)

---

[⬅️ Guías docentes del eje](README.md)
