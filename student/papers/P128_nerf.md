# 🎒 Ficha de estudio — P128 · NeRF: representar escenas como campos de radiancia neuronal

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis* (2020)
**Nivel:** L3 · **Notebook:** [`P128_nerf.ipynb`](../../notebooks/papers/P128_nerf.ipynb)

## En una frase

Sustituye la escena explícita por una función continua que un perceptrón representa, y sintetiza vistas nuevas con una fidelidad que no se había visto.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «Representar una escena 3D como rejilla de vóxeles cuesta O(n³) en memoria: la resolución se paga al cubo y las rejillas finas no caben. Y las mallas exigen reconstruir geometría explícita, que falla con pelo, humo o vidrio.»
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

- `síntesis de vistas`
- `representación implícita`
- `renderizado volumétrico`
- `codificación posicional`
- `3D`

## Fuentes primarias

- [doi:10.1007/978-3-030-58452-8_24](https://doi.org/10.1007/978-3-030-58452-8_24)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P128_nerf/README.md)
