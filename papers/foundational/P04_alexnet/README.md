# P04 — AlexNet

> El resultado que sacó al deep learning del laboratorio: no una idea nueva, sino la
> combinación que demostró que las ideas viejas escalaban.

**Nivel:** L3 · **Motor:** `convnet` · **Notebook:** [`P04_alexnet.ipynb`](../../../notebooks/papers/P04_alexnet.ipynb)
· **Anexo:** [álgebra y geometría](../../annexes/A01_ALGEBRA_Y_GEOMETRIA.md)

## 1. Identificación

| Campo | Valor |
|---|---|
| **Título original** | *ImageNet Classification with Deep Convolutional Neural Networks* |
| **Autoría** | Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton |
| **Año** | 2012 |
| **Venue** | NeurIPS (entonces NIPS) 2012 |
| **Fuente primaria** | [papers.nips.cc — actas de 2012](https://papers.nips.cc/paper_files/paper/2012) · [versión CACM 2017](https://doi.org/10.1145/3065386) |
| **Acceso** | Abierto |
| **Fecha de consulta** | 2026-08-16 |

## 2. Problema anterior

Hasta 2012, la visión por computador se hacía con **descriptores diseñados a mano** (SIFT,
HOG) seguidos de un clasificador. Un humano decidía qué características eran relevantes; el
aprendizaje solo ocurría en la última etapa.

Las CNN existían desde LeNet (LeCun et al., 1998) y funcionaban en dígitos manuscritos, pero
la comunidad dudaba de que escalaran a imágenes naturales de mil categorías. Faltaban tres
cosas a la vez: **datos** (ImageNet llegó en 2009), **cómputo** (las GPU programables) y
**técnicas de entrenamiento** que evitaran que una red profunda se estancara o memorizara.

## 3. Propuesta

Una CNN profunda —5 capas convolucionales y 3 completamente conectadas— entrenada
directamente sobre ImageNet, combinando:

- **ReLU** en lugar de sigmoide o tanh: no satura para valores positivos y acelera mucho el
  entrenamiento;
- **entrenamiento en dos GPU** con la red repartida entre ambas, por límite de memoria;
- **dropout** en las capas densas, para reducir el sobreajuste;
- **aumento de datos** (recortes, reflejos, alteración de color);
- **pooling solapado** y normalización de respuesta local.

Ninguna pieza es enteramente nueva. La contribución es la **combinación funcionando a escala**
y el resultado que la respaldó.

## 4. Intuición sin fórmulas

Un detector de bordes no debería reaprenderse en cada esquina de la imagen. La convolución
desliza el mismo detector por toda la imagen: muchos menos parámetros y, sobre todo, la
posición del objeto deja de importar. Apilando capas, los detectores simples (bordes) se
componen en detectores complejos (texturas, partes, objetos).

**Dónde deja de funcionar la analogía:** un kernel no «reconoce» nada por sí solo. Lo que
existe es un patrón de activación distribuido en muchos filtros; la interpretación limpia de
«esta neurona detecta caras» es casi siempre una simplificación.

## 5. Matemática mínima

```text
Convolución (correlación cruzada):
    (I * K)[r, c] = Σᵢ Σⱼ I[r+i, c+j] · K[i, j]

Activación:
    ReLU(z) = max(0, z)          ReLU'(z) = 1 si z > 0, 0 si z < 0

Max-pooling:
    P[r, c] = max de la ventana correspondiente

Dropout (entrenamiento):
    h̃ = h ⊙ m,  m ~ Bernoulli(p)
```

**Recuento de parámetros.** Una capa densa que conecte una entrada de `H×W` con una salida de
`H'×W'` necesita `H·W·H'·W'` pesos. Un kernel `k×k` necesita `k²`, reutilizados en toda la
imagen. Esa reducción es lo que hace viable la profundidad.

<!-- puente:inicio -->
> [!TIP]
> **Puente matemático.** Esta sección da por sabido lo siguiente. Si algo no te suena,
> léelo primero: está explicado una sola vez, en un solo sitio, y sirve para todas las fichas.

| Dónde | Qué necesitas de ahí |
|---|---|
| [**A01 §4** · Matrices como transformaciones](../../annexes/A01_ALGEBRA_Y_GEOMETRIA.md#4-matrices-como-transformaciones) | una convolución es una transformación lineal con pesos compartidos |
| [**A05 §3** · La cuenta que decide el hardware: memoria](../../annexes/A05_COMPLEJIDAD_Y_COSTE.md#3-la-cuenta-que-decide-el-hardware-memoria) | la cuenta de memoria que obligó a partir la red en dos GPU |
<!-- puente:fin -->

## 6. Arquitectura o flujo

```text
imagen 224×224×3
   │
   ├─ conv1 ─► ReLU ─► norm ─► maxpool
   ├─ conv2 ─► ReLU ─► norm ─► maxpool
   ├─ conv3 ─► ReLU
   ├─ conv4 ─► ReLU
   ├─ conv5 ─► ReLU ─► maxpool
   │
   ├─ fc6 ─► ReLU ─► dropout
   ├─ fc7 ─► ReLU ─► dropout
   └─ fc8 ─► softmax (1000 categorías)

Repartida entre 2 GPU, con comunicación solo en capas concretas.
```

## 7. Qué observar en el paper original

- La **figura de la arquitectura** con la red partida en dos flujos: es una restricción de
  hardware convertida en decisión de diseño.
- La sección de **ReLU**: la comparación de velocidad de convergencia frente a tanh es uno de
  los argumentos más citados del artículo.
- La **visualización de los filtros de la primera capa**: bordes orientados y manchas de
  color, sin que nadie los programara.
- La **sección de reducción de sobreajuste**: aumento de datos y dropout.
- La tabla de resultados de ILSVRC-2012 con el error top-1 y top-5, y el margen respecto al
  segundo clasificado.

## 8. Evidencia y resultados

El sistema ganó el certamen ILSVRC-2012 de clasificación con un **error top-5 en torno al
15 %, frente a alrededor del 26 % del siguiente participante** — un margen inusual en una
competición donde las mejoras anuales eran de uno o dos puntos.

> Los valores exactos de top-1 y top-5, para el modelo individual y para el conjunto, están en
> la tabla de resultados del artículo. Verificarlos ahí antes de citarlos: circulan versiones
> distintas según se refieran al modelo único, al *ensemble* o al conjunto de validación.

El paper incluye **ablaciones** que muestran cuánto pierde el modelo al quitar capas
convolucionales, y experimentos de recuperación por vecinos en el espacio de la penúltima
capa.

## 9. Impacto

- Cambió el método por defecto de la visión por computador en menos de dos años.
- Consolidó la **GPU** como plataforma estándar de entrenamiento.
- Popularizó ReLU y dropout, que pasaron a ser configuración por defecto.
- Estableció la práctica de **preentrenar en un dominio grande y transferir** a tareas con
  pocos datos.
- Fuera del campo, es el resultado que convirtió el deep learning en tema de portada y
  desencadenó el ciclo de inversión posterior.

## 10. Limitaciones

1. **Coste de cómputo y datos.** El resultado depende de ImageNet y de GPU: no es reproducible
   con un dataset pequeño.
2. **Sensible a la traslación, no a la rotación ni a la escala.** La equivarianza es solo
   traslacional; el resto se aproxima con aumento de datos.
3. **Frágil ante perturbaciones adversarias**, como mostró trabajo posterior
   (Szegedy et al., 2013; Goodfellow et al., 2014).
4. **Poco interpretable** más allá de la primera capa.
5. **Sesgo del dataset.** Lo que la red «sabe» está determinado por qué contiene ImageNet y
   cómo se etiquetó; esa discusión llegó años después.
6. **La normalización de respuesta local** que propone acabó abandonada: trabajos posteriores
   mostraron que aporta poco frente a la normalización por lotes.

## 11. Errores comunes

| Error | Corrección |
|---|---|
| «AlexNet inventó las CNN» | LeNet es de 1998; la convolución con retropropagación es anterior. AlexNet demostró que **escalaban**. |
| «AlexNet inventó ReLU y dropout» | Ambas son anteriores o contemporáneas (Nair y Hinton, 2010; Hinton et al., 2012). AlexNet las combinó y las popularizó. |
| «Ganó porque era más profunda» | Ganó por la combinación de profundidad, datos, GPU, ReLU, dropout y aumento de datos. La ablación del propio paper lo respalda. |
| «Las CNN son mejores que los métodos clásicos» | Afirmación vacía sin tarea, dataset, métrica y línea base. |
| «El 15 % de error significa que entiende las imágenes» | Significa que acierta una métrica en un conjunto concreto. Nada más. |

## 12. Relación con trabajos anteriores

- **[P02 Backpropagation](../P02_backpropagation/README.md) (1986)** — el método de entrenamiento.
- **LeCun et al. (1998)** — LeNet: convolución, pooling y retropropagación.
- **Deng et al. (2009)** — ImageNet, el dataset sin el cual no hay resultado.
- **Nair y Hinton (2010)** — unidades rectificadas.
- **Hinton et al. (2012)** — dropout. [arXiv:1207.0580](https://arxiv.org/abs/1207.0580)

## 13. Relación con trabajos posteriores

- **VGG (2014), GoogLeNet (2014), ResNet (2015)** — la carrera de profundidad que AlexNet abrió.
  ResNet resuelve el problema de entrenar cientos de capas con conexiones residuales, el mismo
  principio aditivo de [P03](../P03_lstm/README.md).
- **Szegedy et al. (2013)** — ejemplos adversarios: el reverso del éxito.
- **[P08 Transformer](../P08_transformer/README.md) (2017)** y **ViT (2020)** — el fin del
  monopolio convolucional en visión.
- **Russakovsky et al. (2015)** — análisis del certamen ILSVRC.
  [arXiv:1409.0575](https://arxiv.org/abs/1409.0575)

## 14. Notebook asociado

[`P04_alexnet.ipynb`](../../../notebooks/papers/P04_alexnet.ipynb)

**Qué implementa:** convolución 2D con kernels de borde escritos a mano, ReLU, max-pooling,
demostración de equivarianza traslacional y comparación de recuento de parámetros frente a una
capa densa equivalente.

**Qué NO implementa:** ningún entrenamiento, ninguna GPU, ningún dato de ImageNet. Los kernels
están escritos, no aprendidos — que es justamente lo contrario de lo que hizo AlexNet.

```bash
ai-evolution paper-lab P04 --seed 7
```

## 15. Actividades Bloom

| Nivel | Actividad |
|---|---|
| **Recordar** | Enumera las cinco técnicas que AlexNet combinó y di cuál es anterior al paper. |
| **Explicar** | Explica por qué ReLU acelera el entrenamiento frente a tanh, en términos de derivada. |
| **Aplicar** | Aplica un kernel horizontal a la imagen del notebook y explica por qué no responde. |
| **Analizar** | Calcula el número de parámetros de una convolución `3×3×64→128` y compáralo con la densa equivalente sobre un mapa `56×56`. |
| **Evaluar** | Un informe afirma «nuestra CNN alcanza 94 % de exactitud». Escribe las cinco preguntas que debes hacer antes de aceptarlo. |
| **Crear** | Diseña un experimento que separe la contribución de ReLU de la del aumento de datos, y di qué necesitarías para ejecutarlo. |

## 16. Autoevaluación

1. ¿Qué significa que la convolución sea *equivariante* a la traslación, y en qué se diferencia
   de ser *invariante*?
2. ¿Por qué compartir pesos reduce el sobreajuste además del cómputo?
3. ¿Qué hace exactamente el dropout durante el entrenamiento, y qué se hace en inferencia?
4. ¿Por qué la red se partió entre dos GPU?
5. ¿Qué componente del paper original acabó siendo abandonado por la comunidad?
6. ¿Por qué un resultado en ILSVRC-2012 no autoriza a afirmar nada sobre «visión» en general?
7. Nombra dos ideas anteriores a 2012 sin las cuales AlexNet no existiría.

## 17. Respuestas esperadas

1. Equivariante: si la entrada se desplaza, el mapa de activación se desplaza igual.
   Invariante: la salida no cambia. El pooling añade invarianza **local**; la convolución sola
   es equivariante.
2. Porque impone una restricción estructural: el mismo detector se aplica en todas las
   posiciones. Menos grados de libertad con la misma capacidad de detección.
3. Desactiva unidades al azar con probabilidad `p`, forzando representaciones redundantes. En
   inferencia se usan todas, con la escala correspondiente para mantener la magnitud esperada.
4. Por límite de memoria de las GPU de la época (3 GB). Es una restricción de hardware, no una
   decisión conceptual.
5. La normalización de respuesta local (LRN).
6. Porque la métrica está definida sobre un dataset concreto, con sus categorías, su
   distribución y sus sesgos. Generalizar a «visión» es un salto sin evidencia.
7. Se aceptan: retropropagación (1986), LeNet (1998), ImageNet (2009), ReLU (2010), dropout
   (2012), CUDA/GPU programables.

## 18. Fuentes primarias

- Krizhevsky, A., Sutskever, I. y Hinton, G. E. (2012). *ImageNet Classification with Deep
  Convolutional Neural Networks*. **NeurIPS 2012**.
  [actas](https://papers.nips.cc/paper_files/paper/2012) · consultado 2026-08-16.
- Krizhevsky, A., Sutskever, I. y Hinton, G. E. (2017). Versión revisada en
  **Communications of the ACM**, 60(6), 84–90.
  [doi.org/10.1145/3065386](https://doi.org/10.1145/3065386) · consultado 2026-08-16.
- Russakovsky, O. et al. (2015). *ImageNet Large Scale Visual Recognition Challenge*.
  [arXiv:1409.0575](https://arxiv.org/abs/1409.0575) · consultado 2026-08-16.

---

[⬅️ Anterior: P03 LSTM](../P03_lstm/README.md) ·
[📇 Índice](../../catalog/PAPERS_INDEX.md) ·
[📝 Evaluación](../../../assessments/papers/P04_alexnet.md) ·
[🏫 Clase 053 del programa](../../../classes/part-04-neural-networks-and-deep-learning/053-cnn-y-aprendizaje-espacial/README.md) ·
[➡️ Siguiente: P05 Word2Vec](../P05_word2vec/README.md)
