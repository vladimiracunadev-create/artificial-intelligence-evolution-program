# 🎒 Ficha de estudio — P08 · La atención es todo lo que necesitas

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *Attention Is All You Need* (2017)
**Nivel:** L4 · **Notebook:** [`P08_transformer.ipynb`](../../notebooks/papers/P08_transformer.ipynb)

## En una frase

Elimina la recurrencia y la convolución del modelado de secuencias: todo el cómputo de una capa se paraleliza.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «La recurrencia impone un cómputo secuencial en la longitud de la secuencia y camina O(n) pasos entre posiciones distantes; eso limita el entrenamiento a gran escala.»
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

- `Transformer`
- `self-attention`
- `multi-head`
- `scaled dot-product`
- `codificación posicional`
- `máscara causal`
- `paralelización`

## Fuentes primarias

- [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)
- [NeurIPS 2017 (proceedings)](https://papers.nips.cc/paper_files/paper/2017)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P08_transformer/README.md)
