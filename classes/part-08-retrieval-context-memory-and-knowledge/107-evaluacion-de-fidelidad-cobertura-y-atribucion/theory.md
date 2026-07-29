
# Teoría — Evaluación de fidelidad, cobertura y atribución

## Ubicación en el mapa de la IA

Esta clase pertenece a **Recuperación, contexto, memoria y conocimiento**. Construye sistemas que conectan modelos con conocimiento verificable mediante búsqueda, RAG, grafos, memoria y evaluación de atribución.

## Modelo mental

`Evaluación de fidelidad, cobertura y atribución` se estudia como un sistema con:

1. **representación:** qué información existe y cómo se codifica;
2. **operación:** qué transformación, inferencia o decisión se ejecuta;
3. **criterio:** cómo se determina si el resultado es mejor que un baseline;
4. **evidencia:** qué artefactos permiten revisar la conclusión;
5. **límites:** cuándo el método deja de ser apropiado.

Conceptos guía: **faithfulness, recall, attribution, citations**.

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

- [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401)
- [FAISS](https://faiss.ai/)
- [GraphRAG](https://microsoft.github.io/graphrag/)
