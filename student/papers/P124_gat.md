# 🎒 Ficha de estudio — P124 · Redes de atención sobre grafos

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *Graph Attention Networks* (2018)
**Nivel:** L3 · **Notebook:** [`P124_gat.ipynb`](../../notebooks/papers/P124_gat.ipynb)

## En una frase

Sustituye el promedio uniforme sobre los vecinos por pesos aprendidos por pareja, sin necesitar conocer la estructura global del grafo.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «La convolución de grafo promedia a todos los vecinos por igual y normaliza por el grado. Eso supone que todos los vecinos importan lo mismo y exige conocer el grafo completo, lo que impide aplicar el modelo a nodos que no se vieron al entrenar.»
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

- `grafos`
- `atención`
- `agregación ponderada`
- `inductivo`
- `vecindario`

## Fuentes primarias

- [arXiv:1710.10903](https://arxiv.org/abs/1710.10903)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P124_gat/README.md)
