# 🎒 Ficha de estudio — P49 · QLoRA: ajuste fino eficiente de modelos cuantizados

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *QLoRA: Efficient Finetuning of Quantized LLMs* (2023)
**Nivel:** L3 · **Notebook:** [`P49_qlora.ipynb`](../../notebooks/papers/P49_qlora.ipynb)

## En una frase

Pone el ajuste fino de un modelo muy grande al alcance de una sola GPU de consumo.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «LoRA reduce los parámetros entrenables, pero el modelo base seguía teniendo que caber en memoria en precisión alta: eso dejaba fuera a casi todo el mundo.»
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

- `QLoRA`
- `cuantización de 4 bits`
- `NF4`
- `ajuste eficiente`
- `memoria`

## Fuentes primarias

- [arXiv:2305.14314](https://arxiv.org/abs/2305.14314)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P49_qlora/README.md)
