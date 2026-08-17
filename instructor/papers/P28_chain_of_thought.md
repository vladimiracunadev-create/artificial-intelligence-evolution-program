# 👩‍🏫 Guía docente — P28 · El prompting de cadena de pensamiento provoca razonamiento en modelos de lenguaje grandes

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models* (2022, arXiv:2201.11903 · NeurIPS 2022)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Los modelos grandes fallaban en aritmética y razonamiento de varios pasos aunque acertaran tareas aparentemente más difíciles: se les pedía el resultado sin dejarles espacio para llegar a él.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Incluir en el prompt unos pocos ejemplos que muestren el razonamiento paso a paso, sin ajuste fino ni datos adicionales.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P28_chain_of_thought.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P28_chain_of_thought`](../../papers/foundational/P28_chain_of_thought/README.md)
- Notebook: [`P28_chain_of_thought.ipynb`](../../notebooks/papers/P28_chain_of_thought.ipynb)
- Evaluación: [`P28_chain_of_thought.md`](../../assessments/papers/P28_chain_of_thought.md)
- Clases del programa relacionadas:
- [114-ciclo-react-y-observacion-del-entorno](../../classes/part-09-ai-agent-engineering/114-ciclo-react-y-observacion-del-entorno/README.md)
- [115-planificacion-y-descomposicion-de-tareas](../../classes/part-09-ai-agent-engineering/115-planificacion-y-descomposicion-de-tareas/README.md)
- [175-razonamiento-y-computo-en-tiempo-de-inferencia](../../classes/part-14-frontier-research-and-capstones/175-razonamiento-y-computo-en-tiempo-de-inferencia/README.md)

---

[⬅️ Guías docentes del eje](README.md)
