# 📝 Evaluación — P108 · CAP doce años después: cómo han cambiado las «reglas»

> Generado por `python scripts/generate_papers.py`.
> Se evalúa comprensión histórica, lectura crítica e interpretación — no memorización de definiciones.

**Paper:** *CAP Twelve Years Later: How the «Rules» Have Changed* (2012, IEEE Computer, 45(2), 23–29) · **Nivel:** L2

## Parte A — Contexto histórico (20 pts)

1. (10) Describe el estado del arte **inmediatamente anterior** a este paper y por qué era insuficiente.
   No menciones la solución del paper en tu respuesta.
2. (10) Nombra un trabajo anterior del que este paper depende y explica qué le tomó prestado.

## Parte B — Lectura crítica (20 pts)

3. (10) Localiza en el paper original una afirmación **cuantitativa** y reescríbela indicando tarea,
   dataset, métrica, línea base y condiciones. Cita la tabla o sección.
4. (10) Identifica una idea que hoy se asocia a este paper pero que **apareció después**. Aporta la
   referencia posterior con año.

## Parte C — Interpretación matemática (15 pts)

5. (15) Explica la ecuación central con tus palabras y señala qué ocurre en un caso límite
   (valor 0, dimensión muy grande, secuencia muy larga… según corresponda).

## Parte D — Implementación e interpretación (25 pts)

6. (10) Ejecuta [`P108_cap.ipynb`](../../notebooks/papers/P108_cap.ipynb) con **tres semillas**
   y reporta qué varía y qué se mantiene.
7. (10) Reproduce el anti-patrón de la sección 11 y explica por qué produce una conclusión errónea.
8. (5) Aporta la corrección con su evidencia.

## Parte E — Límites y transferencia (20 pts)

9. (10) Escribe una limitación de la **miniatura** y una del **paper original**. No pueden ser la misma idea.
10. (10) Conecta este hito con el siguiente de la ruta: ¿qué quedó sin resolver que motivó el paso siguiente?

## Rúbrica

| Nivel | Descripción |
|---|---|
| **A — Excelente** | Distingue hecho documentado, simplificación didáctica e inferencia propia. Cita fuentes primarias con sección o tabla. Sus límites son propios, no copiados. |
| **B — Suficiente** | Explica el mecanismo y ejecuta la miniatura correctamente, pero repite los límites de la ficha y cita de forma imprecisa. |
| **C — Insuficiente** | Describe el paper con narrativa retrospectiva, atribuye ideas posteriores, o presenta la salida de la miniatura como reproducción del experimento original. |

## Criterio automático de rechazo

Se devuelve sin nota cualquier entrega que:

- atribuya al paper resultados, métricas o autores que no aparecen en la fuente primaria;
- presente la ejecución del notebook como reproducción de los resultados del paper;
- cite un paper que no se abrió (se comprueba pidiendo el número de figura o tabla).

---

[⬅️ Evaluaciones del eje](README.md) · [Ficha](../../papers/foundational/P108_cap/README.md)
