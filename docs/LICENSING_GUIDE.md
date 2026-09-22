# Guía de licenciamiento

Esta guía explica cómo clasificar material antes de añadirlo. No es asesoría
jurídica; ante una duda material, no incorpore ni redistribuya el archivo hasta
obtener permiso.

## Decisión rápida

| Si añade... | Licencia / registro |
|---|---|
| Código Python/JS, scripts, configuración o fragmentos ejecutables | MIT (`LICENSE`) |
| Clases, explicaciones, tutoriales, ejercicios, evaluaciones, rutas o prompts originales | CC BY-NC-SA 4.0 (`LICENSE-CONTENT.md`) |
| Notebook mixto | Código MIT; texto y estructura pedagógica CC BY-NC-SA 4.0 |
| Dataset o muestra de datos | No hereda licencia; registrar en `DATA_LICENSES.md` antes de incorporarlo |
| Modelo, adapter o pesos | No hereda licencia; registrar versión y términos en `MODEL_LICENSES.md` |
| Imagen, fuente, audio, icono o captura | Registrar en `ASSET_LICENSES.md` |
| Código o texto de terceros | Conservar licencia y aviso en `THIRD_PARTY_NOTICES.md`; no copiar si es incompatible |
| Nombre, logotipo o marca | Solo uso nominativo conforme a `TRADEMARKS.md` |

## Atribución sugerida

> Artificial Intelligence Evolution Program, por Vladimir Acuña
> (`vladimiracunadev-create`), versión o commit `<identificador>`, bajo CC
> BY-NC-SA 4.0. Cambios: `<descripción>`.

Para código, conserve el aviso MIT incluido en `LICENSE`.

## Compatibilidad práctica

- CC BY-NC-SA 4.0 **no es una licencia de código** y su cláusula no comercial no
  cumple la definición OSI de open source. Describa el repositorio como público,
  gratuito y de licencia mixta; describa solo el código MIT como open source.
- No mezcle contenido CC BY-NC-SA dentro de una obra que deba distribuirse bajo
  términos incompatibles. Un enlace o una cita breve con atribución es distinto
  de copiar una obra.
- MIT y Apache-2.0 suelen permitir agregación, pero conserve ambos avisos. No se
  migró el código propio a Apache-2.0 en esta revisión.
- Una tarjeta de Hugging Face es metadato, no garantía. Compare licencia, archivos,
  modelos base y términos del publicador original para la revisión descargada.
- `unknown`, “research use”, “non-commercial” y licencias comunitarias con
  restricciones no deben describirse como open source. Use `source-available` u
  `open-weight` cuando corresponda y explique la restricción.

## Checklist para una contribución

1. Identificar autor, fuente y si existe material de terceros.
2. Elegir la fila de la matriz anterior.
3. Registrar URL, versión/hash, licencia y restricciones.
4. Conservar `LICENSE`, `NOTICE`, atribución y cambios requeridos aguas arriba.
5. Evitar datos personales, secretos, material sin permiso y términos
   incompatibles.
6. Ejecutar tests, validadores y comprobación de enlaces.
7. Revisar que README, manifiestos de paquete y artefactos no afirmen una licencia
   global única.
