# 🎒 Ficha de estudio — P38 · Bayes variacional con autocodificación

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *Auto-Encoding Variational Bayes* (2013)
**Nivel:** L3 · **Notebook:** [`P38_vae.ipynb`](../../notebooks/papers/P38_vae.ipynb)

## En una frase

Hace entrenable un modelo generativo latente: el truco de reparametrización deja pasar el gradiente a través del muestreo.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «Un modelo generativo con variables latentes exige muestrear, y muestrear es un nodo estocástico que bloquea el gradiente: no se podía entrenar por retropropagación.»
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

- `VAE`
- `reparametrización`
- `ELBO`
- `espacio latente`
- `inferencia variacional`

## Fuentes primarias

- [arXiv:1312.6114](https://arxiv.org/abs/1312.6114)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P38_vae/README.md)
