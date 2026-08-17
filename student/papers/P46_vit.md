# 🎒 Ficha de estudio — P46 · Una imagen vale 16x16 palabras: Transformers para reconocimiento de imágenes a escala

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale* (2020)
**Nivel:** L3 · **Notebook:** [`P46_vit.ipynb`](../../notebooks/papers/P46_vit.ipynb)

## En una frase

Trata la imagen como una secuencia de parches y aplica un Transformer puro: la convolución deja de ser imprescindible en visión.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «La convolución traía de fábrica localidad y equivarianza a la traslación, y se asumía que sin esos sesgos inductivos la visión no funcionaría.»
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

- `ViT`
- `parches`
- `sesgo inductivo`
- `preentrenamiento a escala`
- `visión`

## Fuentes primarias

- [arXiv:2010.11929](https://arxiv.org/abs/2010.11929)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P46_vit/README.md)
