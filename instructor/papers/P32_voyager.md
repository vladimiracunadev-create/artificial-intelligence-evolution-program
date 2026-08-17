# 👩‍🏫 Guía docente — P32 · Voyager: un agente encarnado de final abierto con modelos de lenguaje grandes

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Voyager: An Open-Ended Embodied Agent with Large Language Models* (2023, arXiv:2305.16291)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Un agente que resuelve tareas cada vez desde cero no mejora con la experiencia, y meter todo lo aprendido en el prompt no escala.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Un currículo automático que propone la siguiente tarea alcanzable, una biblioteca de habilidades ejecutables indexada por nombre, y un bucle iterativo que depura el código con la retroalimentación del entorno.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P32_voyager.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P32_voyager`](../../papers/foundational/P32_voyager/README.md)
- Notebook: [`P32_voyager.ipynb`](../../notebooks/papers/P32_voyager.ipynb)
- Evaluación: [`P32_voyager.md`](../../assessments/papers/P32_voyager.md)
- Clases del programa relacionadas:
- [133-agent-skills-como-capacidades-portables](../../classes/part-10-multi-agent-systems-and-interoperability/133-agent-skills-como-capacidades-portables/README.md)
- [147-proyecto-agente-que-actua-con-limites](../../classes/part-11-embodied-ai-robotics-and-computer-use/147-proyecto-agente-que-actua-con-limites/README.md)

---

[⬅️ Guías docentes del eje](README.md)
