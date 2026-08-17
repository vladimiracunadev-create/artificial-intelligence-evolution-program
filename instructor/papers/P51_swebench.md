# 👩‍🏫 Guía docente — P51 · SWE-bench: ¿pueden los modelos resolver incidencias reales de GitHub?

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?* (2023, arXiv:2310.06770 · ICLR 2024)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Los benchmarks de programación usaban problemas de juguete autocontenidos y se saturaban rápido; no medían nada parecido al trabajo real de mantener un repositorio.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Construir el conjunto a partir de incidencias y parches reales de proyectos populares, y evaluar con un criterio objetivo: aplicar el parche generado y ejecutar los tests del propio repositorio.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P51_swebench.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P51_swebench`](../../papers/foundational/P51_swebench/README.md)
- Notebook: [`P51_swebench.ipynb`](../../notebooks/papers/P51_swebench.ipynb)
- Evaluación: [`P51_swebench.md`](../../assessments/papers/P51_swebench.md)
- Clases del programa relacionadas:
- [160-diseno-de-evaluaciones-y-criterios-de-exito](../../classes/part-13-evaluation-safety-security-and-governance/160-diseno-de-evaluaciones-y-criterios-de-exito/README.md)
- [122-evaluacion-y-depuracion-de-agentes](../../classes/part-09-ai-agent-engineering/122-evaluacion-y-depuracion-de-agentes/README.md)

---

[⬅️ Guías docentes del eje](README.md)
