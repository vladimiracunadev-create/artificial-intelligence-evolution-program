# 🔍 Prompt — lectura crítica de un paper

> Para cuando encuentras un paper y quieres interrogarlo, no que te lo resuman.
> Sustituye `{{URL}}` y `{{TITULO}}` antes de usarlo.

---

## Prompt

```text
Voy a analizar el paper "{{TITULO}}" ({{URL}}).

Actúa como un revisor escéptico y riguroso. No resumas el paper: INTERRÓGALO.

Estructura tu respuesta en estas ocho preguntas, en este orden:

1. ¿Qué se hacía antes de este trabajo y por qué no bastaba?
   No menciones la solución del paper en esta respuesta.

2. ¿Cuál es la afirmación central, en una frase, SIN usar el vocabulario del paper?

3. ¿Qué evidencia la sostiene? Para cada resultado principal indica:
   tarea · dataset · métrica · línea base · número de ejecuciones · semillas · cómputo.
   Si alguno de los seis falta en el paper, dilo explícitamente.

4. ¿Contra qué se compara y recibió esa línea base el mismo esfuerzo de ajuste?

5. ¿Qué dicen las ablaciones? Si no hay ablaciones, dilo: es una debilidad, no un olvido.

6. ¿Qué NO demuestra este paper? Mínimo tres cosas.

7. ¿Qué resultado imaginable lo refutaría? Si no existe ninguno, no es una afirmación empírica.

8. ¿Qué ideas que hoy se le atribuyen aparecieron en realidad DESPUÉS?
   Da la referencia posterior con año.

REGLAS OBLIGATORIAS:
- Marca cada afirmación tuya como [DOCUMENTADO], [INFERENCIA] o [NO VERIFICADO].
- No inventes cifras. Si no la viste en una tabla concreta, escribe
  "verificar en la fuente" e indica en qué tabla o sección debería estar.
- No inventes autores, años, DOIs ni URLs.
- Si no tienes acceso al texto completo, dilo al principio y limita tu análisis
  a lo que el abstract permite.
```

---

## Cómo usar el resultado

1. **Verifica todo lo marcado como `[DOCUMENTADO]`** abriendo el paper. Es el paso que no se
   puede delegar.
2. Convierte lo verificado en una entrada de tu
   [bitácora](../student/papers/BITACORA.md).
3. Si el paper merece pasar a la pasada 3 del
   [método de 5 pasadas](../papers/guides/METODO_DE_LECTURA_EN_5_PASADAS.md), escribe la
   miniatura del mecanismo.
4. Si merece entrar al eje, usa el
   [prompt maestro](PROMPT_MAESTRO_PAPERS.md) y la
   [plantilla de ficha](../papers/guides/PLANTILLA_FICHA_PAPER.md).

---

[⬅️ Prompts](README.md) · [📖 Cómo leer un paper](../papers/guides/COMO_LEER_UN_PAPER_DE_IA.md)
