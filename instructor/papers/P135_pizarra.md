# 👩‍🏫 Guía docente — P135 · El sistema Hearsay-II: integrar conocimiento para resolver incertidumbre

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *The Hearsay-II Speech-Understanding System: Integrating Knowledge to Resolve Uncertainty* (1980, ACM Computing Surveys, 12(2), 213–253)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Entender habla exige combinar conocimiento acústico, léxico, sintáctico y semántico. Ninguna fuente decide sola, y encadenarlas en una tubería fija obliga a comprometerse pronto: un error temprano llega intacto al final.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Una estructura compartida —la pizarra— donde cada fuente escribe hipótesis parciales con su credibilidad, y un control oportunista que decide a quién invocar según lo que ya hay escrito. Nadie se compromete hasta que hay evidencia.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P135_pizarra.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P135_pizarra`](../../papers/foundational/P135_pizarra/README.md)
- Notebook: [`P135_pizarra.ipynb`](../../notebooks/papers/P135_pizarra.ipynb)
- Evaluación: [`P135_pizarra.md`](../../assessments/papers/P135_pizarra.md)
- Clases del programa relacionadas:
- [130-blackboard-y-memoria-compartida](../../classes/part-10-multi-agent-systems-and-interoperability/130-blackboard-y-memoria-compartida/README.md)

---

[⬅️ Guías docentes del eje](README.md)
