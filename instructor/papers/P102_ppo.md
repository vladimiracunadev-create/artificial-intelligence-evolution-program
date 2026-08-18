# 👩‍🏫 Guía docente — P102 · Algoritmos de optimización proximal de políticas

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Proximal Policy Optimization Algorithms* (2017, arXiv:1707.06347)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *En gradiente de políticas, un paso demasiado grande destruye la política: se vuelve casi determinista, deja de explorar y no puede recuperarse. TRPO lo resolvía con una restricción de divergencia KL, a costa de una optimización de segundo orden compleja.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Sustituir la restricción por un **recorte** del cociente de probabilidades entre la política nueva y la vieja. Pasado el umbral, mejorar más no aporta al objetivo, así que el gradiente deja de empujar. Sin restricciones, sin segundo orden.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P102_ppo.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P102_ppo`](../../papers/foundational/P102_ppo/README.md)
- Notebook: [`P102_ppo.ipynb`](../../notebooks/papers/P102_ppo.ipynb)
- Evaluación: [`P102_ppo.md`](../../assessments/papers/P102_ppo.md)
- Clases del programa relacionadas:
- [140-control-clasico-y-control-aprendido](../../classes/part-11-embodied-ai-robotics-and-computer-use/140-control-clasico-y-control-aprendido/README.md)

---

[⬅️ Guías docentes del eje](README.md)
