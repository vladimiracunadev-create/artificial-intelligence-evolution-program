# 👩‍🏫 Guía docente — P100 · Requisitos para robots seguros: mediciones, análisis y nuevas conclusiones

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Requirements for Safe Robots: Measurements, Analysis and New Insights* (2009, The International Journal of Robotics Research, 28(11–12), 1507–1527)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La seguridad de los robots industriales se resolvía con vallas: separación física total. Para trabajar junto a personas hacía falta saber qué daño produce realmente un impacto, y ese dato no existía — se legislaba y se diseñaba a ojo.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Medir. Impactos instrumentados con maniquíes y voluntarios, análisis de los criterios de lesión de la industria del automóvil aplicados a la robótica, y la conclusión incómoda: la masa importa menos de lo que se creía y la velocidad, mucho más.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P100_seguridad_fisica.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P100_seguridad_fisica`](../../papers/foundational/P100_seguridad_fisica/README.md)
- Notebook: [`P100_seguridad_fisica.ipynb`](../../notebooks/papers/P100_seguridad_fisica.ipynb)
- Evaluación: [`P100_seguridad_fisica.md`](../../assessments/papers/P100_seguridad_fisica.md)
- Clases del programa relacionadas:
- [143-robots-colaborativos-y-seguridad-fisica](../../classes/part-11-embodied-ai-robotics-and-computer-use/143-robots-colaborativos-y-seguridad-fisica/README.md)

---

[⬅️ Guías docentes del eje](README.md)
