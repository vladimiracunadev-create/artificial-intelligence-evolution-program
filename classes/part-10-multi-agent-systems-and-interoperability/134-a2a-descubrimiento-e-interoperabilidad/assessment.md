
# Evaluación — 134 A2A, descubrimiento e interoperabilidad

## ❓ Preguntas

1. ¿Qué diferencia la versión del agente de `protocolVersions` en su Agent Card?
2. Negocia una versión común y explica el rol de `A2A-Version`.
3. Altera un campo de la card después de firmarla: ¿qué debe detectar el cliente?
4. ¿Por qué `input-required` no es un fallo y Artifact no es un Message?
5. Compara HTTP+JSON y gRPC sin cambiar la semántica de Task.

## 🏆 Reto verificable

Implementa negociación que acepte `1.0`, degrade explícitamente a `0.3` y rechace
pares sin versión común. Registra la decisión junto al artefacto.

## ✅ Criterio de aceptación

- [ ] `lab.py` termina con código 0.
- [ ] El resultado contiene `kind`, `seed`, `evidence` y `limitations`.
- [ ] Verifica la card antes de delegar.
- [ ] Conserva el ciclo de estados y separa Artifact de mensajes.
- [ ] Declara por qué HMAC no autentica organizaciones reales.

---

> [⬅️ Volver a la clase](README.md) · [📚 Índice de la parte](../README.md)
