# 👩‍🏫 Guía docente — P91 · Fusión, propagación y estructuración en redes de creencia

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Fusion, Propagation, and Structuring in Belief Networks* (1986, Artificial Intelligence, 29(3), 241–288)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Aplicar probabilidad a un dominio con decenas de variables exige una tabla conjunta con 2ⁿ entradas: imposible de almacenar, de estimar y de actualizar. Esa fue la razón técnica por la que la IA de los setenta la abandonó en favor de los factores de certeza.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Representar las dependencias con un grafo dirigido acíclico. Las independencias condicionales que el grafo codifica reducen la conjunta a un producto de condicionales locales, y permiten propagar creencias por paso de mensajes entre nodos vecinos.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P91_redes_bayesianas.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P91_redes_bayesianas`](../../papers/foundational/P91_redes_bayesianas/README.md)
- Notebook: [`P91_redes_bayesianas.ipynb`](../../notebooks/papers/P91_redes_bayesianas.ipynb)
- Evaluación: [`P91_redes_bayesianas.md`](../../assessments/papers/P91_redes_bayesianas.md)
- Clases del programa relacionadas:
- [027-redes-bayesianas-e-independencia-condicional](../../classes/part-02-probabilistic-evolutionary-and-decision-ai/027-redes-bayesianas-e-independencia-condicional/README.md)

---

[⬅️ Guías docentes del eje](README.md)
