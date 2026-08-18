# 👩‍🏫 Guía docente — P133 · Los modelos de IA colapsan al entrenarse con datos generados recursivamente

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *AI models collapse when trained on recursively generated data* (2024, Nature, 631, 755–759)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La web se está llenando de texto e imágenes generadas. Los corpus futuros se recogerán de ahí, y nadie sabía qué le ocurre a un modelo entrenado sobre lo que generó la generación anterior.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Formalizar y medir el fenómeno en modelos de lenguaje, autocodificadores variacionales y mezclas de gaussianas: el error de muestreo acumulado basta para que las colas desaparezcan primero y la distribución converja a algo degenerado.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P133_colapso_de_modelo.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P133_colapso_de_modelo`](../../papers/foundational/P133_colapso_de_modelo/README.md)
- Notebook: [`P133_colapso_de_modelo.ipynb`](../../notebooks/papers/P133_colapso_de_modelo.ipynb)
- Evaluación: [`P133_colapso_de_modelo.md`](../../assessments/papers/P133_colapso_de_modelo.md)
- Clases del programa relacionadas:
- [097-datos-sinteticos-utilidad-y-contaminacion](../../classes/part-07-generative-ai-across-media/097-datos-sinteticos-utilidad-y-contaminacion/README.md)

---

[⬅️ Guías docentes del eje](README.md)
