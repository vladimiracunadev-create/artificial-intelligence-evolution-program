# Registro de modelos y pesos

El árbol Git auditado **no contiene pesos, checkpoints, adapters ni modelos
serializados** (`.safetensors`, `.pt`, `.pth`, `.ckpt`, `.onnx`, `.gguf`, `.pkl`
o `.joblib`). Las menciones de arquitecturas en clases y papers son referencias
pedagógicas, no distribución del artefacto.

La licencia del código de carga, de una librería o de Hugging Face **no licencia
los pesos**. Antes de añadir o descargar un modelo debe fijarse repositorio,
revisión, variante y licencia exactos.

Estado verificado el **2026-09-22**.

| Modelo o servicio citado | Licencia / términos | Clasificación y restricciones relevantes | Estado en este repositorio |
|---|---|---|---|
| DeepSeek-R1 | [MIT para código y pesos](https://huggingface.co/deepseek-ai/DeepSeek-R1) | El modelo principal permite uso comercial. Los distill sobre Qwen remiten a Apache-2.0; los distill sobre Llama conservan además la licencia comunitaria de Llama correspondiente. | Referencia pedagógica; no se distribuyen pesos. |
| Meta Llama 3.x | [Llama Community License](https://github.com/meta-llama/llama-models/tree/main/models) | Licencia personalizada con política de uso, avisos, requisitos de nombre/atribución y umbral comercial de 700 millones de usuarios para Llama 3.3. **Source-available/open-weight; no describir como open source OSI.** | Referencia pedagógica; no se distribuyen pesos. |
| Stable Diffusion | Licencia específica de cada versión; por ejemplo [Stability AI Community License para SD 3.5](https://huggingface.co/stabilityai/stable-diffusion-3.5-large/blob/main/LICENSE.md) | SD 3.5 limita el uso comercial gratuito según ingresos y exige registro/avisos; versiones anteriores pueden usar OpenRAIL. **No asumir una licencia común a toda la familia ni llamarla open source sin calificar.** | Referencia pedagógica; no se distribuyen pesos. |
| Gemma | [Términos de Gemma 3 y anteriores](https://ai.google.dev/gemma/terms); Gemma 4 declara Apache-2.0 en su model card | Las versiones anteriores a Gemma 4 incluyen restricciones de uso y obligaciones de redistribución; son open-weight/source-available, no equivalentes a Apache-2.0. Registrar versión exacta. | Referencia pedagógica; no se distribuyen pesos. |
| Mistral | [Política de licencias de modelos](https://help.mistral.ai/en/articles/347393-under-which-license-are-mistral-s-open-models-available) | La familia mezcla Apache-2.0 y licencias modificadas con umbrales comerciales. La marca de familia no basta: manda la model card de la revisión. | Referencia pedagógica; no se distribuyen pesos. |
| BERT, T5, CLIP, Whisper y otros checkpoints académicos | Variable por publicador, checkpoint y derivados | El paper o la arquitectura no concede licencia sobre un checkpoint. Registrar cada identificador antes de incorporarlo. | Solo conceptos, miniaturas locales o enlaces; no hay pesos. |
| OpenAI, Anthropic y Gemini API | Términos contractuales del proveedor, no licencia de software/pesos | Servicios propietarios; revisar términos, políticas de uso, privacidad, datos de entrada y derechos sobre salida vigentes al ejecutar. **No son componentes open source.** | APIs opcionales descritas; no son dependencia de ejecución ni se incluyen credenciales. |

## Campos obligatorios para futuras incorporaciones

Nombre, proveedor, identificador exacto, revisión/hash, URL, autor/titular,
licencia completa, restricciones comerciales y de uso, modelos base, licencia de
datos de entrenamiento cuando se conozca, fecha de verificación, ruta/checksum y
si se redistribuye o solo se descarga bajo decisión del usuario.
