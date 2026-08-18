# 👩‍🏫 Guía docente — P131 · Una marca de agua para modelos de lenguaje grandes

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *A Watermark for Large Language Models* (2023, ICML 2023 · arXiv:2301.10226)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Distinguir texto generado de texto humano se intentaba con clasificadores entrenados a posteriori, que fallan, envejecen con cada modelo nuevo y producen falsos positivos con consecuencias reales sobre personas.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Partir el vocabulario en cada paso en una lista «verde» y otra «roja», determinadas por un hash del token anterior, y sesgar la generación hacia la verde. Un texto marcado tiene una proporción de verdes anómala, y una prueba estadística la detecta sin acceso al modelo.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P131_marcas_de_agua.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P131_marcas_de_agua`](../../papers/foundational/P131_marcas_de_agua/README.md)
- Notebook: [`P131_marcas_de_agua.ipynb`](../../notebooks/papers/P131_marcas_de_agua.ipynb)
- Evaluación: [`P131_marcas_de_agua.md`](../../assessments/papers/P131_marcas_de_agua.md)
- Clases del programa relacionadas:
- [098-procedencia-marcas-y-autenticidad](../../classes/part-07-generative-ai-across-media/098-procedencia-marcas-y-autenticidad/README.md)

---

[⬅️ Guías docentes del eje](README.md)
