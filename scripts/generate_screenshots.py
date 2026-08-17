from __future__ import annotations

"""Capturas del sitio y de las apps para la documentación.

El sitio es lo que muestran la PWA y la app Android —Capacitor carga `site/`
dentro de un WebView—, así que estas capturas son la interfaz real de la app,
no una maqueta. La app de escritorio es nativa (tkinter) y se captura aparte
con `--escritorio`, que abre una ventana.

Requiere Chrome o Edge instalado (mismo binario que usa `generate_pdfs.py`).

Uso::

    python scripts/generate_screenshots.py            # sitio, móvil y escritorio
    python scripts/generate_screenshots.py --escritorio  # además, la app nativa
"""

import argparse
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "screenshots"

BROWSERS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium-browser",
]

# (nombre, página del sitio, ancho, alto)
CAPTURAS = [
    ("app-movil-portada", "index.html", 412, 915),
    ("app-movil-clase", "classes/055.html", 412, 915),
    ("app-movil-paper", "papers/P08_transformer.html", 412, 915),
    ("sitio-portada", "index.html", 1440, 900),
    ("sitio-clase", "classes/055.html", 1440, 1100),
    ("sitio-matriz", "papers/matriz.html", 1440, 1100),
    ("sitio-ficha", "papers/P44_resnet.html", 1440, 1100),
]


def find_browser() -> str:
    for candidate in BROWSERS:
        if Path(candidate).exists():
            return candidate
    raise SystemExit("no se encontró Chrome/Edge para capturar")


MARCO = """<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;padding:0;background:#070b17;overflow:hidden}}
iframe{{width:{ancho}px;height:{alto}px;border:0;display:block}}
</style></head><body><iframe src="{origen}"></iframe></body></html>"""


def capturar(browser: str, nombre: str, pagina: str, ancho: int, alto: int) -> Path:
    """Captura la página con un viewport REAL de `ancho`×`alto`.

    `--window-size` de Chrome headless solo recorta la imagen: la maquetación
    sigue usando el viewport por defecto, así que una captura «de móvil» salía
    con el texto cortado aunque el sitio es responsive. Un `iframe` del tamaño
    exacto sí crea un viewport de ese ancho y las media queries se aplican.
    """
    destino = OUT / f"{nombre}.png"
    origen = (ROOT / "site" / pagina).as_uri()
    with tempfile.TemporaryDirectory() as tmp:
        marco = Path(tmp) / "marco.html"
        marco.write_text(MARCO.format(ancho=ancho, alto=alto, origen=origen), encoding="utf-8")
        subprocess.run(
            [
                browser,
                "--headless=new",
                "--disable-gpu",
                "--hide-scrollbars",
                "--allow-file-access-from-files",
                f"--window-size={ancho},{alto}",
                "--virtual-time-budget=20000",
                f"--screenshot={destino}",
                marco.as_uri(),
            ],
            check=True,
            capture_output=True,
            timeout=180,
        )
    if not destino.exists() or destino.stat().st_size < 5_000:
        raise SystemExit(f"captura vacía o ausente: {destino}")
    return destino


TITULO_VENTANA = "Artificial Intelligence Evolution Program"


def _rect_de_la_ventana(titulo: str) -> tuple[int, int, int, int] | None:
    """Coordenadas de la ventana por título, en Windows. None si no se encuentra."""
    if sys.platform != "win32":
        return None
    import ctypes
    from ctypes import wintypes

    user32 = ctypes.windll.user32
    hwnd = user32.FindWindowW(None, titulo)
    if not hwnd:
        return None
    user32.SetForegroundWindow(hwnd)
    rect = wintypes.RECT()
    # ventana visible real: incluye sombra y bordes de DWM
    ok = ctypes.windll.dwmapi.DwmGetWindowAttribute(
        wintypes.HWND(hwnd), ctypes.c_uint(9),  # DWMWA_EXTENDED_FRAME_BOUNDS
        ctypes.byref(rect), ctypes.sizeof(rect))
    if ok != 0:
        user32.GetWindowRect(hwnd, ctypes.byref(rect))
    return rect.left, rect.top, rect.right, rect.bottom


def capturar_escritorio() -> Path | None:
    """Abre la app nativa, captura SOLO su ventana y la cierra.

    Nunca se captura la pantalla completa: arrastraría lo que haya abierto en el
    escritorio de quien ejecuta el script, y esta imagen se publica.
    """
    try:
        from PIL import ImageGrab
    except ImportError:
        print("  · app de escritorio omitida: falta Pillow (`pip install pillow`)")
        return None
    # se arranca en proceso aparte con un guion que despliega una parte y
    # selecciona una clase: la app vacia no ensena lo que la app hace
    guion = f'''
import sys, pathlib
sys.path.insert(0, r"{(ROOT / "apps" / "desktop").as_posix()}")
from main import ProgramApp
app = ProgramApp()
app.geometry("1100x680+40+40")
app.update()
partes = app.tree.get_children()
if partes:
    objetivo = partes[4] if len(partes) > 4 else partes[0]
    app.tree.item(objetivo, open=True)
    clases = app.tree.get_children(objetivo)
    if clases:
        app.tree.selection_set(clases[6] if len(clases) > 6 else clases[0])
        app.tree.see(clases[6] if len(clases) > 6 else clases[0])
app.update()
app.mainloop()
'''
    proceso = subprocess.Popen([sys.executable, "-c", guion])
    try:
        time.sleep(6)  # que termine de pintar el catálogo
        rect = _rect_de_la_ventana(TITULO_VENTANA)
        if rect is None:
            print("  · app de escritorio omitida: no se localizó la ventana; "
                  "no se captura la pantalla completa por privacidad")
            return None
        destino = OUT / "app-escritorio.png"
        ImageGrab.grab(bbox=rect).save(destino)
        return destino
    finally:
        proceso.terminate()


def main() -> int:
    parser = argparse.ArgumentParser(description="Capturas para la documentación")
    parser.add_argument("--escritorio", action="store_true",
                        help="captura además la app nativa (abre una ventana)")
    args = parser.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    browser = find_browser()
    for nombre, pagina, ancho, alto in CAPTURAS:
        destino = capturar(browser, nombre, pagina, ancho, alto)
        print(f"  · {destino.relative_to(ROOT).as_posix()} → {destino.stat().st_size // 1024} kB")

    if args.escritorio:
        destino = capturar_escritorio()
        if destino:
            print(f"  · {destino.relative_to(ROOT).as_posix()} → {destino.stat().st_size // 1024} kB")

    print(f"capturas en {OUT.relative_to(ROOT).as_posix()}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
