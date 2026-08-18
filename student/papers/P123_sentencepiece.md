# 🎒 Ficha de estudio — P123 · SentencePiece: un tokenizador y detokenizador de subpalabras simple e independiente del idioma

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing* (2018)
**Nivel:** L2 · **Notebook:** [`P123_sentencepiece.ipynb`](../../notebooks/papers/P123_sentencepiece.ipynb)

## En una frase

Elimina la pretokenización por espacios y hace la detokenización exacta, lo que convierte al tokenizador en una pieza reproducible e independiente del idioma.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «BPE suponía texto ya partido por espacios, y eso no es universal: el japonés y el chino no los usan. Además cada implementación normalizaba a su manera, así que reconstruir el texto original era imposible y los resultados no eran comparables.»
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

- `tokenización`
- `reversibilidad`
- `modelo unigrama`
- `multilingüe`
- `regularización de subpalabra`

## Fuentes primarias

- [doi:10.18653/v1/D18-2012](https://doi.org/10.18653/v1/D18-2012)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P123_sentencepiece/README.md)
