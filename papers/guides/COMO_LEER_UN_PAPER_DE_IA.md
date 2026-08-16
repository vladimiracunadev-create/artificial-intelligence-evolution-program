# 📖 Cómo leer un paper de IA

> Leer un paper no es leer un texto de principio a fin. Es un **interrogatorio**: entras con
> preguntas, buscas dónde se responden y decides si la respuesta te convence.

Esta guía enseña qué preguntarle a un paper. El [método en 5 pasadas](METODO_DE_LECTURA_EN_5_PASADAS.md)
enseña en qué **orden** hacerlo.

## 🧱 Anatomía de un paper y qué esconde cada parte

| Sección | Qué dice | Qué NO dice | Trampa habitual |
|---|---|---|---|
| **Título** | La consigna del trabajo | No es un teorema | *Attention Is All You Need* no significa que baste la atención |
| **Abstract** | La versión más optimista | Las condiciones | Los resultados aparecen sin su línea base |
| **Introducción** | El problema y la promesa | Los fracasos previos de los autores | Presenta como nuevo lo que ya existía |
| **Trabajo relacionado** | Genealogía según los autores | Lo que ignoraron | Se citan a sí mismos con generosidad |
| **Método** | Lo que hay que reproducir | Los trucos no documentados | Un hiperparámetro decisivo en una nota al pie |
| **Experimentos** | Evidencia | Los experimentos que no salieron | Comparar contra una línea base débil |
| **Ablaciones** | Qué componente aporta qué | — | **La sección más honesta; se salta casi siempre** |
| **Limitaciones** | Los límites que los autores admiten | Los que no vieron | Puede faltar por completo |
| **Apéndice** | Los detalles que importan | — | Ahí vive lo que hace falta para reproducir |

> [!TIP]
> Si tienes 10 minutos, léete el **abstract**, mira las **figuras** y ve directo a las
> **ablaciones**. Ese recorrido te dice más que leer las 4 primeras páginas seguidas.

## ❓ Las siete preguntas

Ninguna es sobre «qué dice el paper». Todas son sobre qué demuestra.

1. **¿Qué se hacía antes y por qué no bastaba?**
   Si no puedes responderla, no entiendes el paper: entiendes su solución fuera de contexto.

2. **¿Cuál es la afirmación central, en una frase?**
   Escríbela sin usar el vocabulario del paper. Si no puedes, aún no la entendiste.

3. **¿Qué evidencia la sostiene?**
   Tarea, dataset, métrica, línea base, número de ejecuciones, semillas, cómputo.
   Faltar cualquiera de estos seis es una debilidad, no un descuido de formato.

4. **¿Contra qué se compara?**
   Una mejora sobre una línea base mal ajustada no es una mejora. Comprueba si la línea base
   recibió el mismo esfuerzo de ajuste que el método propuesto.

5. **¿Qué se rompe si quito una pieza?**
   Es la pregunta de las ablaciones. Si no hay ablaciones, no sabes qué componente explica el
   resultado — y probablemente los autores tampoco.

6. **¿Qué NO demuestra?**
   Lo más valioso que puedes escribir sobre un paper. Casi siempre queda fuera del abstract.

7. **¿Qué haría falta para refutarlo?**
   Si no existe ningún resultado imaginable que lo contradiga, no es una afirmación empírica.

## 🚩 Señales de alarma

- **Métricas sin línea base.** «Alcanzamos 92 % de exactitud» no significa nada solo.
- **Una sola ejecución.** Sin varianza ni semillas, la diferencia puede ser ruido.
- **Benchmark contaminado.** Si el test pudo estar en el corpus de preentrenamiento, la
  métrica mide memorización, no capacidad.
- **Comparación entre desiguales.** Distinto cómputo, distintos datos, distinto ajuste.
- **Cherry-picking cualitativo.** Cinco ejemplos preciosos elegidos entre mil.
- **Ausencia de sección de limitaciones.** No significa que no las haya.
- **El código no existe, o existe y no reproduce las tablas.**
- **Un número que solo aparece en el abstract** y no se puede rastrear a ninguna tabla.

## 🕰️ El error específico de leer papers históricos

Es el error que más penaliza este eje: **atribuir a un paper ideas que llegaron después**.

| Se dice… | Pero en realidad… |
|---|---|
| «La LSTM tiene puerta de olvido desde 1997» | La añadieron Gers, Schmidhuber y Cummins en 1999/2000 |
| «Rumelhart inventó la retropropagación» | La popularizó para redes; la diferenciación en modo reverso es de Linnainmaa (1970) y Werbos (1974) |
| «AlexNet inventó las CNN» | LeNet es de 1998; AlexNet demostró que escalaban |
| «El Transformer eliminó todo menos la atención» | También usa FFN, residuales, layer norm y codificación posicional |
| «GPT-3 aprende de los ejemplos del prompt» | Se **condiciona**; no hay actualización de pesos |

Un paper se lee **con la información que existía cuando se escribió**. La narrativa
retrospectiva —«ya se veía venir»— es cómoda y casi siempre falsa.

## 🧪 Tres categorías que hay que separar siempre

Al escribir sobre un paper, cada frase pertenece a una de estas cajas. Etiquétalas:

| Categoría | Ejemplo |
|---|---|
| **Hecho documentado** | «El paper reporta la configuración base con N=6 capas y h=8 cabezas (sección 3).» |
| **Simplificación didáctica** | «Q es lo que preguntas, K la etiqueta y V el contenido.» |
| **Inferencia propia** | «Probablemente la escala √d_k importa más al crecer d_k.» ← verificable, pero mía |
| **Práctica moderna posterior** | «Hoy se usa RMSNorm y pre-norm en vez de post-norm.» ← no está en el paper |

Mezclarlas es lo que convierte un resumen en desinformación con buena intención.

## 📐 Cómo leer la matemática sin bloquearse

1. **Identifica los símbolos antes que las operaciones.** ¿Qué es un vector, qué una matriz,
   qué un escalar, qué un índice?
2. **Comprueba las dimensiones.** Si las formas no cuadran, has entendido mal algo. Es el
   depurador más rápido que existe.
3. **Evalúa el caso trivial.** ¿Qué pasa con n=1? ¿Con d=1? ¿Si el peso es 0? ¿Si es 1?
4. **Busca el caso límite.** ¿Qué ocurre cuando la secuencia es muy larga, la dimensión muy
   grande o la probabilidad se acerca a 0?
5. **Implementa la versión de 10 líneas.** La ecuación se entiende cuando corre.

Ese paso 5 es exactamente lo que hacen los notebooks de este eje.

## ✍️ Producto mínimo de una lectura

No has leído un paper hasta que puedes producir esto, sin volver a abrirlo:

- [ ] El problema anterior, en dos frases.
- [ ] La propuesta, en una.
- [ ] La ecuación o el diagrama central, dibujado de memoria.
- [ ] Una evidencia concreta con su tabla o figura de origen.
- [ ] Una limitación que el paper admite.
- [ ] Una limitación que el paper **no** admite.
- [ ] Una idea que hoy se le atribuye y llegó después.
- [ ] El hito siguiente que este paper hizo posible.

Esa lista es, literalmente, el esqueleto de la [plantilla de ficha](PLANTILLA_FICHA_PAPER.md).

---

**Referencia externa recomendada:** S. Keshav, *How to Read a Paper* (ACM SIGCOMM CCR, 2007),
origen del método de tres pasadas que este eje extiende a cinco.
[DOI](https://doi.org/10.1145/1273445.1273458)

[⬅️ Eje de papers](../README.md) ·
[🔁 Método en 5 pasadas](METODO_DE_LECTURA_EN_5_PASADAS.md) ·
[🌐 Fuentes y venues](FUENTES_Y_VENUES.md) ·
[📚 Glosario](GLOSARIO_PAPERS_IA.md)
