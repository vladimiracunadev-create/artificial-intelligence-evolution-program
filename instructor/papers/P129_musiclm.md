# 👩‍🏫 Guía docente — P129 · MusicLM: generar música a partir de texto

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *MusicLM: Generating Music From Text* (2023, arXiv:2301.11325)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Los pares texto-música son escasísimos comparados con los pares texto-imagen, y la música tiene estructura a escalas que no caben en una sola ventana de contexto: el timbre se juega en milisegundos y la forma, en minutos.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Una jerarquía de dos tipos de token —semánticos, a baja frecuencia, que llevan la estructura, y acústicos, a alta frecuencia, que llevan el detalle— y un entrenamiento que aprovecha audio sin etiquetar mediante una representación conjunta de texto y música.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P129_musiclm.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P129_musiclm`](../../papers/foundational/P129_musiclm/README.md)
- Notebook: [`P129_musiclm.ipynb`](../../notebooks/papers/P129_musiclm.ipynb)
- Evaluación: [`P129_musiclm.md`](../../assessments/papers/P129_musiclm.md)
- Clases del programa relacionadas:
- [093-generacion-musical-y-de-audio](../../classes/part-07-generative-ai-across-media/093-generacion-musical-y-de-audio/README.md)

---

[⬅️ Guías docentes del eje](README.md)
