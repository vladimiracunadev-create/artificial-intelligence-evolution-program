
# Teoría — Registro y promoción champion-challenger

## Ubicación en el mapa de la IA

Esta clase pertenece a **Ingeniería de IA, MLOps, LLMOps y AgentOps**. Industrializa datos, modelos y agentes mediante CI/CD, registros, serving, observabilidad, control de costos, recuperación y operación segura.

## Modelo mental

`Registro y promoción champion-challenger` se estudia como un sistema con:

1. **representación:** qué información existe y cómo se codifica;
2. **operación:** qué transformación, inferencia o decisión se ejecuta;
3. **criterio:** cómo se determina si el resultado es mejor que un baseline;
4. **evidencia:** qué artefactos permiten revisar la conclusión;
5. **límites:** cuándo el método deja de ser apropiado.

Conceptos guía: **registry, version, champion, challenger**.

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

- [MLflow Documentation](https://mlflow.org/docs/latest/)
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/)
- [Designing Machine Learning Systems](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/)
