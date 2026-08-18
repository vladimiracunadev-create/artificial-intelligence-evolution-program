# 👩‍🏫 Guía docente — P69 · Un modelo de razonamiento inexacto en medicina

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *A Model of Inexact Reasoning in Medicine* (1975, Mathematical Biosciences, 23(3–4), 351–379)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *El conocimiento médico está lleno de indicios que no son ni ciertos ni falsos. Aplicar probabilidad bayesiana exigía distribuciones conjuntas que nadie podía estimar ni declarar.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Los factores de certeza: un número en [−1, 1] por regla, con un álgebra de combinación que satura y admite evidencia en contra, más una traza que hace explicable cada conclusión.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P69_mycin.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P69_mycin`](../../papers/foundational/P69_mycin/README.md)
- Notebook: [`P69_mycin.ipynb`](../../notebooks/papers/P69_mycin.ipynb)
- Evaluación: [`P69_mycin.md`](../../assessments/papers/P69_mycin.md)
- Clases del programa relacionadas:
- [022-sistemas-expertos-y-motores-de-reglas](../../classes/part-01-symbolic-ai-search-logic-and-planning/022-sistemas-expertos-y-motores-de-reglas/README.md)

---

[⬅️ Guías docentes del eje](README.md)
