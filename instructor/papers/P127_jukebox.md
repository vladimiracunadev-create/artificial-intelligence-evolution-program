# 👩‍🏫 Guía docente — P127 · Jukebox: un modelo generativo de música

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Jukebox: A Generative Model for Music* (2020, arXiv:2005.00341)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Cuatro minutos de audio a 44,1 kHz son más de diez millones de muestras. Ningún modelo autorregresivo opera sobre esa longitud, y comprimir a una sola escala obliga a elegir entre estructura larga y detalle tímbrico.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Un cuantizador vectorial jerárquico que codifica el audio en tres niveles de compresión distintos, y un modelo autorregresivo por nivel: el grueso decide la estructura y los finos reconstruyen el timbre condicionados por él.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P127_jukebox.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P127_jukebox`](../../papers/foundational/P127_jukebox/README.md)
- Notebook: [`P127_jukebox.ipynb`](../../notebooks/papers/P127_jukebox.ipynb)
- Evaluación: [`P127_jukebox.md`](../../assessments/papers/P127_jukebox.md)
- Clases del programa relacionadas:
- [093-generacion-musical-y-de-audio](../../classes/part-07-generative-ai-across-media/093-generacion-musical-y-de-audio/README.md)

---

[⬅️ Guías docentes del eje](README.md)
