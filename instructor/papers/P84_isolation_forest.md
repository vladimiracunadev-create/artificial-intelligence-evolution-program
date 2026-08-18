# 👩‍🏫 Guía docente — P84 · Bosque de aislamiento

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Isolation Forest* (2008, ICDM 2008, 413–422)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Los métodos de detección de anomalías construían un modelo de la normalidad y medían la distancia a él. Eso cuesta caro, supone una forma para la distribución normal y dedica casi todo el esfuerzo a los puntos que no interesan.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Cortar el espacio al azar y contar cuántos cortes hacen falta para dejar cada punto solo. Lo raro vive en zonas poco pobladas y se aísla antes; la longitud media del camino, normalizada, es la puntuación de anomalía.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P84_isolation_forest.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P84_isolation_forest`](../../papers/foundational/P84_isolation_forest/README.md)
- Notebook: [`P84_isolation_forest.ipynb`](../../notebooks/papers/P84_isolation_forest.ipynb)
- Evaluación: [`P84_isolation_forest.md`](../../assessments/papers/P84_isolation_forest.md)
- Clases del programa relacionadas:
- [044-deteccion-de-anomalias](../../classes/part-03-classical-machine-learning/044-deteccion-de-anomalias/README.md)

---

[⬅️ Guías docentes del eje](README.md)
