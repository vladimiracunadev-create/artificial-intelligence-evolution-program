# 🎒 Ficha de estudio — P101 · Una reducción del aprendizaje por imitación al aprendizaje en línea sin arrepentimiento

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning* (2011)
**Nivel:** L3 · **Notebook:** [`P101_dagger.ipynb`](../../notebooks/papers/P101_dagger.ipynb)

## En una frase

Explica por qué la clonación de comportamiento se degrada con el horizonte, y da un algoritmo que reduce el error de orden T² a orden T.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «Al clonar el comportamiento de un experto, el modelo se entrena con los estados que visita el EXPERTO y se ejecuta sobre los estados que visita ÉL MISMO. Un error lo saca de la distribución de entrenamiento, donde comete más errores, y la desviación se realimenta.»
3. Abre el notebook y **escribe tu predicción** (sección 7) antes de ejecutar nada.
4. Ejecuta y contrasta. Si acertaste, explica por qué; si fallaste, explica qué supusiste mal.
5. Haz el anti-patrón (sección 11) y su corrección. Es la parte que más se evalúa.
6. Escribe una limitación de la miniatura y una del paper. No las copies de la ficha.

## Checklist de «lo entendí»

- [ ] Sé qué se hacía antes de este paper y por qué no bastaba.
- [ ] Puedo dibujar el mecanismo sin mirar.
- [ ] Ejecuté la miniatura e interpreté su salida sin repetir el texto de la ficha.
- [ ] Sé nombrar una cosa que el paper **no** demostró.
- [ ] Sé qué idea de las que suelen atribuírsele llegó en realidad después.
- [ ] Puedo conectar este hito con el siguiente en una frase.

## Conceptos que debes poder definir

- `aprendizaje por imitación`
- `clonación de comportamiento`
- `cambio de distribución`
- `aprendizaje en línea`
- `arrepentimiento`

## Fuentes primarias

- [arXiv:1011.0686](https://arxiv.org/abs/1011.0686)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P101_dagger/README.md)
