# 👩‍🏫 Guía docente — P132 · Splatting de gaussianas 3D para renderizado de campos de radiancia en tiempo real

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *3D Gaussian Splatting for Real-Time Radiance Field Rendering* (2023, ACM Transactions on Graphics, 42(4))
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *NeRF produce vistas excelentes y renderiza lentísimo: cada píxel exige decenas de consultas a un perceptrón a lo largo de su rayo, y la mayoría caen en el vacío. Eso lo deja fuera de cualquier aplicación interactiva.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Representar la escena como un conjunto de gaussianas 3D anisótropas con color y opacidad, optimizadas desde las vistas de entrada, y renderizarlas proyectándolas y mezclándolas por orden de profundidad con un rasterizador diseñado a medida.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P132_gaussian_splatting.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P132_gaussian_splatting`](../../papers/foundational/P132_gaussian_splatting/README.md)
- Notebook: [`P132_gaussian_splatting.ipynb`](../../notebooks/papers/P132_gaussian_splatting.ipynb)
- Evaluación: [`P132_gaussian_splatting.md`](../../assessments/papers/P132_gaussian_splatting.md)
- Clases del programa relacionadas:
- [096-generacion-3d-y-mundos-sinteticos](../../classes/part-07-generative-ai-across-media/096-generacion-3d-y-mundos-sinteticos/README.md)

---

[⬅️ Guías docentes del eje](README.md)
