# 👩‍🏫 Guía docente — P47 · Predicción de estructura de proteínas de alta precisión con AlphaFold

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Highly accurate protein structure prediction with AlphaFold* (2021, Nature 596, 583–589 (2021))
**Nivel:** L4 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Predecir la estructura tridimensional de una proteína a partir de su secuencia de aminoácidos llevaba décadas sin resolverse, y determinarla experimentalmente cuesta meses o años por proteína.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Una arquitectura que razona conjuntamente sobre alineamientos múltiples de secuencias y sobre representaciones de pares de residuos, con un módulo que produce coordenadas 3D directamente.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P47_alphafold.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P47_alphafold`](../../papers/foundational/P47_alphafold/README.md)
- Notebook: [`P47_alphafold.ipynb`](../../notebooks/papers/P47_alphafold.ipynb)
- Evaluación: [`P47_alphafold.md`](../../assessments/papers/P47_alphafold.md)
- Clases del programa relacionadas:
- [181-ia-para-ciencia-clima-y-salud-responsable](../../classes/part-14-frontier-research-and-capstones/181-ia-para-ciencia-clima-y-salud-responsable/README.md)

---

[⬅️ Guías docentes del eje](README.md)
