# 🤝 Contribuir

## 📋 Antes de proponer una clase

1. Clasifica el tema como `stable`, `current`, `emerging` o `historical`.
2. Incluye una fuente primaria o documentación oficial.
3. Define resultado de aprendizaje y evidencia verificable.
4. Implementa laboratorio local o documenta por qué requiere un entorno externo.
5. Declara licencias, riesgos, costos y límites.

## 📜 Antes de proponer un paper para el eje fundacional

1. Comprueba los criterios de ascenso de
   [`prompts/VIGILANCIA_DE_FRONTERA.md`](prompts/VIGILANCIA_DE_FRONTERA.md).
   Mientras no los cumpla, va a `frontier/`, no a `papers/foundational/`.
2. Registra la entrada en `papers/catalog/papers.json` con autoría, año, venue,
   URL y fecha de consulta.
3. Escribe la ficha con las 18 secciones de
   [`papers/guides/PLANTILLA_FICHA_PAPER.md`](papers/guides/PLANTILLA_FICHA_PAPER.md).
4. Añade el motor determinista y su especificación de notebook.
5. Ejecuta `python scripts/generate_papers.py` y **no edites a mano** lo generado.

Reglas que el CI verifica y que no son negociables: no atribuir al paper ideas
posteriores, no inventar autores, fechas, datasets ni métricas, y no
redistribuir material con copyright — se enlaza.

## ✅ Validación

```bash
python -m unittest discover -s tests -v
python scripts/validate_repository.py --strict
python scripts/generate_papers.py --check
python scripts/link_papers_to_classes.py --check
python -m compileall -q src scripts classes apps
```

Esa es exactamente la tanda del workflow `CI`. Para no tener que acordarse,
instala una sola vez el hook que la corre antes de cada `git push`:

```bash
make hooks
```

El fallo más habitual es olvidar regenerar tras editar contenido: el manifiesto
de hashes queda desfasado y caen los nueve jobs de la matriz. Se arregla con
`python scripts/generate_papers.py` y `python scripts/link_papers_to_classes.py`.

## 📝 Commits

Usa Conventional Commits. No reescribas hechos históricos del changelog para
sincronizar el estado actual.
