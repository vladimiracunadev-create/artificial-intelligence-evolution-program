# 🎒 Ficha de estudio — P21 · Mixtral: mezcla dispersa de expertos

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *Mixtral of Experts* (2024)
**Nivel:** L3 · **Notebook:** [`P21_moe.ipynb`](../../notebooks/papers/P21_moe.ipynb)

## En una frase

Desacopla capacidad de cómputo: 47 000 millones de parámetros totales, 13 000 millones activos por token.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «En un modelo denso, cada token paga TODOS los parámetros. Crecer en capacidad implica crecer en coste de inferencia en la misma proporción.»
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

- `mezcla de expertos`
- `router`
- `top-2`
- `parámetros activos`
- `balanceo de carga`
- `Apache 2.0`

## Fuentes primarias

- [arXiv:2401.04088](https://arxiv.org/abs/2401.04088)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P21_moe/README.md)
