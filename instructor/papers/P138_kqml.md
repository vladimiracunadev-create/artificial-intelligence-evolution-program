# 👩‍🏫 Guía docente — P138 · KQML como lenguaje de comunicación entre agentes

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *KQML as an agent communication language* (1994, CIKM '94, 456–463)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Dos agentes que intercambian «puerta(abierta)» no pueden saber si eso es una afirmación, una pregunta, una orden o una negación. Y sin una capa común, conectar N agentes con M lenguajes de contenido exige un adaptador por pareja.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Un lenguaje de mensajes en tres capas —contenido, mensaje y comunicación— donde una **performativa** declara el acto de habla: tell, ask-if, achieve, subscribe. El contenido va dentro y puede estar en cualquier lenguaje.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P138_kqml.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P138_kqml`](../../papers/foundational/P138_kqml/README.md)
- Notebook: [`P138_kqml.ipynb`](../../notebooks/papers/P138_kqml.ipynb)
- Evaluación: [`P138_kqml.md`](../../assessments/papers/P138_kqml.md)
- Clases del programa relacionadas:
- [134-a2a-descubrimiento-e-interoperabilidad](../../classes/part-10-multi-agent-systems-and-interoperability/134-a2a-descubrimiento-e-interoperabilidad/README.md)

---

[⬅️ Guías docentes del eje](README.md)
