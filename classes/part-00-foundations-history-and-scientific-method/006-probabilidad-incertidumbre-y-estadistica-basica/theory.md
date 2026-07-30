
# Teoría — Probabilidad, incertidumbre y estadística básica

## 🗺️ Ubicación en el mapa de la IA

La probabilidad es el cálculo de la incertidumbre, y la IA opera casi siempre bajo
incertidumbre: sensores ruidosos, datos incompletos, mundos parcialmente observables. El
giro probabilístico de los años 90 (redes bayesianas, métodos estadísticos) sacó al campo
de su segundo invierno, y hoy todo clasificador emite probabilidades y todo LLM es,
literalmente, una distribución de probabilidad sobre el siguiente token. Esta clase da el
mínimo necesario para las partes de machine learning y para leer métricas con honestidad.

## 📖 Fundamentos

### 🎲 Axiomas y vocabulario

Una probabilidad asigna a cada evento A un número P(A) que cumple (Kolmogórov):

```text
1. P(A) ≥ 0
2. P(Ω) = 1              (algo del espacio muestral ocurre)
3. P(A ∪ B) = P(A) + P(B)   si A y B son disjuntos
```

De ahí: P(¬A) = 1 − P(A), y la **regla de la suma general**
P(A∪B) = P(A) + P(B) − P(A∩B). Dos lecturas filosóficas conviven: frecuentista
(límite de frecuencias relativas) y bayesiana (grado de creencia coherente); en la práctica
de IA se usan ambas según convenga al problema.

### 🔗 Probabilidad condicional e independencia

```text
P(A|B) = P(A∩B) / P(B)          (probabilidad de A sabiendo que ocurrió B)
regla del producto:  P(A∩B) = P(A|B) P(B)
independencia:       P(A∩B) = P(A) P(B)   ⇔   P(A|B) = P(A)
```

Condicionar es *actualizar el universo*: al saber B, el espacio muestral se reduce a B.
La independencia es un supuesto de modelado, no un hecho por defecto: asumirla donde no
existe (p. ej., entre features correlacionadas) es una fuente clásica de modelos
sobreconfiados.

### 🔄 Teorema de Bayes

```text
P(H|E) = P(E|H) · P(H) / P(E)

posterior = verosimilitud × prior / evidencia
```

Bayes invierte la dirección del condicional: de "probabilidad de la evidencia dada la
hipótesis" (que el modelo o el test médico conocen) a "probabilidad de la hipótesis dada la
evidencia" (que es lo que uno quiere). P(E) se expande por probabilidad total:
`P(E) = P(E|H)P(H) + P(E|¬H)P(¬H)`. Es el fundamento de los clasificadores naive Bayes,
del filtrado de spam, de la inferencia en redes bayesianas y del razonamiento diagnóstico.

### 📊 Variables aleatorias, esperanza y varianza

Una variable aleatoria X asigna números a resultados. Sus resúmenes centrales:

```text
esperanza:  E[X] = Σ x · P(X=x)          (media ponderada por probabilidad)
varianza:   Var(X) = E[(X − E[X])²]      (dispersión alrededor de la media)
desviación estándar: σ = √Var(X)
```

Distribuciones que hay que reconocer: **Bernoulli** (un ensayo sí/no), **binomial** (número
de éxitos en n ensayos), **uniforme**, **normal/gaussiana** (suma de muchos efectos
pequeños independientes — teorema central del límite). La **ley de los grandes números**
garantiza que el promedio muestral converge a E[X]: es la licencia matemática para estimar
probabilidades simulando (método Monte Carlo), que es exactamente lo que hace el laboratorio
de esta clase con una semilla fija.

### ⚠️ Estadística mínima para leer resultados

- Un **estimador** calculado sobre una muestra tiene **error muestral**: reportar una
  métrica sin tamaño de muestra ni intervalo es reportar ruido potencial.
- **Correlación no es causalidad:** dos variables pueden covariar por una causa común o
  por azar (con suficientes comparaciones, el azar *garantiza* correlaciones espurias).
- La media es sensible a outliers; la mediana no. Elegir el resumen según la distribución.

## 🧮 Ejemplo trabajado

El clásico problema del test diagnóstico, que casi todo el mundo responde mal la primera vez.
Una enfermedad afecta al 1 % de la población. El test detecta al 90 % de los enfermos
(sensibilidad) y da falso positivo en el 9 % de los sanos. Si una persona da positivo,
¿cuál es la probabilidad de que esté enferma?

Con 10 000 personas, en números enteros:

```text
Enfermos:  100   → positivos verdaderos: 100 × 0.90 =  90
Sanos:    9900   → falsos positivos:    9900 × 0.09 = 891

P(enfermo | positivo) = 90 / (90 + 891) = 90/981 ≈ 0.092  →  ~9 %
```

Por Bayes directamente: P(H|E) = (0.90 · 0.01) / (0.90·0.01 + 0.09·0.99)
= 0.009/0.0981 ≈ **0.092**. La intuición dice "90 %"; la respuesta correcta es ~9 %,
porque el **prior** (1 %) domina: hay muchos más sanos que pueden dar falso positivo que
enfermos que den verdadero positivo. Moraleja directa para IA: un clasificador "90 %
preciso" sobre una clase rara produce mayoritariamente falsas alarmas — por eso exigimos
precisión/recall y no solo accuracy.

## 📊 Propiedades y comparación

| Concepto | Qué responde | Trampa típica |
|---|---|---|
| P(A) | Frecuencia/creencia marginal | Ignorar que depende de la población de referencia |
| P(A\|B) | Creencia actualizada por evidencia | Confundir P(A\|B) con P(B\|A) (falacia del fiscal) |
| Bayes | Invierte el condicional con el prior | Omitir el prior (ignorar la tasa base) |
| E[X] | Valor promedio a largo plazo | Usarla con distribuciones sin media estable o con outliers |
| Var(X) | Dispersión esperada | Reportar medias sin dispersión ni n |
| Monte Carlo | Estima E[X] simulando | Olvidar la semilla → resultados irreproducibles |

```mermaid
flowchart TD
    PRIOR["Prior P(H)<br/>tasa base: 1% enfermos"] --> BAYES["Teorema de Bayes<br/>P(H|E) = P(E|H)·P(H) / P(E)"]
    LIKE["Verosimilitud P(E|H)<br/>sensibilidad del test: 90%"] --> BAYES
    FP["P(E|¬H)<br/>tasa de falsos positivos: 9%"] --> EV["Evidencia P(E)<br/>= 0.9·0.01 + 0.09·0.99"]
    EV --> BAYES
    BAYES --> POST["Posterior P(H|E) ≈ 9%<br/>la evidencia actualiza,<br/>no reemplaza, el prior"]
    POST -->|"nueva evidencia"| PRIOR
```

## ⚠️ Errores conceptuales frecuentes

1. **Confundir P(A|B) con P(B|A).** "El 90 % de los enfermos da positivo" no implica "el
   90 % de los positivos está enfermo" — la diferencia la pone el prior (ver ejemplo).
2. **Ignorar la tasa base.** Evaluar un detector de fraude, spam o enfermedad rara por su
   accuracy global: un modelo que dice siempre "no" acierta 99 % y es inútil.
3. **"Independiente" como valor por defecto.** Multiplicar probabilidades solo es válido
   bajo independencia; features de un mismo individuo raramente lo son.
4. **Tratar la probabilidad del modelo como calibrada.** Que un softmax diga 0.97 no
   significa que el modelo acierte el 97 % de las veces que dice 0.97; la calibración se
   mide, no se asume.
5. **Confundir significancia con importancia.** Con n enorme, diferencias triviales se
   vuelven "significativas"; con n pequeño, efectos reales quedan invisibles. Siempre
   reportar tamaño de efecto y n.

## 🚀 Del aprendizaje a la operación

En producción este material se convierte en: medir la **calibración** de las probabilidades
del modelo (reliability diagrams, ECE) antes de usarlas para decidir; fijar umbrales de
decisión según costos asimétricos de falso positivo/negativo, no en 0.5 por defecto;
monitorear el cambio del prior en el tiempo (la tasa base de fraude de ayer no es la de
mañana); y acompañar toda métrica reportada de su n, su intervalo y la semilla del
experimento que la produjo.

## 🔗 Referencias

- [Russell, S. & Norvig, P. *AIMA*, 4.ª ed., caps. 12-13 (quantifying uncertainty)](https://aima.cs.berkeley.edu/)
- [Deisenroth, Faisal & Ong. *Mathematics for Machine Learning*, cap. 6 (PDF oficial gratuito)](https://mml-book.github.io/)
- [Goodfellow, Bengio & Courville. *Deep Learning*, cap. 3: Probability and Information Theory](https://www.deeplearningbook.org/)
- [Seeing Theory — visualizaciones interactivas de probabilidad (Brown University)](https://seeing-theory.brown.edu/)
- [Ioannidis, J. (2005). Why Most Published Research Findings Are False. *PLoS Medicine*](https://doi.org/10.1371/journal.pmed.0020124)

---

> [⬅️ Volver a la clase](README.md) · [📝 Evaluación](assessment.md) · [📚 Índice de la parte](../README.md)
