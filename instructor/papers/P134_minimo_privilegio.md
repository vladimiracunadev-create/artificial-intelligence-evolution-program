# 👩‍🏫 Guía docente — P134 · La protección de la información en los sistemas informáticos

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *The Protection of Information in Computer Systems* (1975, Proceedings of the IEEE, 63(9), 1278–1308)
**Nivel:** L1 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Los sistemas compartidos daban acceso amplio por comodidad, y cada mecanismo de protección se diseñaba ad hoc. No había criterios explícitos para decidir qué permisos conceder ni para juzgar si un diseño era defendible.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Ocho principios, de los cuales dos gobiernan el resto: valores por defecto a prueba de fallos —denegar salvo permiso explícito— y mínimo privilegio —lo justo para la tarea—. Más mediación completa: comprobar cada acceso, no solo el primero.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P134_minimo_privilegio.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P134_minimo_privilegio`](../../papers/foundational/P134_minimo_privilegio/README.md)
- Notebook: [`P134_minimo_privilegio.ipynb`](../../notebooks/papers/P134_minimo_privilegio.ipynb)
- Evaluación: [`P134_minimo_privilegio.md`](../../assessments/papers/P134_minimo_privilegio.md)
- Clases del programa relacionadas:
- [119-permisos-sandbox-y-minimo-privilegio](../../classes/part-09-ai-agent-engineering/119-permisos-sandbox-y-minimo-privilegio/README.md)

---

[⬅️ Guías docentes del eje](README.md)
