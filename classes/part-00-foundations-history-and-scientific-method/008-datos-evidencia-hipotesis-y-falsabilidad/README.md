
# 008 — Datos, evidencia, hipótesis y falsabilidad

> [← Clase anterior](../../../classes/part-00-foundations-history-and-scientific-method/007-logica-algoritmos-y-complejidad-computacional/README.md) · [Índice de la parte](../README.md) · [Clase siguiente →](../../../classes/part-00-foundations-history-and-scientific-method/009-entornos-python-git-y-experimentos-reproducibles/README.md)

**Parte:** 00 — Fundamentos, historia y método científico  
**Nivel:** fundamentos · **Horas estimadas:** 4  
**Laboratorio:** `evaluation` · **Estado:** `EXECUTABLE_CORE`

## 🎯 Propósito

Comprender **datos, evidencia, hipótesis y falsabilidad** dentro de la evolución de la inteligencia
artificial, implementar un experimento mínimo verificable y distinguir qué parte
constituye evidencia frente a una afirmación todavía no comprobada.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. Explicar datos, evidencia, hipótesis y falsabilidad usando los conceptos `datos`, `hipótesis`, `falsabilidad`, `reproducibilidad`.
2. Ejecutar el laboratorio con una semilla explícita y revisar su contrato JSON.
3. Identificar al menos un supuesto, una limitación y un riesgo de aplicación.
4. Comparar el enfoque con la etapa anterior de la ruta de aprendizaje.
5. Producir una evidencia reproducible y una conclusión que no exceda los datos.

## 🧩 Conceptos centrales

`datos`, `hipótesis`, `falsabilidad`, `reproducibilidad`

## 🗺️ Ubicación en el mapa de la IA

La IA es una disciplina empírica: sus afirmaciones ("este modelo es mejor", "esta técnica
generaliza") se sostienen o caen con experimentos. Esta clase importa el criterio de
demarcación de Popper — falsabilidad — al trabajo con modelos y datos, y es el fundamento
metodológico de los entornos reproducibles (clase 009), de la lectura crítica de papers
(clase 010) y de cada laboratorio del programa, cuyo contrato JSON separa explícitamente
`evidence` de `limitations`.

## 📖 Fundamentos

### 🔍 Falsabilidad como criterio de demarcación

Para Popper, una hipótesis es **científica** si y solo si existe alguna observación posible
que la refutaría. "Este modelo alcanza ≥ 0.85 de F1 en datos de 2025 no vistos" es
falsable; "este modelo entiende el lenguaje" no lo es hasta que se traduzca a predicciones
observables. Dos consecuencias operativas:

- La ciencia avanza por **conjeturas y refutaciones**: proponer hipótesis audaces y
  someterlas a los tests más duros disponibles, no buscar confirmaciones.
- Ninguna cantidad de confirmaciones *demuestra* una hipótesis universal (problema de la
  inducción de Hume); una sola refutación sólida la derriba. La asimetría es el motor.

### 🧪 De la pregunta al experimento

Estructura mínima de una hipótesis experimental en IA:

```text
H: "El sistema/técnica X supera al baseline B en la métrica M
    sobre la población de datos D, por al menos δ."

Falsable porque: si M(X) − M(B) < δ en una muestra representativa de D,  H queda refutada.
```

Cada componente es obligatorio: sin baseline B no hay comparación; sin población D definida
no se sabe a qué generaliza; sin margen δ cualquier diferencia de ruido "confirma"; sin
métrica M fijada *antes* de mirar los resultados, se cae en la selección post-hoc.

### 📊 Jerarquía de la evidencia en IA

No toda evidencia pesa igual. De más débil a más fuerte:

1. **Anécdota / demo:** un ejemplo elegido a mano. Sirve para ilustrar, no para concluir.
2. **Evaluación en muestra de entrenamiento:** inválida — memorizar no es generalizar.
3. **Held-out interno:** partición de test del mismo dataset. Mínimo aceptable; vulnerable
   a fuga de información (*leakage*) y a sobreajuste al benchmark.
4. **Datos externos / fuera de distribución:** otra fuente, otro periodo temporal.
5. **Replicación independiente:** otro equipo, otro código, mismos resultados. El patrón
   oro; su escasez en ML es la "crisis de reproducibilidad" documentada por Kapoor y
   Narayanan (2023), que hallaron leakage en cientos de papers aplicados.

### 🕳️ Patologías del razonamiento con datos

- **Fuga de datos (leakage):** información del test contamina el entrenamiento (duplicados,
  features derivadas del futuro, normalizar antes de particionar). Produce métricas
  ficticiamente altas que colapsan en producción.
- **p-hacking / garden of forking paths:** probar configuraciones hasta que una "funciona"
  y reportar solo esa. Con 20 variantes y α=0.05, se espera un falso positivo por puro azar.
- **HARKing** (*Hypothesizing After Results are Known*): presentar un hallazgo exploratorio
  como si fuera la hipótesis original. Legítimo como exploración, fraudulento como
  confirmación.
- **Sesgo de supervivencia y de publicación:** solo se publican los experimentos que
  salieron bien; el registro público sobreestima sistemáticamente el efecto real
  (Ioannidis, 2005).
- **Goodhart:** cuando la métrica se vuelve objetivo, deja de medir lo que medía —
  sobreajuste comunitario a benchmarks públicos incluido.

### ✅ Contrato de evidencia del programa

Cada laboratorio de este repositorio emite un JSON con `seed`, `evidence` y `limitations`.
Es una implementación en miniatura del criterio popperiano: la evidencia es inspeccionable
y reproducible (misma semilla → mismo resultado), y las limitaciones declaran de antemano
dónde la conclusión deja de valer — el equivalente a especificar qué observación refutaría
el claim.

## 🧮 Ejemplo trabajado

Un equipo afirma: "nuestro clasificador de fraude tiene accuracy 0.99". Auditemos con
números. El dataset tiene 100 000 transacciones, 1 000 fraudulentas (1 %).

```text
Modelo trivial "nunca es fraude":  acierta 99 000 / 100 000 = 0.99 de accuracy
                                   recall sobre fraude = 0/1000 = 0.0
```

El claim es literalmente cierto y prácticamente vacío: no supera al baseline trivial.
Reformulación falsable correcta:

```text
H: "El modelo alcanza recall ≥ 0.70 con precisión ≥ 0.80 sobre transacciones
    de un mes posterior al periodo de entrenamiento (validación temporal)."
```

Supongamos que en ese mes hay 900 fraudes y el modelo marca 950 transacciones, de las
cuales 720 son fraude real: precisión = 720/950 ≈ 0.758 → **H queda refutada** (0.758 <
0.80) aunque recall = 720/900 = 0.80 cumpla. La refutación es informativa: dice exactamente
qué mejorar y evita desplegar un sistema que generaría ~230 falsas alarmas mensuales.

## 📊 Propiedades y comparación

| Nivel de evidencia | Ejemplo | ¿Falsable? | Riesgo principal |
|---|---|---|---|
| Demo elegida a mano | "Mira cómo responde bien" | No | Cherry-picking |
| Métrica en entrenamiento | acc=0.99 (train) | Sí, pero irrelevante | Memorización |
| Held-out interno | acc en test split | Sí | Leakage, sobreajuste al benchmark |
| Validación temporal/externa | Datos de otro periodo | Sí | Deriva de distribución (informativa) |
| Replicación independiente | Otro equipo reproduce | Sí | Costo; escasez de incentivos |

```mermaid
flowchart TD
    C["Conjetura audaz<br/>'X supera a B en M sobre D por δ'"] --> P["Predicción observable<br/>y criterio de refutación FIJADO ANTES"]
    P --> E["Experimento con semilla,<br/>datos particionados sin fuga"]
    E --> R{"¿Resultado contradice<br/>la predicción?"}
    R -- "Sí" --> F["❌ Refutada:<br/>información valiosa, revisar H o modelo"]
    R -- "No" --> S["✔️ Corroborada (NO probada):<br/>sobrevive por ahora"]
    S --> T["Someterla a un test más duro:<br/>datos externos, otro periodo, replicación"]
    T --> R
    F --> C
```

## ⚠️ Errores conceptuales frecuentes

1. **"Los datos hablan por sí mismos."** Los datos solo responden preguntas bien planteadas;
   sin hipótesis previa, cualquier patrón encontrado puede ser ruido con buena prensa.
2. **"Mi hipótesis fue confirmada, luego es verdadera."** La corroboración no es prueba;
   solo indica que la hipótesis sobrevivió a *ese* test. La confianza se gana con tests
   progresivamente más duros.
3. **"Más accuracy = mejor modelo."** Sin baseline, tasa base, métrica apropiada al costo
   de error y población definida, la cifra no significa nada (ver ejemplo trabajado).
4. **"Explorar datos está mal."** La exploración es legítima y necesaria; el error es
   disfrazar hallazgos exploratorios de confirmaciones (HARKing). La solución es declarar
   qué fue exploratorio y validar en datos frescos.
5. **"La reproducibilidad es burocracia."** Es la condición mínima para que un resultado
   sea evidencia y no anécdota: sin semilla, versión y datos fijados, ni siquiera el propio
   autor puede verificar su claim.

## 🚀 Del aprendizaje a la operación

En un flujo profesional esto se institucionaliza: hipótesis y métrica de éxito escritas
*antes* del experimento (pre-registro interno); particiones temporales y auditoría de
leakage como paso obligatorio del pipeline; un registro de experimentos fallidos (los
silencios sesgan tanto como los éxitos); y monitoreo post-despliegue que trata cada
predicción en producción como un test continuo de la hipótesis del modelo — con criterios
de rollback definidos de antemano.

## 🧪 Laboratorio

```bash
python lab.py
```

El laboratorio llama a `ai_evolution.labs.run_lab("evaluation")`. Esta
decisión evita 183 implementaciones divergentes: cada clase tiene un entrypoint
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

- [Popper, K. — entrada en la Stanford Encyclopedia of Philosophy (falsabilidad y demarcación)](https://plato.stanford.edu/entries/popper/)
- [Ioannidis, J. (2005). Why Most Published Research Findings Are False. *PLoS Medicine*](https://doi.org/10.1371/journal.pmed.0020124)
- [Kapoor, S. & Narayanan, A. (2023). Leakage and the Reproducibility Crisis in ML-based Science](https://arxiv.org/abs/2207.07048)
- [Sandve et al. (2013). Ten Simple Rules for Reproducible Computational Research. *PLoS Comp Bio*](https://doi.org/10.1371/journal.pcbi.1003285)
- [Pineau et al. (2021). Improving Reproducibility in Machine Learning Research](https://arxiv.org/abs/2003.12206)

---

## ⬅️ Clase anterior

[007 — Lógica, algoritmos y complejidad computacional](../../part-00-foundations-history-and-scientific-method/007-logica-algoritmos-y-complejidad-computacional/README.md)

## ➡️ Siguiente clase

[009 — Entornos Python, Git y experimentos reproducibles](../../part-00-foundations-history-and-scientific-method/009-entornos-python-git-y-experimentos-reproducibles/README.md)
