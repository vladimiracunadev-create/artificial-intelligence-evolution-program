# 👩‍🏫 Guía docente — P137 · Principios del metarrazonamiento

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Principles of Metareasoning* (1991, Artificial Intelligence, 49(1–3), 361–395)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Un agente con recursos limitados no puede deliberar indefinidamente, y los sistemas fijaban el presupuesto de cómputo a mano. Un número fijo piensa de más en las instancias fáciles y de menos en las difíciles, y siempre en la proporción equivocada.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Tratar cada paso de deliberación como una acción con coste y con beneficio esperado —el **valor de la computación**— y seguir deliberando solo mientras la mejora esperada supere el coste. La parada se deduce, no se elige.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P137_metarrazonamiento.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P137_metarrazonamiento`](../../papers/foundational/P137_metarrazonamiento/README.md)
- Notebook: [`P137_metarrazonamiento.ipynb`](../../notebooks/papers/P137_metarrazonamiento.ipynb)
- Evaluación: [`P137_metarrazonamiento.md`](../../assessments/papers/P137_metarrazonamiento.md)
- Clases del programa relacionadas:
- [121-presupuestos-de-pasos-tokens-costo-y-tiempo](../../classes/part-09-ai-agent-engineering/121-presupuestos-de-pasos-tokens-costo-y-tiempo/README.md)

---

[⬅️ Guías docentes del eje](README.md)
