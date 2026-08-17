# 👩‍🏫 Guía docente — P52 · Hacia la monosemanticidad: descomponer modelos de lenguaje con aprendizaje de diccionario

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Towards Monosemanticity: Decomposing Language Models With Dictionary Learning* (2023, Transformer Circuits Thread)
**Nivel:** L5 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Al inspeccionar neuronas individuales de un modelo se encuentra que responden a conceptos no relacionados entre sí. La interpretabilidad neurona a neurona no funcionaba, y no se sabía por qué.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *La hipótesis de superposición: el modelo representa MÁS características que dimensiones tiene, como direcciones casi ortogonales con interferencia. Y un autoencoder disperso puede recuperar esas direcciones.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P52_superposition.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P52_superposition`](../../papers/foundational/P52_superposition/README.md)
- Notebook: [`P52_superposition.ipynb`](../../notebooks/papers/P52_superposition.ipynb)
- Evaluación: [`P52_superposition.md`](../../assessments/papers/P52_superposition.md)
- Clases del programa relacionadas:
- [162-red-teaming-y-abuso](../../classes/part-13-evaluation-safety-security-and-governance/162-red-teaming-y-abuso/README.md)
- [160-diseno-de-evaluaciones-y-criterios-de-exito](../../classes/part-13-evaluation-safety-security-and-governance/160-diseno-de-evaluaciones-y-criterios-de-exito/README.md)

---

[⬅️ Guías docentes del eje](README.md)
