# 🎒 Ficha de estudio — P41 · Adam: un método de optimización estocástica

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *Adam: A Method for Stochastic Optimization* (2014)
**Nivel:** L2 · **Notebook:** [`P41_adam.ipynb`](../../notebooks/papers/P41_adam.ipynb)

## En una frase

Un paso de aprendizaje por dimensión, adaptado a la escala de su propio gradiente. Es el optimizador por defecto de casi todo lo que vino después.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «SGD usa la misma tasa de aprendizaje en todas las direcciones. En un problema mal condicionado, o oscila en las direcciones de mucha curvatura o se arrastra en las de poca.»
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

- `Adam`
- `optimización adaptativa`
- `momentos`
- `corrección de sesgo`
- `tasa de aprendizaje`

## Fuentes primarias

- [arXiv:1412.6980](https://arxiv.org/abs/1412.6980)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P41_adam/README.md)
