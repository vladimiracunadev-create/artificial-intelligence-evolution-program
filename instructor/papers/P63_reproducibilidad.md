# 👩‍🏫 Guía docente — P63 · Mejorar la reproducibilidad en la investigación en aprendizaje automático

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Improving Reproducibility in Machine Learning Research (A Report from the NeurIPS 2019 Reproducibility Program)* (2021, Journal of Machine Learning Research, 22(164), 1–20)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Los resultados se comparaban sin declarar semillas, entorno, búsqueda de hiperparámetros ni número de corridas. Muchas mejoras publicadas no sobrevivían a un intento de repetirlas.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Un checklist obligatorio en el envío, un desafío de reproducibilidad y política de código, con evidencia empírica de su efecto sobre lo que se publica.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P63_reproducibilidad.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P63_reproducibilidad`](../../papers/foundational/P63_reproducibilidad/README.md)
- Notebook: [`P63_reproducibilidad.ipynb`](../../notebooks/papers/P63_reproducibilidad.ipynb)
- Evaluación: [`P63_reproducibilidad.md`](../../assessments/papers/P63_reproducibilidad.md)
- Clases del programa relacionadas:
- [009-entornos-python-git-y-experimentos-reproducibles](../../classes/part-00-foundations-history-and-scientific-method/009-entornos-python-git-y-experimentos-reproducibles/README.md)

---

[⬅️ Guías docentes del eje](README.md)
