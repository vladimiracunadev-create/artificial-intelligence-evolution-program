# 👩‍🏫 Guía docente — P80 · Modelización estadística: las dos culturas

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Statistical Modeling: The Two Cultures* (2001, Statistical Science, 16(3), 199–231)
**Nivel:** L1 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La estadística académica suponía que los datos venían de un modelo con forma conocida y juzgaba los métodos por el ajuste a ese supuesto. Si el supuesto es falso —y casi siempre lo es— las conclusiones sobre el mecanismo no valen nada.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Distinguir dos culturas y sus criterios: la del modelo de datos, que valida supuestos, y la algorítmica, que trata el mecanismo como desconocido y se juzga por exactitud predictiva medida fuera de muestra.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P80_dos_culturas.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P80_dos_culturas`](../../papers/foundational/P80_dos_culturas/README.md)
- Notebook: [`P80_dos_culturas.ipynb`](../../notebooks/papers/P80_dos_culturas.ipynb)
- Evaluación: [`P80_dos_culturas.md`](../../assessments/papers/P80_dos_culturas.md)
- Clases del programa relacionadas:
- [037-flujo-supervisado-y-particion-train-validation-test](../../classes/part-03-classical-machine-learning/037-flujo-supervisado-y-particion-train-validation-test/README.md)
- [047-metricas-calibracion-sesgo-y-costo-de-error](../../classes/part-03-classical-machine-learning/047-metricas-calibracion-sesgo-y-costo-de-error/README.md)

---

[⬅️ Guías docentes del eje](README.md)
