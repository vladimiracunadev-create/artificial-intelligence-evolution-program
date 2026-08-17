# 🎒 Ficha de estudio — P34 · RoFormer: Transformer mejorado con codificación posicional rotatoria

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *RoFormer: Enhanced Transformer with Rotary Position Embedding* (2021)
**Nivel:** L3 · **Notebook:** [`P34_rope.ipynb`](../../notebooks/papers/P34_rope.ipynb)

## En una frase

La posición se codifica rotando, y la atención pasa a depender solo de la distancia relativa. Es la base de casi todo modelo actual.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «La codificación sinusoidal del Transformer se SUMA al embedding y codifica posición absoluta; la atención no ve directamente la distancia entre dos tokens, que es lo que importa en lenguaje.»
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

- `RoPE`
- `posición relativa`
- `rotación`
- `contexto largo`
- `decaimiento con la distancia`

## Fuentes primarias

- [arXiv:2104.09864](https://arxiv.org/abs/2104.09864)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P34_rope/README.md)
