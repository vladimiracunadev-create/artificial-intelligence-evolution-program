# 🎒 Ficha de estudio — P03 · Memoria larga de corto plazo

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *Long Short-Term Memory* (1997)
**Nivel:** L2 · **Notebook:** [`P03_lstm.ipynb`](../../notebooks/papers/P03_lstm.ipynb)

## En una frase

Primera arquitectura recurrente capaz de mantener información a través de cientos de pasos sin que el gradiente se desvanezca.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «En un RNN el gradiente se multiplica en cada paso temporal: se desvanece o explota, y la red no aprende dependencias largas.»
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

- `LSTM`
- `gradiente desvaneciente`
- `puertas`
- `estado de celda`
- `dependencias largas`

## Fuentes primarias

- [DOI (Neural Computation)](https://doi.org/10.1162/neco.1997.9.8.1735)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P03_lstm/README.md)
