# 👩‍🏫 Guía docente — P30 · Reflexion: agentes de lenguaje con refuerzo verbal

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Reflexion: Language Agents with Verbal Reinforcement Learning* (2023, arXiv:2303.11366 · NeurIPS 2023)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Un bucle ReAct que falla vuelve a empezar de cero y repite el mismo error, porque no conserva nada de lo aprendido en el intento anterior.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Tras cada fallo, generar una reflexión verbal sobre qué salió mal y conservarla en una memoria episódica que condiciona el siguiente intento.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P30_reflexion.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P30_reflexion`](../../papers/foundational/P30_reflexion/README.md)
- Notebook: [`P30_reflexion.ipynb`](../../notebooks/papers/P30_reflexion.ipynb)
- Evaluación: [`P30_reflexion.md`](../../assessments/papers/P30_reflexion.md)
- Clases del programa relacionadas:
- [122-evaluacion-y-depuracion-de-agentes](../../classes/part-09-ai-agent-engineering/122-evaluacion-y-depuracion-de-agentes/README.md)
- [129-critica-revision-y-debate-controlado](../../classes/part-10-multi-agent-systems-and-interoperability/129-critica-revision-y-debate-controlado/README.md)

---

[⬅️ Guías docentes del eje](README.md)
