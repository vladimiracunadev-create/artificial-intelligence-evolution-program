# 👩‍🏫 Guía docente — P103 · Aleatorización de dominio para transferir redes profundas de la simulación al mundo real

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World* (2017, IROS 2017, 23–30 · arXiv:1703.06907)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Entrenar en simulación es barato y seguro; desplegar en el mundo real falla. El hueco entre simulación y realidad se atacaba mejorando el simulador, una carrera cara y sin final: siempre queda algo que no se modeló.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Aleatorizar agresivamente los parámetros del simulador —texturas, iluminación, posiciones de cámara, ruido— durante el entrenamiento. Si la variabilidad es suficiente, al modelo la realidad le parece una configuración más de las que ya vio.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P103_domain_randomization.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P103_domain_randomization`](../../papers/foundational/P103_domain_randomization/README.md)
- Notebook: [`P103_domain_randomization.ipynb`](../../notebooks/papers/P103_domain_randomization.ipynb)
- Evaluación: [`P103_domain_randomization.md`](../../assessments/papers/P103_domain_randomization.md)
- Clases del programa relacionadas:
- [142-simulacion-sim-to-real-y-digital-twins](../../classes/part-11-embodied-ai-robotics-and-computer-use/142-simulacion-sim-to-real-y-digital-twins/README.md)

---

[⬅️ Guías docentes del eje](README.md)
