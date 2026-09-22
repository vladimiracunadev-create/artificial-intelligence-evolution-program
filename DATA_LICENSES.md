# Registro de licencias de datasets

El repositorio mantiene enlaces y metadatos; **no contiene copias de estos
datasets**. La licencia general del proyecto no se aplica a los datos descargados.
Antes de descargar, redistribuir o usar comercialmente una versión, compruebe su
ficha y conserve la evidencia de licencia de esa versión.

Estado verificado el **2026-09-22**.

| Dataset | Origen y fuente | Autor o responsable | Licencia declarada | Restricciones / riesgo | Uso previsto aquí |
|---|---|---|---|---|---|
| Adult (Census Income) | [UCI, DOI 10.24432/C5XW20](https://archive.ics.uci.edu/dataset/2/adult) | Barry Becker y Ronny Kohavi | CC BY 4.0 | Atribución; contiene atributos demográficos sensibles; revisar finalidad, sesgo y normativa aplicable. | Clasificación, fairness y costo de error. |
| Wine Quality | [UCI, DOI 10.24432/C56S3T](https://archive.ics.uci.edu/dataset/186/wine+quality) | Paulo Cortez, A. Cerdeira, F. Almeida, T. Matos y J. Reis | CC BY 4.0 | Atribución y cita de la versión. | Regresión, clasificación y calibración. |
| CIFAR-10 | [Página oficial](https://www.cs.toronto.edu/~kriz/cifar.html) | Alex Krizhevsky, Vinod Nair y Geoffrey Hinton | **No se encontró licencia explícita** en la fuente oficial | No asumir permiso de redistribución; deriva de 80 Million Tiny Images. Descargar solo para el uso permitido por la fuente y pedir autorización para redistribución/comercialización. | Visión y aprendizaje autosupervisado. |
| Fashion-MNIST | [Repositorio oficial](https://github.com/zalandoresearch/fashion-mnist) | Han Xiao, Kashif Rasul, Roland Vollgraf / Zalando SE | MIT en el repositorio, incluidos los datos allí publicados | Conservar copyright y licencia; citar el paper. Verificar cualquier espejo por separado. | Clasificación, VAE, GAN y difusión. |
| AG News (`fancyzhx/ag_news`) | [Tarjeta en Hugging Face](https://huggingface.co/datasets/fancyzhx/ag_news) | Xiang Zhang, Junbo Zhao y Yann LeCun; espejo `fancyzhx` | **Unknown** en la tarjeta | Incluye noticias de Reuters, AP y otros editores. No redistribuir ni usar comercialmente sin aclarar derechos del corpus y artículos subyacentes. | Clasificación y fine-tuning, solo tras revisión. |
| IMDb Large Movie Review v1.0 | [Fuente de Stanford](https://ai.stanford.edu/~amaas/data/sentiment/) | Andrew L. Maas et al.; reseñas de usuarios de IMDb | **No se encontró licencia explícita** | La publicación como benchmark no equivale a una licencia general; contenido y términos de IMDb pueden limitar reutilización. No redistribuir ni usar comercialmente sin autorización. | Sentimiento, RNN y transformers. |
| Speech Commands v0.02 | [Descarga original](http://download.tensorflow.org/data/speech_commands_v0.02.tar.gz) y [catálogo TFDS](https://www.tensorflow.org/datasets/catalog/speech_commands) | Pete Warden / Google y participantes | CC BY 4.0, según el archivo de licencia de la distribución | Atribución; conservar versión y licencia del archivo descargado. La licencia Apache de TFDS cubre el cargador, no sustituye la del dataset. | Audio y edge AI. |
| Mozilla Common Voice | [Mozilla Data Collective](https://commonvoice.mozilla.org/en/datasets) | Mozilla y comunidad de contribuyentes | CC0 1.0 para las versiones que así lo indiquen | La versión y locale deben registrarse; pueden existir condiciones de acceso/privacidad y datasets excepcionales con otra licencia. | ASR y evaluación por grupos. |
| Cora / Planetoid | [Documentación PyG](https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.Planetoid.html) y [fuente LINQS](https://linqs.org/datasets/) | LINQS / Sen et al. | **No se encontró licencia explícita del dataset** | La licencia de PyTorch Geometric no cubre Cora. No redistribuir ni usar comercialmente hasta obtener términos claros de la fuente. | GNN y grafos de conocimiento. |
| SWE-bench | [Repositorio oficial](https://github.com/SWE-bench/SWE-bench) y [dataset](https://huggingface.co/datasets/SWE-bench/SWE-bench) | Carlos E. Jimenez et al. / SWE-bench Team | MIT para el repositorio; revisar la tarjeta de cada variante | Las instancias incorporan issues, parches y código de repositorios con licencias propias. Cumplir cada licencia aguas arriba; algunas variantes no declaran licencia separada. | Evaluación de agentes de programación. |
| WebArena | [Repositorio oficial](https://github.com/web-arena-x/webarena) | Shuyan Zhou et al. | Apache-2.0 para el repositorio | Los sitios, dumps, imágenes, contenido y servicios simulados pueden tener avisos propios; la licencia del código no cubre automáticamente todos los datos. | Evaluación de agentes de navegador. |
| MMLU | [Repositorio oficial](https://github.com/hendrycks/test) | Dan Hendrycks et al. | MIT declarada por el repositorio | Preguntas recopiladas de fuentes educativas externas; la licencia de la colección puede no resolver derechos de cada pregunta. No redistribuir una copia sin revisar procedencia. | Evaluación de conocimiento y límites de benchmarks. |

## Regla de incorporación

Toda nueva entrada debe registrar: identificador y versión exacta, origen, URL,
autor, licencia con enlace, restricciones, finalidad, fecha de verificación y, si
se almacena localmente, checksum y ruta. `desconocida` no significa dominio
público: bloquea la redistribución hasta resolverla.
