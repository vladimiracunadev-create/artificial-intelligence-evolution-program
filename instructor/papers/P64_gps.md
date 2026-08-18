# 👩‍🏫 Guía docente — P64 · Informe sobre un programa general de resolución de problemas

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Report on a General Problem-Solving Program* (1959, IFIP Congress 1959, París, 256–264)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Cada programa de los años cincuenta resolvía un problema y solo uno. No existía un método general que pudiera aplicarse a dominios distintos sin reescribirlo entero.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Representar el problema como diferencias entre el estado actual y la meta, y asociar cada tipo de diferencia con los operadores que la reducen. Si el operador no es aplicable, se crea un subobjetivo para hacerlo aplicable.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P64_gps.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P64_gps`](../../papers/foundational/P64_gps/README.md)
- Notebook: [`P64_gps.ipynb`](../../notebooks/papers/P64_gps.ipynb)
- Evaluación: [`P64_gps.md`](../../assessments/papers/P64_gps.md)
- Clases del programa relacionadas:
- [013-espacios-de-estados-y-formulacion-de-problemas](../../classes/part-01-symbolic-ai-search-logic-and-planning/013-espacios-de-estados-y-formulacion-de-problemas/README.md)

---

[⬅️ Guías docentes del eje](README.md)
