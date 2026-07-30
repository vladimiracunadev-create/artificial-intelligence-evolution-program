# 🛡️ Threat model

## 💎 Activos

Credenciales, datos de usuario, herramientas con efectos laterales, memoria,
historial de acciones, artefactos y decisiones.

## ⚠️ Amenazas

- prompt injection desde contenido recuperado;
- tool calls con exceso de permisos;
- exfiltración de secretos;
- acciones irreversibles sin aprobación;
- dependencia o modelo comprometido;
- memoria envenenada;
- datos personales en trazas;
- handoff sin filtrar contexto;
- benchmark contaminado o manipulado.

## 🔒 Controles mínimos

Allowlist, sandbox, separación lectura/escritura, validación de schemas,
aprobaciones, límites de pasos/costo, trazas redactadas, idempotencia,
rollback, evaluación adversarial y respuesta a incidentes.
