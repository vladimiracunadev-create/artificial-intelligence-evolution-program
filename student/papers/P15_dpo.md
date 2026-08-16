# 🎒 Ficha de estudio — P15 · Optimización directa de preferencias: tu modelo de lenguaje ya es un modelo de recompensa

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *Direct Preference Optimization: Your Language Model is Secretly a Reward Model* (2023)
**Nivel:** L4 · **Notebook:** [`P15_dpo.ipynb`](../../notebooks/papers/P15_dpo.ipynb)

## En una frase

Alinear un modelo con preferencias humanas sin modelo de recompensa explícito ni bucle de aprendizaje por refuerzo.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «El pipeline RLHF es frágil y caro: entrena un modelo extra, requiere muestreo on-policy y ajustar PPO es delicado.»
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

- `DPO`
- `preferencias`
- `recompensa implícita`
- `KL`
- `alineación`
- `pérdida de clasificación`

## Fuentes primarias

- [arXiv:2305.18290](https://arxiv.org/abs/2305.18290)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P15_dpo/README.md)
