# 👩‍🏫 Guía docente — P105 · SeeClick: aprovechar el anclaje visual para agentes avanzados de interfaz gráfica

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents* (2024, ACL 2024 · arXiv:2401.10935)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Los agentes de interfaz dependían del árbol de accesibilidad o del HTML: texto estructurado que muchas aplicaciones no exponen, y que no cubre los elementos que solo son un icono. Sin ese texto, el agente no puede ni referirse al botón.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Trabajar directamente sobre la captura de pantalla y entrenar específicamente el anclaje: dada una instrucción en lenguaje natural, devolver las coordenadas del elemento. Con un banco de pruebas propio para medir esa capacidad por separado.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P105_seeclick.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P105_seeclick`](../../papers/foundational/P105_seeclick/README.md)
- Notebook: [`P105_seeclick.ipynb`](../../notebooks/papers/P105_seeclick.ipynb)
- Evaluación: [`P105_seeclick.md`](../../assessments/papers/P105_seeclick.md)
- Clases del programa relacionadas:
- [144-computer-use-basado-en-vision](../../classes/part-11-embodied-ai-robotics-and-computer-use/144-computer-use-basado-en-vision/README.md)

---

[⬅️ Guías docentes del eje](README.md)
