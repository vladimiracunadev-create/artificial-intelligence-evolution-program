# 👩‍🏫 Guía docente — P55 · Una teoría matemática de la comunicación

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *A Mathematical Theory of Communication* (1948, Bell System Technical Journal, 27(3–4), 379–423 y 623–656)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Se sabía transmitir señales, pero no había forma de medir cuánta información llevaban ni de saber cuánto se podía comprimir o transmitir sin error.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Separar la información del significado y medirla por la sorpresa de cada símbolo. De ahí salen la entropía como cota inferior de compresión y la capacidad como cota de canal.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P55_shannon.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P55_shannon`](../../papers/foundational/P55_shannon/README.md)
- Notebook: [`P55_shannon.ipynb`](../../notebooks/papers/P55_shannon.ipynb)
- Evaluación: [`P55_shannon.md`](../../assessments/papers/P55_shannon.md)
- Clases del programa relacionadas:
- [006-probabilidad-incertidumbre-y-estadistica-basica](../../classes/part-00-foundations-history-and-scientific-method/006-probabilidad-incertidumbre-y-estadistica-basica/README.md)

---

[⬅️ Guías docentes del eje](README.md)
