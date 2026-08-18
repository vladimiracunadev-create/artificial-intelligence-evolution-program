# 👩‍🏫 Guía docente — P116 · Por qué Johnny no sabe hacer prompts: cómo los no expertos intentan (y fallan) diseñar prompts

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Why Johnny Can't Prompt: How Non-AI Experts Try (and Fail) to Design LLM Prompts* (2023, CHI '23)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Escribir prompts parece accesible a cualquiera, y por eso se hace sin ninguna disciplina de ingeniería: sin versionar, sin conjunto de evaluación y mirando dos o tres ejemplos. Con muestras pequeñas, el ruido tiene el mismo tamaño que las mejoras que se buscan.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Un estudio con participantes no expertos que documenta sus estrategias reales, identifica el patrón dominante —iteración oportunista basada en anécdotas— y argumenta que el prompt necesita las prácticas del software: versionado, evaluación fija y una hipótesis por cambio.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P116_gestion_de_prompts.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P116_gestion_de_prompts`](../../papers/foundational/P116_gestion_de_prompts/README.md)
- Notebook: [`P116_gestion_de_prompts.ipynb`](../../notebooks/papers/P116_gestion_de_prompts.ipynb)
- Evaluación: [`P116_gestion_de_prompts.md`](../../assessments/papers/P116_gestion_de_prompts.md)
- Clases del programa relacionadas:
- [155-llmops-y-gestion-de-prompts](../../classes/part-12-ai-engineering-mlops-llmops-and-agentops/155-llmops-y-gestion-de-prompts/README.md)

---

[⬅️ Guías docentes del eje](README.md)
