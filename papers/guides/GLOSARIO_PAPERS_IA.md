# 📚 Glosario del eje de papers

> Términos que aparecen **leyendo papers**: vocabulario de publicación, de evaluación y de
> los mecanismos de la ruta mínima. Para el vocabulario general del programa (agentes,
> harness, context engineering, MLOps…) usa el [glosario principal](../../docs/GLOSSARY.md).
>
> Cada entrada marca su tipo: 🧱 concepto técnico · 🏛️ proceso editorial · 📏 evaluación · ⚠️ trampa.

## A

**Ablación** 📏 — Quitar un componente y medir cuánto empeora el resultado. Es la única forma
de saber qué pieza explica la mejora. Un paper sin ablaciones afirma que su método funciona,
pero no por qué.

**Abstract** 🏛️ — Resumen de 150–250 palabras. Contiene la versión más favorable de los
resultados: casi nunca menciona la línea base ni las condiciones.

**Alineación (alignment)** 🧱 — Hacer que el comportamiento del modelo coincida con la
intención humana. Ver [P12](../foundational/P12_instructgpt_rlhf/README.md) y
[P15](../foundational/P15_dpo/README.md).

**Anacronismo de atribución** ⚠️ — Adjudicar a un paper una idea que apareció después. El
error más penalizado en este eje. Ejemplo: la puerta de olvido de la LSTM.

**arXiv** 🏛️ — Repositorio de preprints. **Sin revisión por pares.** Ver
[fuentes y venues](FUENTES_Y_VENUES.md).

**Atención** 🧱 — Mecanismo que calcula pesos que suman 1 sobre un conjunto de elementos y
devuelve su combinación ponderada. Introducida para traducción en
[P07](../foundational/P07_attention_bahdanau/README.md).

**Aprendizaje en contexto (in-context learning)** 🧱 — Adaptación al condicionar con ejemplos
en el prompt, **sin actualizar pesos**. Ver [P10](../foundational/P10_gpt3/README.md).

**Autorregresivo** 🧱 — Modelo que genera el elemento *t* condicionado a los anteriores:
`p(x_t | x_<t)`. La familia GPT.

## B

**Benchmark** 📏 — Conjunto estandarizado de tareas y métricas. Útil para comparar; peligroso
cuando se optimiza directamente contra él (ley de Goodhart).

**BLEU** 📏 — Métrica de traducción basada en solapamiento de n-gramas con referencias
humanas. Correlaciona con calidad de forma imperfecta y no es comparable entre papers que
usan distinta tokenización.

**Bradley-Terry** 🧱 — Modelo estadístico de comparaciones por pares:
`p(a ≻ b) = σ(r(a) − r(b))`. Base del modelo de recompensa en RLHF.

## C

**Camino máximo** 🧱 — Número de pasos que debe recorrer una señal entre dos posiciones de una
secuencia. `O(n)` en un RNN, `O(1)` en self-attention. Explica por qué el Transformer entrena
mejor en dependencias largas.

**Carrusel de error constante (CEC)** 🧱 — Ruta aditiva de la celda LSTM por la que el
gradiente viaja sin multiplicarse por activaciones. Ver [P03](../foundational/P03_lstm/README.md).

**Contaminación de benchmark** ⚠️ — Que los datos de test hayan aparecido en el corpus de
entrenamiento. Convierte la métrica en una medida de memorización.

**Cross-attention** 🧱 — Atención donde las consultas vienen de una secuencia y las claves y
valores de otra. Es lo que conecta decoder con encoder.

## D

**DPO (Direct Preference Optimization)** 🧱 — Alinear con preferencias sin modelo de
recompensa ni RL. Ver [P15](../foundational/P15_dpo/README.md).

**DOI** 🏛️ — Identificador persistente de una publicación. Preferible a una URL cuando existe.

## E

**Embedding** 🧱 — Representación vectorial densa. Ver [P05](../foundational/P05_word2vec/README.md).

**Entropía de la atención** 📏 — Cuánto se reparten los pesos α. Baja = atención concentrada;
alta = repartida. Un softmax saturado tiene entropía casi nula y gradientes casi nulos.

**Escalado (scaling laws)** 🧱 — Relación empírica entre cómputo, datos, parámetros y pérdida.
Kaplan et al. (2020) y Hoffmann et al. (2022).

## F

**Few-shot / one-shot / zero-shot** 📏 — Protocolos de evaluación según cuántos ejemplos se
incluyen en el prompt. **No** son formas de entrenamiento.

**Fine-tuning** 🧱 — Ajustar los pesos de un modelo preentrenado sobre una tarea concreta.
Distinto de condicionar con un prompt.

**FFN por posición** 🧱 — Red densa aplicada de forma independiente a cada posición dentro de
un bloque Transformer. Concentra la mayoría de los parámetros del bloque.

## G

**Gradiente desvaneciente** ⚠️ — El gradiente se hace exponencialmente pequeño al propagarse
por muchas capas o pasos temporales, y las primeras capas dejan de aprender.

**GLUE** 📏 — Colección de tareas de comprensión del lenguaje usada para evaluar BERT y
sucesores.

## H

**Hipótesis distribucional** 🧱 — «Una palabra se caracteriza por la compañía que mantiene»
(Firth, 1957; Harris, 1954). Fundamento de los embeddings.

**Hoja de ruta del hito** 🧱 — En este eje, la cadena problema → propuesta → límite → siguiente
paper. Es lo que evita estudiar los papers como una lista inconexa.

## K

**KL (divergencia)** 🧱 — Medida de cuánto se aleja una distribución de otra. En RLHF penaliza
que la política se separe del modelo base; en DPO aparece implícita en el log-ratio.

## L

**Layer normalization** 🧱 — Normaliza cada vector de activación a media 0 y varianza 1. Sin
su epsilon, un vector constante produce división por cero.

**Línea base (baseline)** 📏 — El método contra el que se compara. **Un resultado sin línea
base no es un resultado.** Comprueba si recibió el mismo esfuerzo de ajuste.

## M

**Máscara causal** 🧱 — Impide que la posición *i* atienda a posiciones futuras. Se aplica
**antes** del softmax, poniendo los scores a −∞.

**Memoria paramétrica / no paramétrica** 🧱 — Lo que el modelo sabe en sus pesos frente a lo
que consulta en un índice externo. La separación que propone RAG.

**MLM (Masked Language Modeling)** 🧱 — Predecir tokens enmascarados usando contexto
bidireccional. Objetivo de preentrenamiento de BERT.

## O

**OpenReview** 🏛️ — Plataforma donde el proceso de revisión es público: revisiones, réplicas
y decisión. La mejor escuela de lectura crítica disponible gratis.

**Overclaiming** ⚠️ — Afirmar más de lo que la evidencia sostiene. Forma más común: convertir
una mejora en un benchmark en una afirmación sobre «comprensión» o «razonamiento».

## P

**Peer review (revisión por pares)** 🏛️ — Evaluación por investigadores del área antes de
publicar. arXiv no la tiene; NeurIPS, ICML, ICLR y ACL sí.

**Preprint** 🏛️ — Versión previa a la revisión formal. Citable, pero declarando que lo es.

**Producto escalar escalado** 🧱 — `QKᵀ/√d_k`. La división evita que el softmax se sature al
crecer la dimensión.

**Positional encoding** 🧱 — Información de orden que se **suma** al embedding, porque la
atención por sí sola es indiferente a las permutaciones.

## R

**RAG** 🧱 — Recuperar documentos y generar condicionando en ellos. Ver
[P11](../foundational/P11_rag/README.md).

**Reproducibilidad** 📏 — Que otra persona, con el paper y el código, obtenga el mismo
resultado. Requiere semillas, versiones, datos y cómputo declarados.

**Residual (conexión)** 🧱 — `x + Sublayer(x)`. Camino identidad que permite apilar decenas o
cientos de capas sin que la señal se apague.

**Reward hacking** ⚠️ — La política maximiza el modelo de recompensa explotando un atajo
(por ejemplo, ser más larga) sin mejorar la calidad real.

**RLHF** 🧱 — Ajuste con retroalimentación humana en tres etapas: SFT, modelo de recompensa y
RL con penalización KL. Ver [P12](../foundational/P12_instructgpt_rlhf/README.md).

## S

**Self-attention** 🧱 — Atención de una secuencia sobre sí misma.

**Semilla (seed)** 📏 — Valor que fija la aleatoriedad. Reportar resultados sin semilla ni
número de ejecuciones impide distinguir mejora de ruido.

**Softmax** 🧱 — Convierte un vector de scores en una distribución de probabilidad. Se
implementa restando el máximo para evitar desbordamiento.

**SOTA (state of the art)** ⚠️ — «Estado del arte». Caduca. Sin fecha y benchmark concretos,
la palabra no informa de nada.

## T

**Tool use** 🧱 — Que el modelo invoque funciones externas. Aprendido de forma autosupervisada
en [P14](../foundational/P14_toolformer/README.md).

**Transformer** 🧱 — Arquitectura basada solo en atención, FFN, residuales, layer norm y
codificación posicional. Ver [P08](../foundational/P08_transformer/README.md).

## V

**Venue** 🏛️ — Dónde se publicó: conferencia, revista o repositorio. Parte obligatoria de una
cita.

**Varianza entre ejecuciones** 📏 — Diferencia de resultados al cambiar solo la semilla. Si la
mejora reportada es menor que la varianza, no hay mejora demostrada.

---

[⬅️ Eje de papers](../README.md) ·
[📖 Cómo leer un paper](COMO_LEER_UN_PAPER_DE_IA.md) ·
[🌐 Fuentes y venues](FUENTES_Y_VENUES.md) ·
[📖 Glosario general del programa](../../docs/GLOSSARY.md)
