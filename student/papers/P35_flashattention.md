# 🎒 Ficha de estudio — P35 · FlashAttention: atención exacta, rápida y eficiente en memoria, consciente de la E/S

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness* (2022)
**Nivel:** L4 · **Notebook:** [`P35_flashattention.ipynb`](../../notebooks/papers/P35_flashattention.ipynb)

## En una frase

El cuello de botella de la atención no eran los FLOPs sino las lecturas y escrituras a memoria. Y la solución es EXACTA, no aproximada.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «Durante años se atacó el coste O(n²) de la atención con aproximaciones (dispersa, lineal), que perdían calidad y a menudo ni siquiera eran más rápidas en la práctica.»
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

- `FlashAttention`
- `consciencia de E/S`
- `tiling`
- `atención exacta`
- `jerarquía de memoria`
- `contexto largo`

## Fuentes primarias

- [arXiv:2205.14135](https://arxiv.org/abs/2205.14135)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P35_flashattention/README.md)
