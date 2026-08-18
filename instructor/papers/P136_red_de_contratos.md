# 👩‍🏫 Guía docente — P136 · El protocolo de red de contratos: comunicación y control en un resolutor distribuido

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *The Contract Net Protocol: High-Level Communication and Control in a Distributed Problem Solver* (1980, IEEE Transactions on Computers, C-29(12), 1104–1113)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Asignar tareas a nodos exige saber qué puede hacer cada uno y cuánto tiene encima. Mantener ese registro centralizado se desactualiza, no escala y falla justo cuando los nodos aparecen y desaparecen.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Invertir el flujo: el coordinador **anuncia** la tarea, los nodos capaces **ofertan** con su coste estimado, y el coordinador **adjudica** a la mejor oferta. Quien conoce su capacidad es quien la declara, en el momento de usarla.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P136_red_de_contratos.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P136_red_de_contratos`](../../papers/foundational/P136_red_de_contratos/README.md)
- Notebook: [`P136_red_de_contratos.ipynb`](../../notebooks/papers/P136_red_de_contratos.ipynb)
- Evaluación: [`P136_red_de_contratos.md`](../../assessments/papers/P136_red_de_contratos.md)
- Clases del programa relacionadas:
- [126-handoffs-y-transferencia-de-contexto](../../classes/part-10-multi-agent-systems-and-interoperability/126-handoffs-y-transferencia-de-contexto/README.md)

---

[⬅️ Guías docentes del eje](README.md)
