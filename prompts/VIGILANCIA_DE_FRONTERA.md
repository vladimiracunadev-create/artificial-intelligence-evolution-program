# 🔭 Prompt — vigilancia de frontera

> Revisión periódica de novedades, con fecha y fuente. Pensado para ejecutarse cada 30–90 días
> y alimentar [`frontier/current-topics.yaml`](../frontier/current-topics.yaml), **no** el eje
> de papers fundacionales.

---

## Prompt

```text
Fecha de hoy: {{FECHA}}
Última revisión registrada: {{FECHA_ANTERIOR}}
Área de vigilancia: {{AREA}}   (ej.: agentes, alineación, contexto largo, evaluación)

Actúa como analista de investigación. Tu salida alimenta un registro de FRONTERA:
lo emergente, con fecha y fuente, sin presentarlo como estable.

Para el periodo entre las dos fechas, entrega:

A) NOVEDADES CON EVIDENCIA (máximo 5)
   Para cada una: título · autoría · año · venue · URL · una frase sobre qué
   demuestra · una frase sobre qué NO demuestra · madurez.
   Madurez, elige una:
     emergente   preprint reciente sin replicación independiente
     en_debate   con revisiones públicas o réplicas contradictorias
     consolidando resultados replicados por terceros
     estable     tratado como conocimiento asentado por la comunidad

B) LO QUE CAMBIÓ DE ESTADO
   Trabajos ya registrados que hayan subido o bajado de madurez, y por qué.

C) RUIDO DESCARTADO
   Qué NO incluiste pese a haber tenido mucha atención, y el motivo.
   Esta sección es obligatoria: sin ella, la vigilancia solo amplifica el hype.

D) IMPACTO SOBRE EL PROGRAMA
   Si algo afecta a una clase o a una ficha existente, di a cuál y qué habría que cambiar.
   Si nada lo afecta, dilo explícitamente. No inventes trabajo.

REGLAS:
- Solo fuentes primarias verificables con URL.
- Nada asciende a papers/foundational/ en esta revisión: eso exige consolidación.
- Si no encontraste nada relevante, dilo. Un periodo sin novedades es un resultado válido.
- No inventes papers, autores, fechas ni URLs. Ante la duda, omite.
```

---

## Qué hacer con la salida

1. Añadir A) y B) a [`frontier/current-topics.yaml`](../frontier/current-topics.yaml) con la
   fecha de revisión.
2. Guardar C) en el propio registro: el ruido descartado es información, y protege de repetir
   el análisis cada trimestre.
3. Si D) señala una ficha del eje, actualizar **la sección 13** de esa ficha (relación con
   trabajos posteriores) y su fecha de consulta.
4. Regenerar y verificar:

```bash
python scripts/generate_papers.py
python scripts/validate_repository.py --strict
```

## Criterio de ascenso a `papers/foundational/`

Un trabajo solo entra en el eje fundacional cuando cumple **todas**:

- [ ] tiene venue revisado por pares o replicación independiente documentada;
- [ ] su resultado ha sido usado como base por trabajos posteriores;
- [ ] existe una miniatura ejecutable posible en Python estándar, sin APIs pagadas;
- [ ] se puede escribir su sección 11 (errores comunes) con casos reales, no hipotéticos;
- [ ] han pasado al menos 12 meses desde su publicación.

Mientras tanto, vive en la frontera. Con fecha.

---

[⬅️ Prompts](README.md) · [📜 Eje de papers](../papers/README.md) ·
[🌐 Fuentes y venues](../papers/guides/FUENTES_Y_VENUES.md)
