# 🎒 Ficha de estudio — P127 · Jukebox: un modelo generativo de música

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *Jukebox: A Generative Model for Music* (2020)
**Nivel:** L3 · **Notebook:** [`P127_jukebox.ipynb`](../../notebooks/papers/P127_jukebox.ipynb)

## En una frase

Genera canciones con voz cantada reconocible modelando códigos discretos en tres escalas temporales, en vez de la forma de onda directamente.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «Cuatro minutos de audio a 44,1 kHz son más de diez millones de muestras. Ningún modelo autorregresivo opera sobre esa longitud, y comprimir a una sola escala obliga a elegir entre estructura larga y detalle tímbrico.»
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

- `música`
- `cuantización vectorial`
- `jerarquía temporal`
- `audio generativo`
- `estructura larga`

## Fuentes primarias

- [arXiv:2005.00341](https://arxiv.org/abs/2005.00341)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P127_jukebox/README.md)
