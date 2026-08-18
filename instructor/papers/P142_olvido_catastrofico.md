# 👩‍🏫 Guía docente — P142 · Interferencia catastrófica en redes conexionistas: el problema del aprendizaje secuencial

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Catastrophic Interference in Connectionist Networks: The Sequential Learning Problem* (1989, Psychology of Learning and Motivation, 24, 109–165)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Las redes conexionistas se presentaban como modelos de la memoria humana. Nadie había comprobado qué ocurre cuando se les enseña algo nuevo después de haber aprendido algo: se suponía interferencia gradual, como en las personas.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Medirlo. Entrenar una red en una tarea, entrenarla después en otra y volver a evaluar la primera. El resultado es un colapso casi inmediato, y eso pone en cuestión el modelo como teoría de la memoria y como sistema práctico.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P142_olvido_catastrofico.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P142_olvido_catastrofico`](../../papers/foundational/P142_olvido_catastrofico/README.md)
- Notebook: [`P142_olvido_catastrofico.ipynb`](../../notebooks/papers/P142_olvido_catastrofico.ipynb)
- Evaluación: [`P142_olvido_catastrofico.md`](../../assessments/papers/P142_olvido_catastrofico.md)
- Clases del programa relacionadas:
- [176-aprendizaje-continuo-y-adaptacion](../../classes/part-14-frontier-research-and-capstones/176-aprendizaje-continuo-y-adaptacion/README.md)

---

[⬅️ Guías docentes del eje](README.md)
