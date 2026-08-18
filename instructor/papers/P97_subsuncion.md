# 👩‍🏫 Guía docente — P97 · Un sistema de control por capas robusto para un robot móvil

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *A Robust Layered Control System for a Mobile Robot* (1986, IEEE Journal of Robotics and Automation, 2(1), 14–23)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La arquitectura percibir-planificar-actuar construye un modelo del mundo, planifica sobre él y ejecuta el plan. Mantener ese modelo es caro, y cuando el mundo cambia a mitad de la ejecución, el plan se vuelve peligroso en vez de inútil.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Descomponer por comportamientos y no por funciones. Cada capa conecta percepción con acción de forma directa, y las capas inferiores —evitar obstáculos— pueden **subsumir** a las superiores. No hay representación compartida.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P97_subsuncion.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P97_subsuncion`](../../papers/foundational/P97_subsuncion/README.md)
- Notebook: [`P97_subsuncion.ipynb`](../../notebooks/papers/P97_subsuncion.ipynb)
- Evaluación: [`P97_subsuncion.md`](../../assessments/papers/P97_subsuncion.md)
- Clases del programa relacionadas:
- [136-arquitectura-percepcion-planificacion-accion](../../classes/part-11-embodied-ai-robotics-and-computer-use/136-arquitectura-percepcion-planificacion-accion/README.md)

---

[⬅️ Guías docentes del eje](README.md)
