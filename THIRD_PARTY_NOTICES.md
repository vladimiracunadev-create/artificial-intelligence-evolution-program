# Avisos de terceros

Este archivo identifica dependencias y materiales de terceros; no sustituye sus
textos de licencia. Las versiones exactas están en `pyproject.toml` y
`apps/android/package-lock.json`. Verificado el **2026-09-22**.

## Dependencias directas

| Componente | Uso | Licencia declarada aguas arriba |
|---|---|---|
| [PyYAML](https://github.com/yaml/pyyaml) | Ejecución principal | MIT |
| [setuptools](https://github.com/pypa/setuptools) y [wheel](https://github.com/pypa/wheel) | Build Python | MIT |
| [MkDocs](https://github.com/mkdocs/mkdocs) | Documentación opcional | BSD-2-Clause |
| [Material for MkDocs](https://github.com/squidfunk/mkdocs-material) | Tema de documentación opcional | MIT |
| [ReportLab](https://github.com/MrBitBucket/reportlab-mirror) | Generación de PDF | BSD-style; revisar `LICENSE.txt` de la versión instalada |
| [python-pptx](https://github.com/scanny/python-pptx) | Generación de presentaciones | MIT |
| [PyInstaller](https://github.com/pyinstaller/pyinstaller) | Empaquetado de escritorio | GPL-2.0-or-later con excepción especial para distribuir aplicaciones empaquetadas; conservar avisos |
| [Capacitor Core, Android y CLI](https://github.com/ionic-team/capacitor) | Aplicación Android | MIT |
| [Mermaid](https://github.com/mermaid-js/mermaid) | Diagramas cargados desde CDN | MIT; la versión debe fijarse al publicar para reproducibilidad |

Las dependencias transitivas conservan sus licencias individuales. Un artefacto
publicado (wheel, exe, MSI o APK) debe generar y adjuntar un inventario SBOM o un
informe de licencias de las versiones efectivamente empaquetadas; esta tabla no
autoriza a omitir avisos requeridos por dependencias transitivas.

## Código, datos y contenido externos

- No se detectó código fuente de terceros copiado o vendorizado en el árbol.
- Papers, libros, normas y documentación se enlazan y citan; no quedan
  relicenciados por este proyecto. El registro bibliográfico vive en `sources/`.
- Datasets y modelos se rigen por `DATA_LICENSES.md` y `MODEL_LICENSES.md`.
- GitHub Actions, Android SDK/JDK, Inno Setup, WiX y herramientas de build se usan
  para construir; cada una conserva sus propios términos y no se redistribuye bajo
  MIT o CC por el mero hecho de aparecer en CI.

## Riesgos operativos abiertos

- El workflow Android invoca `npx capacitor-assets` sin declararlo como dependencia
  directa fijada; antes de una release debe fijarse la versión y capturarse su
  licencia en el inventario del build.
- Los recursos cargados desde CDN deben fijar versión e integridad cuando sea
  viable; disponibilidad pública no equivale a permiso de relicenciamiento.
