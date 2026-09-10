
# Evaluación — 132 MCP: tools, resources y prompts

## ❓ Preguntas

1. Contrasta el handshake de 2025 con una petición stateless de 2026-07-28.
2. ¿Qué información debe viajar en `_meta` y qué autorizan `Mcp-Method`/`Mcp-Name`?
3. Valida el `inputSchema` de `buscar_clase` antes de ejecutar `tools/call`.
4. Explica cuándo `server/discover` aporta valor y por qué no es obligatorio.
5. Diseña una prueba negativa para una tool desconocida y otra para versión incompatible.

## 🏆 Reto verificable

Añade una segunda tool de sólo lectura, ordena el catálogo de manera determinista y
demuestra que dos respuestas `tools/list` equivalentes producen la misma clave de caché.

## ✅ Criterio de aceptación

- [ ] `lab.py` termina con código 0.
- [ ] El resultado contiene `kind`, `seed`, `evidence` y `limitations`.
- [ ] No introduce `initialize`, sesiones implícitas ni estado global.
- [ ] Rechaza argumentos que no satisfacen el schema.
- [ ] Distingue núcleo, extensión y política del host.

---

> [⬅️ Volver a la clase](README.md) · [📚 Índice de la parte](../README.md)
