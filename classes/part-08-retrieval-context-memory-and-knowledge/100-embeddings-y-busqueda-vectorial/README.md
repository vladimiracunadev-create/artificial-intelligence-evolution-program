
# 100 — Embeddings y búsqueda vectorial

> [← Clase anterior](../../../classes/part-07-generative-ai-across-media/099-proyecto-pipeline-creativo-trazable/README.md) · [Índice de la parte](../README.md) · [Clase siguiente →](../../../classes/part-08-retrieval-context-memory-and-knowledge/101-segmentacion-metadatos-y-ventanas/README.md)

**Parte:** 08 — Recuperación, contexto, memoria y conocimiento  
**Nivel:** avanzado · **Horas estimadas:** 6  
**Laboratorio:** `retrieval` · **Estado:** `EXECUTABLE_CORE`

## 🎯 Propósito

Comprender **embeddings y búsqueda vectorial** dentro de la evolución de la inteligencia
artificial, implementar un experimento mínimo verificable y distinguir qué parte
constituye evidencia frente a una afirmación todavía no comprobada.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. Explicar embeddings y búsqueda vectorial usando los conceptos `embeddings`, `vector search`, `cosine`, `índices`.
2. Ejecutar el laboratorio con una semilla explícita y revisar su contrato JSON.
3. Identificar al menos un supuesto, una limitación y un riesgo de aplicación.
4. Comparar el enfoque con la etapa anterior de la ruta de aprendizaje.
5. Producir una evidencia reproducible y una conclusión que no exceda los datos.

## 🧩 Conceptos centrales

`embeddings`, `vector search`, `cosine`, `índices`

## 🗺️ Ubicación en el mapa de la IA

Los embeddings son el puente entre el texto discreto y la geometría continua: convierten
palabras, frases y documentos en vectores densos donde la cercanía codifica similitud
semántica. Heredan la hipótesis distribucional de la lingüística de corpus y los modelos
de lenguaje neuronales (partes 05 y 06), y son el cimiento de toda la parte 08: sin
búsqueda vectorial no hay RAG, ni memoria a largo plazo, ni caches semánticos. Lo que
esta clase establece —representar para recuperar— reaparece en cada clase siguiente.

## 📖 Fundamentos

### 🔢 Qué es un embedding

Un **embedding** es una función `E: texto → ℝ^d` aprendida por una red neuronal, con
`d` típicamente entre 256 y 3072. La propiedad que la hace útil es que la geometría
refleja la semántica: textos con significado parecido quedan en regiones cercanas del
espacio, aunque no compartan ninguna palabra ("automóvil" y "coche" acaban próximos).
Los modelos modernos (p. ej. Sentence-BERT y sus derivados) se entrenan con
**aprendizaje contrastivo**: acercar pares relacionados (pregunta/respuesta,
oración/paráfrasis) y alejar pares negativos.

### 📐 Similitud coseno

Dados dos vectores `u, v ∈ ℝ^d`, la similitud coseno es el coseno del ángulo entre ellos:

```text
cos(u, v) = (u · v) / (‖u‖ · ‖v‖)      con  u · v = Σᵢ uᵢvᵢ  y  ‖u‖ = √(Σᵢ uᵢ²)
```

- Rango `[−1, 1]`; 1 = misma dirección, 0 = ortogonales, −1 = opuestos.
- Es **invariante a la escala**: `cos(u, 3v) = cos(u, v)`. Mide orientación, no magnitud.
- Si los vectores están **normalizados** (`‖u‖ = ‖v‖ = 1`), el coseno se reduce al
  producto punto, y ordenar por coseno equivale a ordenar por distancia euclídea,
  porque `‖u − v‖² = 2 − 2·cos(u, v)`. Por eso casi todos los índices normalizan.

### 🔍 Búsqueda exacta vs. aproximada (ANN)

La búsqueda **exacta** (índice *flat*) compara la consulta contra los `n` vectores:
coste `O(n · d)` por consulta. Con `n = 10⁶` y `d = 768` son ~10⁹ multiplicaciones:
viable en batch, prohibitivo a baja latencia. Los índices **ANN**
(*approximate nearest neighbor*) sacrifican exactitud garantizada por velocidad:

- **IVF** (*inverted file*): agrupa los vectores en `k` celdas por k-means; en consulta
  solo se exploran las `nprobe` celdas más cercanas al centroide de la consulta.
- **PQ** (*product quantization*): comprime cada vector en subvectores cuantizados,
  reduciendo memoria ~10-100× a costa de comparar contra aproximaciones.
- **HNSW** (*Hierarchical Navigable Small World*, Malkov & Yashunin,
  [arXiv:1603.09320](https://arxiv.org/abs/1603.09320)): un grafo de proximidad por
  capas. Las capas superiores tienen pocos nodos con aristas largas (autopistas); las
  inferiores, todos los nodos con aristas cortas. La búsqueda entra por arriba, avanza
  con voraz *greedy* hacia el vecino más cercano y desciende de capa, logrando
  complejidad empírica `O(log n)` con recall alto controlado por `efSearch`.

```text
buscar_hnsw(q):
  nodo ← entrada de la capa superior
  para capa L..1:                      # descenso por autopistas
      nodo ← greedy_mas_cercano(q, nodo, capa)
  return busqueda_en_haz(q, nodo, capa 0, ef=efSearch)   # refinamiento final
```

La métrica clave de un índice ANN es **recall@k frente a latencia**: qué fracción de
los verdaderos k vecinos devuelve y en cuánto tiempo. Nunca se reporta una sin la otra.

## 🧮 Ejemplo trabajado

Consulta y tres documentos ya embebidos en 3 dimensiones (didáctico; en la práctica `d` ≥ 256):

```text
q  = (1, 2, 2)          ‖q‖  = √(1+4+4) = 3
d1 = (2, 4, 4)          ‖d1‖ = √(4+16+16) = 6
d2 = (0, 3, 4)          ‖d2‖ = √(0+9+16) = 5
d3 = (2, −1, 2)         ‖d3‖ = √(4+1+4) = 3

cos(q,d1) = (2+8+8)  / (3·6) = 18/18 = 1.000   ← misma dirección que q (d1 = 2q)
cos(q,d2) = (0+6+8)  / (3·5) = 14/15 ≈ 0.933
cos(q,d3) = (2−2+4)  / (3·3) = 4/9   ≈ 0.444

Ranking: d1 > d2 > d3
```

Obsérvese que `d1 = 2·q`: su magnitud es el doble pero el coseno es exactamente 1,
mientras que la distancia euclídea `‖q − d1‖ = 3` no es cero. Coseno y euclídea solo
coinciden en ranking cuando todos los vectores están normalizados.

## 📊 Propiedades y comparación

| Índice | Búsqueda | Memoria | Recall | Inserciones | Uso típico |
|---|---|---|---|---|---|
| Flat (exacto) | `O(n·d)` | `O(n·d)` | 100 % | triviales | n pequeño, baseline obligado |
| IVF | `O((n/k)·nprobe·d)` | `O(n·d)` | alto, depende de `nprobe` | requiere reentrenar centroides | colecciones medianas estáticas |
| IVF-PQ | sublineal | ~10-100× menos | medio | ídem | miles de millones de vectores |
| HNSW | `O(log n)` empírico | `O(n·d + n·M)` (grafo) | muy alto (`efSearch`) | incrementales nativas | servicio online de baja latencia |

```mermaid
flowchart LR
    T[Texto] --> E[Modelo de embeddings E]
    E --> V["vector q ∈ ℝ^d (normalizado)"]
    subgraph Indice[Índice vectorial]
        C1[Capa 2: aristas largas] --> C2[Capa 1] --> C3[Capa 0: todos los nodos]
    end
    V --> C1
    C3 --> K["top-k vecinos por coseno"]
    K --> R[recall@k vs latencia]
```

## ⚠️ Errores conceptuales frecuentes

1. **"Coseno alto = relevancia"**. El coseno mide similitud semántica de superficie;
   una pregunta y su negación pueden tener coseno > 0.9. Relevancia exige señales
   adicionales (clase 104, re-ranking).
2. **Comparar embeddings de modelos distintos**. Cada modelo define su propio espacio;
   los vectores de dos modelos no son comparables ni promediables. Cambiar de modelo
   obliga a reindexar toda la colección.
3. **Tratar ANN como búsqueda exacta**. HNSW o IVF pueden omitir el verdadero vecino
   más cercano; si el recall@k no se mide contra un baseline flat, no se sabe cuánto se pierde.
4. **Ignorar la normalización**. Mezclar vectores normalizados y sin normalizar, o usar
   producto punto sobre vectores de normas muy dispares, produce rankings sesgados hacia
   documentos "largos" en norma.
5. **Intuición euclídea en alta dimensión**. Con `d` grande las distancias se concentran
   (todas parecen similares) y el volumen se acumula en la corteza: las intuiciones 2D/3D
   sobre "cercanía" fallan; por eso se valida con métricas, no con dibujos.

## 🚀 Del aprendizaje a la operación

Entre este núcleo y un buscador vectorial real faltan: la elección y evaluación del
modelo de embeddings sobre el dominio propio (no el benchmark público), el pipeline de
reindexado cuando el modelo cambia de versión, filtros de metadatos combinados con la
búsqueda ANN (pre- vs post-filtrado), la operación del índice (memoria, réplicas,
snapshots) y el monitoreo de recall en producción con consultas etiquetadas. Motores
como faiss o Qdrant resuelven la infraestructura, no la calidad del embedding.

## 🧪 Laboratorio

```bash
python lab.py
```

El laboratorio llama a `ai_evolution.labs.run_lab("retrieval")`. Esta
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

- Malkov, Y. & Yashunin, D. (2016). *Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs*. [arXiv:1603.09320](https://arxiv.org/abs/1603.09320)
- Reimers, N. & Gurevych, I. (2019). *Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks*. [arXiv:1908.10084](https://arxiv.org/abs/1908.10084)
- Johnson, J., Douze, M. & Jégou, H. (2017). *Billion-scale similarity search with GPUs* (faiss). [arXiv:1702.08734](https://arxiv.org/abs/1702.08734)
- Jurafsky, D. & Martin, J. H. *Speech and Language Processing* (3.ª ed., borrador), cap. "Vector Semantics and Embeddings". [https://web.stanford.edu/~jurafsky/slp3/](https://web.stanford.edu/~jurafsky/slp3/)
- Documentación oficial de faiss: [https://faiss.ai/](https://faiss.ai/)
- Documentación oficial de Qdrant: [https://qdrant.tech/documentation/](https://qdrant.tech/documentation/)

---

## ⬅️ Clase anterior

[099 — Proyecto: pipeline creativo trazable](../../part-07-generative-ai-across-media/099-proyecto-pipeline-creativo-trazable/README.md)

## ➡️ Siguiente clase

[101 — Segmentación, metadatos y ventanas](../../part-08-retrieval-context-memory-and-knowledge/101-segmentacion-metadatos-y-ventanas/README.md)
