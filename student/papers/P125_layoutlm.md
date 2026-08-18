# 🎒 Ficha de estudio — P125 · LayoutLM: preentrenamiento de texto y disposición para comprensión de documentos

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *LayoutLM: Pre-training of Text and Layout for Document Image Understanding* (2020)
**Nivel:** L2 · **Notebook:** [`P125_layoutlm.ipynb`](../../notebooks/papers/P125_layoutlm.ipynb)

## En una frase

Añade la posición en la página como una incrustación más, y con eso convierte un modelo de lenguaje en un lector de formularios y facturas.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «Un documento no es una secuencia de texto: es texto colocado. Al linealizar una factura de dos columnas, el OCR intercala campos que no se relacionan, y un modelo que solo ve la cadena no puede emparejar cada etiqueta con su valor.»
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

- `documentos`
- `disposición`
- `OCR`
- `extracción de campos`
- `multimodal`

## Fuentes primarias

- [doi:10.1145/3394486.3403172](https://doi.org/10.1145/3394486.3403172)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P125_layoutlm/README.md)
