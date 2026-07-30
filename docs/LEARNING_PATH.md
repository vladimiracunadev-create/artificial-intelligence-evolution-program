# 🧭 Ruta de aprendizaje

```mermaid
flowchart TD
    START(["🎓 Inicio"]) --> Q{"¿Cuál es tu objetivo?"}
    Q -->|"Dominar todo el mapa"| FULL["🛤️ Ruta completa<br/>Partes 00–14<br/>70–95 semanas"]
    Q -->|"Construir agentes"| AG["🤖 Ruta para agentes<br/>00 · 01 · 06 · 08 · 09<br/>10 · 12 · 13 · capstone"]
    Q -->|"Entrenar y servir modelos"| MOD["⚙️ Ruta de ingeniería de modelos<br/>00 · 03 · 04 · 05 · 06<br/>07 · 12 · 13"]
    Q -->|"Producto y gobernanza"| PROD["📦 Ruta de producto<br/>00 · 03 · 06 · 09<br/>12 · 13 + proyectos"]
    FULL --> CAP(["🏁 Capstone 180"])
    AG --> CAP
    MOD --> SPEC(["🔗 Especializaciones<br/>conectadas"])
    PROD --> CAP
    CAP --> SPEC
```

## 🛤️ Ruta completa

Sigue las partes 00 a 14. Dedica entre 70 y 95 semanas a ritmo de dos clases
por semana, incluyendo proyectos.

## 🤖 Ruta para agentes

1. Parte 00: clases 001, 004, 008 y 011.
2. Parte 01: búsqueda, reglas y planificación.
3. Parte 06: prompting, resultados estructurados y tool calling.
4. Parte 08: RAG, memoria y evaluación de atribución.
5. Parte 09 completa.
6. Parte 10 completa.
7. Parte 12: observabilidad, AgentOps, costos y resiliencia.
8. Parte 13: seguridad, evals y gobernanza.
9. Capstone 180.

## ⚙️ Ruta para ingeniería de modelos

Partes 00, 03, 04, 05, 06, 07, 12 y 13; después profundiza en los dos
repositorios especializados.

## 📦 Ruta para producto y gobernanza

Partes 00, 03, 06, 09, 12, 13 y los proyectos de cada parte.
