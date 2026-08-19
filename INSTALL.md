# 📦 Instalación

## ⚙️ Núcleo

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .
ai-evolution validate
```

Requiere Python 3.11 o superior. La única dependencia del núcleo es `PyYAML`:
las 183 clases y los 148 papers se ejecutan con la biblioteca estándar.

## 📜 Eje de papers

```bash
ai-evolution papers                 # los 148 hitos del eje
ai-evolution paper P08              # ficha de Attention Is All You Need
ai-evolution paper-lab P08 --seed 7 # ejecuta su miniatura
jupyter lab notebooks/papers/       # los 156 notebooks
```

## 🛠️ Desarrollo

```bash
pip install -e ".[dev,docs,assets]"
python -m unittest discover -s tests -v
python scripts/generate_papers.py --check
```

## 📕 Regenerar PDFs

Requiere Chrome o Edge instalado (impresión headless) y `pip install markdown`.

```bash
python scripts/generate_pdfs.py --papers   # solo el eje de papers
python scripts/generate_pdfs.py --clases   # partes y programa completo
```

## 🌐 Web

```bash
python -m http.server 8080
```

## 🖥️ Escritorio

```bash
python apps/desktop/main.py
```

## 🐳 Docker

```bash
docker compose up --build
```
