# 👩‍🏫 Guía docente — P11 · Generación aumentada por recuperación para tareas de PLN intensivas en conocimiento

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (2020, arXiv:2005.11401 · NeurIPS 2020)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Todo lo que un modelo sabe está congelado en sus pesos: no se puede actualizar sin reentrenar, ni auditar de dónde salió una afirmación.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Combinar un recuperador denso (DPR) sobre un índice de Wikipedia con un generador seq2seq (BART), entrenados de forma conjunta.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P11_rag.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P11_rag`](../../papers/foundational/P11_rag/README.md)
- Notebook: [`P11_rag.ipynb`](../../notebooks/papers/P11_rag.ipynb)
- Evaluación: [`P11_rag.md`](../../assessments/papers/P11_rag.md)
- Clases del programa relacionadas:
- [102-busqueda-lexica-y-bm25](../../classes/part-08-retrieval-context-memory-and-knowledge/102-busqueda-lexica-y-bm25/README.md)
- [103-busqueda-hibrida-y-fusion-de-rankings](../../classes/part-08-retrieval-context-memory-and-knowledge/103-busqueda-hibrida-y-fusion-de-rankings/README.md)
- [104-re-ranking-y-filtros-de-evidencia](../../classes/part-08-retrieval-context-memory-and-knowledge/104-re-ranking-y-filtros-de-evidencia/README.md)
- [105-rag-basico-con-citas](../../classes/part-08-retrieval-context-memory-and-knowledge/105-rag-basico-con-citas/README.md)
- [106-transformacion-y-descomposicion-de-consultas](../../classes/part-08-retrieval-context-memory-and-knowledge/106-transformacion-y-descomposicion-de-consultas/README.md)
- [110-evaluacion-de-fidelidad-cobertura-y-atribucion](../../classes/part-08-retrieval-context-memory-and-knowledge/110-evaluacion-de-fidelidad-cobertura-y-atribucion/README.md)
- [111-proyecto-rag-productivo-y-auditable](../../classes/part-08-retrieval-context-memory-and-knowledge/111-proyecto-rag-productivo-y-auditable/README.md)
- [168-alucinacion-grounding-y-abstencion](../../classes/part-13-evaluation-safety-security-and-governance/168-alucinacion-grounding-y-abstencion/README.md)

---

[⬅️ Guías docentes del eje](README.md)
