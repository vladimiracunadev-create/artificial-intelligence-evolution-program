# 🎒 Ficha de estudio — P102 · Algoritmos de optimización proximal de políticas

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *Proximal Policy Optimization Algorithms* (2017)
**Nivel:** L3 · **Notebook:** [`P102_ppo.ipynb`](../../notebooks/papers/P102_ppo.ipynb)

## En una frase

Consigue la estabilidad de TRPO con una función objetivo que se implementa en unas líneas y se optimiza con descenso de gradiente corriente.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «En gradiente de políticas, un paso demasiado grande destruye la política: se vuelve casi determinista, deja de explorar y no puede recuperarse. TRPO lo resolvía con una restricción de divergencia KL, a costa de una optimización de segundo orden compleja.»
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

- `gradiente de políticas`
- `recorte`
- `región de confianza`
- `aprendizaje por refuerzo`
- `estabilidad`

## Fuentes primarias

- [arXiv:1707.06347](https://arxiv.org/abs/1707.06347)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P102_ppo/README.md)
