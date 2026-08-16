# P02 — Backpropagation

> El procedimiento que hizo entrenables las capas ocultas: la red deja de recibir las
> representaciones y empieza a descubrirlas.

**Nivel:** L2 · **Motor:** `backprop` · **Notebook:** [`P02_backpropagation.ipynb`](../../../notebooks/papers/P02_backpropagation.ipynb)

## 1. Identificación

| Campo | Valor |
|---|---|
| **Título original** | *Learning representations by back-propagating errors* |
| **Autoría** | David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams |
| **Año** | 1986 |
| **Venue** | *Nature*, 323, 533–536 |
| **Fuente primaria** | [doi.org/10.1038/323533a0](https://doi.org/10.1038/323533a0) |
| **Acceso** | Restringido (revista de suscripción) |
| **Fecha de consulta** | 2026-08-16 |

## 2. Problema anterior

El [perceptrón](../P01_perceptron/README.md) solo traza fronteras lineales. La solución
evidente —apilar capas— chocaba con un obstáculo práctico: **¿cuánta culpa del error final
tiene un peso de la capa intermedia?** Ese peso no está conectado directamente con la salida;
su efecto pasa por todas las unidades que vienen después.

Se le llamó el *credit assignment problem*. Sin resolverlo, las capas ocultas eran una idea
sin algoritmo: se podían dibujar, no entrenar.

## 3. Propuesta

Aplicar la **regla de la cadena** recorriendo la red hacia atrás:

1. propagación hacia adelante: se calcula la salida y la pérdida;
2. propagación hacia atrás: el error de cada capa se expresa en función del error de la
   siguiente, multiplicando por los pesos y por la derivada de la activación;
3. actualización: cada peso se mueve en la dirección opuesta a su gradiente.

La aportación decisiva del artículo no es la fórmula —ya existía en otras formulaciones— sino
**mostrar que funciona en la práctica y que las unidades ocultas aprenden representaciones
internas útiles y no diseñadas por nadie**. El título lo dice: *learning representations*.

## 4. Intuición sin fórmulas

Una cadena de montaje produce una pieza defectuosa. El responsable de calidad no reparte la
culpa al azar: retrocede puesto por puesto preguntando «¿cuánto habría cambiado el defecto si
tú hubieras hecho tu parte un poco distinta?». Cada puesto recibe una responsabilidad
proporcional a su influencia real.

**Dónde deja de funcionar la analogía:** la cadena de montaje tiene un número fijo de puestos
con influencia comparable. En una red profunda, la influencia se multiplica en cada paso, y
ese producto puede colapsar a cero o dispararse — el problema que P03 tendrá que atacar.

## 5. Matemática mínima

Red `x → h = σ(W₁x + b₁) → o = σ(W₂h + b₂)`, pérdida `L = (o − y)²`, con `σ(z) = 1/(1+e⁻ᶻ)`
y `σ'(z) = σ(z)(1 − σ(z))`:

```text
δ_o = ∂L/∂o_in = 2(o − y) · σ'(o_in)

∂L/∂W₂ = δ_o · hᵀ
∂L/∂b₂ = δ_o

δ_h = (W₂ᵀ δ_o) ⊙ σ'(h_in)          ← el error "viaja" hacia atrás

∂L/∂W₁ = δ_h · xᵀ
∂L/∂b₁ = δ_h

Actualización:  θ ← θ − η · ∂L/∂θ
```

El único ingrediente nuevo respecto al cálculo elemental es el orden: computar `δ` de atrás
hacia adelante evita recalcular derivadas repetidas. Eso es lo que lo hace viable.

## 6. Arquitectura o flujo

```text
   ADELANTE  ────────────────────────────────────►
   x ──► [W₁,b₁] ──► h ──► [W₂,b₂] ──► o ──► L(o,y)

   ◄──────────────────────────────────  ATRÁS
       δ_h  ◄── W₂ᵀ·δ_o ⊙ σ'(h_in) ◄── δ_o
        │                                │
        ▼                                ▼
   ∂L/∂W₁                            ∂L/∂W₂
```

## 7. Qué observar en el paper original

- El artículo de *Nature* es **muy breve** (4 páginas). La formulación extendida está en el
  capítulo 8 de *Parallel Distributed Processing* (Rumelhart, Hinton y Williams, 1986).
- El experimento de las **representaciones internas**: la red descubre codificaciones en las
  unidades ocultas que corresponden a regularidades del dominio (por ejemplo, simetría o
  relaciones familiares) sin que se las especifique.
- Lo que **no** aparece: ReLU, dropout, normalización por lotes, Adam, inicialización
  cuidadosa, GPU. Todo eso es posterior y es lo que hizo escalar el método décadas después.

## 8. Evidencia y resultados

El paper demuestra, con problemas pequeños, que una red multicapa entrenada así:

- resuelve tareas no linealmente separables;
- **desarrolla representaciones internas interpretables** en las unidades ocultas.

> Los problemas del artículo son de juguete para los estándares actuales; su valor es de
> **existencia** («esto se puede entrenar»), no de escala. Verificar las figuras concretas en
> la fuente primaria antes de citar cualquier resultado numérico.

La miniatura de este eje produce evidencia complementaria y verificable: XOR resuelto con 9
parámetros, y comprobación numérica del gradiente con error `≈1e-8`.

## 9. Impacto

- Desbloquea las redes multicapa y cierra el invierno abierto por el análisis de 1969.
- Es el algoritmo que **sigue entrenando todo hoy**: cada modelo del resto de esta ruta —
  LSTM, AlexNet, Transformer, GPT — se entrena con retropropagación.
- Establece la idea de *representación aprendida*, que es el concepto central del deep
  learning y da nombre a una conferencia entera (ICLR).

## 10. Limitaciones

1. **Gradiente desvaneciente o explosivo.** Al encadenar muchas capas, el producto de
   derivadas colapsa o diverge. El paper no lo aborda; será el tema de P03.
2. **Óptimos locales y mesetas.** No hay garantía de convergencia al mínimo global.
3. **Coste de memoria.** Hay que guardar las activaciones de la pasada hacia adelante.
4. **Sensibilidad a la inicialización y a la tasa de aprendizaje.** Con sigmoides y pesos mal
   escalados, el entrenamiento se estanca en la zona de saturación.
5. **Poca plausibilidad biológica.** El cerebro no dispone de un canal simétrico que
   transporte el error hacia atrás con los mismos pesos (*weight transport problem*).
6. **Requiere activaciones diferenciables**, lo que excluye la función escalón de P01.

## 11. Errores comunes

| Error | Corrección |
|---|---|
| «Rumelhart, Hinton y Williams inventaron la retropropagación» | La **popularizaron para redes neuronales**. La diferenciación en modo reverso es anterior: Linnainmaa (1970), Werbos (1974). El propio artículo reconoce trabajo previo. |
| «Backpropagation es un algoritmo de optimización» | Es un algoritmo para **calcular gradientes**. Quien optimiza es SGD, Adam u otro. |
| «Backprop garantiza encontrar la mejor solución» | Encuentra un punto donde el gradiente se anula, no el óptimo global. |
| «El paper usa ReLU» | No. Usa sigmoides. ReLU se generaliza a partir de 2010–2012. |
| «Basta con más capas» | Sin las técnicas posteriores (inicialización, normalización, residuales), más capas empeoran el entrenamiento. |

## 12. Relación con trabajos anteriores

- **[P01 Perceptrón](../P01_perceptron/README.md) (1958)** — el límite lineal que motiva todo.
- **Linnainmaa (1970)** — diferenciación automática en modo reverso.
  [doi.org/10.1007/BF01931367](https://doi.org/10.1007/BF01931367)
- **Werbos (1974)** — tesis doctoral que aplica la idea a modelos de ciencias sociales.
- **Minsky y Papert (1969)** — el análisis que definió el problema a superar.

## 13. Relación con trabajos posteriores

- **[P03 LSTM](../P03_lstm/README.md) (1997)** — ataca el gradiente desvaneciente en secuencias.
- **[P04 AlexNet](../P04_alexnet/README.md) (2012)** — demuestra que el método escala con GPU,
  ReLU, dropout y datos masivos.
- **Glorot y Bengio (2010), He et al. (2015)** — inicialización que evita la saturación.
- **Autograd moderno** (Theano, TensorFlow, PyTorch, JAX) — la generalización del método a
  grafos de cómputo arbitrarios.

## 14. Notebook asociado

[`P02_backpropagation.ipynb`](../../../notebooks/papers/P02_backpropagation.ipynb)

**Qué implementa:** una red 2-2-1 con sigmoides entrenada sobre XOR, con gradientes derivados
**a mano** (sin autograd) y verificación numérica del gradiente.

**Qué NO implementa:** el experimento de representaciones internas del paper, ni ninguna red
de tamaño realista.

```bash
ai-evolution paper-lab P02 --seed 7
```

## 15. Actividades Bloom

| Nivel | Actividad |
|---|---|
| **Recordar** | Escribe la expresión de `δ_h` en función de `δ_o` y explica cada factor. |
| **Explicar** | Explica por qué se calcula `δ` de atrás hacia adelante y no al revés. |
| **Aplicar** | Cambia la sigmoide por `tanh` en el notebook y ajusta la derivada correspondiente. |
| **Analizar** | Calcula el producto de derivadas de sigmoide en 10 capas suponiendo `σ' ≈ 0,25`. ¿Qué queda del gradiente? |
| **Evaluar** | Un modelo entrena y la pérdida baja, pero la verificación numérica del gradiente da `1e-2` de diferencia. ¿Confías en el entrenamiento? Justifica. |
| **Crear** | Implementa la comprobación de gradiente como una función reutilizable que reciba cualquier red y devuelva el error relativo máximo. |

## 16. Autoevaluación

1. ¿Por qué la retropropagación es eficiente frente a calcular cada derivada parcial por separado?
2. ¿Qué papel juega `σ'(h_in)` en la propagación del error hacia atrás?
3. ¿Por qué `σ' ≤ 0,25` es una mala noticia en redes profundas?
4. ¿Qué diferencia hay entre backpropagation y descenso de gradiente estocástico?
5. ¿Por qué la verificación numérica del gradiente usa diferencia centrada y no hacia adelante?
6. ¿Qué ocurre si inicializas todos los pesos a cero? ¿Y todos al mismo valor no nulo?
7. ¿Qué idea del deep learning moderno **no** está en este paper y suele atribuírsele?

## 17. Respuestas esperadas

1. Porque reutiliza los `δ` ya calculados: el coste es proporcional al de una pasada hacia
   adelante, en lugar de una evaluación por parámetro.
2. Mide la sensibilidad local de la unidad. Si la neurona está saturada, `σ' ≈ 0` y el error
   deja de propagarse por esa ruta.
3. Porque los factores se multiplican: `0,25¹⁰ ≈ 1e-6`. Las capas iniciales reciben una señal
   despreciable y dejan de aprender.
4. Backprop **calcula** el gradiente; SGD **usa** ese gradiente para actualizar. Son piezas
   distintas y se pueden sustituir por separado.
5. Porque su error es `O(ε²)` frente a `O(ε)` de la diferencia hacia adelante: da varios
   dígitos más de precisión con el mismo número de evaluaciones.
6. Con todos a cero (o todos iguales), todas las unidades ocultas reciben el mismo gradiente y
   permanecen idénticas para siempre: la simetría no se rompe y la capa oculta es inútil.
7. ReLU, dropout, normalización por lotes, Adam, conexiones residuales, GPU. Todo posterior.

## 18. Fuentes primarias

- Rumelhart, D. E., Hinton, G. E. y Williams, R. J. (1986). *Learning representations by
  back-propagating errors*. **Nature**, 323, 533–536.
  [doi.org/10.1038/323533a0](https://doi.org/10.1038/323533a0) · consultado 2026-08-16.
- Linnainmaa, S. (1976). *Taylor expansion of the accumulated rounding error*. **BIT
  Numerical Mathematics**, 16, 146–160.
  [doi.org/10.1007/BF01931367](https://doi.org/10.1007/BF01931367) · consultado 2026-08-16.
- Werbos, P. (1974). *Beyond Regression: New Tools for Prediction and Analysis in the
  Behavioral Sciences*. Tesis doctoral, Universidad de Harvard.

---

[⬅️ Anterior: P01 Perceptrón](../P01_perceptron/README.md) ·
[📇 Índice](../../catalog/PAPERS_INDEX.md) ·
[📝 Evaluación](../../../assessments/papers/P02_backpropagation.md) ·
[🏫 Clase 050 del programa](../../../classes/part-04-neural-networks-and-deep-learning/050-mlp-y-backpropagation/README.md) ·
[➡️ Siguiente: P03 LSTM](../P03_lstm/README.md)
