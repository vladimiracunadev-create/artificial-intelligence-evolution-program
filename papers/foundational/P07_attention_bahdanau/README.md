# P07 — Atención (Bahdanau)

> El decodificador deja de depender de un único vector y aprende a mirar la parte de la
> entrada que necesita en cada paso. Nace el mecanismo que tres años después dará nombre al
> paper más influyente del campo.

**Nivel:** L3 · **Motor:** `bahdanau` · **Notebook:** [`P07_attention_bahdanau.ipynb`](../../../notebooks/papers/P07_attention_bahdanau.ipynb)
· **Anexo:** [probabilidad y verosimilitud](../../annexes/A02_PROBABILIDAD_Y_VEROSIMILITUD.md)

## 1. Identificación

| Campo | Valor |
|---|---|
| **Título original** | *Neural Machine Translation by Jointly Learning to Align and Translate* |
| **Autoría** | Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio |
| **Año** | 2014 (arXiv) · 2015 (ICLR) |
| **Venue** | arXiv:1409.0473 · ICLR 2015 |
| **Fuente primaria** | [arXiv:1409.0473](https://arxiv.org/abs/1409.0473) |
| **Acceso** | Abierto |
| **Fecha de consulta** | 2026-08-16 |

## 2. Problema anterior

[Seq2Seq](../P06_seq2seq/README.md) comprime la frase de origen en un vector de tamaño fijo.
Los propios autores de aquel trabajo documentaron que la calidad **cae con la longitud**: un
vector de dimensión constante no puede sostener frases cada vez más largas.

El diagnóstico era claro y el parche disponible (invertir la entrada) no atacaba la causa.
La pregunta abierta era: **¿y si el decodificador no tuviera que depender de un único vector?**

## 3. Propuesta

Que el decodificador construya **un vector de contexto distinto en cada paso de salida**, como
suma ponderada de **todos** los estados del codificador. Los pesos los calcula una pequeña red
que puntúa la compatibilidad entre el estado actual del decodificador y cada estado de
entrada, y se normalizan con softmax.

Dos consecuencias, ambas en el título:

- **align** — los pesos son una alineación suave entre origen y destino, y se pueden inspeccionar;
- **translate** — todo se entrena junto, con la pérdida de traducción. **Nadie etiqueta la
  alineación**: emerge sola.

El codificador además pasa a ser **bidireccional**, para que cada estado `h_j` resuma el
contexto a ambos lados de la posición `j`.

## 4. Intuición sin fórmulas

En lugar de memorizar la frase entera y cerrar los ojos, el traductor deja el texto original
sobre la mesa y, para cada palabra que escribe, vuelve a mirar la parte que le hace falta.

**Dónde deja de funcionar la analogía:** un traductor humano sabe **por qué** mira donde mira.
Los pesos `α` indican dónde se concentró la mezcla, no una razón. Confundir ambas cosas es el
error que la sección 11 documenta.

## 5. Matemática mínima

```text
Puntuación de compatibilidad (aditiva, con una capa oculta):
    e_ij = vᵀ · tanh(W · s_{i−1} + U · h_j)

Normalización:
    α_ij = exp(e_ij) / Σ_k exp(e_ik)        →  Σ_j α_ij = 1

Vector de contexto del paso i:
    c_i = Σ_j α_ij · h_j

Salida:
    s_i = f(s_{i−1}, y_{i−1}, c_i)
    p(y_i | y_<i, x) = g(y_{i−1}, s_i, c_i)
```

- `h_j` : estado del codificador bidireccional en la posición `j` de origen.
- `s_{i−1}` : estado del decodificador antes de emitir el token `i`.
- `v`, `W`, `U` : parámetros **aprendidos** junto con el resto del modelo.

Obsérvese que `c_i` depende de `i`: **hay un contexto por paso de salida**, no uno por frase.

<!-- puente:inicio -->
> [!TIP]
> **Puente matemático.** Esta sección da por sabido lo siguiente. Si algo no te suena,
> léelo primero: está explicado una sola vez, en un solo sitio, y sirve para todas las fichas.

| Dónde | Qué necesitas de ahí |
|---|---|
| [**A02 §1** · Softmax](../../annexes/A02_PROBABILIDAD_Y_VEROSIMILITUD.md#1-softmax) | los pesos de alineación son un softmax: suman 1 y compiten entre sí |
| [**A04** · la atención paso a paso](../../annexes/A04_ATENCION_PASO_A_PASO.md) | el mecanismo completo, paso a paso, con números |
<!-- puente:fin -->

## 6. Arquitectura o flujo

```text
       h₁    h₂    h₃    h₄          ← codificador BIDIRECCIONAL
        │     │     │     │
        └──┬──┴──┬──┴──┬──┘
           │     │     │
      ┌────▼─────▼─────▼────┐
      │  e_ij = vᵀtanh(...)  │  ← puntuación aprendida
      └──────────┬───────────┘
                 ▼
              softmax  →  α_i1 … α_i4   (suman 1)
                 │
                 ▼
        c_i = Σ_j α_ij · h_j            ← contexto PROPIO del paso i
                 │
                 ▼
      s_{i−1} ──► decodificador ──► y_i
```

## 7. Qué observar en el paper original

- Las **matrices de alineación** visualizadas como mapas de calor entre frase de origen y
  traducción. Es la figura más reproducida del artículo y muestra que la alineación aprendida
  se corresponde con la intuición lingüística, incluida la reordenación entre idiomas.
- La **curva de BLEU frente a longitud de frase**: el modelo con atención no se degrada como
  el de vector fijo. Ese gráfico **es** el argumento del paper.
- La justificación del **codificador bidireccional**.
- El detalle de que la red de puntuación es pequeña y se entrena de forma conjunta.

## 8. Evidencia y resultados

Traducción inglés → francés sobre WMT'14, comparando el modelo con atención (llamado
*RNNsearch*) contra el codificador–decodificador de vector fijo (*RNNenc*), con dos límites de
longitud de entrenamiento.

El resultado central no es una cifra puntual sino una **forma de curva**: el modelo de vector
fijo pierde calidad conforme crece la longitud de la frase, y el modelo con atención mantiene
su rendimiento.

> Los valores de BLEU por configuración están en las tablas y figuras del artículo.
> Verificarlos allí antes de citarlos.

La miniatura de este eje aporta evidencia del mecanismo: una atención aditiva con 18
parámetros aprende una alineación correcta 4/4 y produce distribuciones con entropía cercana a
cero, con `Σ α = 1` en cada fila.

## 9. Impacto

- Fija la atención como componente estándar de la traducción automática neuronal.
- Introduce la idea de **acceso a contenido por compatibilidad aprendida**, que es exactamente
  lo que generaliza el [Transformer](../P08_transformer/README.md).
- Abre la línea de **interpretabilidad por atención**, con su promesa y su posterior crítica.
- Reformula el problema: de «comprimir bien» a «recuperar lo relevante en cada paso» — un
  cambio de marco que reaparece en [RAG](../P11_rag/README.md).

## 10. Limitaciones

1. **Coste cuadrático** en el producto (longitud de entrada × longitud de salida): se calcula
   una puntuación por cada par de posiciones.
2. **Sigue siendo recurrente.** No paraleliza sobre la longitud; ese límite persiste hasta P08.
3. **La atención no es una explicación.** Trabajo posterior mostró que existen distribuciones
   de atención muy distintas que producen la misma salida.
4. **Una sola «cabeza»**: un único tipo de relación por paso. El multi-head de P08 lo generaliza.
5. **La alineación aprendida no siempre coincide** con la alineación lingüística, y cuando
   coincide no hay garantía de que sea la causa de la traducción.
6. **Depende de corpus paralelos** grandes.

## 11. Errores comunes

| Error | Corrección |
|---|---|
| «La atención muestra en qué se fijó el modelo, luego explica su decisión» | Jain y Wallace (2019) mostraron que se pueden construir distribuciones de atención muy distintas con la misma salida. Es una pista, no una explicación causal. |
| «Este paper inventó el Transformer» | Inventó el mecanismo de atención para traducción. El Transformer (2017) lo generaliza y elimina la recurrencia. |
| «La atención de Bahdanau es producto escalar» | Es **aditiva**: una capa con tanh. La multiplicativa es de Luong et al. (2015). |
| «Los pesos α son parámetros del modelo» | Son **calculados** en cada paso a partir de la entrada. Los parámetros son `v`, `W`, `U`. |
| «La alineación se supervisa» | No. Emerge de entrenar únicamente la traducción. Esa es la parte notable. |

## 12. Relación con trabajos anteriores

- **[P06 Seq2Seq](../P06_seq2seq/README.md) (2014)** — el cuello de botella que motiva el trabajo.
- **Cho et al. (2014)** — codificador–decodificador con GRU, del mismo grupo.
  [arXiv:1406.1078](https://arxiv.org/abs/1406.1078)
- **Graves (2013)** — mecanismos de atención sobre secuencias en generación de escritura.
- **Alineación en traducción estadística** (modelos IBM, 1993) — la noción clásica de
  alineación que aquí se vuelve suave y diferenciable.

## 13. Relación con trabajos posteriores

- **Luong et al. (2015)** — atención multiplicativa, global y local.
  [arXiv:1508.04025](https://arxiv.org/abs/1508.04025)
- **[P08 Transformer](../P08_transformer/README.md) (2017)** — self-attention multi-cabeza sin
  recurrencia.
- **Jain y Wallace (2019)** — *Attention is not Explanation*.
  [arXiv:1902.10186](https://arxiv.org/abs/1902.10186)
- **Wiegreffe y Pinter (2019)** — *Attention is not not Explanation*: la réplica. Leer ambas
  es un ejercicio de nivel L3.

## 14. Notebook asociado

[`P07_attention_bahdanau.ipynb`](../../../notebooks/papers/P07_attention_bahdanau.ipynb)

**Qué implementa:** atención aditiva con `W` y `U` diagonales, entrenada por descenso de
gradiente hasta producir una matriz de alineación correcta; medición de entropía por fila y
comprobación de que los pesos suman 1.

**Qué NO implementa:** traducción real, codificador bidireccional entrenado, ni alineación
latente. **Aquí la alineación se supervisa**; en el paper emerge sola. La diferencia es
importante y se declara en el propio notebook.

```bash
ai-evolution paper-lab P07 --seed 7
```

## 15. Actividades Bloom

| Nivel | Actividad |
|---|---|
| **Recordar** | Escribe las tres ecuaciones de la atención aditiva y nombra cada símbolo. |
| **Explicar** | Explica por qué `c_i` lleva subíndice `i` y qué habría cambiado si no lo llevara. |
| **Aplicar** | Ejecuta el notebook con tres semillas y compara entropías. |
| **Analizar** | Sustituye el softmax por una normalización dividiendo por la suma y explica qué se rompe. |
| **Evaluar** | Lee el resumen de Jain y Wallace (2019) y decide si invalida el uso de la atención para depurar modelos. Argumenta. |
| **Crear** | Diseña un experimento que distinga «la atención señala lo relevante» de «la atención causa la salida». Di qué necesitarías para ejecutarlo. |

## 16. Autoevaluación

1. ¿Qué problema concreto de Seq2Seq resuelve este mecanismo, y cómo se mide que lo resuelve?
2. ¿Por qué los pesos `α` deben sumar 1?
3. ¿Qué se aprende exactamente: los pesos `α` o los parámetros `v`, `W`, `U`?
4. ¿Por qué el codificador es bidireccional?
5. ¿Qué diferencia hay entre atención aditiva y multiplicativa?
6. ¿Por qué una matriz de atención interpretable no equivale a una explicación?
7. ¿Qué límite de este trabajo persiste y motiva el paper siguiente?

## 17. Respuestas esperadas

1. El cuello de botella del vector fijo. Se mide con la curva de calidad frente a longitud de
   frase: con atención deja de degradarse.
2. Porque `c_i` es una **combinación convexa** de los estados del codificador. Sumar 1
   garantiza que el contexto viva en el casco convexo de `h_j` y que la mezcla sea comparable
   entre pasos.
3. Se aprenden `v`, `W`, `U`. Los `α` se **calculan** en cada paso a partir de la entrada
   concreta.
4. Para que `h_j` resuma el contexto a ambos lados de la posición `j`, y no solo lo anterior.
5. La aditiva usa una capa con tanh y un vector `v`; la multiplicativa usa directamente un
   producto escalar (opcionalmente con una matriz). La segunda es más barata y es la que
   adopta el Transformer con la escala `√d_k`.
6. Porque correlación entre peso y salida no implica causalidad; existen distribuciones
   alternativas que producen la misma predicción.
7. La recurrencia: el cómputo sigue siendo secuencial en la longitud, y eso limita la escala
   del entrenamiento.

## 18. Fuentes primarias

- Bahdanau, D., Cho, K. y Bengio, Y. (2014). *Neural Machine Translation by Jointly Learning
  to Align and Translate*. **ICLR 2015**.
  [arXiv:1409.0473](https://arxiv.org/abs/1409.0473) · consultado 2026-08-16.
- Luong, M.-T., Pham, H. y Manning, C. D. (2015). *Effective Approaches to Attention-based
  Neural Machine Translation*. **EMNLP 2015**.
  [arXiv:1508.04025](https://arxiv.org/abs/1508.04025) · consultado 2026-08-16.
- Jain, S. y Wallace, B. C. (2019). *Attention is not Explanation*. **NAACL 2019**.
  [arXiv:1902.10186](https://arxiv.org/abs/1902.10186) · consultado 2026-08-16.

---

[⬅️ Anterior: P06 Seq2Seq](../P06_seq2seq/README.md) ·
[📇 Índice](../../catalog/PAPERS_INDEX.md) ·
[📝 Evaluación](../../../assessments/papers/P07_attention_bahdanau.md) ·
[🏫 Clase 055 del programa](../../../classes/part-04-neural-networks-and-deep-learning/055-atencion-y-arquitectura-transformer/README.md) ·
[➡️ Siguiente: P08 Transformer](../P08_transformer/README.md)
