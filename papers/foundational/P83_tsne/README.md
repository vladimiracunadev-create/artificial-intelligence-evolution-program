# P83 — t-SNE

> Ruta clásica · Hace visible la estructura local de datos de muchas dimensiones. Y hay
> tres cosas del mapa resultante que no significan nada, aunque todo el mundo las lea.

**Nivel:** L3 · **Motor:** `tsne` · **Notebook:** [`P83_tsne.ipynb`](../../../notebooks/papers/P83_tsne.ipynb)
· **Anexo:** [probabilidad y verosimilitud](../../annexes/A02_PROBABILIDAD_Y_VEROSIMILITUD.md)

## 1. Identificación

| Campo | Valor |
|---|---|
| **Título original** | *Visualizing Data using t-SNE* |
| **Autoría** | Laurens van der Maaten, Geoffrey Hinton |
| **Año** | 2008 |
| **Venue** | Journal of Machine Learning Research, 9, 2579–2605 |
| **Fuente primaria** | [JMLR 9:2579–2605](https://www.jmlr.org/papers/v9/vandermaaten08a.html) |
| **Acceso** | Abierto |
| **Fecha de consulta** | 2026-08-17 |

## 2. Problema anterior

Al proyectar de muchas dimensiones a dos, aparece un problema geométrico que no es un defecto del
método sino del espacio de partida: en dimensión alta hay **muchísimo más sitio lejos que cerca**.
El volumen de una corona esférica crece con el radio elevado a la dimensión.

Cuando se intenta reproducir esas distancias en un plano, todos los puntos moderadamente lejanos se
apiñan en el centro y la estructura desaparece. Es el **problema del apiñamiento**, y era el
límite de SNE, el método anterior de los mismos autores.

## 3. Propuesta

Dos cambios sobre SNE. El primero es técnico: simetrizar las afinidades, lo que simplifica el
gradiente.

El segundo es la idea central: usar en el **mapa** una distribución con cola pesada —una t de
Student con un grado de libertad— mientras en el espacio **original** se sigue usando una
gaussiana.

La asimetría es deliberada. La cola pesada deja mucha más masa de probabilidad a distancias
grandes, así que dos puntos moderadamente lejanos en el espacio original pueden colocarse **muy
lejos** en el mapa sin penalización. Eso libera espacio en el centro y la estructura local se
puede desplegar.

## 4. Intuición sin fórmulas

Un mapa del metro. Conserva perfectamente qué estación viene después de cuál y qué líneas se
cruzan. No conserva ni las distancias ni las direcciones, y a nadie le extraña: para lo que sirve
el mapa, esa información sobra.

t-SNE hace lo mismo con datos: preserva **quién está cerca de quién** y sacrifica todo lo demás.

**Dónde deja de funcionar la analogía:** el mapa del metro es siempre el mismo. Dos ejecuciones de
t-SNE con semillas distintas producen mapas distintos —los mismos vecinos, otras posiciones— y eso
sorprende a mucha gente que interpreta la primera figura que le sale.

## 5. Matemática mínima

```text
Espacio original:  p_j|i ∝ exp(−‖xᵢ − xⱼ‖² / 2σᵢ²)      gaussiana, σᵢ por perplejidad
Mapa:              q_ij  ∝ (1 + ‖yᵢ − yⱼ‖²)⁻¹           t de Student, 1 grado de libertad

Objetivo:  minimizar  KL(P ‖ Q)  por descenso de gradiente
```

Por qué la cola pesada resuelve el apiñamiento:

| Distancia | Gaussiana | t de Student | Razón |
|---:|---:|---:|---:|
| 1 | 6,07e−01 | 5,00e−01 | 0,82 |
| 2 | 1,35e−01 | 2,00e−01 | 1,48 |
| 4 | 3,35e−04 | 5,88e−02 | 175 |
| 8 | 1,27e−14 | 1,54e−02 | **1,2e+12** |

A distancia 8 la t deja una masa un billón de veces mayor. Y sobre la estabilidad, la miniatura
ejecuta dos veces con semillas distintas:

- vecinos conservados: **0,9556** en ambas;
- desplazamiento medio de los puntos entre las dos: **2,85**.

La vecindad es estable. La posición, no.

<!-- puente:inicio -->
> [!TIP]
> **Puente matemático.** Esta sección da por sabido lo siguiente. Si algo no te suena,
> léelo primero: está explicado una sola vez, en un solo sitio, y sirve para todas las fichas.

| Dónde | Qué necesitas de ahí |
|---|---|
| [**A02 §4** · Divergencia KL](../../annexes/A02_PROBABILIDAD_Y_VEROSIMILITUD.md#4-divergencia-kl) | qué mide KL(P‖Q), por qué no es simétrica y qué penaliza más: separar lo cercano o juntar lo lejano |
<!-- puente:fin -->

## 6. Arquitectura o flujo

```mermaid
flowchart LR
    X["datos en alta dimensión"] --> P["afinidades p_ij<br/>gaussiana + perplejidad"]
    Y["mapa 2D inicial<br/>aleatorio"] --> Q["afinidades q_ij<br/>t de Student"]
    P --> KL["minimizar KL(P‖Q)"]
    Q --> KL
    KL --> G["gradiente sobre las<br/>posiciones del mapa"]
    G --> Y
    style Q fill:#1a3a2a,stroke:#3fb950,color:#f0f6fc
```

## 7. Qué observar en el paper original

- La **justificación de la cola pesada**: es el corazón del artículo y lo que lo separa de SNE.
- El papel de la **perplejidad**: fija cuántos vecinos efectivos considera cada punto. Es el
  hiperparámetro que más cambia el resultado, y el artículo recomienda probar varios valores.
- La **exageración temprana**: multiplicar las afinidades originales durante las primeras
  iteraciones para que los grupos se separen antes de afinar. Es un truco de optimización, no parte
  del modelo.
- La discusión sobre **qué NO preserva**, que está en el artículo y que casi nadie cita.

## 8. Evidencia y resultados

Comparaciones visuales y cuantitativas contra Sammon, Isomap, LLE y SNE sobre conjuntos de
referencia —dígitos manuscritos, caras, documentos— con medidas de preservación de vecindad.

> La evidencia es en buena parte visual, que es lo apropiado para una herramienta de
> visualización, y se complementa con métricas de vecinos conservados.

La miniatura implementa el mecanismo sobre quince puntos con anchura fija en lugar de perplejidad
ajustada por punto. Sirve para exhibir las dos propiedades que importan al leer un mapa —vecindad
estable, posición inestable— no para reproducir el método.

## 9. Impacto

- Se convirtió en la figura por defecto de media década de artículos de aprendizaje automático y
  de biología computacional.
- En genómica de célula única es una herramienta estándar de exploración.
- Su éxito generó también un problema: la sobreinterpretación de mapas. El artículo de Distill
  «How to Use t-SNE Effectively» (2016) existe porque hacía falta.
- **UMAP** (2018) lo desplazó parcialmente por velocidad y por preservar algo mejor la estructura
  global, con los mismos avisos de lectura.

## 10. Limitaciones

1. **La distancia entre grupos no es interpretable.** El objetivo no la restringe.
2. **El tamaño aparente de un grupo tampoco**: depende de la densidad local, no del número de
   puntos.
3. **Depende fuertemente de la perplejidad.** Con valores distintos aparecen estructuras distintas,
   y hay que probar varios antes de concluir nada.
4. **No es determinista.** Dos semillas dan mapas distintos: en la miniatura, un desplazamiento
   medio de 2,85 con los mismos vecinos.
5. **No es una reducción de dimensionalidad para alimentar modelos.** No hay transformación
   aplicable a datos nuevos, y usar sus coordenadas como rasgos es un error frecuente.

## 11. Errores comunes

| Error | Corrección |
|---|---|
| «Estos dos grupos están lejos, luego son muy distintos» | La distancia entre grupos no está restringida por el objetivo. Con otra semilla pueden quedar más cerca. |
| «Este grupo es más grande, luego tiene más elementos» | El tamaño aparente depende de la densidad local en el espacio original, no del número de puntos. |
| «t-SNE reduce dimensionalidad como PCA» | PCA da una transformación lineal aplicable a datos nuevos. t-SNE optimiza posiciones para este conjunto concreto: no hay función que aplicar a un punto nuevo. |
| «El mapa es reproducible» | Depende de la inicialización aleatoria. Los vecinos son estables; las posiciones, no. |
| «Con la perplejidad por defecto basta» | Es el hiperparámetro que más cambia el resultado. El propio artículo recomienda explorar varios valores antes de concluir. |

## 12. Relación con trabajos anteriores

- **Hinton y Roweis (2002)** — SNE: el método anterior, con gaussiana también en el mapa y por
  tanto con el problema del apiñamiento.
- **[P53 PCA](../P53_pca/README.md) (1901)** — la reducción lineal, que sí da una transformación
  aplicable a datos nuevos.
- **[P73 k-medias](../P73_kmeans/README.md) (1982)** — la alternativa que impone grupos en vez de
  mostrarlos.

## 13. Relación con trabajos posteriores

- **Wattenberg, Viégas y Johnson (2016)** — *How to Use t-SNE Effectively*: la guía de lectura que
  hizo falta escribir. [doi:10.23915/distill.00002](https://doi.org/10.23915/distill.00002)
- **McInnes et al. (2018)** — UMAP: más rápido y con mejor estructura global.
  [arXiv:1802.03426](https://arxiv.org/abs/1802.03426)
- **[P05 word2vec](../P05_word2vec/README.md) (2013)** — los espacios de representación que t-SNE
  se usa constantemente para inspeccionar.
- **[P18 CLIP](../P18_clip/README.md) (2021)** — otro espacio de representación cuyo mapa aparece
  en casi todas las presentaciones.

## 14. Notebook asociado

[`P83_tsne.ipynb`](../../../notebooks/papers/P83_tsne.ipynb)

**Qué implementa:** una implementación mínima del gradiente de t-SNE sobre quince puntos, dos ejecuciones con semillas distintas para comparar vecindad y posición, y la tabla de masa de las dos distribuciones a distancias crecientes.

**Qué NO implementa:** no hay perplejidad ajustada por punto, ni exageración temprana, ni aproximación de Barnes-Hut. Con quince puntos se ve el mecanismo, no el comportamiento a escala.

```bash
ai-evolution paper-lab P83 --seed 7
```

## 15. Actividades Bloom

| Nivel | Actividad |
|---|---|
| **Recordar** | Explica en qué consiste el problema del apiñamiento. |
| **Explicar** | Explica por qué una cola pesada en el mapa lo resuelve. |
| **Aplicar** | Ejecuta el notebook y compara las dos ejecuciones. |
| **Analizar** | Analiza qué preserva t-SNE y qué no. |
| **Evaluar** | «Estos dos grupos están lejos en el mapa, luego son muy distintos». Evalúa la afirmación. |
| **Crear** | Aplica t-SNE a datos reales con dos perplejidades y dos semillas, y documenta qué conclusiones sobreviven a los cuatro mapas. |

## 16. Autoevaluación

1. ¿Qué es el problema del apiñamiento?
2. ¿Qué distribución usa t-SNE en el mapa y por qué?
3. ¿Qué preserva t-SNE?
4. ¿Qué NO preserva?
5. ¿Es determinista?
6. ¿Se puede usar para transformar datos nuevos?
7. ¿Qué hiperparámetro es el más importante?

## 17. Respuestas esperadas

1. Que en dimensión alta hay muchísimo más volumen lejos que cerca, y al proyectar a dos dimensiones todos los puntos moderadamente lejanos se apiñan en el centro.
2. Una t de Student con un grado de libertad. Su cola pesada deja mucha más masa a distancias grandes —a distancia 8, del orden de 10¹² veces más que una gaussiana—, lo que permite separar grupos sin comprimir el centro.
3. La **vecindad**: qué puntos están cerca de qué otros. En la miniatura, dos ejecuciones distintas conservan la misma proporción de vecinos.
4. Las distancias entre grupos, el tamaño aparente de los grupos y las posiciones absolutas. Ninguna de las tres cosas está restringida por el objetivo.
5. No. Depende de la inicialización aleatoria: en la miniatura, dos semillas producen un desplazamiento medio de 2,85 con los mismos vecinos.
6. No. No aprende una transformación aplicable: optimiza las posiciones de estos puntos concretos. Usar sus coordenadas como rasgos de un modelo es un error frecuente.
7. La perplejidad, que fija cuántos vecinos efectivos considera cada punto. El propio artículo recomienda explorar varios valores.

## 18. Fuentes primarias

- Van der Maaten, L. y Hinton, G. (2008). *Visualizing Data using t-SNE*. **JMLR**, 9, 2579–2605.
  [JMLR](https://www.jmlr.org/papers/v9/vandermaaten08a.html) · consultado 2026-08-17.
- Wattenberg, M., Viégas, F. y Johnson, I. (2016). *How to Use t-SNE Effectively*.
  [doi:10.23915/distill.00002](https://doi.org/10.23915/distill.00002) · consultado 2026-08-17.
- McInnes, L., Healy, J. y Melville, J. (2018). *UMAP: Uniform Manifold Approximation and
  Projection*. [arXiv:1802.03426](https://arxiv.org/abs/1802.03426) · consultado 2026-08-17.

---

[⬅️ Anterior: P82 Calibración](../P82_calibracion/README.md) ·
[📇 Índice](../../catalog/PAPERS_INDEX.md) ·
[📝 Evaluación](../../../assessments/papers/P83_tsne.md) ·
[🏫 Clase 043 · Clustering y reducción de dimensionalidad](../../../classes/part-03-classical-machine-learning/043-clustering-y-reduccion-de-dimensionalidad/README.md) ·
[➡️ Siguiente: P84 Bosque de aislamiento](../P84_isolation_forest/README.md)
