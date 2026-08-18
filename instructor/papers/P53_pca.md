# 👩‍🏫 Guía docente — P53 · Sobre las líneas y planos de ajuste más próximo a sistemas de puntos en el espacio

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *On Lines and Planes of Closest Fit to Systems of Points in Space* (1901, Philosophical Magazine, Series 6, 2(11), 559–572)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Los mínimos cuadrados miden el error en vertical, y por tanto tratan una variable como causa y la otra como efecto. Cuando ninguna de las dos lo es, hay dos rectas distintas y ningún criterio para elegir.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Buscar la recta —o el plano— que minimiza la distancia perpendicular a los puntos. Esa dirección es simétrica en todas las variables y da los ejes principales.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P53_pca.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P53_pca`](../../papers/foundational/P53_pca/README.md)
- Notebook: [`P53_pca.ipynb`](../../notebooks/papers/P53_pca.ipynb)
- Evaluación: [`P53_pca.md`](../../assessments/papers/P53_pca.md)
- Clases del programa relacionadas:
- [005-vectores-matrices-y-geometria-para-ia](../../classes/part-00-foundations-history-and-scientific-method/005-vectores-matrices-y-geometria-para-ia/README.md)
- [043-clustering-y-reduccion-de-dimensionalidad](../../classes/part-03-classical-machine-learning/043-clustering-y-reduccion-de-dimensionalidad/README.md)

---

[⬅️ Guías docentes del eje](README.md)
