
# Teoría — Agentes de navegador

## 🗺️ Ubicación en el mapa de la IA

Esta clase pertenece a **IA encarnada, robótica y uso de computadores**. Lleva la toma de decisiones al mundo físico y a interfaces digitales, con sensores, control, simulación, navegación y acciones verificables.

## 🧠 Modelo mental

`Agentes de navegador` se estudia como un sistema con:

1. **representación:** qué información existe y cómo se codifica;
2. **operación:** qué transformación, inferencia o decisión se ejecuta;
3. **criterio:** cómo se determina si el resultado es mejor que un baseline;
4. **evidencia:** qué artefactos permiten revisar la conclusión;
5. **límites:** cuándo el método deja de ser apropiado.

Conceptos guía: **browser, DOM, navigation, forms**.

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

- [ROS 2 Documentation](https://docs.ros.org/en/rolling/)
- [Gymnasium Documentation](https://gymnasium.farama.org/)
- [Sutton and Barto — Reinforcement Learning](http://incompleteideas.net/book/the-book-2nd.html)

---

> [⬅️ Volver a la clase](README.md) · [📝 Evaluación](assessment.md) · [📚 Índice de la parte](../README.md)
