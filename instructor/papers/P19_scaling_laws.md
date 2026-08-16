# 👩‍🏫 Guía docente — P19 · Entrenar modelos de lenguaje grandes con cómputo óptimo

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Training Compute-Optimal Large Language Models* (2022, arXiv:2203.15556 · NeurIPS 2022)
**Nivel:** L4 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Tras GPT-3 la industria escalaba parámetros asumiendo que era la variable dominante, sin medir el reparto óptimo entre parámetros y tokens a cómputo constante.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Ajustar empíricamente L(N, D) y resolver el reparto que minimiza la pérdida bajo la restricción C = 6ND.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P19_scaling_laws.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P19_scaling_laws`](../../papers/foundational/P19_scaling_laws/README.md)
- Notebook: [`P19_scaling_laws.ipynb`](../../notebooks/papers/P19_scaling_laws.ipynb)
- Evaluación: [`P19_scaling_laws.md`](../../assessments/papers/P19_scaling_laws.md)
- Clases del programa relacionadas:
- [074-objetivos-de-preentrenamiento](../../classes/part-06-foundation-models-and-llm-engineering/074-objetivos-de-preentrenamiento/README.md)
- [086-seleccion-de-modelo-costo-latencia-y-privacidad](../../classes/part-06-foundation-models-and-llm-engineering/086-seleccion-de-modelo-costo-latencia-y-privacidad/README.md)

---

[⬅️ Guías docentes del eje](README.md)
