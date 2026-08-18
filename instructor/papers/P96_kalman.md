# 👩‍🏫 Guía docente — P96 · Un nuevo enfoque para los problemas de filtrado y predicción lineales

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *A New Approach to Linear Filtering and Prediction Problems* (1960, Journal of Basic Engineering, 82(1), 35–45)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Un sensor da medidas ruidosas y un modelo del movimiento acumula error. Promediarlos trata igual a los dos, e ignora que la confianza en cada uno cambia con el tiempo. Los métodos anteriores exigían guardar todo el historial.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Mantener una estimación y su varianza, predecir con el modelo, y corregir con la medida usando una ganancia que sale del cociente entre las dos incertidumbres. Recursivo: solo hace falta el estado anterior.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P96_kalman.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P96_kalman`](../../papers/foundational/P96_kalman/README.md)
- Notebook: [`P96_kalman.ipynb`](../../notebooks/papers/P96_kalman.ipynb)
- Evaluación: [`P96_kalman.md`](../../assessments/papers/P96_kalman.md)
- Clases del programa relacionadas:
- [137-sensores-actuadores-y-fusion](../../classes/part-11-embodied-ai-robotics-and-computer-use/137-sensores-actuadores-y-fusion/README.md)

---

[⬅️ Guías docentes del eje](README.md)
