
# Evaluación — 164 Seguridad de tools, MCP y supply chain

## ❓ Preguntas

1. Mapea A1–A4 a la taxonomía OWASP Agentic 2026 y justifica cada control.
2. ¿Por qué una fuente confiable no convierte `publish` en una acción permitida?
3. ¿Qué diferencia tool poisoning, rug pull y abuso de identidad?
4. Diseña una política para lectura, escritura y borrado con ámbitos distintos.
5. Explica qué evidencia exigirías para aprobar una actualización de servidor MCP.

## 🏆 Reto verificable

Añade una acción permitida y confiable, una denegada sólo por permiso y otra denegada
sólo por confianza. Demuestra que los dos controles son independientes.

## ✅ Criterio de aceptación

- [ ] `lab.py` termina con código 0.
- [ ] El resultado contiene `kind`, `seed`, `evidence` y `limitations`.
- [ ] La política es deny-by-default.
- [ ] Cada decisión conserva riesgo, acción, confianza y razones.
- [ ] Se declara qué control requiere aislamiento real fuera de la miniatura.

---

> [⬅️ Volver a la clase](README.md) · [📚 Índice de la parte](../README.md)
