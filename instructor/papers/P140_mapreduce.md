# 👩‍🏫 Guía docente — P140 · MapReduce: procesamiento simplificado de datos en clústeres grandes

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *MapReduce: simplified data processing on large clusters* (2004, OSDI 2004 · Communications of the ACM, 51(1), 107–113)
**Nivel:** L1 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Procesar terabytes en miles de máquinas exigía escribir a mano el particionado, la comunicación, la recuperación de fallos y la agregación. Cada trabajo reimplementaba lo mismo, y la lógica del problema quedaba enterrada bajo la fontanería.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Dos funciones: **map**, que transforma cada registro en parejas clave-valor, y **reduce**, que agrega todos los valores de una clave. El sistema se encarga del reparto, del movimiento de datos y de reejecutar lo que falle.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P140_mapreduce.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P140_mapreduce`](../../papers/foundational/P140_mapreduce/README.md)
- Notebook: [`P140_mapreduce.ipynb`](../../notebooks/papers/P140_mapreduce.ipynb)
- Evaluación: [`P140_mapreduce.md`](../../assessments/papers/P140_mapreduce.md)
- Clases del programa relacionadas:
- [128-paralelismo-fan-out-y-map-reduce](../../classes/part-10-multi-agent-systems-and-interoperability/128-paralelismo-fan-out-y-map-reduce/README.md)

---

[⬅️ Guías docentes del eje](README.md)
