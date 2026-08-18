# 👩‍🏫 Guía docente — P60 · Por qué la mayoría de los hallazgos publicados son falsos

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Why Most Published Research Findings Are False* (2005, PLoS Medicine, 2(8), e124)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La significancia estadística se leía como sinónimo de verdad. Nadie ponía número a la pregunta que de verdad importa: dado que se publicó, ¿qué probabilidad hay de que sea cierto?* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Modelar el valor predictivo positivo en función de las odds previas, el poder estadístico, el nivel de significancia, el sesgo y el número de equipos que compiten.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P60_valor_predictivo.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P60_valor_predictivo`](../../papers/foundational/P60_valor_predictivo/README.md)
- Notebook: [`P60_valor_predictivo.ipynb`](../../notebooks/papers/P60_valor_predictivo.ipynb)
- Evaluación: [`P60_valor_predictivo.md`](../../assessments/papers/P60_valor_predictivo.md)
- Clases del programa relacionadas:
- [008-datos-evidencia-hipotesis-y-falsabilidad](../../classes/part-00-foundations-history-and-scientific-method/008-datos-evidencia-hipotesis-y-falsabilidad/README.md)

---

[⬅️ Guías docentes del eje](README.md)
