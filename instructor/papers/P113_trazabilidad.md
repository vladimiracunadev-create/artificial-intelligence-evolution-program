# 👩‍🏫 Guía docente — P113 · Aprendizaje por refuerzo profundo que importa

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Deep Reinforcement Learning That Matters* (2018, AAAI 2018)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Los resultados en aprendizaje por refuerzo se comparaban con tres o cinco corridas, sin declarar semillas, implementación ni hiperparámetros. Con la varianza real entre semillas, ese protocolo no distingue algoritmos: produce rankings que se invierten al repetir el experimento.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Medirlo. Ejecutar los mismos algoritmos con muchas semillas, con distintas implementaciones y en distintos entornos, y cuantificar cuánto de la diferencia publicada es señal y cuánto es elección de semilla, de código o de entorno.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P113_trazabilidad.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P113_trazabilidad`](../../papers/foundational/P113_trazabilidad/README.md)
- Notebook: [`P113_trazabilidad.ipynb`](../../notebooks/papers/P113_trazabilidad.ipynb)
- Evaluación: [`P113_trazabilidad.md`](../../assessments/papers/P113_trazabilidad.md)
- Clases del programa relacionadas:
- [149-experimentos-semillas-y-trazabilidad](../../classes/part-12-ai-engineering-mlops-llmops-and-agentops/149-experimentos-semillas-y-trazabilidad/README.md)

---

[⬅️ Guías docentes del eje](README.md)
