# 👩‍🏫 Guía docente — P107 · Dapper, una infraestructura de trazado de sistemas distribuidos a gran escala

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Dapper, a Large-Scale Distributed Systems Tracing Infrastructure* (2010, Google Technical Report)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *En una arquitectura distribuida, cada servicio tiene sus métricas y sus registros. Cuando una petición va lenta, nadie puede reconstruir por dónde pasó ni dónde se gastó el tiempo: se ve el total y nada más.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Propagar un identificador de traza con la petición por todos los servicios, registrar un span por operación con su relación padre-hijo, y muestrear una fracción de las trazas para que el coste sea asumible sin perder los agregados.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P107_dapper.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P107_dapper`](../../papers/foundational/P107_dapper/README.md)
- Notebook: [`P107_dapper.ipynb`](../../notebooks/papers/P107_dapper.ipynb)
- Evaluación: [`P107_dapper.md`](../../assessments/papers/P107_dapper.md)
- Clases del programa relacionadas:
- [153-observabilidad-logs-metricas-y-trazas](../../classes/part-12-ai-engineering-mlops-llmops-and-agentops/153-observabilidad-logs-metricas-y-trazas/README.md)

---

[⬅️ Guías docentes del eje](README.md)
