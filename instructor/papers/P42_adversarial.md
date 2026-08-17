# 👩‍🏫 Guía docente — P42 · Explicar y aprovechar los ejemplos adversarios

> Generado por `python scripts/generate_papers.py`. Las notas de aula se editan en la ficha.

**Paper:** *Explaining and Harnessing Adversarial Examples* (2014, arXiv:1412.6572 · ICLR 2015)
**Nivel:** L3 · **Duración sugerida:** 1 sesión de 90 min + trabajo autónomo

## Sesión de 90 minutos

| Bloque | Min | Qué ocurre | Evidencia |
|---|---:|---|---|
| Contexto histórico | 15 | Se plantea el problema anterior sin nombrar la solución: *Szegedy et al. (2013) habían descubierto que perturbaciones minúsculas engañaban a las redes, y se atribuía a la extrema no linealidad de los modelos profundos.* | El grupo propone al menos 2 soluciones ingenuas |
| Propuesta | 15 | Se presenta la idea: *Mostrar que la explicación es la contraria —el comportamiento demasiado LINEAL en alta dimensión— y derivar de ahí un ataque de un solo paso (FGSM) y una defensa por entrenamiento adversario.* | Cada estudiante la reformula en una frase |
| Predicción | 10 | Sección 7 del notebook, **antes** de ejecutar | Predicciones escritas y visibles |
| Ejecución | 20 | Notebook `P42_adversarial.ipynb`, secciones 6–9 | Salida del experimento controlado |
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

- Ficha completa: [`P42_adversarial`](../../papers/foundational/P42_adversarial/README.md)
- Notebook: [`P42_adversarial.ipynb`](../../notebooks/papers/P42_adversarial.ipynb)
- Evaluación: [`P42_adversarial.md`](../../assessments/papers/P42_adversarial.md)
- Clases del programa relacionadas:
- [053-cnn-y-aprendizaje-espacial](../../classes/part-04-neural-networks-and-deep-learning/053-cnn-y-aprendizaje-espacial/README.md)
- [162-red-teaming-y-abuso](../../classes/part-13-evaluation-safety-security-and-governance/162-red-teaming-y-abuso/README.md)
- [163-prompt-injection-e-instrucciones-no-confiables](../../classes/part-13-evaluation-safety-security-and-governance/163-prompt-injection-e-instrucciones-no-confiables/README.md)

---

[⬅️ Guías docentes del eje](README.md)
