
# Teoría — Teorema de Bayes y actualización de creencias

## Ubicación en el mapa de la IA

Esta clase pertenece a **IA probabilística, evolutiva y de decisión**. Introduce decisiones bajo incertidumbre, modelos temporales, simulación, lógica difusa y métodos de búsqueda inspirados en la naturaleza.

## Modelo mental

`Teorema de Bayes y actualización de creencias` se estudia como un sistema con:

1. **representación:** qué información existe y cómo se codifica;
2. **operación:** qué transformación, inferencia o decisión se ejecuta;
3. **criterio:** cómo se determina si el resultado es mejor que un baseline;
4. **evidencia:** qué artefactos permiten revisar la conclusión;
5. **límites:** cuándo el método deja de ser apropiado.

Conceptos guía: **Bayes, prior, likelihood, posterior**.

## Preguntas técnicas

- ¿Cuál es el estado o entrada mínima?
- ¿Qué decisiones son deterministas y cuáles dependen de datos o modelo?
- ¿Qué información podría filtrarse o perderse?
- ¿Qué baseline permite saber si el aumento de complejidad aporta valor?
- ¿Cómo se interrumpe, revierte o audita el proceso?

## Del aprendizaje a la operación

El laboratorio demuestra un mecanismo reducido. Para elevarlo a una aplicación
real deben añadirse contratos de entrada y salida, validación de datos, manejo de
errores, permisos, trazas, evaluación de regresión y revisión humana proporcional
al riesgo.

## Referencias primarias o técnicas

- [Causality — Judea Pearl](https://bayes.cs.ucla.edu/BOOK-2K/)
- [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html)
- [Probabilistic Machine Learning — Kevin Murphy](https://probml.github.io/pml-book/)
