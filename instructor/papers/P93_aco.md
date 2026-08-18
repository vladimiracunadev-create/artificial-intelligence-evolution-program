# 👩‍🏫 Guía docente — P93 · Sistema de hormigas: optimización mediante una colonia de agentes cooperantes

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Ant System: Optimization by a Colony of Cooperating Agents* (1996, IEEE Transactions on Systems, Man and Cybernetics, Part B, 26(1), 29–41)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *En problemas combinatorios como el del viajante, las heurísticas golosas se quedan atrapadas en decisiones tempranas y no tienen forma de aprender de los intentos anteriores sin una memoria global costosa.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Agentes simples que construyen soluciones eligiendo el siguiente paso según una combinación de feromona acumulada y heurística local, y que depositan feromona proporcional a la calidad de la solución construida. La evaporación evita el estancamiento.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P93_aco.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P93_aco`](../../papers/foundational/P93_aco/README.md)
- Notebook: [`P93_aco.ipynb`](../../notebooks/papers/P93_aco.ipynb)
- Evaluación: [`P93_aco.md`](../../assessments/papers/P93_aco.md)
- Clases del programa relacionadas:
- [034-optimizacion-por-enjambre-y-colonia](../../classes/part-02-probabilistic-evolutionary-and-decision-ai/034-optimizacion-por-enjambre-y-colonia/README.md)

---

[⬅️ Guías docentes del eje](README.md)
