# 👩‍🏫 Guía docente — P146 · Aprendizaje eficiente en comunicación de redes profundas con datos descentralizados

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Communication-Efficient Learning of Deep Networks from Decentralized Data* (2017, AISTATS 2017, PMLR 54, 1273–1282)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Los datos más útiles para entrenar —lo que se escribe en el teclado, lo que se fotografía— son los más sensibles y viven en millones de dispositivos con conexión lenta e intermitente. Centralizarlos es caro en comunicación y problemático en privacidad.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Promediado federado: cada cliente entrena varias épocas en local sobre sus propios datos y envía solo los pesos resultantes; el servidor los promedia y devuelve el modelo. Más cómputo local a cambio de menos rondas de comunicación.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P146_federado.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P146_federado`](../../papers/foundational/P146_federado/README.md)
- Notebook: [`P146_federado.ipynb`](../../notebooks/papers/P146_federado.ipynb)
- Evaluación: [`P146_federado.md`](../../assessments/papers/P146_federado.md)
- Clases del programa relacionadas:
- [177-privacidad-diferencial-y-aprendizaje-federado](../../classes/part-14-frontier-research-and-capstones/177-privacidad-diferencial-y-aprendizaje-federado/README.md)

---

[⬅️ Guías docentes del eje](README.md)
