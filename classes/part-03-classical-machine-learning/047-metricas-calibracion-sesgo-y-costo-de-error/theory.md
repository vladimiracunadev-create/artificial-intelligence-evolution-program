
# Teoría — Métricas, calibración, sesgo y costo de error

## 🗺️ Ubicación en el mapa de la IA

Esta clase pertenece a **Machine learning clásico**. Cubre el aprendizaje a partir de datos antes de las redes profundas, con énfasis en baselines, validación, interpretabilidad y costo de error.

## 🧠 Modelo mental

`Métricas, calibración, sesgo y costo de error` se estudia como un sistema con:

1. **representación:** qué información existe y cómo se codifica;
2. **operación:** qué transformación, inferencia o decisión se ejecuta;
3. **criterio:** cómo se determina si el resultado es mejor que un baseline;
4. **evidencia:** qué artefactos permiten revisar la conclusión;
5. **límites:** cuándo el método deja de ser apropiado.

Conceptos guía: **métricas, calibración, fairness, costo**.

```mermaid
flowchart LR
    R["🗂️ Representación<br/>qué información existe<br/>y cómo se codifica"] --> O["⚙️ Operación<br/>qué transformación o<br/>decisión se ejecuta"]
    O --> C["📏 Criterio<br/>cómo se compara<br/>contra un baseline"]
    C --> E["🔍 Evidencia<br/>artefactos que permiten<br/>revisar la conclusión"]
    E --> L["🚧 Límites<br/>cuándo el método<br/>deja de ser apropiado"]
```

## 🔧 Preguntas técnicas

- ¿Cuál es el estado o entrada mínima?
- ¿Qué decisiones son deterministas y cuáles dependen de datos o modelo?
- ¿Qué información podría filtrarse o perderse?
- ¿Qué baseline permite saber si el aumento de complejidad aporta valor?
- ¿Cómo se interrumpe, revierte o audita el proceso?

## 🚀 Del aprendizaje a la operación

El laboratorio demuestra un mecanismo reducido. Para elevarlo a una aplicación
real deben añadirse contratos de entrada y salida, validación de datos, manejo de
errores, permisos, trazas, evaluación de regresión y revisión humana proporcional
al riesgo.

## 🔗 Referencias primarias o técnicas

- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [An Introduction to Statistical Learning](https://www.statlearning.com/)
- [Python Data Science Program](https://github.com/vladimiracunadev-create/python-data-science-program)

---

> [⬅️ Volver a la clase](README.md) · [📝 Evaluación](assessment.md) · [📚 Índice de la parte](../README.md)
