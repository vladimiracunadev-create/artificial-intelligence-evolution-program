# 👩‍🏫 Guía docente — P17 · Modelos probabilísticos de difusión con eliminación de ruido

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Denoising Diffusion Probabilistic Models* (2020, arXiv:2006.11239 · NeurIPS 2020)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Las GAN generaban imágenes de calidad pero eran inestables de entrenar y colapsaban la diversidad; los VAE eran estables y producían muestras borrosas.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Un proceso directo que añade ruido gaussiano en T pasos con forma cerrada, y una red que aprende a predecir ese ruido para invertirlo.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P17_diffusion.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P17_diffusion`](../../papers/foundational/P17_diffusion/README.md)
- Notebook: [`P17_diffusion.ipynb`](../../notebooks/papers/P17_diffusion.ipynb)
- Evaluación: [`P17_diffusion.md`](../../assessments/papers/P17_diffusion.md)
- Clases del programa relacionadas:
- [090-modelos-de-difusion](../../classes/part-07-generative-ai-across-media/090-modelos-de-difusion/README.md)
- [091-texto-a-imagen-y-condicionamiento](../../classes/part-07-generative-ai-across-media/091-texto-a-imagen-y-condicionamiento/README.md)
- [092-control-estructural-y-edicion-generativa](../../classes/part-07-generative-ai-across-media/092-control-estructural-y-edicion-generativa/README.md)
- [095-generacion-y-edicion-de-video](../../classes/part-07-generative-ai-across-media/095-generacion-y-edicion-de-video/README.md)

---

[⬅️ Guías docentes del eje](README.md)
