# 👩‍🏫 Guía docente — P143 · Calibrar el ruido a la sensibilidad en el análisis privado de datos

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Calibrating Noise to Sensitivity in Private Data Analysis* (2006, TCC 2006, 265–284)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La anonimización fallaba una y otra vez: cruzando datos supuestamente anónimos con otras fuentes se reidentificaba a personas. El problema de fondo es que cualquier definición basada en «quitar los identificadores» depende de qué más sepa quien ataca, y eso no se puede acotar.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Definir la privacidad como una propiedad del **mecanismo**: que la salida cambie poco —acotado por ε— cuando se añade o quita una persona. Y dar un mecanismo que la cumple: añadir ruido de Laplace calibrado a la sensibilidad de la consulta.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P143_privacidad_diferencial.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P143_privacidad_diferencial`](../../papers/foundational/P143_privacidad_diferencial/README.md)
- Notebook: [`P143_privacidad_diferencial.ipynb`](../../notebooks/papers/P143_privacidad_diferencial.ipynb)
- Evaluación: [`P143_privacidad_diferencial.md`](../../assessments/papers/P143_privacidad_diferencial.md)
- Clases del programa relacionadas:
- [165-privacidad-secretos-y-minimizacion-de-datos](../../classes/part-13-evaluation-safety-security-and-governance/165-privacidad-secretos-y-minimizacion-de-datos/README.md)
- [177-privacidad-diferencial-y-aprendizaje-federado](../../classes/part-14-frontier-research-and-capstones/177-privacidad-diferencial-y-aprendizaje-federado/README.md)

---

[⬅️ Guías docentes del eje](README.md)
