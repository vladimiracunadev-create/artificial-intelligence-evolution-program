
# Teoría — MCP: tools, resources y prompts

## Ubicación en el mapa de la IA

Esta clase pertenece a **Sistemas multiagente e interoperabilidad**. Diseña equipos de agentes con contratos, delegación, protocolos, persistencia y coordinación entre runtimes y proveedores.

## Modelo mental

`MCP: tools, resources y prompts` se estudia como un sistema con:

1. **representación:** qué información existe y cómo se codifica;
2. **operación:** qué transformación, inferencia o decisión se ejecuta;
3. **criterio:** cómo se determina si el resultado es mejor que un baseline;
4. **evidencia:** qué artefactos permiten revisar la conclusión;
5. **límites:** cuándo el método deja de ser apropiado.

Conceptos guía: **MCP, tools, resources, prompts**.

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

- [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro)
- [Agent2Agent Protocol](https://a2a-protocol.org/latest/)
- [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [LangGraph Subgraphs](https://docs.langchain.com/oss/python/langgraph/use-subgraphs)
