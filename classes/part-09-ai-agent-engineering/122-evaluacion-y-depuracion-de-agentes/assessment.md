
# Evaluación — 122 Evaluación y depuración de agentes

## ❓ Preguntas

1. ¿Por qué T2 es éxito de resultado y fracaso de proceso?
2. Calcula a mano `outcome_success_rate`, `honest_success_rate` y costo por éxito honesto.
3. Localiza la primera divergencia de cada fallo y justifica la taxonomía asignada.
4. Explica por qué `policy_bypass` debe cerrar el gate aunque aumente la tasa de resultado.
5. Añade una tarea donde el entorno falle sin que el agente sea responsable.

## 🏆 Reto verificable

Implementa una comparación baseline/candidato que rechace el candidato si mejora el
resultado global pero introduce una violación o una regresión por categoría.

## ✅ Criterio de aceptación

- [ ] `lab.py` termina con código 0.
- [ ] El resultado contiene `kind`, `seed`, `evidence` y `limitations`.
- [ ] Recalcula las métricas desde las tareas, no desde constantes copiadas.
- [ ] Reporta primera divergencia, causa, costo y violaciones.
- [ ] El gate tiene al menos una prueba positiva y una negativa.

---

> [⬅️ Volver a la clase](README.md) · [📚 Índice de la parte](../README.md)
