# 🎒 Ficha de estudio — P99 · Localización y mapeo simultáneos: parte I

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *Simultaneous Localization and Mapping: Part I* (2006)
**Nivel:** L3 · **Notebook:** [`P99_slam.ipynb`](../../notebooks/papers/P99_slam.ipynb)

## En una frase

Formaliza el problema circular de la robótica móvil: no se puede localizar sin mapa ni mapear sin localización, y hay que resolver ambos a la vez.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «Un robot que se mueve acumula error de odometría sin límite. Corregirlo exige referencias externas; pero si el mapa no existe de antemano, hay que construirlo con la misma pose incierta que se quiere corregir.»
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

- `SLAM`
- `covarianza cruzada`
- `cierre de bucle`
- `asociación de datos`
- `odometría`

## Fuentes primarias

- [doi:10.1109/MRA.2006.1638022](https://doi.org/10.1109/MRA.2006.1638022)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P99_slam/README.md)
