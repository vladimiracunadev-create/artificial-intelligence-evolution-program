
# Teoría — Agentes racionales, entornos y medidas de desempeño

## 🗺️ Ubicación en el mapa de la IA

El marco de agentes racionales (AIMA, cap. 2) es el lenguaje unificador de la IA moderna:
permite describir con el mismo vocabulario un termostato, un buscador de rutas, un jugador
de ajedrez y un modelo de lenguaje con herramientas. Sustituye la pregunta filosófica
"¿piensa?" por la pregunta de ingeniería "¿maximiza su medida de desempeño en su entorno?".
Todo el resto del programa — búsqueda, aprendizaje, RL, agentes con LLM — son formas de
construir la función del agente.

## 📖 Fundamentos

### 🤖 Agente, percepción y función del agente

Un **agente** es cualquier entidad que percibe su entorno mediante **sensores** y actúa
sobre él mediante **actuadores**. Formalmente:

```text
secuencia de percepciones:  p₁, p₂, ..., pₜ
función del agente:         f: P* → A   (de historiales de percepción a acciones)
programa del agente:        implementación concreta y finita de f
```

La distinción función/programa importa: la función es la especificación matemática
(potencialmente una tabla infinita); el programa es el código que la aproxima con memoria
y cómputo finitos.

### 🎯 Racionalidad y medida de desempeño

Un **agente racional** elige, para cada secuencia de percepciones, la acción que **maximiza
el valor esperado de la medida de desempeño**, dado el conocimiento previo y las
percepciones hasta el momento. Cuatro precisiones críticas:

1. **Racional ≠ omnisciente:** la racionalidad maximiza el resultado *esperado* con la
   información disponible; no exige conocer el resultado real.
2. **Racional ≠ perfecto:** un agente racional puede obtener malos resultados por mala
   suerte; se juzga la decisión, no el desenlace.
3. La medida de desempeño debe evaluar **estados del entorno**, no estados del agente
   ("cuánta suciedad aspiró" es hackeable aspirando y tirando la misma suciedad; "qué tan
   limpio está el suelo por hora" no).
4. La racionalidad incluye **recopilar información** y **aprender**: ignorar percepciones
   disponibles es irracional.

### 📋 Especificación PEAS

Antes de diseñar un agente se especifica su entorno de tareas con **PEAS**:

- **P**erformance (medida de desempeño): qué se maximiza.
- **E**nvironment (entorno): dónde opera.
- **A**ctuators (actuadores): con qué actúa.
- **S**ensors (sensores): qué percibe.

### 🌍 Dimensiones del entorno

Las propiedades del entorno determinan qué arquitectura de agente es viable:

| Dimensión | Extremo fácil | Extremo difícil |
|---|---|---|
| Observabilidad | Totalmente observable | Parcialmente observable |
| N.º de agentes | Un agente | Multiagente (competitivo/cooperativo) |
| Determinismo | Determinista | Estocástico |
| Episodicidad | Episódico | Secuencial (las acciones afectan el futuro) |
| Dinámica | Estático | Dinámico (cambia mientras el agente delibera) |
| Estados/tiempo | Discreto | Continuo |
| Conocimiento | Conocido (reglas dadas) | Desconocido (hay que aprenderlas) |

El caso más difícil (parcialmente observable, multiagente, estocástico, secuencial,
dinámico, continuo, desconocido) es, por ejemplo, conducir en tráfico real.

### 🏗️ Taxonomía de programas de agente

1. **Reflejo simple:** reglas condición→acción sobre la percepción actual. Solo funciona
   con observabilidad total.
2. **Reflejo con estado (basado en modelo):** mantiene un estado interno actualizado con un
   modelo de transición del mundo; tolera observabilidad parcial.
3. **Basado en metas:** delibera — busca secuencias de acciones que alcanzan una meta
   explícita (conecta con búsqueda, parte 01).
4. **Basado en utilidad:** compara estados por *cuán deseables* son (función de utilidad),
   maneja metas en conflicto y riesgo mediante utilidad esperada.
5. **Que aprende:** cualquiera de los anteriores más un elemento de aprendizaje, un crítico
   y un generador de problemas (exploración). Es la arquitectura general del ML moderno.

## 🧮 Ejemplo trabajado

Especificación PEAS de un agente aspirador en el mundo de dos casillas (A, B) de AIMA:

- **P:** +1 por casilla limpia por paso de tiempo, durante 1000 pasos; −1 por movimiento.
- **E:** dos casillas; la suciedad puede reaparecer con probabilidad 0.1 por paso.
- **A:** `Izquierda`, `Derecha`, `Aspirar`, `NoOp`.
- **S:** posición actual y si la casilla actual está sucia — observabilidad **parcial**
  (no ve la otra casilla).

Traza de un agente reflejo con estado, empezando en A, ambas sucias:

| t | Percepción | Estado interno (creencia) | Acción | Razón |
|---|---|---|---|---|
| 1 | (A, sucia) | B: desconocido | Aspirar | limpiar rinde +1/paso futuro |
| 2 | (A, limpia) | B: desconocido | Derecha | recopilar información es racional |
| 3 | (B, sucia) | A: limpia (hace 1 paso) | Aspirar | idem t=1 |
| 4 | (B, limpia) | A: limpia con prob. 0.9 | NoOp | moverse cuesta −1 y no hay evidencia de suciedad |

Nótese la decisión en t=4: un reflejo simple sin estado oscilaría entre casillas pagando −1
por viaje; el estado interno permite quedarse quieto hasta que la probabilidad de suciedad
acumulada justifique el costo del viaje. La racionalidad depende de la medida P: si el
movimiento no costara nada, patrullar sería óptimo.

## 📊 Propiedades y comparación

| Arquitectura | Requiere modelo del mundo | Maneja obs. parcial | Maneja metas en conflicto | Costo computacional |
|---|---|---|---|---|
| Reflejo simple | No | No | No | Mínimo |
| Reflejo con estado | Sí (transición) | Sí | No | Bajo |
| Basado en metas | Sí | Sí | No (meta binaria) | Medio (búsqueda) |
| Basado en utilidad | Sí | Sí | Sí (utilidad esperada) | Alto |
| Que aprende | Lo aprende | Sí | Sí | Variable + entrenamiento |

```mermaid
flowchart TD
    subgraph Agente
        S1["Sensores"] --> E1["Estado interno<br/>(¿cómo es el mundo ahora?)"]
        E1 --> D{"Selección de acción"}
        M["Modelo de transición<br/>(¿qué causan mis acciones?)"] --> E1
        U["Medida de desempeño /<br/>utilidad"] --> D
        D --> A1["Actuadores"]
        C["Crítico + aprendizaje<br/>(ajusta modelo y política)"] -.-> M
        C -.-> D
    end
    W(("Entorno")) --> S1
    A1 --> W
    W --> C
```

## ⚠️ Errores conceptuales frecuentes

1. **"Racional significa que siempre gana."** La racionalidad se define sobre el valor
   *esperado* con la información disponible; un resultado malo no implica una decisión
   irracional (ni viceversa).
2. **"La medida de desempeño es un detalle."** Es la especificación completa del objetivo:
   medidas mal diseñadas producen agentes que optimizan literalmente lo que se midió
   (aspirar y volcar la suciedad para volver a aspirarla).
3. **"Más deliberación siempre es mejor."** En entornos dinámicos, deliberar tiene costo de
   oportunidad; un reflejo rápido puede ser más racional que un plan óptimo tardío.
4. **"Los agentes con LLM son otra cosa."** Encajan en el marco: percepciones (contexto,
   resultados de herramientas), acciones (llamadas a herramientas, texto), medida de
   desempeño (criterio de éxito de la tarea). El marco expone justamente lo que les falta:
   medidas de desempeño explícitas y verificables.
5. **"Entorno determinista = agente trivial."** El ajedrez es determinista y totalmente
   observable, y aun así intratable por fuerza bruta: el tamaño del espacio de estados es
   una dificultad independiente.

## 🚀 Del aprendizaje a la operación

Llevar un agente a operación exige: escribir la especificación PEAS como documento revisable
antes de codificar; validar la medida de desempeño contra el fenómeno de Goodhart (¿qué
comportamiento absurdo la maximizaría?); clasificar el entorno real en las siete dimensiones
para dimensionar sensores y frecuencia de decisión; y definir qué hace el agente cuando sus
percepciones salen del dominio previsto (fallback a humano, modo seguro). El laboratorio de
esta clase ejercita solo el primer eslabón: agente, entorno y medida en versión mínima.

## 🔗 Referencias

- [Russell, S. & Norvig, P. *Artificial Intelligence: A Modern Approach*, 4.ª ed., cap. 2](https://aima.cs.berkeley.edu/)
- [Turing, A. M. (1950). Computing Machinery and Intelligence (criterio conductual precursor)](https://doi.org/10.1093/mind/LIX.236.433)
- [Sutton, R. & Barto, A. *Reinforcement Learning: An Introduction*, 2.ª ed., cap. 1 (agente-entorno-recompensa)](http://incompleteideas.net/book/the-book-2nd.html)
- [Nilsson, N. (2010). *The Quest for Artificial Intelligence* (PDF oficial)](https://ai.stanford.edu/~nilsson/QAI/qai.pdf)

---

> [⬅️ Volver a la clase](README.md) · [📝 Evaluación](assessment.md) · [📚 Índice de la parte](../README.md)
