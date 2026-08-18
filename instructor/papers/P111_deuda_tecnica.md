# 👩‍🏫 Guía docente — P111 · Deuda técnica oculta en los sistemas de aprendizaje automático

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Hidden Technical Debt in Machine Learning Systems* (2015, NeurIPS 2015)
**Nivel:** L1 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Los equipos medían su trabajo por la calidad del modelo mientras el sistema alrededor —ingestión, características, servicio, monitorización, configuración— crecía sin control. Y esa parte acumula formas de deuda que no tienen equivalente en software convencional: dependencias de datos que ningún compilador comprueba.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Un catálogo de antipatrones específicos del aprendizaje automático: dependencias de datos no declaradas, características huérfanas, bucles de realimentación ocultos, código de pegamento, deuda de configuración, y el principio CACE — cambiar cualquier cosa lo cambia todo.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P111_deuda_tecnica.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P111_deuda_tecnica`](../../papers/foundational/P111_deuda_tecnica/README.md)
- Notebook: [`P111_deuda_tecnica.ipynb`](../../notebooks/papers/P111_deuda_tecnica.ipynb)
- Evaluación: [`P111_deuda_tecnica.md`](../../assessments/papers/P111_deuda_tecnica.md)
- Clases del programa relacionadas:
- [148-ciclo-de-vida-de-datos-modelos-y-agentes](../../classes/part-12-ai-engineering-mlops-llmops-and-agentops/148-ciclo-de-vida-de-datos-modelos-y-agentes/README.md)

---

[⬅️ Guías docentes del eje](README.md)
