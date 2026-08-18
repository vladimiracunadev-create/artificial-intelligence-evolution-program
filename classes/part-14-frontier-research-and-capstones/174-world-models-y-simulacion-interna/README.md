
# 174 — World models y simulación interna

> [← Clase anterior](../../../classes/part-14-frontier-research-and-capstones/173-causal-ai-y-descubrimiento-cientifico/README.md) · [Índice de la parte](../README.md) · [Clase siguiente →](../../../classes/part-14-frontier-research-and-capstones/175-razonamiento-y-computo-en-tiempo-de-inferencia/README.md)

**Parte:** 14 — Frontera, investigación y proyectos integradores  
**Nivel:** frontera · **Horas estimadas:** 6  
**Laboratorio:** `frontier` · **Estado:** `EXECUTABLE_CORE`

## 🎯 Propósito

Comprender **world models y simulación interna** dentro de la evolución de la inteligencia
artificial, implementar un experimento mínimo verificable y distinguir qué parte
constituye evidencia frente a una afirmación todavía no comprobada.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. Explicar world models y simulación interna usando los conceptos `world models`, `simulation`, `planning`, `latent`.
2. Ejecutar el laboratorio con una semilla explícita y revisar su contrato JSON.
3. Identificar al menos un supuesto, una limitación y un riesgo de aplicación.
4. Comparar el enfoque con la etapa anterior de la ruta de aprendizaje.
5. Producir una evidencia reproducible y una conclusión que no exceda los datos.

## 🧩 Conceptos centrales

`world models`, `simulation`, `planning`, `latent`

## 🗺️ Ubicación en el mapa de la IA

En la Parte 2 viste agentes que planifican sobre modelos dados (MDP conocidos) y
en RL model-free el agente aprende sin modelo, pagando en muestras. Los *world
models* cierran esa brecha: el agente **aprende un modelo del entorno y planifica
dentro de él** — "sueña" trayectorias en lugar de sufrirlas. Es frontera porque la
predicción en espacio latente (JEPA, Dreamer) es una de las apuestas principales
para agentes que entiendan consecuencias físicas antes de actuar, y conecta
directamente con la robótica de la Parte 11: un robot que simula internamente
choca menos en el mundo real.

## 📖 Fundamentos

### 🧱 La arquitectura V-M-C (Ha & Schmidhuber, 2018)

*World Models* (arXiv:1803.10122) descompone el agente en tres módulos:

```text
V (Vision):     un autoencoder variacional comprime cada frame o
                observación o_t en un código latente z_t (p. ej. 64 dims
                en vez de 64×64×3 píxeles).
M (Memory):     una RNN con salida de mezcla de gaussianas (MDN-RNN)
                aprende la dinámica en el latente:
                P(z_{t+1} | z_t, a_t, h_t)  — predicción estocástica.
C (Controller): una política diminuta (lineal en el paper) que decide
                a_t = C([z_t, h_t]). Al ser pequeña, puede optimizarse
                con métodos evolutivos (CMA-ES).
```

El resultado célebre: el controlador puede **entrenarse íntegramente dentro del
sueño** — trayectorias generadas por M sin tocar el entorno real— y la política
transferirse al entorno verdadero. Dos condiciones lo hacen posible: el modelo M
captura suficiente dinámica, y se controla la "temperatura" del sueño para que el
agente no explote errores del modelo (atajos que solo existen en la imaginación).

### 🔮 Por qué predecir en latente y no en píxeles

Predecir píxeles futuros obliga a modelar detalles irrelevantes (textura de la
hierba) y promedia futuros posibles en imágenes borrosas. La familia **JEPA**
(Joint-Embedding Predictive Architecture, LeCun 2022; I-JEPA, arXiv:2301.08243)
lleva el principio al extremo: predecir la **representación** de la parte
faltante/futura, no su apariencia. La pérdida vive en el espacio de embeddings;
lo impredecible o irrelevante puede simplemente no representarse. Dreamer
(Hafner et al.) aplica lo mismo a RL: aprende un modelo recurrente de estados
latentes (RSSM) y entrena actor y crítico con **imaginación**: rollouts latentes
de ~15 pasos. DreamerV3 (arXiv:2301.04104) resuelve más de 150 tareas con
hiperparámetros fijos, incluida la obtención de diamantes en Minecraft desde cero.

### ⚙️ Planificar con el modelo: el ciclo general

```text
1. Recolectar experiencia real (o_t, a_t, r_t, o_{t+1}).
2. Ajustar el world model: encoder φ: o→z y dinámica
   T: (z_t, a_t) → distribución sobre z_{t+1} (+ recompensa r̂).
3. Imaginar: desde el z actual, desplegar K trayectorias con
   acciones candidatas, SIN tocar el entorno.
4. Elegir el plan con mejor retorno imaginado (o entrenar la
   política sobre esas trayectorias).
5. Ejecutar 1 acción real, observar, y volver a 1 (el error del
   modelo se corrige con re-planificación frecuente).
```

Este es el mismo patrón Dyna de Sutton & Barto (cap. 8), con la diferencia de que
el modelo ya no es una tabla sino una red que comprime observaciones de alta
dimensión.

### ⚠️ El talón de Aquiles: explotación del modelo

Un planificador que optimiza dentro del modelo encuentra sus errores: si M
predice mal una zona, el plan "óptimo" puede vivir exactamente ahí (model
exploitation). Mitigaciones: horizonte corto, penalizar incertidumbre del modelo
(ensembles), re-planificar a menudo, y mezclar experiencia real con imaginada.

## 🧮 Ejemplo trabajado

World model tabular mínimo: un robot en 3 estados latentes {A, B, C}; C da
recompensa 1 al entrar, el resto 0. Dinámica aprendida de la experiencia
(estocástica):

```text
T(z'|z, avanzar):  A→B 0.9, A→A 0.1;  B→C 0.8, B→B 0.2;  C→C 1.0
T(z'|z, saltar):   A→C 0.4, A→A 0.6;  B→C 0.5, B→B 0.5;  C→C 1.0
```

Desde A, horizonte 2, comparar dos planes **por imaginación** (sin entorno real):

**Plan 1: [avanzar, avanzar]** — llegar a C en t≤2:
paso 1: P(B)=0.9, P(A)=0.1. Paso 2: desde B, P(C)=0.8 → 0.9·0.8 = 0.72;
desde A, P(C con avanzar)=0 → 0. Retorno esperado = **0.72**.

**Plan 2: [saltar, saltar]** — P(C en t=1) = 0.4 (recompensa ya asegurada);
si no (0.6 en A), P(C en t=2) = 0.4 → 0.6·0.4 = 0.24.
Retorno esperado = 0.4 + 0.24 = **0.64**.

El agente elige el plan 1 sin ejecutar nada. Ahora el límite: si la probabilidad
real de B→C fuera 0.5 (el modelo la sobreestima en 0.8), el retorno real del
plan 1 sería 0.9·0.5 = 0.45 < 0.64: el plan "óptimo imaginado" es peor en el
mundo. Eso es explotación del modelo, y por eso se re-planifica tras cada paso.

## 📊 Propiedades y comparación

| Enfoque | Muestras reales | Cómputo | Riesgo específico | Ejemplo |
|---|---|---|---|---|
| Model-free (DQN, PPO) | Muchas | Medio | Ineficiencia muestral | Atari clásico |
| World model + imaginación | Pocas | Alto (entrenar modelo) | Explotación del modelo | Dreamer, V-M-C |
| Planificación con modelo dado | Ninguna (modelo exacto) | Depende del horizonte | El modelo casi nunca es exacto | MDP de la Parte 2 |
| Predicción en píxeles | — | Muy alto | Futuros borrosos, detalle irrelevante | video prediction |
| Predicción en latente (JEPA) | — | Medio | Colapso de representaciones | I-JEPA, V-JEPA |

```mermaid
flowchart LR
    O[Observación o_t] --> V[Encoder V<br/>o_t → z_t]
    V --> M[Dinámica M<br/>"P(z_t+1 | z_t, a_t)"]
    M --> IM[Imaginación:<br/>rollouts latentes K pasos]
    IM --> C[Controlador C<br/>elige a_t]
    C -->|acción real| ENV[Entorno]
    ENV -->|o_t+1, r_t| O
    ENV -.->|experiencia| TRAIN[Reentrenar V y M]
    TRAIN -.-> V
```

## ⚠️ Errores conceptuales frecuentes

1. **"El world model debe predecir el futuro con exactitud"**. Basta con que
   ordene bien los planes candidatos; JEPA renuncia explícitamente a predecir
   apariencia y predice representaciones.
2. **"Entrenar en el sueño siempre transfiere"**. Solo si se controla la
   explotación del modelo (temperatura en Ha & Schmidhuber, ensembles,
   horizontes cortos); un plan óptimo en un modelo erróneo puede ser pésimo.
3. **"Un generador de video es ya un world model"**. Generar video plausible no
   implica dinámica consistente con acciones ni física estable a largo plazo;
   la evidencia debe evaluarse con intervenciones (¿responde bien a acciones?),
   no con calidad visual.
4. **"Latente = caja negra inútil"**. El latente es inspeccionable: se puede
   decodificar, medir qué factores captura y detectar cuándo la incertidumbre
   del modelo crece (señal para no confiar en el plan).
5. **"Model-based siempre gana a model-free"**. Con simuladores baratos y
   muestras infinitas, model-free sigue siendo competitivo y más simple; la
   ventaja del modelo aparece cuando las muestras reales son caras o peligrosas.

## 🚀 Del aprendizaje a la operación

Del ejemplo tabular a un sistema real faltan: aprender el encoder y la dinámica
desde observaciones crudas (VAE/RSSM con sus inestabilidades de entrenamiento);
cuantificar la incertidumbre del modelo para penalizar planes que la exploten;
presupuestar el cómputo de imaginación (K rollouts × horizonte × frecuencia de
re-planificación) contra la latencia de control real; y validar la transferencia
sueño→realidad con métricas de intervención, no solo con retorno imaginado.

## 🧪 Laboratorio

```bash
python lab.py
```

El laboratorio llama a `ai_evolution.labs.run_lab("frontier")`. Esta
decisión evita 183 implementaciones divergentes: cada clase tiene un entrypoint
propio, pero los motores didácticos se prueban como una biblioteca común.

### 🔍 Evidencia esperada

- tipo de laboratorio y semilla;
- entradas o decisiones observables;
- resultado estructurado;
- lista `evidence` con hechos que pueden inspeccionarse;
- lista `limitations` que impide presentar la demo como producción.

## 📓 Notebooks

- [📓 `notebook.ipynb`](notebook.ipynb): recorrido guiado con la materia resumida.
- [✍️ `notebook_student.ipynb`](notebook_student.ipynb): ejercicios para resolver.
- [✅ `notebook_solution.ipynb`](notebook_solution.ipynb): solución de referencia explicada.

## 📝 Evaluación

| Criterio | Peso |
|---|---:|
| Comprensión conceptual | 25 % |
| Ejecución reproducible | 25 % |
| Interpretación basada en evidencia | 25 % |
| Riesgos, límites y mejora propuesta | 25 % |

Consulta [assessment.md](assessment.md) para preguntas y criterio de aceptación.

## ⚠️ Errores comunes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El código corre, pero no hay conclusión | Se confundió ejecución con aprendizaje | Explica qué demuestra y qué no demuestra |
| El resultado cambia sin explicación | No se registró semilla o configuración | Conserva semilla, versión y parámetros |
| Se promete uso real | Se extrapoló desde una demo educativa | Declara entorno, datos, límites y revisión humana |
| Se copia una métrica aislada | No existe baseline ni costo de error | Añade comparación y criterio de decisión |

## ❓ Preguntas frecuentes

**¿Debo usar una API comercial?**  
No. El núcleo funciona localmente. Las extensiones LIVE se documentan por separado.

**¿El laboratorio representa una implementación industrial?**  
No por sí solo. Enseña el contrato y el patrón; producción exige integración,
seguridad, observabilidad, pruebas y operación.

**¿Dónde profundizo?**  
Revisa las especializaciones enlazadas en el README raíz y la ruta siguiente.

## 🔗 Referencias

- Ha, D. & Schmidhuber, J. (2018). *World Models*. [arXiv:1803.10122](https://arxiv.org/abs/1803.10122)
- Hafner, D. et al. (2023). *Mastering Diverse Domains through World Models* (DreamerV3). [arXiv:2301.04104](https://arxiv.org/abs/2301.04104)
- LeCun, Y. (2022). *A Path Towards Autonomous Machine Intelligence*. [OpenReview](https://openreview.net/forum?id=BZ5a1r-kVsf)
- Assran, M. et al. (2023). *Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture* (I-JEPA). CVPR 2023. [arXiv:2301.08243](https://arxiv.org/abs/2301.08243)
- Sutton, R. & Barto, A. (2018). *Reinforcement Learning: An Introduction* (2.ª ed.), cap. 8 (Dyna, planning and learning). [PDF oficial](http://incompleteideas.net/book/the-book-2nd.html)

<!-- papers:inicio -->

---

## 📜 Papers que fundamentan esta clase

> Bloque generado por `python scripts/link_papers_to_classes.py`. La fuente es [`papers/catalog/papers.json`](../../../papers/catalog/papers.json).

| Paper | Año | Qué desbloqueó | Miniatura |
|---|---:|---|---|
| [P147 · Los modelos recurrentes del mundo facilitan la evolución de políticas](../../../papers/foundational/P147_world_models/README.md) | 2018 | Entrena la política **dentro** de un modelo del entorno aprendido, y demuestra que la política resultante funciona en el entorno real. | [notebook](../../../notebooks/papers/P147_world_models.ipynb) |

Cada ficha explica el problema anterior, la matemática mínima, los límites y los errores de atribución más frecuentes. Para leerlas con método: [cómo leer un paper de IA](../../../papers/guides/COMO_LEER_UN_PAPER_DE_IA.md) · [anexos matemáticos](../../../papers/annexes/README.md).
<!-- papers:fin -->
---

## ⬅️ Clase anterior

[173 — Causal AI y descubrimiento científico](../../part-14-frontier-research-and-capstones/173-causal-ai-y-descubrimiento-cientifico/README.md)

## ➡️ Siguiente clase

[175 — Razonamiento y cómputo en tiempo de inferencia](../../part-14-frontier-research-and-capstones/175-razonamiento-y-computo-en-tiempo-de-inferencia/README.md)
