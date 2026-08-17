# 🎒 Ficha de estudio — P43 · Normalización por lotes: acelerar el entrenamiento profundo

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift* (2015)
**Nivel:** L2 · **Notebook:** [`P43_batchnorm.ipynb`](../../notebooks/papers/P43_batchnorm.ipynb)

## En una frase

Normalizar las activaciones dentro de la red permite tasas de aprendizaje mucho mayores y hace el entrenamiento profundo mucho menos frágil.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «Entrenar redes profundas exigía inicializaciones cuidadosas y tasas de aprendizaje pequeñas: la distribución de las activaciones de cada capa se desplazaba durante el entrenamiento.»
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

- `normalización por lotes`
- `activaciones`
- `tasa de aprendizaje`
- `γ y β`
- `estabilidad`

## Fuentes primarias

- [arXiv:1502.03167](https://arxiv.org/abs/1502.03167)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P43_batchnorm/README.md)
