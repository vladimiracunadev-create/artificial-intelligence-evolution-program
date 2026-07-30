# 📦 Instalación

## ⚙️ Núcleo

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .
ai-evolution validate
```

## 🛠️ Desarrollo

```bash
pip install -e ".[dev,docs,assets]"
python -m unittest discover -s tests -v
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
