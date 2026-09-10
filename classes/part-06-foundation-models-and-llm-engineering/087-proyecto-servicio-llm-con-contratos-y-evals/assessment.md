
# Evaluación — 087 Proyecto: servicio LLM con contratos y evals

## ❓ Preguntas

1. Separa contrato HTTP, contrato estructurado del modelo y reglas de negocio.
2. ¿Qué evita la clave de idempotencia cuando una solicitud durable se reintenta?
3. Fuerza una salida sin `citations`: ¿por qué debe cerrar el gate aun si el texto parece bueno?
4. Define qué estados son terminales y cómo se recupera un trabajo interrumpido.
5. Propón métricas de costo, latencia y calidad que permitan comparar dos proveedores.

## 🏆 Reto verificable

Añade un caso fallido al lifecycle, una respuesta degradada honesta y una prueba que
demuestre que repetir el mismo `request_id` no duplica el trabajo.

## ✅ Criterio de aceptación

- [ ] `lab.py` termina con código 0.
- [ ] El resultado contiene `kind`, `seed`, `evidence` y `limitations`.
- [ ] Valida schema y evidencia antes de promover.
- [ ] El lifecycle distingue fallo, cancelación y finalización.
- [ ] La solución permanece independiente de un proveedor concreto.

---

> [⬅️ Volver a la clase](README.md) · [📚 Índice de la parte](../README.md)
