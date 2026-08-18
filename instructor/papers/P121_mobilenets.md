# 👩‍🏫 Guía docente — P121 · MobileNets: redes convolucionales eficientes para visión en dispositivos móviles

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications* (2017, arXiv:1704.04861)
**Nivel:** L2 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Las redes de visión que funcionaban exigían un centro de datos. En un teléfono, un sensor o un vehículo, el presupuesto es de milivatios y milisegundos, y no había forma sistemática de elegir dónde recortar.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Convolución separable en profundidad —filtrar cada canal por separado y luego combinarlos con núcleos de 1×1—, más un multiplicador de anchura y otro de resolución que parametrizan la familia entera.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P121_mobilenets.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P121_mobilenets`](../../papers/foundational/P121_mobilenets/README.md)
- Notebook: [`P121_mobilenets.ipynb`](../../notebooks/papers/P121_mobilenets.ipynb)
- Evaluación: [`P121_mobilenets.md`](../../assessments/papers/P121_mobilenets.md)
- Clases del programa relacionadas:
- [071-sensores-series-y-percepcion-en-el-borde](../../classes/part-05-language-vision-audio-and-multimodal-ai/071-sensores-series-y-percepcion-en-el-borde/README.md)

---

[⬅️ Guías docentes del eje](README.md)
