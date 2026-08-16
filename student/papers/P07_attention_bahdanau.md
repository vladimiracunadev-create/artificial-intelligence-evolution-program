# 🎒 Ficha de estudio — P07 · Traducción automática neuronal aprendiendo conjuntamente a alinear y traducir

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *Neural Machine Translation by Jointly Learning to Align and Translate* (2014)
**Nivel:** L3 · **Notebook:** [`P07_attention_bahdanau.ipynb`](../../notebooks/papers/P07_attention_bahdanau.ipynb)

## En una frase

Nace la atención: el decodificador deja de depender de un único vector y consulta toda la entrada en cada paso.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «Comprimir una frase entera en un vector fijo degrada la traducción de frases largas: es un cuello de botella de información.»
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

- `atención`
- `alineación`
- `vector de contexto dinámico`
- `softmax`
- `atención aditiva`

## Fuentes primarias

- [arXiv:1409.0473](https://arxiv.org/abs/1409.0473)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P07_attention_bahdanau/README.md)
