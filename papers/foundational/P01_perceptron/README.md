# P01 — El perceptrón

> El momento en que una máquina deja de ejecutar reglas escritas por una persona y empieza a
> ajustar sus propios parámetros a partir de ejemplos.

**Nivel:** L1 · **Motor:** `perceptron` · **Notebook:** [`P01_perceptron.ipynb`](../../../notebooks/papers/P01_perceptron.ipynb)
· **Anexo:** [álgebra y geometría](../../annexes/A01_ALGEBRA_Y_GEOMETRIA.md)

## 1. Identificación

| Campo | Valor |
|---|---|
| **Título original** | *The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain* |
| **Autoría** | Frank Rosenblatt |
| **Año** | 1958 |
| **Venue** | *Psychological Review*, 65(6), 386–408 |
| **Fuente primaria** | [doi.org/10.1037/h0042519](https://doi.org/10.1037/h0042519) |
| **Acceso** | Restringido (revista de suscripción) |
| **Fecha de consulta** | 2026-08-16 |

## 2. Problema anterior

En los años 50 un programa hacía exactamente lo que su autor había escrito. McCulloch y Pitts
(1943) habían mostrado que una neurona de umbral podía computar funciones lógicas, pero sus
pesos los fijaba el diseñador: la red no cambiaba con la experiencia. Hebb (1949) había
propuesto que el aprendizaje biológico era plasticidad sináptica, pero como principio, no como
algoritmo.

Faltaba lo del medio: **un procedimiento concreto y ejecutable para que un sistema modifique
su comportamiento observando datos etiquetados**. Sin eso, «aprender» era una metáfora.

## 3. Propuesta

Rosenblatt propone una unidad que:

1. recibe entradas `x`, las pondera con `w` y suma un sesgo `b`;
2. decide con una función escalón: positivo → clase 1, negativo → clase 0;
3. y —la parte nueva— **corrige `w` y `b` solo cuando se equivoca**, empujando el hiperplano
   hacia el ejemplo mal clasificado.

Lo enmarca como modelo probabilístico de almacenamiento de información en el cerebro, no como
herramienta de ingeniería. El Mark I Perceptron lo implementó en hardware con conexiones
ajustables físicamente.

## 4. Intuición sin fórmulas

Imagina puntos de dos colores sobre una hoja y una regla que intenta separarlos. Cada vez que
un punto queda del lado equivocado, empujas la regla un poco hacia él. Si existe alguna
posición de la regla que los separe, este procedimiento la encuentra.

**Dónde deja de funcionar la analogía:** si no existe ninguna recta que los separe, la regla
no se «acerca poco a poco» a una solución aproximada — oscila indefinidamente. No hay
degradación elegante.

## 5. Matemática mínima

```text
z = w · x + b = Σᵢ wᵢxᵢ + b

ŷ = 1  si z ≥ 0
ŷ = 0  si z < 0

Regla de actualización (solo si ŷ ≠ y):
    w ← w + η(y − ŷ)x
    b ← b + η(y − ŷ)
```

- `x ∈ ℝⁿ` entrada · `w ∈ ℝⁿ` pesos · `b ∈ ℝ` sesgo · `η > 0` tasa de aprendizaje.
- `w · x + b = 0` define un **hiperplano**: la frontera de decisión.
- **Teorema de convergencia** (Novikoff, 1962 — posterior al paper): si los datos son
  linealmente separables con margen `γ > 0` y radio `R`, el algoritmo converge en a lo sumo
  `(R/γ)²` correcciones.

<!-- puente:inicio -->
> [!TIP]
> **Puente matemático.** Esta sección da por sabido lo siguiente. Si algo no te suena,
> léelo primero: está explicado una sola vez, en un solo sitio, y sirve para todas las fichas.

| Dónde | Qué necesitas de ahí |
|---|---|
| [**A01 §3** · Hiperplanos y separabilidad](../../annexes/A01_ALGEBRA_Y_GEOMETRIA.md#3-hiperplanos-y-separabilidad) | la regla de aprendizaje mueve un **hiperplano**; sin esa imagen, «ajustar pesos» no significa nada geométrico |
| [**A01 §1** · Producto escalar](../../annexes/A01_ALGEBRA_Y_GEOMETRIA.md#1-producto-escalar) | el producto escalar es lo que decide de qué lado del hiperplano cae un punto |
<!-- puente:fin -->

## 6. Arquitectura o flujo

```text
x₁ ──w₁──┐
x₂ ──w₂──┤
  ⋮      ├──► Σ ──► escalón ──► ŷ
xₙ ──wₙ──┤              │
   b ────┘              │
                        ▼
             ¿ŷ ≠ y?  ──sí──► w ← w + η(y−ŷ)x
                        │
                       no ──► no se toca nada
```

La última línea es la esencia del paper: **sin error no hay aprendizaje**.

## 7. Qué observar en el paper original

- La **motivación biológica**: Rosenblatt escribe para psicólogos, no para ingenieros. El
  vocabulario es de sistemas nerviosos, no de optimización.
- El planteamiento **probabilístico** de la conectividad, hoy poco recordado frente a la
  versión algorítmica simplificada que circula en los manuales.
- La ausencia de: función de pérdida diferenciable, descenso de gradiente y capas ocultas
  entrenables. Ninguna de esas ideas está en este trabajo.

## 8. Evidencia y resultados

El artículo es teórico y conceptual, acompañado del programa experimental del Mark I. La
demostración formal de convergencia para datos separables es **posterior** (Novikoff, 1962;
Block, 1962).

> Verificar en la fuente primaria antes de citar cualquier cifra de desempeño: este eje no
> reproduce números de los experimentos originales de 1958 porque no fueron formulados con el
> protocolo de tarea/dataset/métrica/línea base que hoy se exige.

La miniatura de este eje sí produce evidencia verificable, con otro alcance: AND converge en
6 épocas con 11 correcciones; XOR no converge en 200 épocas.

## 9. Impacto

- Inaugura el **conexionismo** como programa de investigación.
- Es el ancestro directo de toda neurona artificial posterior: la forma `σ(w·x + b)` es la
  misma en un MLP, en una CNN y en la FFN de un Transformer.
- Su límite provocó el primer invierno de las redes neuronales tras el análisis de Minsky y
  Papert (1969) — un impacto negativo que resultó igual de determinante que el positivo.

**Cuidado con la narrativa retrospectiva:** la historia habitual («Minsky mató las redes
neuronales») es una simplificación. El libro de 1969 es un análisis matemático riguroso de
qué puede y qué no puede computar un perceptrón; la interpretación institucional que se hizo
de él es otra cosa.

## 10. Limitaciones

1. **Solo fronteras lineales.** Si las clases no son linealmente separables, no hay solución
   dentro de la clase de hipótesis. XOR es el contraejemplo mínimo.
2. **No degrada con elegancia.** Con datos no separables no converge a una «mejor
   aproximación»: oscila. No devuelve nada útil.
3. **Sin noción de margen.** Cualquier hiperplano que separe le vale; no busca el mejor. Eso
   lo resolverán las SVM tres décadas después.
4. **Sin probabilidades.** La salida es 0 o 1: no expresa confianza.
5. **Sensible a la escala** de las características y al orden de presentación de los ejemplos.
6. **Sin capas ocultas entrenables.** El paper no ofrece forma de entrenar representaciones
   intermedias.

## 11. Errores comunes

| Error | Corrección |
|---|---|
| «El perceptrón usa descenso de gradiente» | Usa una **regla de corrección de error**. La función escalón no es diferenciable. |
| «Minsky y Papert demostraron que las redes neuronales no sirven» | Demostraron límites del **perceptrón de una capa**. El propio libro discute redes multicapa. |
| «El teorema de convergencia está en el paper de 1958» | Es de Novikoff y Block, 1962. |
| «El perceptrón fracasó» | Funcionó exactamente como su teoría predecía. Lo que falló fueron las expectativas construidas sobre él. |
| «No converge porque le faltan épocas» | Con XOR no existe solución que alcanzar. Es un límite de capacidad, no de presupuesto. |

## 12. Relación con trabajos anteriores

- **McCulloch y Pitts (1943)** — neurona de umbral con pesos fijos. Rosenblatt añade el
  aprendizaje.
- **Hebb (1949)** — la plasticidad sináptica como mecanismo de aprendizaje. Rosenblatt la
  convierte en un algoritmo con señal de error supervisada.

## 13. Relación con trabajos posteriores

- **Minsky y Papert (1969)** — *Perceptrons*: formalizan qué no puede computar.
- **Novikoff (1962)** — teorema de convergencia con margen.
- **[P02 Backpropagation](../P02_backpropagation/README.md) (1986)** — resuelve el límite
  entrenando capas ocultas.
- **Vapnik y colaboradores (1992–1995)** — SVM: separadores lineales con margen máximo y
  kernels, otra respuesta al mismo límite.

## 14. Notebook asociado

[`P01_perceptron.ipynb`](../../../notebooks/papers/P01_perceptron.ipynb)

**Qué implementa:** la regla de aprendizaje original en 20 líneas, sobre AND y XOR, con
historial de errores por época.

**Qué NO implementa:** el modelo probabilístico de conectividad del paper, el hardware Mark I,
ni ningún experimento de percepción visual.

```bash
ai-evolution paper-lab P01 --seed 7
```

## 15. Actividades Bloom

| Nivel | Actividad |
|---|---|
| **Recordar** | Escribe la regla de actualización y define cada símbolo sin mirar. |
| **Explicar** | Explica por qué la regla no hace nada cuando la predicción es correcta, y qué consecuencia tiene. |
| **Aplicar** | Ejecuta el perceptrón sobre OR y NAND. Anota épocas hasta converger. |
| **Analizar** | Demuestra algebraicamente que XOR no es linealmente separable (4 desigualdades). |
| **Evaluar** | Un compañero afirma: «con más épocas, XOR converge». Refuta con evidencia experimental **y** con el argumento algebraico. |
| **Crear** | Diseña un conjunto de datos 2D donde el perceptrón converja muy lentamente sin dejar de ser separable, y explica qué propiedad geométrica lo provoca. |

## 16. Autoevaluación

1. ¿Por qué la función escalón impide usar descenso de gradiente?
2. Con `w = (0,0)`, `b = 0` y `η = 1`, ejecuta a mano dos épocas de AND. ¿Qué valores obtienes?
3. ¿Qué garantiza exactamente el teorema de convergencia, y bajo qué condición?
4. ¿Qué le ocurre a la cota `(R/γ)²` cuando el margen `γ` tiende a cero? ¿Qué significa eso en la práctica?
5. Si añades la característica `x₃ = x₁·x₂` a XOR, ¿se vuelve separable? ¿Qué te dice eso sobre la relación entre representación y separabilidad?
6. Nombra dos límites del perceptrón que **no** sean «no resuelve XOR».
7. ¿Qué idea que hoy se asocia al perceptrón apareció en realidad después de 1958?

## 17. Respuestas esperadas

1. La derivada del escalón es 0 en todas partes salvo en el salto, donde no existe. Sin
   gradiente informativo, no hay dirección de descenso.
2. Debe llegar a valores intermedios y converger hacia `w = (2,1)`, `b = −3` alrededor de la
   sexta época. Lo evaluable es el **procedimiento** paso a paso, no el número final.
3. Que si existe un hiperplano separador con margen `γ > 0`, el algoritmo hace un número
   **finito** de correcciones, acotado por `(R/γ)²`. No garantiza nada si no hay separabilidad.
4. La cota diverge. Datos casi colineales o casi solapados pueden necesitar un número enorme
   de correcciones aun siendo técnicamente separables: la garantía existe pero es inútil.
5. Sí. Muestra que la separabilidad no es propiedad de los datos sino del **espacio de
   representación**. Es la idea que fundamenta tanto los kernels como las capas ocultas.
6. Se aceptan: ausencia de margen máximo, salida no probabilística, no degradación elegante,
   sensibilidad a la escala, dependencia del orden de presentación.
7. El teorema de convergencia (1962), el descenso de gradiente sobre pérdidas diferenciables,
   la idea de margen máximo y cualquier mención a capas ocultas entrenables.

## 18. Fuentes primarias

- Rosenblatt, F. (1958). *The Perceptron: A Probabilistic Model for Information Storage and
  Organization in the Brain*. **Psychological Review**, 65(6), 386–408.
  [doi.org/10.1037/h0042519](https://doi.org/10.1037/h0042519) · consultado 2026-08-16.
- Minsky, M. y Papert, S. (1969). *Perceptrons*. MIT Press.
  [ficha del editor](https://mitpress.mit.edu/9780262534772/perceptrons/) · consultado 2026-08-16.
- McCulloch, W. y Pitts, W. (1943). *A Logical Calculus of the Ideas Immanent in Nervous
  Activity*. **Bulletin of Mathematical Biophysics**, 5, 115–133.
  [doi.org/10.1007/BF02478259](https://doi.org/10.1007/BF02478259) · consultado 2026-08-16.

---

[⬅️ Índice de papers](../../catalog/PAPERS_INDEX.md) ·
[🗺️ Ruta](../../ROADMAP.md) ·
[📝 Evaluación](../../../assessments/papers/P01_perceptron.md) ·
[🏫 Clase 049 del programa](../../../classes/part-04-neural-networks-and-deep-learning/049-perceptron-y-limites-de-separabilidad/README.md) ·
[➡️ Siguiente: P02 Backpropagation](../P02_backpropagation/README.md)
