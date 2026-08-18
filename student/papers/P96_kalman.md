# 🎒 Ficha de estudio — P96 · Un nuevo enfoque para los problemas de filtrado y predicción lineales

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *A New Approach to Linear Filtering and Prediction Problems* (1960)
**Nivel:** L3 · **Notebook:** [`P96_kalman.ipynb`](../../notebooks/papers/P96_kalman.ipynb)

## En una frase

Fusiona un modelo del movimiento con un sensor ruidoso ponderando cada fuente por su propia incertidumbre, y lo hace de forma recursiva.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «Un sensor da medidas ruidosas y un modelo del movimiento acumula error. Promediarlos trata igual a los dos, e ignora que la confianza en cada uno cambia con el tiempo. Los métodos anteriores exigían guardar todo el historial.»
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

- `filtro de Kalman`
- `fusión de sensores`
- `estimación de estado`
- `ganancia`
- `recursivo`

## Fuentes primarias

- [doi:10.1115/1.3662552](https://doi.org/10.1115/1.3662552)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P96_kalman/README.md)
