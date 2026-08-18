# 👩‍🏫 Guía docente — P112 · La puntuación de pruebas de ML: una rúbrica de preparación para producción

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction* (2017, IEEE Big Data 2017, 1123–1132)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La decisión de promocionar un modelo a producción se tomaba mirando su métrica de calidad. Nada garantizaba que existieran pruebas de los datos, de la infraestructura, de la capacidad de revertir ni de la monitorización.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Una rúbrica con cuatro categorías —datos, modelo, infraestructura y monitorización— y siete pruebas en cada una, con una puntuación global que es el **mínimo** entre categorías: un sistema es tan robusto como su parte más débil.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P112_ml_test_score.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P112_ml_test_score`](../../papers/foundational/P112_ml_test_score/README.md)
- Notebook: [`P112_ml_test_score.ipynb`](../../notebooks/papers/P112_ml_test_score.ipynb)
- Evaluación: [`P112_ml_test_score.md`](../../assessments/papers/P112_ml_test_score.md)
- Clases del programa relacionadas:
- [151-ci-cd-y-pruebas-para-sistemas-de-ia](../../classes/part-12-ai-engineering-mlops-llmops-and-agentops/151-ci-cd-y-pruebas-para-sistemas-de-ia/README.md)

---

[⬅️ Guías docentes del eje](README.md)
