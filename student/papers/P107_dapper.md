# 🎒 Ficha de estudio — P107 · Dapper, una infraestructura de trazado de sistemas distribuidos a gran escala

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *Dapper, a Large-Scale Distributed Systems Tracing Infrastructure* (2010)
**Nivel:** L2 · **Notebook:** [`P107_dapper.ipynb`](../../notebooks/papers/P107_dapper.ipynb)

## En una frase

Hace observable una petición que atraviesa decenas de servicios, con un identificador que viaja con ella y un muestreo que la hace asequible.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «En una arquitectura distribuida, cada servicio tiene sus métricas y sus registros. Cuando una petición va lenta, nadie puede reconstruir por dónde pasó ni dónde se gastó el tiempo: se ve el total y nada más.»
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

- `trazado distribuido`
- `span`
- `observabilidad`
- `muestreo`
- `latencia`

## Fuentes primarias

- [Informe técnico de Google](https://research.google/pubs/pub36356/)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P107_dapper/README.md)
