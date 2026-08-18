# 🎒 Ficha de estudio — P65 · Un programa de máquina para demostración de teoremas

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *A Machine Program for Theorem-Proving* (1962)
**Nivel:** L2 · **Notebook:** [`P65_dpll.ipynb`](../../notebooks/papers/P65_dpll.ipynb)

## En una frase

El algoritmo que sigue siendo el esqueleto de todo solucionador SAT moderno: propagar primero, ramificar solo cuando no queda deducción por hacer.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «El procedimiento de Davis y Putnam (1960) era correcto pero consumía memoria de forma impracticable al eliminar variables por resolución.»
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

- `SAT`
- `propagación unitaria`
- `literal puro`
- `retroceso`
- `forma normal conjuntiva`

## Fuentes primarias

- [doi:10.1145/368273.368557](https://doi.org/10.1145/368273.368557)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P65_dpll/README.md)
