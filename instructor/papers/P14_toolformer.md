# 👩‍🏫 Guía docente — P14 · Toolformer: los modelos de lenguaje pueden enseñarse a sí mismos a usar herramientas

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Toolformer: Language Models Can Teach Themselves to Use Tools* (2023, arXiv:2302.04761 · NeurIPS 2023)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Enseñar a un modelo a llamar APIs requería datos anotados por humanos, caros y limitados a las herramientas anotadas.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Generar llamadas candidatas, ejecutarlas y conservar solo las que reducen la pérdida de predecir el texto siguiente; reentrenar con ese corpus filtrado.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P14_toolformer.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P14_toolformer`](../../papers/foundational/P14_toolformer/README.md)
- Notebook: [`P14_toolformer.ipynb`](../../notebooks/papers/P14_toolformer.ipynb)
- Evaluación: [`P14_toolformer.md`](../../assessments/papers/P14_toolformer.md)
- Clases del programa relacionadas:
- [080-tool-calling-y-ejecucion-controlada](../../classes/part-06-foundation-models-and-llm-engineering/080-tool-calling-y-ejecucion-controlada/README.md)
- [113-anatomia-instrucciones-herramientas-estado-y-salida](../../classes/part-09-ai-agent-engineering/113-anatomia-instrucciones-herramientas-estado-y-salida/README.md)

---

[⬅️ Guías docentes del eje](README.md)
