
# 073 — Tokenización moderna y vocabularios

> [← Clase anterior](../../../classes/part-05-language-vision-audio-and-multimodal-ai/072-proyecto-asistente-multimodal-accesible/README.md) · [Índice de la parte](../README.md) · [Clase siguiente →](../../../classes/part-06-foundation-models-and-llm-engineering/074-objetivos-de-preentrenamiento/README.md)

**Parte:** 06 — Modelos fundacionales e ingeniería de LLM  
**Nivel:** avanzado · **Horas estimadas:** 6  
**Laboratorio:** `llm` · **Estado:** `EXECUTABLE_CORE`

## 🎯 Propósito

Comprender **tokenización moderna y vocabularios** dentro de la evolución de la inteligencia
artificial, implementar un experimento mínimo verificable y distinguir qué parte
constituye evidencia frente a una afirmación todavía no comprobada.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. Explicar tokenización moderna y vocabularios usando los conceptos `BPE`, `SentencePiece`, `tokens`, `vocabulario`.
2. Ejecutar el laboratorio con una semilla explícita y revisar su contrato JSON.
3. Identificar al menos un supuesto, una limitación y un riesgo de aplicación.
4. Comparar el enfoque con la etapa anterior de la ruta de aprendizaje.
5. Producir una evidencia reproducible y una conclusión que no exceda los datos.

## 🧩 Conceptos centrales

`BPE`, `SentencePiece`, `tokens`, `vocabulario`

## 🗺️ Ubicación en el mapa de la IA

La tokenización es la frontera entre el texto humano y los enteros que consume un
Transformer: ningún LLM "ve" letras, ve identificadores de un vocabulario fijo.
Hereda el problema clásico de PLN de las palabras fuera de vocabulario (OOV) y lo
resuelve con unidades subpalabra (BPE, unigram), decisión que condiciona todo lo que
sigue en esta parte: el costo por token, la longitud efectiva de contexto, la
aritmética "rara" de los LLM y hasta el precio de una llamada a una API se explican
desde el tokenizador.

## 📖 Fundamentos

### 🔤 Del carácter a la subpalabra

Hay tres granularidades posibles y ninguna gratuita:

| Granularidad | Vocabulario | Secuencias | Problema principal |
|---|---|---|---|
| Carácter | ~100–1 000 | Muy largas | Secuencias enormes; semántica diluida |
| Palabra | 10⁵–10⁶ | Cortas | OOV: toda palabra nueva es `<unk>` |
| Subpalabra | 3·10⁴–2,5·10⁵ | Intermedias | Cortes a veces poco intuitivos |

Los LLM modernos usan subpalabras: palabras frecuentes quedan como un token único
("the", "de"), palabras raras se descomponen ("tokenización" → "token" + "ización")
y cualquier cadena es representable, porque en el peor caso se cae a bytes o
caracteres. No hay OOV por construcción.

### ⚙️ BPE (Byte-Pair Encoding)

BPE (Sennrich et al., 2016, adaptado de un algoritmo de compresión de 1994) aprende
el vocabulario por *fusiones* (merges) codiciosas:

```text
Entrenamiento BPE
1. Inicializa el vocabulario con símbolos base (caracteres o bytes).
2. Cuenta la frecuencia de cada PAR adyacente de símbolos en el corpus.
3. Fusiona el par más frecuente en un símbolo nuevo y regístralo como merge.
4. Repite 2–3 hasta alcanzar el tamaño de vocabulario objetivo.

Inferencia (tokenizar texto nuevo)
1. Divide la palabra en símbolos base.
2. Aplica las merges aprendidas EN EL MISMO ORDEN de entrenamiento,
   siempre que el par esté presente.
```

GPT-2/GPT-4 usan *byte-level BPE*: los símbolos base son los 256 bytes, de modo que
emoji, chino o binario siempre son tokenizables sin `<unk>`.

### 🎲 Unigram LM (SentencePiece)

El modelo unigram (Kudo, 2018) trabaja al revés: parte de un vocabulario grande de
candidatos y lo **poda**. Asume que una segmentación x = (t₁,…,tₖ) tiene probabilidad
P(x) = Π P(tᵢ) y busca la segmentación de máxima probabilidad (algoritmo de Viterbi).
En cada iteración estima P(tᵢ) con EM, calcula cuánto empeora la verosimilitud del
corpus si se elimina cada token, y descarta el ~20 % menos útil hasta llegar al
tamaño objetivo. SentencePiece implementa BPE y unigram tratando el texto crudo como
secuencia (el espacio se marca como `▁`), sin pretokenización dependiente del idioma.

### 📏 Consecuencias prácticas del vocabulario

- **Fertilidad**: tokens promedio por palabra. En idiomas poco representados en el
  corpus, la fertilidad sube: el mismo texto cuesta 2–4× más tokens (y más dinero).
- **Contexto efectivo**: una ventana de 128k tokens contiene menos texto real si la
  fertilidad es alta.
- **Aritmética y deletreo**: "1234" puede ser un token único y "1235" dos; el modelo
  no ve dígitos, ve trozos arbitrarios. Igual con contar letras de una palabra.
- **Tamaño del embedding**: la matriz de embeddings es `|V| × d_model`; con
  |V| = 128 000 y d = 4 096 son ~524 M de parámetros solo en embeddings.

## 🧮 Ejemplo trabajado

Corpus de juguete (con frecuencia): `low ×5`, `lower ×2`, `newest ×6`, `widest ×3`.
Símbolos base = caracteres, con marcador de fin de palabra `_`.

```text
Estado inicial: l o w _ (5) | l o w e r _ (2) | n e w e s t _ (6) | w i d e s t _ (3)

Conteo de pares (los relevantes):
  (e,s): 6+3 = 9   ← máximo
  (s,t): 6+3 = 9   (empate; se rompe por orden de aparición)
  (l,o): 5+2 = 7
  (w,e): 2+6 = 8

Merge 1: (e,s) → "es"      newest → n e w es t _ ; widest → w i d es t _
Merge 2: (es,t) → "est"    n e w est _ ; w i d est _   (frecuencia 9)
Merge 3: (est,_) → "est_"  (frecuencia 9)
Merge 4: (l,o) → "lo"      lo w _ ; lo w e r _   (frecuencia 7)
Merge 5: (lo,w) → "low"    low _ ; low e r _     (frecuencia 7)
```

Con estas 5 merges, la palabra **nueva** "lowest" (nunca vista) se tokeniza:
`l o w e s t _` → (es) → (est) → (est_) → (lo) → (low) → `low est_`: dos tokens con
sentido morfológico, sin haberla visto jamás. Ese es el punto de BPE.

## 📊 Propiedades y comparación

| Propiedad | BPE | WordPiece | Unigram (SentencePiece) |
|---|---|---|---|
| Estrategia | Fusión codiciosa por frecuencia | Fusión por máxima verosimilitud | Poda de vocabulario grande |
| Segmentación | Determinista (orden de merges) | Determinista (longest-match) | Probabilística (Viterbi; permite muestreo) |
| Regularización subword | No nativa (BPE-dropout aparte) | No | Sí (muestrear segmentaciones) |
| Usada en | GPT-2/3/4, Llama, RoBERTa | BERT | T5, Llama (vía SentencePiece), mT5 |
| OOV | Imposible (byte-level) | `[UNK]` posible | Imposible con fallback a bytes |

```mermaid
flowchart LR
    A[Texto crudo] --> B[Pretokenización / bytes]
    B --> C{Algoritmo}
    C -->|BPE| D[Aplicar merges en orden]
    C -->|Unigram| E[Viterbi: segmentación mas probable]
    D --> F[Tokens subpalabra]
    E --> F
    F --> G[IDs enteros del vocabulario]
    G --> H[Matriz de embeddings |V| x d]
```

## ⚠️ Errores conceptuales frecuentes

1. **"Un token es una palabra."** Falso: es una unidad subpalabra estadística; en
   inglés ~0,75 palabras/token, y en otros idiomas bastante menos.
2. **"El tokenizador entiende morfología."** No: BPE fusiona por frecuencia; que
   "ización" salga como sufijo es un efecto estadístico, no análisis lingüístico.
3. **"Se puede cambiar el tokenizador de un modelo entrenado."** No sin reentrenar:
   los embeddings están ligados a los IDs del vocabulario original.
4. **"Vocabulario más grande siempre es mejor."** Trade-off real: menos tokens por
   texto, pero matriz de embeddings más cara y tokens raros peor entrenados.
5. **"El modelo ve caracteres."** No: por eso falla contando letras o comparando
   números; opera sobre trozos opacos de texto.

## 🚀 Del aprendizaje a la operación

Entre este ejemplo a mano y un tokenizador real faltan: entrenamiento sobre corpus
de cientos de GB con pretokenización cuidadosa (espacios, dígitos, código), byte
fallback y tokens especiales (`<|endoftext|>`, plantillas de chat), auditoría de
fertilidad por idioma y dominio, y compatibilidad estricta tokenizador↔checkpoint:
en producción, mezclar versiones de tokenizador es un bug silencioso que degrada
todo sin lanzar errores.

## 🧪 Laboratorio

```bash
python lab.py
```

El laboratorio llama a `ai_evolution.labs.run_lab("llm")`. Esta
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

- Sennrich, Haddow y Birch (2016), *Neural Machine Translation of Rare Words with Subword Units* (BPE): <https://arxiv.org/abs/1508.07909>
- Kudo (2018), *Subword Regularization* (modelo unigram): <https://arxiv.org/abs/1804.10959>
- Kudo y Richardson (2018), *SentencePiece*: <https://arxiv.org/abs/1808.06226>
- Jurafsky y Martin, *Speech and Language Processing* (3.ª ed., borrador), cap. 2: <https://web.stanford.edu/~jurafsky/slp3/>
- Documentación oficial de Hugging Face Tokenizers: <https://huggingface.co/docs/tokenizers>

---

## ⬅️ Clase anterior

[072 — Proyecto: asistente multimodal accesible](../../part-05-language-vision-audio-and-multimodal-ai/072-proyecto-asistente-multimodal-accesible/README.md)

## ➡️ Siguiente clase

[074 — Objetivos de preentrenamiento](../../part-06-foundation-models-and-llm-engineering/074-objetivos-de-preentrenamiento/README.md)
