# 👩‍🏫 Guía docente — P122 · Síntesis de voz natural condicionando WaveNet con espectrogramas mel predichos

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Natural TTS Synthesis by Conditioning WaveNet on Mel Spectrogram Predictions* (2018, ICASSP 2018, 4779–4783)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Predecir la forma de onda directamente desde el texto es intratable: tres segundos de audio son decenas de miles de pasos autorregresivos, y ningún modelo con atención puede alinear texto contra una secuencia de esa longitud.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Dos modelos con una interfaz explícita: uno predice el espectrograma mel desde el texto con atención, y un vocoder neuronal convierte ese espectrograma en forma de onda. Cada etapa se entrena y se sustituye por separado.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P122_tacotron.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P122_tacotron`](../../papers/foundational/P122_tacotron/README.md)
- Notebook: [`P122_tacotron.ipynb`](../../notebooks/papers/P122_tacotron.ipynb)
- Evaluación: [`P122_tacotron.md`](../../assessments/papers/P122_tacotron.md)
- Clases del programa relacionadas:
- [068-sintesis-de-voz-y-clonacion-responsable](../../classes/part-05-language-vision-audio-and-multimodal-ai/068-sintesis-de-voz-y-clonacion-responsable/README.md)

---

[⬅️ Guías docentes del eje](README.md)
