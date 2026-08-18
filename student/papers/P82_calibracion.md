# 🎒 Ficha de estudio — P82 · Predecir buenas probabilidades con aprendizaje supervisado

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *Predicting Good Probabilities with Supervised Learning* (2005)
**Nivel:** L3 · **Notebook:** [`P82_calibracion.ipynb`](../../notebooks/papers/P82_calibracion.ipynb)

## En una frase

Separa dos cosas que se confundían: ordenar bien los ejemplos y estimar bien la probabilidad de cada uno.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «Las salidas de un clasificador se usan como probabilidades para decidir con umbrales de coste o para combinarlas con otras. Pero un modelo puede tener un AUC excelente y probabilidades sistemáticamente sesgadas, y nadie lo estaba midiendo.»
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

- `calibración`
- `diagrama de fiabilidad`
- `Brier`
- `escalado de Platt`
- `regresión isotónica`

## Fuentes primarias

- [doi:10.1145/1102351.1102430](https://doi.org/10.1145/1102351.1102430)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P82_calibracion/README.md)
