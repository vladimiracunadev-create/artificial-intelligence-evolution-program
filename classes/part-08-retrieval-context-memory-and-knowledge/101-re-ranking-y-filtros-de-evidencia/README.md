
# 101 — Re-ranking y filtros de evidencia

> [← Clase anterior](../../../classes/part-08-retrieval-context-memory-and-knowledge/100-busqueda-hibrida-y-fusion-de-rankings/README.md) · [Índice de la parte](../README.md) · [Clase siguiente →](../../../classes/part-08-retrieval-context-memory-and-knowledge/102-rag-basico-con-citas/README.md)

**Parte:** 08 — Recuperación, contexto, memoria y conocimiento  
**Nivel:** avanzado · **Horas estimadas:** 6  
**Laboratorio:** `retrieval` · **Estado:** `EXECUTABLE_CORE`

## 🎯 Propósito

Comprender **re-ranking y filtros de evidencia** dentro de la evolución de la inteligencia
artificial, implementar un experimento mínimo verificable y distinguir qué parte
constituye evidencia frente a una afirmación todavía no comprobada.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. Explicar re-ranking y filtros de evidencia usando los conceptos `reranking`, `cross-encoder`, `filtros`, `calidad`.
2. Ejecutar el laboratorio con una semilla explícita y revisar su contrato JSON.
3. Identificar al menos un supuesto, una limitación y un riesgo de aplicación.
4. Comparar el enfoque con la etapa anterior de la ruta de aprendizaje.
5. Producir una evidencia reproducible y una conclusión que no exceda los datos.

## 🧩 Conceptos centrales

`reranking`, `cross-encoder`, `filtros`, `calidad`

## 🗺️ Ubicación en el mapa de la IA

La recuperación de las clases 097-100 optimiza el *recall*: traer candidatos plausibles
rápido y barato. El re-ranking optimiza la *precisión*: reordenar esos candidatos con un
modelo más caro y preciso que ya puede leer consulta y documento juntos. Este patrón de
dos etapas —recuperar amplio, refinar caro— viene de los buscadores web clásicos y es hoy
la arquitectura estándar de todo pipeline RAG serio: la calidad del contexto que llega al
generador (clase 102) depende directamente de este filtro.

## 📖 Fundamentos

### ⚖️ Bi-encoder vs. cross-encoder

Un **bi-encoder** (como los modelos de embeddings de la clase 097) codifica consulta y
documento **por separado** en vectores, y la relevancia se estima con una función barata
(coseno). Eso permite pre-computar los vectores de toda la colección e indexarlos: coste
por consulta `O(1)` embeddings + búsqueda ANN. El precio es expresividad: el modelo nunca
ve consulta y documento juntos, así que no puede modelar interacciones finas
(negaciones, coincidencia de entidades, condiciones).

Un **cross-encoder** (Nogueira & Cho, [arXiv:1901.04085](https://arxiv.org/abs/1901.04085))
concatena consulta y documento en una sola entrada —`[CLS] consulta [SEP] documento`— y
un transformer produce un **score de relevancia** con atención completa entre todos los
tokens de ambos textos. Es mucho más preciso, pero no hay nada pre-computable: cada par
(q, d) exige una pasada completa del modelo. Con `n = 10⁶` documentos es inviable como
primera etapa; con los `k = 50` candidatos de la primera etapa, es trivial.

```text
Pipeline retrieve-then-rerank:
  1. Recuperación (bi-encoder / BM25 / híbrida)  → top-100 candidatos     (barato, alto recall)
  2. Re-ranking (cross-encoder sobre 100 pares)  → top-10 reordenados     (caro, alta precisión)
  3. Filtros de evidencia                        → top-k final al LLM     (umbral, dedup, diversidad)
```

### 🔀 MMR: relevancia con diversidad

Los k mejores documentos por score suelen ser redundantes (variantes del mismo pasaje).
**Maximal Marginal Relevance** (Carbonell & Goldstein, 1998,
[DOI 10.1145/290941.291025](https://doi.org/10.1145/290941.291025)) selecciona
iterativamente el documento que maximiza un compromiso entre relevancia y novedad:

```text
MMR(d) = λ · sim(q, d) − (1 − λ) · max_{s ∈ S} sim(d, s)
```

donde `S` es el conjunto ya seleccionado y `λ ∈ [0, 1]` controla el equilibrio:
`λ = 1` es ranking puro por relevancia; `λ = 0` maximiza solo diversidad. En cada
iteración se recalcula el término de penalización porque `S` creció.

### 🧹 Filtros de evidencia

Después del re-ranking, antes de pasar contexto al generador, se aplican filtros que
convierten "candidatos ordenados" en "evidencia admisible":

- **Umbral de score**: descartar documentos bajo un mínimo calibrado; con score bajo es
  mejor entregar k' < k documentos (o ninguno y declarar "no hay evidencia") que rellenar.
- **Deduplicación**: eliminar pasajes casi idénticos (similitud entre documentos > 0.95).
- **Filtros de metadatos**: fecha, fuente autorizada, permisos de acceso del usuario.
- **Presupuesto de tokens**: el contexto del LLM es finito; k se elige por presupuesto,
  no por costumbre.

El principio: es preferible un contexto corto y limpio que uno largo y ruidoso, porque
el generador no distingue por sí solo la evidencia buena de la mala.

## 🧮 Ejemplo trabajado

MMR a mano con `λ = 0.7`, k = 2, y cuatro candidatos ya puntuados:

```text
sim(q,·):   d1 = 0.90   d2 = 0.85   d3 = 0.70   d4 = 0.60
sim entre documentos:  sim(d1,d2) = 0.95 (casi duplicados)
                       sim(d1,d3) = 0.30   sim(d1,d4) = 0.20
                       sim(d2,d3) = 0.35   sim(d2,d4) = 0.25

Iteración 1 (S = ∅, sin penalización): gana el más relevante → d1.  S = {d1}

Iteración 2 (penaliza similitud con d1):
  MMR(d2) = 0.7·0.85 − 0.3·0.95 = 0.595 − 0.285 = 0.310
  MMR(d3) = 0.7·0.70 − 0.3·0.30 = 0.490 − 0.090 = 0.400   ← gana
  MMR(d4) = 0.7·0.60 − 0.3·0.20 = 0.420 − 0.060 = 0.360

Selección final: {d1, d3}
```

Nótese que d2, el segundo más relevante, **queda fuera**: su casi-duplicidad con d1
(0.95) lo penaliza más de lo que su relevancia lo favorece. Con `λ = 0.9` la penalización
pesaría 0.1 y d2 ganaría (0.765 − 0.095 = 0.670 > 0.603 de d3): λ decide qué significa
"mejor contexto".

## 📊 Propiedades y comparación

| Arquitectura | Interacción q-d | Pre-cómputo | Coste por consulta | Calidad | Rol en el pipeline |
|---|---|---|---|---|---|
| Bi-encoder | ninguna (vectores separados) | sí (índice) | muy bajo | media | 1.ª etapa, recall |
| Late interaction (ColBERT) | por token, tardía | parcial | medio | media-alta | 1.ª etapa mejorada |
| Cross-encoder | atención completa | no | alto (1 pasada por par) | alta | 2.ª etapa, precisión |
| MMR | entre documentos | no | bajo (`O(k²)` sims) | diversidad | selección final |

```mermaid
flowchart LR
    Q[Consulta] --> R1["1ª etapa: bi-encoder / BM25<br/>top-100, alto recall"]
    R1 --> CE["2ª etapa: cross-encoder<br/>score(q,d) por par"]
    CE --> F["Filtros: umbral de score<br/>dedup > 0.95, metadatos"]
    F --> MMR["MMR: λ·relevancia − (1−λ)·redundancia"]
    MMR --> K["top-k final → contexto del LLM"]
```

## ⚠️ Errores conceptuales frecuentes

1. **"El cross-encoder es mejor, úsalo para todo"**. Sin primera etapa es inviable:
   puntuar 10⁶ pares por consulta son horas de GPU. Su rol es refinar decenas, no
   explorar millones.
2. **Re-rankear no mejora el recall**. Si el documento correcto no está en el top-100 de
   la primera etapa, ningún re-ranker lo recuperará: el re-ranking solo reordena. Un
   recall@100 bajo se arregla en la etapa 1, no en la 2.
3. **Comparar scores de cross-encoder entre consultas**. El score es un ordinal dentro de
   la misma consulta; 0.62 en una consulta y 0.62 en otra no significan la misma
   relevancia. Los umbrales requieren calibración sobre datos propios.
4. **MMR con λ arbitrario**. λ = 0.5 "por defecto" puede excluir el documento más útil.
   λ se ajusta observando el efecto en la calidad de la respuesta final, no se hereda.
5. **Filtrar después de truncar**. Aplicar el presupuesto de tokens antes de deduplicar
   desperdicia contexto en repeticiones; el orden correcto es: score → dedup →
   diversidad → presupuesto.

## 🚀 Del aprendizaje a la operación

Entre este núcleo y un re-ranker en producción faltan: elegir y evaluar un modelo de
cross-encoder sobre pares etiquetados del dominio propio (no MS MARCO), medir la latencia
añadida por la segunda etapa bajo carga real (suele dominar el p95 del pipeline),
calibrar umbrales de score con validación periódica, decidir el comportamiento cuando
ningún candidato supera el umbral (responder "sin evidencia" es una función del producto),
y monitorear la deriva: un corpus que crece cambia la distribución de scores.

## 🧪 Laboratorio

```bash
python lab.py
```

El laboratorio llama a `ai_evolution.labs.run_lab("retrieval")`. Esta
decisión evita 180 implementaciones divergentes: cada clase tiene un entrypoint
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

- Nogueira, R. & Cho, K. (2019). *Passage Re-ranking with BERT*. [arXiv:1901.04085](https://arxiv.org/abs/1901.04085)
- Carbonell, J. & Goldstein, J. (1998). *The Use of MMR, Diversity-Based Reranking for Reordering Documents and Producing Summaries*. SIGIR '98. [DOI 10.1145/290941.291025](https://doi.org/10.1145/290941.291025)
- Khattab, O. & Zaharia, M. (2020). *ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT*. [arXiv:2004.12832](https://arxiv.org/abs/2004.12832)
- Reimers, N. & Gurevych, I. (2019). *Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks*. [arXiv:1908.10084](https://arxiv.org/abs/1908.10084)
- Documentación de cross-encoders en sentence-transformers: [https://www.sbert.net/examples/applications/cross-encoder/README.html](https://www.sbert.net/examples/applications/cross-encoder/README.html)

---

## ⬅️ Clase anterior

[100 — Búsqueda híbrida y fusión de rankings](../../part-08-retrieval-context-memory-and-knowledge/100-busqueda-hibrida-y-fusion-de-rankings/README.md)

## ➡️ Siguiente clase

[102 — RAG básico con citas](../../part-08-retrieval-context-memory-and-knowledge/102-rag-basico-con-citas/README.md)
