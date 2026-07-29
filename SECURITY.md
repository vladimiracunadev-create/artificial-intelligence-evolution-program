# Seguridad

## Reporte

No publiques vulnerabilidades, credenciales ni datos personales en issues.
Describe el problema de manera privada al mantenedor.

## Postura

- Los laboratorios base no requieren secretos.
- Las integraciones externas deben usar variables de entorno.
- Tools con efectos laterales deben aplicar allowlists y aprobación.
- No se ejecutan instrucciones recuperadas desde documentos como si fueran confiables.
- Los datasets no se descargan ni reemplazan silenciosamente.
- El sitio no envía telemetría; el progreso usa `localStorage`.

## Amenazas cubiertas pedagógicamente

Prompt injection, tool abuse, exfiltración de secretos, exceso de permisos,
dependencias comprometidas, contenido no confiable, datos sensibles,
alucinaciones y automatización irreversible.

Consulta `docs/THREAT_MODEL.md`.
