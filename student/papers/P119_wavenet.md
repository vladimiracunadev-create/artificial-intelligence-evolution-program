# 🎒 Ficha de estudio — P119 · WaveNet: un modelo generativo de audio en crudo

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *WaveNet: A Generative Model for Raw Audio* (2016)
**Nivel:** L3 · **Notebook:** [`P119_wavenet.ipynb`](../../notebooks/papers/P119_wavenet.ipynb)

## En una frase

Genera la forma de onda muestra a muestra con convoluciones causales dilatadas, y cierra la brecha de naturalidad que arrastraba la síntesis de voz.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «Modelar audio directamente exige un contexto de miles de muestras: a 16 kHz, un segundo son 16 000 valores. Una convolución normal necesitaría miles de capas para verlo, y una recurrente no puede entrenarse en paralelo sobre esa longitud.»
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

- `audio`
- `convolución dilatada`
- `causalidad`
- `μ-law`
- `síntesis de voz`

## Fuentes primarias

- [arXiv:1609.03499](https://arxiv.org/abs/1609.03499)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P119_wavenet/README.md)
