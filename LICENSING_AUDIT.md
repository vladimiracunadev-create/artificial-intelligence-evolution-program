# Auditoría de licenciamiento

Fecha de corte: **2026-09-22**

Repositorio: `vladimiracunadev-create/artificial-intelligence-evolution-program`

Último commit anterior a los cambios: `00828f8`

## Resultado

Se adoptó un modelo de licencia mixta que preserva las concesiones MIT históricas:
MIT para software; CC BY-NC-SA 4.0 para nuevo contenido educativo y prompts;
registros separados para datos, modelos, activos y terceros; y ausencia de licencia
implícita sobre marcas.

No se migró el código a Apache-2.0. El historial solo muestra a Vladimir Acuña como
autor humano y a Dependabot como automatización, por lo que una migración futura
del código propio podría evaluarse, pero mantener MIT evita introducir una
relicencia innecesaria. Cualquier código copiado o contribución humana descubierta
posteriormente deberá revisarse antes de migrar.

## Evidencia revisada

- `LICENSE`, README, `pyproject.toml`, CONTRIBUTING y documentación principal.
- Historial completo de `LICENSE`, autores, trailers de coautoría y shortlog.
- Código en `src/`, `scripts/` y `apps/`; notebooks, clases, evaluaciones,
  prompts, papers y documentación generada.
- Catálogo de 12 datasets y referencias a modelos/servicios.
- Activos rastreados: iconos, capturas y 165 PDFs generados.
- Dependencias Python y Node declaradas, lockfile Android y herramientas de build.
- Búsqueda de pesos/checkpoints y formatos de datasets dentro de Git.

## Hallazgos y riesgos

| Severidad | Hallazgo | Tratamiento |
|---|---|---|
| Alta | MIT se presentaba como licencia única para código y documentación, incompatible con el alcance CC no comercial deseado. | Alcance separado en `LICENSE`, `LICENSE-CONTENT.md` y matriz del README; el historial MIT se preserva expresamente. |
| Alta | AG News declara licencia `unknown`; CIFAR-10, IMDb y Cora no muestran una licencia de datos explícita en sus fuentes primarias. | Marcados como no determinados y no redistribuibles/comerciales hasta aclaración. |
| Alta | SWE-bench, WebArena y MMLU agregan material procedente de terceros; la licencia del repositorio no necesariamente limpia cada instancia. | Registro exige revisar repositorios, contenido y variantes aguas arriba. |
| Alta | Llama, varias versiones de Gemma y Stable Diffusion usan licencias con restricciones; llamarlas simplemente “open source” sería inexacto. | `MODEL_LICENSES.md` las clasifica como open-weight/source-available cuando corresponde. |
| Media | No había registro de modelos aunque el currículo cita familias con licencias incompatibles entre variantes. | Registro preventivo; ningún peso está versionado actualmente. |
| Media | Los iconos con 🧠 pueden incorporar un glifo de una fuente del sistema al rasterizarse. | Riesgo documentado; se recomienda sustituirlo por un vector original verificable. |
| Media | `npx capacitor-assets` no está fijado como dependencia directa. | Registrar y fijar versión antes de la próxima release; generar inventario de licencias del artefacto. |
| Media | Los paquetes y binarios publicados carecen de un SBOM/archivo de avisos transitivos generado por build. | Requisito documentado en `THIRD_PARTY_NOTICES.md`; pendiente automatización. |
| Baja | Los prompts no tenían alcance expreso. | Incluidos explícitamente en CC BY-NC-SA 4.0. |
| Baja | Las marcas de proveedores podían confundirse con licencias de contenido. | `TRADEMARKS.md` aclara uso nominativo y ausencia de patrocinio. |

## Inventario negativo

No se encontraron pesos, checkpoints, modelos serializados ni datos tabulares/binarios
de los datasets catalogados. Tampoco se detectaron fotografías de stock, copias de
papers originales o código vendorizado. Los PDFs versionados son salidas generadas
desde material pedagógico propio y referencias enlazadas.

## Límite jurídico de la transición

La CC BY-NC-SA 4.0 no revoca la licencia MIT de revisiones anteriores. Quien obtuvo
una copia histórica puede seguir usándola bajo MIT. La nueva licencia gobierna las
nuevas contribuciones y el contenido creativo añadido o modificado desde el primer
commit que contiene estos avisos. Esa realidad reduce el alcance práctico de la
restricción no comercial sobre material que ya existía, y se documenta para no
crear una expectativa jurídica falsa.

## Pendientes recomendados

1. Fijar `@capacitor/assets` y Mermaid por versión e integridad.
2. Generar SBOM y avisos de licencias para wheel, ejecutables, MSI y APK.
3. Sustituir el emoji rasterizado por un icono vectorial original o con licencia
   registrada.
4. Mantener bloqueadas para redistribución las entradas con licencia desconocida.
5. Repetir esta auditoría cuando se añada un dataset, modelo, peso, asset o
   dependencia de runtime.

## Validación ejecutada

- `python -m unittest discover -s tests -v`: **61 tests OK**, incluida la
  ejecución de notebooks y motores.
- `python scripts/validate_repository.py --strict`: **OK**, 15 partes, 183
  clases, 549 notebooks de clase, 148 papers y 156 notebooks de papers.
- `python scripts/generate_papers.py --check`: artefactos al día.
- `python scripts/link_papers_to_classes.py --check`: 171 enlaces de vuelta al día.
- `python -m compileall -q src scripts classes apps`: **OK**.
- `python scripts/verify-sources --json`: **OK**, 618 entradas y 100 % de
  cobertura registrada.
- `python scripts/check_external_links.py`: inventario de **1059** URLs externas;
  las nuevas URLs jurídicas y fuentes primarias se abrieron durante la auditoría.
  El script del proyecto, deliberadamente, no convierte fallos de red en fallos de
  CI local.
- Comprobación temporal de enlaces Markdown locales en los documentos tocados:
  **91 enlaces resueltos, 0 rotos**.
- Búsqueda final de `MIT`: las coincidencias restantes son alcance del código,
  licencias específicas de terceros o referencias históricas expresamente
  preservadas; no queda la afirmación vigente “código y documentación bajo MIT”.
