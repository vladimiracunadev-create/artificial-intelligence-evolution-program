# 👩‍🏫 Guía docente — P104 · WebArena: un entorno web realista para construir agentes autónomos

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *WebArena: A Realistic Web Environment for Building Autonomous Agents* (2023, arXiv:2307.13854 · ICLR 2024)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Los agentes de navegador se evaluaban con capturas, con juicios de un modelo o con el propio informe del agente. Un agente elocuente puntuaba alto sin haber completado la tarea, y los resultados no eran comparables entre trabajos.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Un entorno reproducible con sitios reales autoalojados —comercio, foro, repositorio, gestor de contenidos— y, para cada tarea, un verificador programático que inspecciona el estado final del sitio.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P104_webarena.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P104_webarena`](../../papers/foundational/P104_webarena/README.md)
- Notebook: [`P104_webarena.ipynb`](../../notebooks/papers/P104_webarena.ipynb)
- Evaluación: [`P104_webarena.md`](../../assessments/papers/P104_webarena.md)
- Clases del programa relacionadas:
- [145-agentes-de-navegador](../../classes/part-11-embodied-ai-robotics-and-computer-use/145-agentes-de-navegador/README.md)

---

[⬅️ Guías docentes del eje](README.md)
