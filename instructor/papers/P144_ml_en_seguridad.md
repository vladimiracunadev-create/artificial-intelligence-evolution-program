# 👩‍🏫 Guía docente — P144 · Fuera del mundo cerrado: sobre el uso de aprendizaje automático para detectar intrusiones

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Outside the Closed World: On Using Machine Learning for Network Intrusion Detection* (2010, IEEE Symposium on Security and Privacy 2010, 305–316)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Cientos de artículos aplicaban aprendizaje automático a la detección de intrusiones con métricas excelentes, y casi ninguno de esos sistemas llegaba a producción. La brecha entre el resultado publicado y el sistema operable no se estaba explicando.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Cinco razones estructurales: la clase base extremadamente desequilibrada hace que una precisión excelente produzca miles de falsas alarmas; el coste de los errores es asimétrico; no hay datos representativos de ataques nuevos; el adversario se adapta al detector; y la alerta hay que poder explicársela a quien actúa.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P144_ml_en_seguridad.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P144_ml_en_seguridad`](../../papers/foundational/P144_ml_en_seguridad/README.md)
- Notebook: [`P144_ml_en_seguridad.ipynb`](../../notebooks/papers/P144_ml_en_seguridad.ipynb)
- Evaluación: [`P144_ml_en_seguridad.md`](../../assessments/papers/P144_ml_en_seguridad.md)
- Clases del programa relacionadas:
- [179-ia-para-ciberseguridad-y-defensa](../../classes/part-14-frontier-research-and-capstones/179-ia-para-ciberseguridad-y-defensa/README.md)

---

[⬅️ Guías docentes del eje](README.md)
