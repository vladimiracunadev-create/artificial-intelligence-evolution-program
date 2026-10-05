# Frontera

Temas cambiantes con fuente, madurez y fecha de revisión. No sustituyen el núcleo estable.

[`current-topics.yaml`](current-topics.yaml) conserva dos cosas distintas:

- `topics`: señales que merece la pena volver a evaluar, cada una con fuente,
  madurez, razón y fecha;
- `review`: periodo cubierto, cambios de estado y ruido descartado. Registrar lo
  descartado evita convertir cada lanzamiento de producto en una clase nueva.

`python scripts/check_frontier.py` verifica fechas, identificadores, fuentes y el
contrato de cada revisión. El método completo y los criterios para ascender un
trabajo están en [`prompts/VIGILANCIA_DE_FRONTERA.md`](../prompts/VIGILANCIA_DE_FRONTERA.md).
