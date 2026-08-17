# 👩‍🏫 Guía docente — P34 · RoFormer: Transformer mejorado con codificación posicional rotatoria

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *RoFormer: Enhanced Transformer with Rotary Position Embedding* (2021, arXiv:2104.09864)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La codificación sinusoidal del Transformer se SUMA al embedding y codifica posición absoluta; la atención no ve directamente la distancia entre dos tokens, que es lo que importa en lenguaje.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Rotar los vectores de consulta y clave en función de su posición, de modo que el producto escalar entre dos posiciones dependa únicamente de su diferencia.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P34_rope.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P34_rope`](../../papers/foundational/P34_rope/README.md)
- Notebook: [`P34_rope.ipynb`](../../notebooks/papers/P34_rope.ipynb)
- Evaluación: [`P34_rope.md`](../../assessments/papers/P34_rope.md)
- Clases del programa relacionadas:
- [055-atencion-y-arquitectura-transformer](../../classes/part-04-neural-networks-and-deep-learning/055-atencion-y-arquitectura-transformer/README.md)
- [079-prompting-contexto-y-resultados-estructurados](../../classes/part-06-foundation-models-and-llm-engineering/079-prompting-contexto-y-resultados-estructurados/README.md)

---

[⬅️ Guías docentes del eje](README.md)
