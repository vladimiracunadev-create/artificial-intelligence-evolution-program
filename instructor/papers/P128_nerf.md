# 👩‍🏫 Guía docente — P128 · NeRF: representar escenas como campos de radiancia neuronal

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis* (2020, ECCV 2020, 405–421)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Representar una escena 3D como rejilla de vóxeles cuesta O(n³) en memoria: la resolución se paga al cubo y las rejillas finas no caben. Y las mallas exigen reconstruir geometría explícita, que falla con pelo, humo o vidrio.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Codificar la escena como una función continua que va de posición y dirección de vista a color y densidad, representada por un perceptrón multicapa, y renderizar integrando esa función a lo largo de cada rayo con la ecuación de volumen.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P128_nerf.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P128_nerf`](../../papers/foundational/P128_nerf/README.md)
- Notebook: [`P128_nerf.ipynb`](../../notebooks/papers/P128_nerf.ipynb)
- Evaluación: [`P128_nerf.md`](../../assessments/papers/P128_nerf.md)
- Clases del programa relacionadas:
- [096-generacion-3d-y-mundos-sinteticos](../../classes/part-07-generative-ai-across-media/096-generacion-3d-y-mundos-sinteticos/README.md)

---

[⬅️ Guías docentes del eje](README.md)
