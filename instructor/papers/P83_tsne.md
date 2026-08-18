# 👩‍🏫 Guía docente — P83 · Visualizar datos con t-SNE

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Visualizing Data using t-SNE* (2008, Journal of Machine Learning Research, 9, 2579–2605)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Al proyectar de muchas dimensiones a dos, los puntos moderadamente distantes se apiñan en el centro: en dimensión alta hay mucho más «sitio lejos» que cerca, y una gaussiana en el mapa no puede acomodarlo. Es el problema del apiñamiento.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Convertir distancias en probabilidades de vecindad, y usar en el mapa una distribución t de Student de un grado de libertad. Su cola pesada deja sitio a los puntos lejanos sin comprimir los cercanos.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P83_tsne.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P83_tsne`](../../papers/foundational/P83_tsne/README.md)
- Notebook: [`P83_tsne.ipynb`](../../notebooks/papers/P83_tsne.ipynb)
- Evaluación: [`P83_tsne.md`](../../assessments/papers/P83_tsne.md)
- Clases del programa relacionadas:
- [043-clustering-y-reduccion-de-dimensionalidad](../../classes/part-03-classical-machine-learning/043-clustering-y-reduccion-de-dimensionalidad/README.md)

---

[⬅️ Guías docentes del eje](README.md)
