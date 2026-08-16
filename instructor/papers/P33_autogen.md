# 👩‍🏫 Guía docente — P33 · AutoGen: aplicaciones de nueva generación mediante conversación multiagente

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation* (2023, arXiv:2308.08155)
**Nivel:** L4 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Un solo agente escribe y juzga su propio trabajo, así que arrastra sus propios puntos ciegos; y no había forma estándar de componer varios agentes con humanos en el bucle.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Agentes conversables y configurables —con o sin persona humana, con o sin ejecución de código— que se coordinan mediante mensajes, con patrones de conversación programables.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P33_autogen.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P33_autogen`](../../papers/foundational/P33_autogen/README.md)
- Notebook: [`P33_autogen.ipynb`](../../notebooks/papers/P33_autogen.ipynb)
- Evaluación: [`P33_autogen.md`](../../assessments/papers/P33_autogen.md)
- Clases del programa relacionadas:
- [124-workflow-subagente-y-sistema-multiagente](../../classes/part-10-multi-agent-systems-and-interoperability/124-workflow-subagente-y-sistema-multiagente/README.md)

---

[⬅️ Guías docentes del eje](README.md)
