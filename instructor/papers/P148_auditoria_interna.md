# 👩‍🏫 Guía docente — P148 · Cerrar la brecha de responsabilidad: un marco de auditoría algorítmica interna

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing* (2020, FAT* '20, 33–44)
**Nivel:** L1 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *La auditoría algorítmica se hacía —cuando se hacía— al final, sobre un sistema ya construido. En ese punto los hallazgos importantes son incorregibles: si faltan las etiquetas de subgrupo, no se puede desagregar la evaluación, y recogerlas exigiría rehacer el conjunto de datos.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Cinco etapas —alcance, correspondencia, recogida de artefactos, pruebas y reflexión— cada una con entregables concretos: declaración de caso de uso, mapa de interesados, hojas de datos, tarjetas de modelo, resultados desagregados y plan de mitigación. La auditoría produce una traza, no un veredicto.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P148_auditoria_interna.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P148_auditoria_interna`](../../papers/foundational/P148_auditoria_interna/README.md)
- Notebook: [`P148_auditoria_interna.ipynb`](../../notebooks/papers/P148_auditoria_interna.ipynb)
- Evaluación: [`P148_auditoria_interna.md`](../../assessments/papers/P148_auditoria_interna.md)
- Clases del programa relacionadas:
- [169-gobernanza-roles-y-gestion-de-riesgo](../../classes/part-13-evaluation-safety-security-and-governance/169-gobernanza-roles-y-gestion-de-riesgo/README.md)
- [170-normativa-auditoria-y-evidencia](../../classes/part-13-evaluation-safety-security-and-governance/170-normativa-auditoria-y-evidencia/README.md)

---

[⬅️ Guías docentes del eje](README.md)
