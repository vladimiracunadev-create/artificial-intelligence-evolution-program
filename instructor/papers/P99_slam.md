# 👩‍🏫 Guía docente — P99 · Localización y mapeo simultáneos: parte I

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Simultaneous Localization and Mapping: Part I* (2006, IEEE Robotics & Automation Magazine, 13(2), 99–110)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Un robot que se mueve acumula error de odometría sin límite. Corregirlo exige referencias externas; pero si el mapa no existe de antemano, hay que construirlo con la misma pose incierta que se quiere corregir.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Estimar el estado conjunto —pose y mapa— reconociendo que sus errores están **correlacionados**. El artículo formaliza la estructura de la covarianza, explica por qué converge y por qué el cierre de bucle corrige la trayectoria entera.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P99_slam.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P99_slam`](../../papers/foundational/P99_slam/README.md)
- Notebook: [`P99_slam.ipynb`](../../notebooks/papers/P99_slam.ipynb)
- Evaluación: [`P99_slam.md`](../../assessments/papers/P99_slam.md)
- Clases del programa relacionadas:
- [138-localizacion-mapeo-y-slam](../../classes/part-11-embodied-ai-robotics-and-computer-use/138-localizacion-mapeo-y-slam/README.md)

---

[⬅️ Guías docentes del eje](README.md)
