# 🎒 Ficha de estudio — P140 · MapReduce: procesamiento simplificado de datos en clústeres grandes

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *MapReduce: simplified data processing on large clusters* (2004)
**Nivel:** L1 · **Notebook:** [`P140_mapreduce.ipynb`](../../notebooks/papers/P140_mapreduce.ipynb)

## En una frase

Reduce el procesamiento distribuido a dos funciones puras y esconde el reparto, la tolerancia a fallos y la recogida de resultados detrás de ellas.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «Procesar terabytes en miles de máquinas exigía escribir a mano el particionado, la comunicación, la recuperación de fallos y la agregación. Cada trabajo reimplementaba lo mismo, y la lógica del problema quedaba enterrada bajo la fontanería.»
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

- `fan-out`
- `particionado`
- `sesgo de datos`
- `combinador`
- `procesamiento por lotes`

## Fuentes primarias

- [doi:10.1145/1327452.1327492](https://doi.org/10.1145/1327452.1327492)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P140_mapreduce/README.md)
