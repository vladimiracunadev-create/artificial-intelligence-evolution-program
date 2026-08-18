# 👩‍🏫 Guía docente — P66 · Una lógica orientada a máquina basada en el principio de resolución

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *A Machine-Oriented Logic Based on the Resolution Principle* (1965, Journal of the ACM, 12(1), 23–41)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Los cálculos lógicos existentes tenían muchas reglas pensadas para el razonamiento humano. Aplicarlas a máquina generaba una explosión de caminos sin criterio.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Una única regla —la resolución— sobre cláusulas, junto con el algoritmo de unificación que calcula el unificador más general: la sustitución mínima que iguala dos términos sin comprometer nada de más.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P66_resolucion.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P66_resolucion`](../../papers/foundational/P66_resolucion/README.md)
- Notebook: [`P66_resolucion.ipynb`](../../notebooks/papers/P66_resolucion.ipynb)
- Evaluación: [`P66_resolucion.md`](../../assessments/papers/P66_resolucion.md)
- Clases del programa relacionadas:
- [020-logica-de-primer-orden-y-unificacion](../../classes/part-01-symbolic-ai-search-logic-and-planning/020-logica-de-primer-orden-y-unificacion/README.md)

---

[⬅️ Guías docentes del eje](README.md)
