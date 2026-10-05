# Evaluación — 171 Proyecto: respuesta a incidentes de IA

## ❓ Preguntas

1. Explica por qué «AI can execute» no implica «AI can own accountability».
2. Clasifica como GREEN, YELLOW o RED: crear un borrador interno, responder un precio
   desde catálogo, publicar un claim médico y firmar un contrato. Justifica el gate.
3. En el caso MEDVi, separa un **hecho regulatorio**, una **alegación periodística**,
   una **respuesta empresarial**, una **interpretación** y una **lección sobre IA**.
4. Un error de origen prepara cuatro campañas con 1.200 destinatarios potenciales.
   Calcula `error_amplification` y diferencia blast radius potencial de impacto real.
5. ¿Por qué `confidence >= 0.90` no sustituye grounding ni source verification?
6. Reconstruye el incidente desde `audit_trail`: primera divergencia, detección,
   escalada, contención, rollback, owner y regresión permanente.

## 🏆 Reto verificable

Amplía el escenario ficticio de SaludNova Labs con una clave `student_extension` que:

- detecte dominio sensible;
- aplique threshold sin tratarlo como evidencia;
- compruebe grounding y fuente;
- clasifique la acción GREEN/YELLOW/RED;
- escale RED a un humano antes de cualquier efecto externo;
- abra circuit breaker o kill switch cuando la política lo exija;
- ejecute rollback y añada eventos append-only al audit trail;
- calcule autonomy rate, human escalation rate, policy violation rate, unverified
  claim rate, error amplification, time to detect, time to contain y blast radius;
- identifique al owner humano u organizacional responsable.

La compañía y todos los productos deben seguir siendo completamente ficticios. No
añadas flujos clínicos, prescripción, pago, farmacia ni proveedores reales.

## ✅ Criterio de aceptación

- [ ] `lab.py` termina con código 0 y es determinista con la misma semilla.
- [ ] El resultado contiene `kind`, `seed`, `evidence` y `limitations`.
- [ ] El claim incorrecto queda bloqueado antes de alcanzar clientes.
- [ ] Cada métrica declara denominador, unidad o reloj.
- [ ] El audit trail permite reconstruir causa, decisión, contención y rollback.
- [ ] Confianza, grounding, fuente y aprobación aparecen como controles distintos.
- [ ] La IA no figura como owner ni como responsable final.
- [ ] La extensión no modifica el comportamiento de otras clases.
- [ ] Se declara al menos una limitación de la miniatura.

---

> [⬅️ Volver a la clase](README.md) · [📚 Índice de la parte](../README.md)
