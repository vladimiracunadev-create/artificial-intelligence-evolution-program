# 🎒 Ficha de estudio — P09 · BERT: preentrenamiento de Transformers bidireccionales profundos para comprensión del lenguaje

> Generado por `python scripts/generate_papers.py`. Tu bitácora personal va en [`BITACORA.md`](BITACORA.md).

**Paper:** *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding* (2018)
**Nivel:** L3 · **Notebook:** [`P09_bert.ipynb`](../../notebooks/papers/P09_bert.ipynb)

## En una frase

Consolida el patrón preentrenar-y-ajustar: un mismo modelo base sirve para muchas tareas con un ajuste pequeño.

## Ruta de trabajo (en este orden)

1. Lee la **pasada 1** de la ficha: título, resumen, figuras. 10 minutos, sin fórmulas.
2. Responde por escrito: *¿qué problema resolvía?* Compáralo con: «Los modelos de lenguaje eran unidireccionales; para comprender una palabra hace falta el contexto de ambos lados, y entrenar bidireccionalmente con predicción del siguiente token es trivialmente degenerado.»
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

- `BERT`
- `MLM`
- `bidireccional`
- `preentrenamiento`
- `fine-tuning`
- `GLUE`

## Fuentes primarias

- [arXiv:1810.04805](https://arxiv.org/abs/1810.04805)
- [ACL Anthology (NAACL 2019)](https://aclanthology.org/N19-1423/)

---

[⬅️ Fichas de estudio](README.md) · [Ficha completa del paper](../../papers/foundational/P09_bert/README.md)
