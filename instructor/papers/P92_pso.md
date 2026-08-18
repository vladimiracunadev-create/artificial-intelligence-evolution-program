# 👩‍🏫 Guía docente — P92 · Optimización por enjambre de partículas

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Particle Swarm Optimization* (1995, Proceedings of ICNN'95, 1942–1948)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Muchas funciones objetivo no se pueden derivar —son simulaciones, cajas negras o tienen ruido— y los métodos de gradiente no se pueden aplicar. Las alternativas poblacionales existentes eran caras y difíciles de ajustar.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Un enjambre de partículas que se mueven por el espacio con una velocidad que combina inercia, atracción hacia su propio mejor histórico y atracción hacia el mejor del grupo. Sin cruce, sin mutación y sin selección.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P92_pso.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P92_pso`](../../papers/foundational/P92_pso/README.md)
- Notebook: [`P92_pso.ipynb`](../../notebooks/papers/P92_pso.ipynb)
- Evaluación: [`P92_pso.md`](../../assessments/papers/P92_pso.md)
- Clases del programa relacionadas:
- [034-optimizacion-por-enjambre-y-colonia](../../classes/part-02-probabilistic-evolutionary-and-decision-ai/034-optimizacion-por-enjambre-y-colonia/README.md)

---

[⬅️ Guías docentes del eje](README.md)
