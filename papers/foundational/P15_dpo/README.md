# P15 — DPO

> El resultado que eliminó el andamiaje: si la política óptima del objetivo RLHF tiene forma
> cerrada, la recompensa se puede despejar y el modelo se ajusta directamente con las
> preferencias. Sin modelo de recompensa. Sin aprendizaje por refuerzo.

**Nivel:** L4 · **Motor:** `dpo` · **Notebook:** [`P15_dpo.ipynb`](../../../notebooks/papers/P15_dpo.ipynb)
· **Anexo:** [probabilidad y verosimilitud](../../annexes/A02_PROBABILIDAD_Y_VEROSIMILITUD.md)

## 1. Identificación

| Campo | Valor |
|---|---|
| **Título original** | *Direct Preference Optimization: Your Language Model is Secretly a Reward Model* |
| **Autoría** | Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, Chelsea Finn |
| **Año** | 2023 |
| **Venue** | arXiv:2305.18290 · NeurIPS 2023 |
| **Fuente primaria** | [arXiv:2305.18290](https://arxiv.org/abs/2305.18290) |
| **Acceso** | Abierto |
| **Fecha de consulta** | 2026-08-16 |

## 2. Problema anterior

El pipeline de [InstructGPT](../P12_instructgpt_rlhf/README.md) funciona, pero es caro y
frágil:

- entrena **un modelo adicional** (el de recompensa) que hay que mantener y validar;
- requiere **muestreo on-policy** durante el entrenamiento por refuerzo;
- **PPO es sensible** a hiperparámetros y difícil de estabilizar;
- hay que mantener **varios modelos en memoria** a la vez (política, referencia, recompensa,
  crítico).

La pregunta: ¿todo ese aparato es necesario, o es un rodeo?

## 3. Propuesta

Un resultado teórico con una consecuencia práctica inmediata.

**El resultado.** La solución óptima del objetivo RLHF con restricción KL tiene forma cerrada:

```text
π*(y | x) = (1 / Z(x)) · π_ref(y | x) · exp( r(x, y) / β )
```

**La consecuencia.** De ahí se despeja la recompensa:

```text
r(x, y) = β · log[ π*(y|x) / π_ref(y|x) ] + β · log Z(x)
```

Al sustituir esto en el objetivo Bradley-Terry, **el término `Z(x)` se cancela** —porque
aparece en ambas ramas de la comparación— y queda una pérdida de clasificación binaria sobre
pares de preferencias, expresada únicamente en términos de la política.

En una frase: **la política ya es el modelo de recompensa**. No hace falta entrenar uno aparte
para luego optimizar contra él; se optimiza la política directamente.

## 4. Intuición sin fórmulas

RLHF entrena un juez y luego entrena al alumno a gustarle al juez. DPO demuestra que el alumno
**ya contiene** al juez: su preferencia se lee comparando lo que dice ahora con lo que decía
antes de entrenarse. Basta con ajustarlo para que suba lo preferido y baje lo rechazado, sin
alejarse demasiado de donde estaba.

**Dónde deja de funcionar la analogía:** el juez de RLHF puede evaluar respuestas nuevas,
generadas durante el entrenamiento. DPO solo aprende de los pares que ya tiene: no explora.

## 5. Matemática mínima

```text
Pérdida DPO:

L = − E_{(x, y_w, y_l)} [ log σ( β·[ log(π(y_w|x)/π_ref(y_w|x))
                                    − log(π(y_l|x)/π_ref(y_l|x)) ] ) ]

Recompensa implícita:
    r̂(x, y) = β · log[ π(y|x) / π_ref(y|x) ]
```

- `y_w` preferida, `y_l` rechazada, `π_ref` la política de referencia (habitualmente el modelo
  SFT), `β` el coeficiente que controla la desviación permitida.
- **`π_ref` es imprescindible.** Sin ella el objetivo premia subir `p(y_w)` sin límite y la
  política colapsa a una distribución degenerada. El log-ratio es lo que convierte «subir» en
  «subir *relativamente a la referencia*», y `β` pone el precio.
- **La restricción KL no desapareció**: quedó absorbida en la forma del log-ratio.

<!-- puente:inicio -->
> [!TIP]
> **Puente matemático.** Esta sección da por sabido lo siguiente. Si algo no te suena,
> léelo primero: está explicado una sola vez, en un solo sitio, y sirve para todas las fichas.

| Dónde | Qué necesitas de ahí |
|---|---|
| [**A02 §5** · Bradley-Terry: aprender de comparaciones](../../annexes/A02_PROBABILIDAD_Y_VEROSIMILITUD.md#5-bradley-terry-aprender-de-comparaciones) | el mismo Bradley-Terry de RLHF, ahora sin modelo de recompensa intermedio |
| [**A02 §4** · Divergencia KL](../../annexes/A02_PROBABILIDAD_Y_VEROSIMILITUD.md#4-divergencia-kl) | la divergencia KL, que es lo que impide alejarse del modelo de referencia |
<!-- puente:fin -->

## 6. Arquitectura o flujo

```text
   RLHF (tres etapas, dos modelos extra)
   ┌─────────┐   ┌───────────────┐   ┌──────────────────┐
   │  SFT    │──►│ modelo de     │──►│ PPO: muestrear,  │──► π
   │         │   │ recompensa r  │   │ puntuar, ajustar │
   └─────────┘   └───────────────┘   └──────────────────┘

   DPO (una etapa, ningún modelo extra)
   ┌─────────┐   ┌──────────────────────────────────────┐
   │  SFT    │──►│ pérdida de clasificación sobre pares │──► π
   │ = π_ref │   │ (π_ref congelada, solo se evalúa)    │
   └─────────┘   └──────────────────────────────────────┘
```

## 7. Qué observar en el paper original

- La **derivación completa** de la forma cerrada y la cancelación de `Z(x)`. Es corta y vale la
  pena seguirla símbolo a símbolo: es el núcleo de todo el trabajo.
- El **análisis del gradiente**: el peso de cada par es mayor cuanto más se equivoca el modelo
  de recompensa implícito, lo que da una lectura intuitiva del comportamiento.
- La **comparación de la frontera recompensa–KL** frente a PPO. No basta con «gana en la
  métrica»: hay que ver a qué distancia de la referencia.
- Los experimentos de **generación controlada de sentimiento**, **resumen** y **diálogo**.
- La discusión sobre **generalización fuera de distribución**, donde los autores son cautos.

## 8. Evidencia y resultados

Tres escenarios:

- **generación controlada de sentimiento**, donde se puede computar la frontera óptima
  recompensa–KL y comparar objetivamente;
- **resumen** (Reddit TL;DR), evaluado con preferencia de un modelo juez;
- **diálogo de un turno** (Anthropic HH).

DPO iguala o supera a PPO en calidad de preferencia, con una implementación mucho más simple,
más estable y sin ajustar un modelo de recompensa separado. En generación de sentimiento, DPO
alcanza una frontera recompensa–KL mejor que PPO.

> Las tasas de victoria y las curvas por escenario están en las figuras del artículo.
> Verificarlas allí antes de citarlas.

La miniatura de este eje muestra el mecanismo en su forma más desnuda: sobre una política de
tres opciones, optimizar la pérdida DPO desplaza la masa hacia la respuesta preferida y produce
recompensas implícitas positivas para ella y negativas para las rechazadas.

## 9. Impacto

- **Simplificó radicalmente la alineación** y la puso al alcance de equipos sin infraestructura
  de RL. Es hoy la vía por defecto para ajustar modelos abiertos con preferencias.
- Abrió una familia de métodos derivados: IPO, KTO, ORPO, SimPO y otros, cada uno con una
  variante de la pérdida.
- Reforzó una lección metodológica: **antes de construir maquinaria, comprobar si el problema
  tiene solución analítica**. El resultado estaba implícito en la formulación de RLHF desde el
  principio.

## 10. Limitaciones

1. **No explora.** Solo aprende de los pares disponibles; RLHF puede muestrear respuestas nuevas
   y evaluarlas. Si los pares no cubren una región, DPO no aprende nada de ella.
2. **Depende críticamente de la calidad y cobertura de las preferencias.** Basura entra,
   basura sale — igual que RLHF, pero sin un modelo de recompensa que se pueda inspeccionar por
   separado.
3. **Sin recompensa explícita que auditar.** En RLHF se puede estudiar `r` de forma aislada:
   qué premia, dónde falla. En DPO esa información está distribuida en la política.
4. **Sensible a `β`**: demasiado bajo, colapso; demasiado alto, apenas se mueve.
5. **Tendencia a reducir la probabilidad de ambas respuestas** del par en algunos regímenes,
   fenómeno documentado en trabajo posterior.
6. **Requiere `π_ref` en memoria** durante todo el entrenamiento.
7. **La equivalencia teórica con RLHF supone** un modelo de preferencias Bradley-Terry y un
   óptimo alcanzable; en la práctica ninguna de las dos cosas se cumple exactamente.

## 11. Errores comunes

| Error | Corrección |
|---|---|
| «DPO es siempre mejor que RLHF» | Es **más simple** y a menudo igual de bueno. RLHF conserva la ventaja de explorar respuestas nuevas on-policy. |
| «DPO no tiene restricción KL» | La tiene, absorbida en el log-ratio contra `π_ref` y escalada por `β`. |
| «Se puede quitar `π_ref` y simplificar más» | Sin `π_ref` no hay ancla y la política colapsa. Es el anti-patrón del notebook. |
| «DPO no necesita datos de preferencia» | Los necesita exactamente igual. Lo que elimina es el **modelo** de recompensa, no los **datos**. |
| «La recompensa implícita es una metáfora» | Es una identidad: `r̂ = β·log(π/π_ref)` se deriva del óptimo del objetivo RLHF. |
| «DPO evita el reward hacking» | Reduce una superficie (el modelo de recompensa explotable), no el problema de fondo: sigue optimizando un proxy de la preferencia. |

## 12. Relación con trabajos anteriores

- **[P12 InstructGPT](../P12_instructgpt_rlhf/README.md) (2022)** — el pipeline que se simplifica.
- **Bradley y Terry (1952)** — el modelo de preferencias por pares.
  [doi.org/10.2307/2334029](https://doi.org/10.2307/2334029)
- **Schulman et al. (2017), PPO** — el algoritmo que DPO evita.
  [arXiv:1707.06347](https://arxiv.org/abs/1707.06347)
- **RL con regularización KL** — la formulación de la que se deriva la forma cerrada.

## 13. Relación con trabajos posteriores

- **IPO (2023)** — corrige supuestos del modelo de preferencias.
  [arXiv:2310.12036](https://arxiv.org/abs/2310.12036)
- **KTO (2024)** — aprende de señales binarias sin necesidad de pares.
  [arXiv:2402.01306](https://arxiv.org/abs/2402.01306)
- **ORPO, SimPO (2024)** — variantes que eliminan `π_ref` o fusionan etapas.
- **[P16 Sistemas agentic](../P16_agentic_systems/README.md)** — la alineación como componente
  de un sistema, no como paso final.

## 14. Notebook asociado

[`P15_dpo.ipynb`](../../../notebooks/papers/P15_dpo.ipynb)

**Qué implementa:** la pérdida DPO optimizada sobre una política categórica de tres opciones,
la comparación entre `π_ref` y `π_DPO`, el cálculo de la recompensa implícita para varios `β`,
y una demostración de por qué eliminar `π_ref` provoca colapso.

**Qué NO implementa:** modelo de lenguaje, generación, tokenización ni longitud variable. Tres
opciones discretas no son una política sobre secuencias; el mecanismo es el mismo, la escala no.

```bash
ai-evolution paper-lab P15 --seed 7
```

## 15. Actividades Bloom

| Nivel | Actividad |
|---|---|
| **Recordar** | Escribe la pérdida DPO y la expresión de la recompensa implícita. |
| **Explicar** | Explica por qué `Z(x)` se cancela y por qué eso es lo que hace viable el método. |
| **Aplicar** | Ejecuta el notebook con tres valores de `β` y compara las recompensas implícitas. |
| **Analizar** | Compara DPO y RLHF en cinco dimensiones: coste, estabilidad, exploración, auditabilidad y datos requeridos. |
| **Evaluar** | ¿Cuándo elegirías RLHF pese a su complejidad? Da dos escenarios concretos. |
| **Crear** | Deriva la pérdida DPO desde el objetivo RLHF con restricción KL, paso a paso, en una página. |

## 16. Autoevaluación

1. ¿Qué significa «tu modelo de lenguaje ya es un modelo de recompensa»?
2. ¿Por qué se cancela `Z(x)` y qué pasaría si no se cancelara?
3. ¿Qué papel juega `π_ref` y qué ocurre exactamente si se elimina?
4. ¿Qué controla `β`?
5. ¿Qué capacidad de RLHF se pierde con DPO?
6. ¿DPO necesita menos datos de preferencia que RLHF?
7. ¿Por qué la simplicidad de un método es un argumento técnico y no solo estético?

## 17. Respuestas esperadas

1. Que la recompensa implícita se puede leer como `β·log(π/π_ref)`. La política contiene la
   información que el modelo de recompensa explícito codificaría, expresada como desviación
   respecto a la referencia.
2. Porque `Z(x)` depende solo de `x` y aparece idéntico en las dos ramas de la comparación
   `r(x,y_w) − r(x,y_l)`. Si no se cancelara, habría que calcular una normalización sobre todas
   las salidas posibles, que es intratable.
3. Es el ancla. Sin ella, la pérdida premia aumentar `p(y_w)` indefinidamente y la política
   colapsa a una distribución degenerada que siempre dice lo mismo.
4. Cuánto se permite que la política se aleje de la referencia: es el equivalente al
   coeficiente de la penalización KL en RLHF.
5. La exploración on-policy. RLHF genera respuestas nuevas durante el entrenamiento y las
   evalúa; DPO solo ve los pares del conjunto de datos.
6. No. Necesita los mismos datos. Elimina el **modelo** de recompensa, no la anotación.
7. Porque menos piezas significan menos hiperparámetros, menos modos de fallo, menos cómputo y
   mayor reproducibilidad. Todo eso es medible.

## 18. Fuentes primarias

- Rafailov, R. et al. (2023). *Direct Preference Optimization: Your Language Model is Secretly a
  Reward Model*. **NeurIPS 2023**.
  [arXiv:2305.18290](https://arxiv.org/abs/2305.18290) · consultado 2026-08-16.
- Bradley, R. A. y Terry, M. E. (1952). *Rank Analysis of Incomplete Block Designs*.
  **Biometrika**, 39(3/4), 324–345.
  [doi.org/10.2307/2334029](https://doi.org/10.2307/2334029) · consultado 2026-08-16.
- Azar, M. G. et al. (2023). *A General Theoretical Paradigm to Understand Learning from Human
  Preferences* (IPO).
  [arXiv:2310.12036](https://arxiv.org/abs/2310.12036) · consultado 2026-08-16.

---

[⬅️ Anterior: P14 Toolformer](../P14_toolformer/README.md) ·
[📇 Índice](../../catalog/PAPERS_INDEX.md) ·
[📝 Evaluación](../../../assessments/papers/P15_dpo.md) ·
[🏫 Clase 078 del programa](../../../classes/part-06-foundation-models-and-llm-engineering/078-rlhf-rlaif-y-dpo/README.md) ·
[➡️ Siguiente: P16 Sistemas agentic](../P16_agentic_systems/README.md)
