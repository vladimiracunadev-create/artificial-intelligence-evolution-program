# 👩‍🏫 Guía docente — P106 · OSWorld: evaluación de agentes multimodales en tareas abiertas sobre entornos informáticos reales

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments* (2024, NeurIPS 2024 · arXiv:2404.07972)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Los bancos de pruebas de agentes se limitaban al navegador o a entornos de juguete. El trabajo de oficina real cruza aplicaciones —hoja de cálculo, ficheros, terminal, navegador— y ahí no había forma comparable de medir nada.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Un entorno de escritorio completo en máquina virtual con estado reiniciable, cientos de tareas reales recogidas de usuarios, y para cada una un script de verificación que inspecciona el estado final del sistema: una celda, un fichero, un código de salida.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P106_osworld.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P106_osworld`](../../papers/foundational/P106_osworld/README.md)
- Notebook: [`P106_osworld.ipynb`](../../notebooks/papers/P106_osworld.ipynb)
- Evaluación: [`P106_osworld.md`](../../assessments/papers/P106_osworld.md)
- Clases del programa relacionadas:
- [146-automatizacion-de-escritorio-y-rpa-agentica](../../classes/part-11-embodied-ai-robotics-and-computer-use/146-automatizacion-de-escritorio-y-rpa-agentica/README.md)

---

[⬅️ Guías docentes del eje](README.md)
