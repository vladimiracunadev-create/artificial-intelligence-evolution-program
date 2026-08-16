# 👩‍🏫 Guía docente — P13 · ReAct: sinergia entre razonar y actuar en modelos de lenguaje

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *ReAct: Synergizing Reasoning and Acting in Language Models* (2022, arXiv:2210.03629 · ICLR 2023)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *El razonamiento en cadena (CoT) no consulta el mundo y alucina hechos; actuar sin razonar no descompone problemas de varios pasos.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Intercalar trazas de pensamiento y acciones sobre un entorno, de modo que cada observación real condicione el siguiente razonamiento.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P13_react.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P13_react`](../../papers/foundational/P13_react/README.md)
- Notebook: [`P13_react.ipynb`](../../notebooks/papers/P13_react.ipynb)
- Evaluación: [`P13_react.md`](../../assessments/papers/P13_react.md)
- Clases del programa relacionadas:
- [114-ciclo-react-y-observacion-del-entorno](../../classes/part-09-ai-agent-engineering/114-ciclo-react-y-observacion-del-entorno/README.md)
- [112-de-modelo-y-automatizacion-a-agente](../../classes/part-09-ai-agent-engineering/112-de-modelo-y-automatizacion-a-agente/README.md)

---

[⬅️ Guías docentes del eje](README.md)
