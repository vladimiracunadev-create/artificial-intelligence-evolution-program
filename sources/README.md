# 🧾 Registro general de fuentes

> Fuente única: [`bibliography.json`](bibliography.json).
> Cifras al día: las escribe `python scripts/verify-sources --write` en el
> [README raíz](../README.md#-registro-de-fuentes). Aquí no se copian a mano.

El eje de papers responde **de dónde salió cada idea**. Este registro responde
**con qué se estudia**: además de los artículos fundacionales incluye los libros de
texto, las normas, la documentación oficial y los conjuntos de datos que las 183
clases citan de hecho.

De aquí salen tres cosas que nadie escribe a mano:

| Sale de aquí | Qué es | Quién lo escribe |
|---|---|---|
| El bloque **📚 Bibliografía de apoyo** de cada clase | la obra que desarrolla el contenido de esa clase, con edición, localizador y el capítulo cuando la cita lo indica | `scripts/link_sources_to_classes.py` |
| [`BIBLIOGRAFIA.md`](BIBLIOGRAFIA.md) | la bibliografía completa del programa, por parte y por obra | `scripts/verify-sources --write` |
| La tabla parte → obra del [README raíz](../README.md#-bibliografía-de-apoyo) | qué obra sostiene cada una de las 15 partes | `scripts/verify-sources --write` |

## El mapa de apoyo

[`support_map.json`](support_map.json) dice qué obra de referencia sostiene cada parte del
programa, con qué alcance y por qué. Es el único fichero **curado a mano** de este directorio, y
aun así no contiene ni un ISBN ni un título: solo identificadores de entradas de
[`bibliography.json`](bibliography.json). El criterio es mapear el manual que las propias clases
de esa parte ya citan; cuando una parte no cita ninguno, se mapea el texto de referencia del área
y la nota dice qué cubre. El verificador rechaza cualquier obra del mapa que no tenga ISBN-13 con
dígito de control válido.

## Qué NO cambia

[`papers/catalog/papers.json`](../papers/catalog/papers.json) funciona y no se toca.
El registro lo **incluye por referencia** en su campo `includes`; el eje de papers
sigue siendo la fuente de verdad de las 148 fichas fundacionales.

## Regla de aceptación

Cada entrada necesita un **localizador resoluble**. Se admiten exactamente tres formas:

| Tipo | Localizador | Forma canónica |
|---|---|---|
| `book` | ISBN-13 con dígito de control válido | `https://openlibrary.org/isbn/{isbn13}` |
| `paper` | DOI | `https://doi.org/{doi}` |
| `standard`, `reference`, `dataset` | URL https de la fuente primaria | la propia URL, con `accessed` |

Lo que no resuelve queda con `"status": "pendiente"` y un `pending_reason` que dice
por qué. **Nunca se borra una fuente que no resolvió y nunca se completa un
localizador por intuición.** Un hueco declarado es información; un hueco rellenado a
ojo es una invención con formato de bibliografía.

## Decisiones que conviene conocer

- **Los tres libros rectores** —AIMA, *Deep Learning* y *Speech and Language
  Processing*— llevan ISBN-13 y la URL del autor en `homepage`. De SLP se registra la
  edición impresa con ISBN: la 3.ª circula como borrador abierto y no tiene ISBN, y eso
  se dice en el campo `edition` en vez de inventar uno.
- **NIST AI RMF** es `standard` con `version` **1.0** —la que declara la propia cita— y fecha
  de consulta. **OWASP Top 10 for LLM Applications** es `standard` con fecha de consulta y
  **sin** `version`: la portada del proyecto no numera la lista, y una versión inventada sería
  exactamente el defecto que este registro existe para evitar.
- **Los ISBN que vienen en la URL del editor** (MIT Press y O'Reilly los ponen en la ruta) se
  toman de ahí, se les comprueba el dígito de control y se resuelven en Open Library. Si el
  título del catálogo no coincide con el que se dedujo del texto de la cita, manda el catálogo:
  el ISBN lo puso el editor, el título lo dedujo un `regex`.
- **La documentación de proveedores de modelos** (Anthropic, OpenAI, Google, Hugging
  Face…) es `reference` volátil: lleva `volatile: true` y `accessed` obligatorio,
  porque cambia sin aviso y sin número de versión.
- **Los artículos de arXiv** usan el DOI que arXiv registra para cada artículo
  (`10.48550/arXiv.<id>`). Los identificadores antiguos (`cs/0301001`) no tienen DOI
  derivable y nacen pendientes.
- **Un contenedor no es una obra.** Cuando un título en cursiva aparece en citas de
  fuentes distintas es la revista o las actas (*Artificial Intelligence*,
  *Communications of the ACM*), y se registra en `container`, no como entrada propia.
- **Las remisiones internas del repositorio** (`frontier/`, un notebook, otra clase) no
  son fuentes externas y no entran en el registro.

## Anatomía de una entrada

```json
{
  "id": "russell-norvig-aima",
  "type": "book",
  "authors": ["Russell, Stuart J.", "Norvig, Peter"],
  "title": "Artificial Intelligence: A Modern Approach",
  "published": "2020",
  "edition": "4.ª",
  "isbn13": "9780134610993",
  "locator": "https://openlibrary.org/isbn/9780134610993",
  "homepage": "https://aima.cs.berkeley.edu/",
  "authority": "Pearson",
  "url_keys": ["aima.cs.berkeley.edu"],
  "aliases": ["artificial intelligence: a modern approach", "aima"],
  "used_in": ["classes/part-00-.../001-.../README.md"],
  "uses": 38,
  "status": "verificada",
  "isbn_source": "edicion-declarada",
  "checked": {"last_check": "AAAA-MM-DD", "method": "openlibrary", "ok": true}
}
```

`url_keys` y `aliases` son las claves con las que el verificador comprueba que **toda**
obra y **todo** enlace que una clase usa existe en el registro. `checked` es lo que
respondió la red la última vez: es un hecho registrado, no una promesa.

## Las dos capas, separadas a propósito

```bash
python scripts/verify-sources          # offline, determinista, bloquea CI
python scripts/verify-sources --write  # además regenera las cifras del README
python scripts/refresh-sources         # en red, manual, NO bloquea
```

`verify-sources` no toca la red. `refresh-sources` sí, y por eso no entra en CI: si la
red entra en el CI, el CI se vuelve inestable y se acaba ignorando. `refresh-sources`
reporta lo que dejó de resolver, sin borrarlo.

Open Library responde de forma **intermitente**: alterna respuestas correctas con
caídas de minutos. Cuando eso pasa, los libros afectados quedan `pendiente` con ese
motivo exacto —no con uno inventado— y se recuperan reintentando. El dígito de control
del ISBN-13 sí se comprueba sin red, así que un ISBN mal copiado se detecta igual.

Para reintentar solo lo pendiente después de una caída de red:

```bash
python scripts/refresh-sources --only pending --sleep 0.6
```

## Cómo se reconstruye

```bash
python scripts/build_sources.py             # registro desde lo que las clases citan
python scripts/annotate_class_sources.py    # declara el uso de cada fuente en su clase
python scripts/link_sources_to_classes.py   # bibliografía de apoyo en cada clase
python scripts/verify-sources --write       # README y BIBLIOGRAFIA.md
```

O de una vez: `make sources`. Para comprobar sin escribir: `make sources-check`.

`build_sources.py` es determinista y offline, y **conserva** todo lo que
`refresh-sources` resolvió: nunca degrada una entrada verificada.

## El uso declarado en cada clase

Cada cita de cada clase declara para qué sirve ahí. Cuando la cita ya traía su propia
explicación se respeta tal cual; cuando no, se añade el papel de la fuente con un
vocabulario controlado y derivado de su tipo:

| Tipo | Uso declarado |
|---|---|
| `paper` | fuente primaria del mecanismo estudiado |
| `book` | desarrollo extendido del tema |
| `standard` | marco normativo de referencia |
| `reference` | referencia consultada en su fuente original |
| `dataset` | datos de referencia |

Es mecánico a propósito. Redactar un motivo distinto para cada par (clase, fuente)
exigiría inventarlo, y este repositorio no inventa aparato crítico.
