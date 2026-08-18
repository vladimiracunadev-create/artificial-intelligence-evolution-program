# 👩‍🏫 Guía docente — P90 · Algoritmos genéticos y la asignación óptima de ensayos

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Genetic Algorithms and the Optimal Allocation of Trials* (1973, SIAM Journal on Computing, 2(2), 88–105)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Buscar en un espacio enorme sin gradiente exige decidir constantemente entre explorar lo desconocido y explotar lo que ya funciona. No había un argumento formal de por qué una población con selección y recombinación resuelve bien ese reparto.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Analizar la población como un proceso que evalúa implícitamente muchos esquemas —patrones con comodines— a la vez, y mostrar que la reproducción proporcional a la aptitud asigna ensayos de forma cercana a la óptima del problema del bandido.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P90_algoritmos_geneticos.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P90_algoritmos_geneticos`](../../papers/foundational/P90_algoritmos_geneticos/README.md)
- Notebook: [`P90_algoritmos_geneticos.ipynb`](../../notebooks/papers/P90_algoritmos_geneticos.ipynb)
- Evaluación: [`P90_algoritmos_geneticos.md`](../../assessments/papers/P90_algoritmos_geneticos.md)
- Clases del programa relacionadas:
- [033-algoritmos-geneticos](../../classes/part-02-probabilistic-evolutionary-and-decision-ai/033-algoritmos-geneticos/README.md)

---

[⬅️ Guías docentes del eje](README.md)
