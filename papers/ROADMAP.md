# 🗺️ Ruta del eje de papers

> Cómo recorrer los 148 hitos: qué nivel exige cada uno, en qué orden, con qué dedicación y
> qué evidencia deja cada tramo.

## 🎓 Los seis niveles

> El eje tiene **dos rutas**: la mínima (P01–P16), que se estudia en orden porque es una
> cadena de dependencias, y la ampliada (P17–P22), ordenada por año, que aporta la cobertura
> que la cadena no da y continúa la historia hasta 2025. Ver [README del eje](README.md).

| Nivel | Nombre | Qué se hace | Evidencia que produce |
|:---:|---|---|---|
| **L0** | Orientación | Entender qué es un paper, cómo se publica y cómo se cita | Una cita completa y bien formada |
| **L1** | Fundamentos | Leer la idea y su contexto histórico, sin ejecutar nada | Ficha de lectura de pasada 1–2 |
| **L2** | Implementación | Escribir o ejecutar la miniatura del mecanismo | Notebook ejecutado con predicción previa |
| **L3** | Análisis | Comparar variantes, medir e interpretar | Experimento controlado con tres semillas |
| **L4** | Reproducción parcial | Replicar una figura, tabla o ablación a escala reducida | Figura reproducida + límites declarados |
| **L5** | Investigación | Leer la frontera con fecha y fuente, proponer preguntas abiertas | Nota de linaje fechada |

L0 no está asignado a ningún paper: es la puerta de entrada. Se cubre con las tres guías
([cómo leer](guides/COMO_LEER_UN_PAPER_DE_IA.md),
[5 pasadas](guides/METODO_DE_LECTURA_EN_5_PASADAS.md),
[fuentes](guides/FUENTES_Y_VENUES.md)) y con la clase
[010 del programa](../classes/part-00-foundations-history-and-scientific-method/010-como-leer-papers-benchmarks-y-claims-de-ia/README.md).

## 📅 Plan de cinco fases

### 🔵 Fase 1 — Cómo aprende una máquina (P01–P04)

**Duración sugerida:** 2 semanas · **Niveles:** L1–L3

De la neurona que corrige su error a la red profunda que gana un certamen. Al terminar sabes
por qué el conexionismo tuvo un invierno y qué lo sacó de él.

| Paper | Nivel | Pregunta que responde |
|---|:---:|---|
| [P01 Perceptrón](foundational/P01_perceptron/README.md) | L1 | ¿Puede una máquina ajustar sus propios parámetros? |
| [P02 Backpropagation](foundational/P02_backpropagation/README.md) | L2 | ¿Cómo se entrena lo que no se observa directamente? |
| [P03 LSTM](foundational/P03_lstm/README.md) | L2 | ¿Cómo se recuerda a través del tiempo? |
| [P04 AlexNet](foundational/P04_alexnet/README.md) | L3 | ¿Qué hizo falta para que la profundidad escalara? |

**Entregable de fase:** un informe de 2 páginas explicando el invierno de las redes
neuronales usando **solo** evidencia de P01 y P02, sin narrativa retrospectiva.

### 🟢 Fase 2 — Del vector a la secuencia (P05–P07)

**Duración sugerida:** 2 semanas · **Niveles:** L2–L3

Las palabras adquieren geometría, las secuencias se transforman en secuencias, y el cuello
de botella del vector fijo aparece y se elimina.

| Paper | Nivel | Pregunta que responde |
|---|:---:|---|
| [P05 Word2Vec](foundational/P05_word2vec/README.md) | L2 | ¿Cómo se representa el significado sin definirlo? |
| [P06 Seq2Seq](foundational/P06_seq2seq/README.md) | L3 | ¿Cómo se mapea longitud variable a longitud variable? |
| [P07 Attention](foundational/P07_attention_bahdanau/README.md) | L3 | ¿Cómo se deja de comprimir la entrada? |

**Entregable de fase:** medir experimentalmente el cuello de botella (P06) y demostrar que la
atención lo elimina (P07), con tres semillas y una conclusión que no exceda los datos.

### 🟡 Fase 3 — El bloque que lo cambió todo (P08–P11)

**Duración sugerida:** 3 semanas · **Niveles:** L3–L4

El Transformer y sus dos descendencias, más la separación entre conocimiento y razonamiento.
Es la fase más densa y la más rentable.

| Paper | Nivel | Pregunta que responde |
|---|:---:|---|
| [P08 Transformer](foundational/P08_transformer/README.md) + [T01–T08](catalog/PAPERS_INDEX.md) | L4 | ¿Y si quitamos la recurrencia por completo? |
| [P09 BERT](foundational/P09_bert/README.md) | L3 | ¿Por qué mirar a ambos lados cambia la comprensión? |
| [P10 GPT-3](foundational/P10_gpt3/README.md) | L3 | ¿Qué aparece al escalar el decoder? |
| [P11 RAG](foundational/P11_rag/README.md) | L3 | ¿Cómo se cita lo que un modelo afirma? |

**Entregable de fase:** las ocho miniaturas T01–T08 ejecutadas, más un texto de una página
titulado *«qué NO dice el título del paper»*.

### 🔴 Fase 4 — Del modelo al agente (P12–P16)

**Duración sugerida:** 3 semanas · **Niveles:** L3–L5

Alineación, herramientas y sistemas. Aquí el eje entra en territorio con menos consenso, y
eso se declara.

| Paper | Nivel | Pregunta que responde |
|---|:---:|---|
| [P12 InstructGPT](foundational/P12_instructgpt_rlhf/README.md) | L3 | ¿Cómo se alinea un modelo con una intención? |
| [P13 ReAct](foundational/P13_react/README.md) | L2 | ¿Cómo se ancla el razonamiento en observaciones reales? |
| [P14 Toolformer](foundational/P14_toolformer/README.md) | L3 | ¿Cómo se aprende *cuándo* usar una herramienta? |
| [P15 DPO](foundational/P15_dpo/README.md) | L4 | ¿Hace falta RL para alinear? |
| [P16 Sistemas agentic](foundational/P16_agentic_systems/README.md) | L5 | ¿Qué convierte un bucle en un sistema? |

**Entregable de fase:** una nota de linaje fechada sobre un tema de
[`frontier/current-topics.yaml`](../frontier/current-topics.yaml), con fuentes primarias y
una declaración explícita de qué no está consolidado.

### 📚 Fase 5 — Ruta ampliada (P17–P22)

**Duración sugerida:** 3 semanas · **Niveles:** L3–L5

Lo que la cadena canónica no cubre —generación, multimodalidad y economía del cómputo— y la
continuación hasta 2025.

| Paper | Nivel | Pregunta que responde |
|---|:---:|---|
| [P17 Difusión](foundational/P17_diffusion/README.md) | L3 | ¿Cómo se genera sin adversario y sin borrosidad? |
| [P18 CLIP](foundational/P18_clip/README.md) | L3 | ¿Cómo se clasifica lo que nadie etiquetó? |
| [P19 Leyes de escalado](foundational/P19_scaling_laws/README.md) | L4 | A cómputo fijo, ¿parámetros o datos? |
| [P20 Mamba](foundational/P20_mamba/README.md) | L4 | ¿Se puede modelar secuencias sin pagar O(n²)? |
| [P21 Mixtral](foundational/P21_moe/README.md) | L3 | ¿Se puede tener capacidad sin pagarla en cada token? |
| [P22 DeepSeek-R1](foundational/P22_deepseek_r1/README.md) | L5 | ¿Se puede aprender a razonar sin trazas humanas? |

**Entregable de fase:** una cuenta de servilleta propia usando el
[anexo A05](annexes/A05_COMPLEJIDAD_Y_COSTE.md): elige un modelo, estima su coste de
entrenamiento y de inferencia, y decide si conviene denso o disperso para tu volumen.

## ⏱️ Dedicación estimada

| Perfil | Ritmo | Alcance |
|---|---|---|
| **Curioso** | 2 h/semana | Pasada 1–2 de todos los papers; miniaturas de P01, P07, P08 |
| **Estudiante** | 6 h/semana | Ruta completa a nivel L2–L3, todas las miniaturas ejecutadas |
| **Profesional** | 10 h/semana | L4 en P08 y P15; reproducción parcial de dos figuras |
| **Investigador** | continuo | L5 permanente: pasada 5 con fecha en su subárea |

## 🎯 Definición de terminado

Un estudiante ha terminado el eje cuando, **sin abrir los papers**, puede:

- [ ] ubicar cada hito en la evolución de la IA y decir qué lo precede y qué lo sigue;
- [ ] explicar qué problema resolvió cada uno y por qué el anterior no bastaba;
- [ ] ejecutar la miniatura del mecanismo e interpretar su salida;
- [ ] señalar al menos un límite del paper que sus autores **no** declararon;
- [ ] diferenciar el paper original de las prácticas modernas que se le atribuyen;
- [ ] reconocer un claim mal formulado y pedir los cinco datos que le faltan
      (tarea, dataset, métrica, línea base, condiciones);
- [ ] citar cualquiera de los 22 con autoría, año, venue, URL y fecha de consulta;
- [ ] explicar por qué el eje termina en 2025 y qué criterio decide lo que entra.

## 🔮 Trabajo pendiente del eje

Lo que aún no está y se declara como tal, en vez de fingir completitud:

| Pendiente | Estado |
|---|---|
| Páginas HTML del eje dentro del sitio PWA | ✅ 163 páginas en `site/papers/`, con buscador en la portada |
| PDF imprimible del eje completo | ✅ [`docs/pdf/papers-fundacionales.pdf`](../docs/pdf/papers-fundacionales.pdf), 1 230 páginas |
| Anexos matemáticos con ejemplos resueltos | ✅ 5 anexos en [`annexes/`](annexes/README.md) |
| Enlaces de vuelta clase → paper | ✅ 171 clases, generados y verificados en CI |
| Ampliación a generativa, multimodal y escalado (P17–P19) | ✅ difusión, CLIP y leyes de escalado |
| Continuación hasta 2025 (P20–P22) | ✅ Mamba, Mixtral y DeepSeek-R1 |
| Fichas de segunda línea (GloVe, ELMo, T5) | ⬜ no iniciado |
| Reproducción parcial guiada de una figura real de P08 | ⬜ no iniciado |
| Traducción de las fichas a inglés | ⬜ no iniciado |

Los papers de frontera **no** se añaden a `foundational/`: se registran en
[`frontier/current-topics.yaml`](../frontier/current-topics.yaml) hasta que se consoliden.

---

[⬅️ Eje de papers](README.md) ·
[📇 Índice](catalog/PAPERS_INDEX.md) ·
[🗺️ Roadmap del programa completo](../ROADMAP.md)
