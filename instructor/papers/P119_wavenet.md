# 👩‍🏫 Guía docente — P119 · WaveNet: un modelo generativo de audio en crudo

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *WaveNet: A Generative Model for Raw Audio* (2016, arXiv:1609.03499)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Modelar audio directamente exige un contexto de miles de muestras: a 16 kHz, un segundo son 16 000 valores. Una convolución normal necesitaría miles de capas para verlo, y una recurrente no puede entrenarse en paralelo sobre esa longitud.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Convoluciones causales con dilatación que se duplica por capa: el campo receptivo crece de forma exponencial con la profundidad. Más cuantización μ-law para que 256 niveles basten sin que la voz suene rota.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P119_wavenet.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P119_wavenet`](../../papers/foundational/P119_wavenet/README.md)
- Notebook: [`P119_wavenet.ipynb`](../../notebooks/papers/P119_wavenet.ipynb)
- Evaluación: [`P119_wavenet.md`](../../assessments/papers/P119_wavenet.md)
- Clases del programa relacionadas:
- [068-sintesis-de-voz-y-clonacion-responsable](../../classes/part-05-language-vision-audio-and-multimodal-ai/068-sintesis-de-voz-y-clonacion-responsable/README.md)

---

[⬅️ Guías docentes del eje](README.md)
