# 👩‍🏫 Guía docente — P115 · Hojas de datos para conjuntos de datos

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Datasheets for Datasets* (2021, Communications of the ACM, 64(12), 86–92)
**Nivel:** L1 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Los conjuntos de datos se comparten sin documentación sobre su origen, su composición, los filtros aplicados o los usos desaconsejados. Quien los reutiliza hereda supuestos que nadie escribió, y muchas de esas preguntas ya no se pueden responder a posteriori.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Un cuestionario que sigue el ciclo de vida del conjunto —motivación, composición, recogida, preprocesado, usos, distribución y mantenimiento— y que hay que responder **mientras se crea**, no después.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P115_hojas_de_datos.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P115_hojas_de_datos`](../../papers/foundational/P115_hojas_de_datos/README.md)
- Notebook: [`P115_hojas_de_datos.ipynb`](../../notebooks/papers/P115_hojas_de_datos.ipynb)
- Evaluación: [`P115_hojas_de_datos.md`](../../assessments/papers/P115_hojas_de_datos.md)
- Clases del programa relacionadas:
- [148-ciclo-de-vida-de-datos-modelos-y-agentes](../../classes/part-12-ai-engineering-mlops-llmops-and-agentops/148-ciclo-de-vida-de-datos-modelos-y-agentes/README.md)

---

[⬅️ Guías docentes del eje](README.md)
