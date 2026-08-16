# ✅ Prompt — verificación de un claim sobre IA

> Para cuando alguien te dice «el modelo X supera a Y en Z» y tienes que decidir si repetirlo.
> Sustituye `{{CLAIM}}` y `{{FUENTE}}`.

---

## Prompt

```text
Claim a verificar: "{{CLAIM}}"
Fuente donde lo vi: {{FUENTE}}

Actúa como auditor técnico. NO evalúes si el claim suena razonable:
evalúa si está SOSTENIDO.

Paso 1 — Descomponer.
Reescribe el claim separando: qué se afirma · sobre qué sistema ·
en qué tarea · con qué métrica · comparado con qué · en qué condiciones.
Marca como [AUSENTE] cada elemento que el claim no especifique.

Paso 2 — Rastrear.
¿De dónde procede el número? Distingue:
  [FUENTE PRIMARIA]  el paper o informe técnico original
  [FUENTE SECUNDARIA] blog, hilo, nota de prensa, resumen
  [SIN RASTREAR]     no se puede llegar al origen
Si es secundaria, indica qué habría que abrir para llegar a la primaria.

Paso 3 — Auditar el protocolo.
Comprueba y reporta: línea base y su esfuerzo de ajuste · número de ejecuciones y
varianza · posible contaminación del benchmark · cómputo comparable ·
si la métrica mide lo que el claim afirma · si hay conflicto de interés
(quién publica el resultado sobre su propio producto).

Paso 4 — Veredicto.
Elige uno y justifícalo en dos líneas:
  SOSTENIDO           evidencia primaria suficiente y protocolo limpio
  SOSTENIDO CON MATIZ evidencia válida, alcance más estrecho que el claim
  INSUFICIENTE        faltan datos para decidir; di exactamente cuáles
  NO SOSTENIDO        la evidencia no respalda lo afirmado

Paso 5 — Reescritura.
Escribe la versión del claim que SÍ sostiene la evidencia.

REGLAS:
- No inventes cifras ni referencias.
- Si no puedes acceder a la fuente primaria, di "INSUFICIENTE: sin acceso"
  en lugar de estimar.
- Distingue "no encontré evidencia" de "no hay evidencia".
```

---

## Señales de alarma que este prompt busca

| Señal | Por qué importa |
|---|---|
| Métrica sin línea base | «92 % de exactitud» no significa nada solo |
| Una sola ejecución | La diferencia puede ser ruido de semilla |
| Benchmark posiblemente contaminado | Mide memorización, no capacidad |
| Cómputo no comparable | Más recursos ≠ mejor método |
| SOTA sin fecha | «Estado del arte» caduca en meses |
| El evaluador es el fabricante | No lo invalida; obliga a exigir replicación independiente |
| Salto de métrica a capacidad | «Gana en el benchmark» → «razona»: no se sigue |

---

Relacionado: [cómo leer un paper](../papers/guides/COMO_LEER_UN_PAPER_DE_IA.md) ·
[clase 010 del programa](../classes/part-00-foundations-history-and-scientific-method/010-como-leer-papers-benchmarks-y-claims-de-ia/README.md)

[⬅️ Prompts](README.md)
