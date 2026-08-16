# 🧾 Plantilla de ficha de paper

> Contrato de 18 secciones. Es **obligatorio y verificado automáticamente**: cada ficha de
> [`papers/foundational/`](../foundational/) debe tener estas 18 secciones, con estos títulos
> exactos y en este orden. Lo comprueba `ai_evolution.papers.validate_papers()`.

Copia el bloque de abajo para dar de alta un paper nuevo. Después registra su entrada en
[`catalog/papers.json`](../catalog/papers.json) y ejecuta:

```bash
python scripts/generate_papers.py
```

## Por qué 18 secciones

Cada una responde a una pregunta que un resumen normal se salta:

| Sección | Pregunta que fuerza a responder |
|---|---|
| 1–3 | ¿Qué había antes, qué propone y quién lo firma? |
| 4–6 | ¿Lo entiendo sin fórmulas, con fórmulas y como flujo? |
| 7–8 | ¿Dónde está la evidencia **en el paper original**? |
| 9–11 | ¿Qué cambió, qué no demuestra y en qué se equivoca la gente? |
| 12–13 | ¿De qué depende y qué hizo posible? |
| 14–17 | ¿Cómo lo ejecuto, lo practico y me autoevalúo? |
| 18 | ¿De dónde salió cada afirmación? |

---

## 📋 Plantilla (copiar desde aquí)

````markdown
# PXX — Título en español

> Una frase que sitúe el hito en la evolución de la IA.

**Nivel:** L? · **Motor:** `nombre` · **Notebook:** enlace relativo a `notebooks/papers/PXX_slug.ipynb`

## 1. Identificación

| Campo | Valor |
|---|---|
| **Título original** | |
| **Autoría** | |
| **Año** | |
| **Venue** | |
| **Fuente primaria** | |
| **Acceso** | abierto / restringido |
| **Fecha de consulta** | AAAA-MM-DD |

## 2. Problema anterior

Qué se hacía antes y por qué no bastaba. **Sin mencionar la solución del paper.**

## 3. Propuesta

La contribución en 3–5 frases. Qué es nuevo y qué reutiliza de trabajos previos.

## 4. Intuición sin fórmulas

Una analogía honesta. Debe declarar dónde deja de funcionar.

## 5. Matemática mínima

Solo las ecuaciones imprescindibles, con todos los símbolos definidos.

## 6. Arquitectura o flujo

Diagrama (mermaid o bloque `text`) del mecanismo, entrada a salida.

## 7. Qué observar en el paper original

Secciones, figuras y tablas concretas que hay que mirar, con su número.

## 8. Evidencia y resultados

Qué demostró, con tarea, dataset, métrica y línea base. Si un número no se ha verificado
en la fuente, se dice explícitamente en lugar de escribirlo.

## 9. Impacto

Qué cambió después. Distinguir impacto documentado de narrativa retrospectiva.

## 10. Limitaciones

Las que el paper admite **y** las que no admite. Mínimo tres.

## 11. Errores comunes

Malentendidos frecuentes, especialmente atribuciones anacrónicas.

## 12. Relación con trabajos anteriores

De qué depende. Con referencia y año.

## 13. Relación con trabajos posteriores

Qué hizo posible. Con referencia y año.

## 14. Notebook asociado

Qué implementa la miniatura, qué **no** implementa y cómo ejecutarla.

## 15. Actividades Bloom

Seis actividades: recordar, explicar, aplicar, analizar, evaluar y crear.

## 16. Autoevaluación

Entre 5 y 8 preguntas. Ninguna de definición pura.

## 17. Respuestas esperadas

Qué debe contener una buena respuesta. No una respuesta modelo para copiar.

## 18. Fuentes primarias

Lista con autores, año, venue, URL y fecha de consulta.
````

---

## ✅ Reglas de calidad no negociables

1. **No inventar** autores, fechas, datasets, métricas ni citas. Si no lo verificaste,
   escribe «verificar en la tabla N del paper» en lugar del número.
2. **No atribuir** al paper ideas posteriores (sección 11 existe para eso).
3. **Marcar** siempre qué es hecho documentado, simplificación didáctica, inferencia propia
   o práctica moderna.
4. **Fuente primaria obligatoria** con URL y fecha de consulta.
5. **No redistribuir** PDFs con restricciones de copyright: se enlaza.
6. **Sin rutas absolutas** en ningún ejemplo ni notebook.
7. **Limitaciones antes que entusiasmo**: la sección 10 no puede quedar en una línea.

## 🔍 Cómo se verifica

```bash
python -c "import sys; sys.path.insert(0,'src'); from ai_evolution.papers import validate_papers; print(validate_papers(strict=True))"
```

Comprueba: las 18 secciones y su orden, la existencia del notebook y sus 17 momentos, que el
motor exista, que haya fuente primaria con URL, que las clases enlazadas existan y que los
SHA-256 del manifiesto estén al día.

---

[⬅️ Eje de papers](../README.md) ·
[📖 Cómo leer un paper](COMO_LEER_UN_PAPER_DE_IA.md) ·
[🔁 Método en 5 pasadas](METODO_DE_LECTURA_EN_5_PASADAS.md) ·
[📚 Glosario](GLOSARIO_PAPERS_IA.md)
