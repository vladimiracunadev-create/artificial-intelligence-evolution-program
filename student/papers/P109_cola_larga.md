# 🎒 Ficha de estudio — P109 · La cola a escala

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *The Tail at Scale* (2013)
**Nivel:** L2 · **Notebook:** [`P109_cola_larga.ipynb`](../../notebooks/papers/P109_cola_larga.ipynb)

## En una frase

Muestra que con abanico grande la latencia de cola de cada componente se convierte en la latencia típica del sistema completo.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «Un servicio con un p99 excelente puede producir un sistema lento si la petición del usuario necesita respuesta de cientos de servidores: basta que uno vaya lento para que toda la petición lo vaya, y con cien servidores eso pasa casi siempre.»
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

- `latencia de cola`
- `p99`
- `abanico`
- `peticiones de cobertura`
- `sistemas a escala`

## Fuentes primarias

- [doi:10.1145/2408776.2408794](https://doi.org/10.1145/2408776.2408794)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P109_cola_larga/README.md)
