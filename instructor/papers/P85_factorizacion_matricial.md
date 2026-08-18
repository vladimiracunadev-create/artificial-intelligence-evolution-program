# 👩‍🏫 Guía docente — P85 · Técnicas de factorización matricial para sistemas de recomendación

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Matrix Factorization Techniques for Recommender Systems* (2009, IEEE Computer, 42(8), 30–37)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Recomendar exige predecir puntuaciones en una matriz usuario×artículo donde falta el 99 % de las celdas. Los métodos por vecindad escalaban mal y no capturaban estructura latente.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Aprender un vector de factores latentes por usuario y por artículo, ajustados solo sobre las celdas observadas por descenso de gradiente, con regularización y con términos de sesgo explícitos para usuario y artículo.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P85_factorizacion_matricial.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P85_factorizacion_matricial`](../../papers/foundational/P85_factorizacion_matricial/README.md)
- Notebook: [`P85_factorizacion_matricial.ipynb`](../../notebooks/papers/P85_factorizacion_matricial.ipynb)
- Evaluación: [`P85_factorizacion_matricial.md`](../../assessments/papers/P85_factorizacion_matricial.md)
- Clases del programa relacionadas:
- [046-sistemas-de-recomendacion](../../classes/part-03-classical-machine-learning/046-sistemas-de-recomendacion/README.md)

---

[⬅️ Guías docentes del eje](README.md)
