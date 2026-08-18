# 👩‍🏫 Guía docente — P75 · Redes de vectores soporte

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Support-Vector Networks* (1995, Machine Learning, 20(3), 273–297)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Cuando varios clasificadores separan perfectamente los datos de entrenamiento, la exactitud no distingue entre ellos, y sin embargo generalizan de forma muy distinta.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Elegir el hiperplano de margen máximo —el que más lejos queda de los puntos de ambas clases— y extender la idea a fronteras no lineales con el truco del núcleo y a datos no separables con el margen blando.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P75_svm.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P75_svm`](../../papers/foundational/P75_svm/README.md)
- Notebook: [`P75_svm.ipynb`](../../notebooks/papers/P75_svm.ipynb)
- Evaluación: [`P75_svm.md`](../../assessments/papers/P75_svm.md)
- Clases del programa relacionadas:
- [039-clasificacion-logistica-y-umbrales](../../classes/part-03-classical-machine-learning/039-clasificacion-logistica-y-umbrales/README.md)

---

[⬅️ Guías docentes del eje](README.md)
