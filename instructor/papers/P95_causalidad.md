# 👩‍🏫 Guía docente — P95 · Las siete herramientas de la inferencia causal, con reflexiones sobre aprendizaje automático

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *The Seven Tools of Causal Inference, with Reflections on Machine Learning* (2019, Communications of the ACM, 62(3), 54–60)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *El aprendizaje automático ajusta funciones sobre distribuciones observadas, y con eso responde preguntas de asociación. Pero las decisiones que importan son de intervención —«¿qué pasa si hago X?»— y esa pregunta no se puede responder solo con datos observacionales, por muchos que sean.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *La escalera de la causalidad y siete herramientas asociadas: modelos gráficos, el operador do, el criterio de puerta trasera, la fórmula de ajuste, mediación, transportabilidad y datos faltantes. La estructura causal se declara; no se estima de la tabla.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P95_causalidad.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P95_causalidad`](../../papers/foundational/P95_causalidad/README.md)
- Notebook: [`P95_causalidad.ipynb`](../../notebooks/papers/P95_causalidad.ipynb)
- Evaluación: [`P95_causalidad.md`](../../assessments/papers/P95_causalidad.md)
- Clases del programa relacionadas:
- [035-programacion-probabilistica-y-causalidad](../../classes/part-02-probabilistic-evolutionary-and-decision-ai/035-programacion-probabilistica-y-causalidad/README.md)
- [036-proyecto-sistema-hibrido-para-decisiones](../../classes/part-02-probabilistic-evolutionary-and-decision-ai/036-proyecto-sistema-hibrido-para-decisiones/README.md)

---

[⬅️ Guías docentes del eje](README.md)
