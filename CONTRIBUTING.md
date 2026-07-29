# Contribuir

## Antes de proponer una clase

1. Clasifica el tema como `stable`, `current`, `emerging` o `historical`.
2. Incluye una fuente primaria o documentación oficial.
3. Define resultado de aprendizaje y evidencia verificable.
4. Implementa laboratorio local o documenta por qué requiere un entorno externo.
5. Declara licencias, riesgos, costos y límites.

## Validación

```bash
python -m unittest discover -s tests -v
python scripts/validate_repository.py --strict
python -m compileall -q src scripts classes apps
```

## Commits

Usa Conventional Commits. No reescribas hechos históricos del changelog para
sincronizar el estado actual.
