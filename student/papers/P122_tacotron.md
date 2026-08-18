# 🎒 Ficha de estudio — P122 · Síntesis de voz natural condicionando WaveNet con espectrogramas mel predichos

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *Natural TTS Synthesis by Conditioning WaveNet on Mel Spectrogram Predictions* (2018)
**Nivel:** L2 · **Notebook:** [`P122_tacotron.ipynb`](../../notebooks/papers/P122_tacotron.ipynb)

## En una frase

Parte la síntesis en dos etapas con el espectrograma mel como interfaz, y alcanza naturalidad indistinguible de una grabación en la escala de opinión media.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «Predecir la forma de onda directamente desde el texto es intratable: tres segundos de audio son decenas de miles de pasos autorregresivos, y ningún modelo con atención puede alinear texto contra una secuencia de esa longitud.»
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

- `síntesis de voz`
- `espectrograma mel`
- `atención monótona`
- `vocoder`
- `arquitectura en dos etapas`

## Fuentes primarias

- [doi:10.1109/ICASSP.2018.8461368](https://doi.org/10.1109/ICASSP.2018.8461368)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P122_tacotron/README.md)
