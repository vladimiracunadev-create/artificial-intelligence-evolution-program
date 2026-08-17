# 🎒 Ficha de estudio — P40 · Dropout: una forma simple de evitar el sobreajuste en redes neuronales

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *Dropout: A Simple Way to Prevent Neural Networks from Overfitting* (2014)
**Nivel:** L2 · **Notebook:** [`P40_dropout.ipynb`](../../notebooks/papers/P40_dropout.ipynb)

## En una frase

Apagar unidades al azar durante el entrenamiento equivale a entrenar un ensamblado exponencial de subredes que comparten pesos.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «Las redes grandes memorizaban el conjunto de entrenamiento, y las unidades desarrollaban co-adaptaciones frágiles: una función solo servía si su 'socia' estaba presente.»
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

- `dropout`
- `regularización`
- `co-adaptación`
- `ensamblado`
- `sobreajuste`

## Fuentes primarias

- [JMLR 15(56)](https://jmlr.org/papers/v15/srivastava14a.html)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P40_dropout/README.md)
