# 👩‍🏫 Guía docente — P22 · DeepSeek-R1: incentivar la capacidad de razonamiento mediante aprendizaje por refuerzo

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning* (2025, arXiv:2501.12948 · Nature 645, 633–638 (2025))
**Nivel:** L5 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La cadena de pensamiento dependía de demostraciones humanas caras, y esa supervisión limitaba la capacidad en problemas complejos.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Recompensar únicamente el RESULTADO verificable y dejar que el comportamiento de razonamiento emerja del refuerzo, para luego transferirlo a modelos menores.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P22_deepseek_r1.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P22_deepseek_r1`](../../papers/foundational/P22_deepseek_r1/README.md)
- Notebook: [`P22_deepseek_r1.ipynb`](../../notebooks/papers/P22_deepseek_r1.ipynb)
- Evaluación: [`P22_deepseek_r1.md`](../../assessments/papers/P22_deepseek_r1.md)
- Clases del programa relacionadas:
- [078-rlhf-rlaif-y-dpo](../../classes/part-06-foundation-models-and-llm-engineering/078-rlhf-rlaif-y-dpo/README.md)
- [114-ciclo-react-y-observacion-del-entorno](../../classes/part-09-ai-agent-engineering/114-ciclo-react-y-observacion-del-entorno/README.md)
- [175-razonamiento-y-computo-en-tiempo-de-inferencia](../../classes/part-14-frontier-research-and-capstones/175-razonamiento-y-computo-en-tiempo-de-inferencia/README.md)

---

[⬅️ Guías docentes del eje](README.md)
