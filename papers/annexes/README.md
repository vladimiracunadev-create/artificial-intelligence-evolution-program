# 🧮 Anexos matemáticos del eje de papers

> Toda la matemática que aparece en las 117 fichas, explicada una sola vez y en un solo sitio.
> Cada anexo dice **qué es**, **por qué aparece**, **dónde se usa** y trae un **ejemplo resuelto
> a mano** que puedes comprobar con lápiz antes de ejecutar nada.

## Por qué existen

Las fichas tienen una sección 5 «Matemática mínima» deliberadamente corta: solo las ecuaciones
imprescindibles de **ese** paper. Pero las mismas herramientas reaparecen una y otra vez —el
producto escalar está en Word2Vec, en la atención y en CLIP; el softmax está en cinco papers; la
regla de la cadena sostiene el entrenamiento de los veintidós—.

Repetir la explicación en cada ficha sería ruido. Omitirla dejaría fuera a quien la necesita.
Los anexos resuelven esa tensión: la ficha enlaza, el anexo explica.

## Los cinco anexos

| Anexo | Cubre | Papers que lo usan |
|---|---|---|
| [A01 · Álgebra y geometría](A01_ALGEBRA_Y_GEOMETRIA.md) | Vectores, producto escalar, norma, coseno, hiperplanos, matrices | P01, P05, P07, P08, P18 |
| [A02 · Probabilidad y verosimilitud](A02_PROBABILIDAD_Y_VEROSIMILITUD.md) | Softmax, entropía, KL, verosimilitud, Bradley-Terry, gaussianas | P08, P09, P10, P12, P15, P17, P22 |
| [A03 · Cálculo y gradientes](A03_CALCULO_Y_GRADIENTES.md) | Derivadas, regla de la cadena, retropropagación, comprobación numérica | P02, P03, P05, P12, P15 |
| [A04 · La atención, paso a paso](A04_ATENCION_PASO_A_PASO.md) | La ecuación 1 desarrollada con números, máscara, multi-cabeza | P07, P08, T01–T08 |
| [A05 · Complejidad, coste y escalado](A05_COMPLEJIDAD_Y_COSTE.md) | Notación O(), memoria, FLOPs, leyes de escalado, coste de inferencia | P06, P08, P19, P20, P21, P22 |

## Cómo usarlos

1. **No los leas seguidos.** Son material de consulta, no un curso de matemáticas.
2. Cuando una ficha te frene en la sección 5, abre el anexo que enlaza, lee **solo** el apartado
   que necesitas y vuelve.
3. Cada apartado termina con un **error común**: si vas con prisa, lee al menos esos.
4. Los ejemplos numéricos están resueltos a mano a propósito. Haz la cuenta tú antes de mirar el
   resultado — es el mismo contrato que el de los notebooks: **predecir, luego comprobar**.

## Nivel asumido

Se asume bachillerato: operaciones con fracciones, potencias, logaritmos y la idea de derivada.
Todo lo demás se construye aquí. Si algo del anexo A03 no se entiende, la
[clase 005 del programa](../../classes/part-00-foundations-history-and-scientific-method/005-vectores-matrices-y-geometria-para-ia/README.md)
cubre los prerrequisitos con más calma.

---

[⬅️ Eje de papers](../README.md) ·
[📇 Índice de papers](../catalog/PAPERS_INDEX.md) ·
[📚 Glosario](../guides/GLOSARIO_PAPERS_IA.md)
