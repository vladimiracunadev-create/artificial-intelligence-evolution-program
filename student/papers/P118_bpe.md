# 🎒 Ficha de estudio — P118 · Traducción automática neuronal de palabras raras con unidades de subpalabra

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *Neural Machine Translation of Rare Words with Subword Units* (2016)
**Nivel:** L2 · **Notebook:** [`P118_bpe.ipynb`](../../notebooks/papers/P118_bpe.ipynb)

## En una frase

Elimina el problema de la palabra desconocida haciendo que la unidad de vocabulario sea más pequeña que la palabra, con un algoritmo que la frecuencia decide sola.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «Un vocabulario de palabras completas siempre se queda corto: llega una palabra que no estaba y el modelo solo puede emitir un símbolo de desconocido, aunque sus raíces y sufijos sí estuvieran en el entrenamiento.»
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
- `subpalabras`
- `BPE`
- `vocabulario abierto`
- `traducción`

## Fuentes primarias

- [doi:10.18653/v1/P16-1162](https://doi.org/10.18653/v1/P16-1162)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P118_bpe/README.md)
