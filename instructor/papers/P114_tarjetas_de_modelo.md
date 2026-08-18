# 👩‍🏫 Guía docente — P114 · Tarjetas de modelo para el reporte de modelos

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Model Cards for Model Reporting* (2019, FAT* '19, 220–229)
**Nivel:** L1 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Un modelo se publica con una cifra agregada de exactitud y sin decir para qué sirve, para qué no, con qué datos se evaluó ni a quién le funciona peor. Quien lo integra no tiene forma de saber si es adecuado para su caso.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Una tarjeta de una o dos páginas con secciones fijas: detalles del modelo, uso previsto, usos fuera de alcance, factores relevantes, métricas, datos de evaluación y entrenamiento, **análisis cuantitativo desagregado**, consideraciones éticas y advertencias.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P114_tarjetas_de_modelo.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P114_tarjetas_de_modelo`](../../papers/foundational/P114_tarjetas_de_modelo/README.md)
- Notebook: [`P114_tarjetas_de_modelo.ipynb`](../../notebooks/papers/P114_tarjetas_de_modelo.ipynb)
- Evaluación: [`P114_tarjetas_de_modelo.md`](../../assessments/papers/P114_tarjetas_de_modelo.md)
- Clases del programa relacionadas:
- [150-registro-y-promocion-champion-challenger](../../classes/part-12-ai-engineering-mlops-llmops-and-agentops/150-registro-y-promocion-champion-challenger/README.md)

---

[⬅️ Guías docentes del eje](README.md)
