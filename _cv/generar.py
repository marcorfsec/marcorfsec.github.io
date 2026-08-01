"""Genera las dos versiones del CV en PDF a partir de un único `cv.html`.

  - **Pública** — `assets/cv/CV-Marco-Rodriguez-Fernandez.pdf`
    Sin teléfono. Es la que se publica en la web, así que queda indexada por
    Google y expuesta a rastreadores. El contacto es el correo.

  - **Privada** — `CV-Marco-Rodriguez-Fernandez-contacto.pdf`
    Con teléfono. Es la que se envía en las candidaturas. **No se sube al
    repositorio**: está en .gitignore.

Las dos salen del mismo fichero fuente, así que no pueden desincronizarse:
al editar `cv.html` se regeneran ambas de una pasada.

Uso:
    python generar.py

El teléfono se lee de `_cv/datos-privados.txt` (ignorado por git), con el
formato:

    telefono=+34 600 11 22 33

Si ese fichero no existe, solo se genera la versión pública.
"""
import re
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
FUENTE = AQUI / "cv.html"
PRIVADOS = AQUI / "datos-privados.txt"
SALIDA = RAIZ / "assets" / "cv"

PUBLICO = SALIDA / "CV-Marco-Rodriguez-Fernandez.pdf"
PRIVADO = SALIDA / "CV-Marco-Rodriguez-Fernandez-contacto.pdf"

MARCA_TEL = "[TU TELÉFONO]"
# Al quitar el teléfono hay que llevarse también su separador.
FRAGMENTO_TEL = f'{MARCA_TEL}<span class="sep">·</span>'

CHROMES = [
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
]

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except AttributeError:
    pass


def buscar_navegador() -> Path:
    for c in CHROMES:
        if c.exists():
            return c
    raise SystemExit("FALLO: no se encontró Chrome ni Edge para generar el PDF.")


def leer_telefono() -> str | None:
    if not PRIVADOS.exists():
        return None
    for linea in PRIVADOS.read_text(encoding="utf-8").splitlines():
        if linea.strip().startswith("telefono="):
            valor = linea.split("=", 1)[1].strip()
            return valor or None
    return None


def quitar_enlaces_pendientes(html: str) -> tuple[str, list[str]]:
    """Elimina los enlaces cuyo destino sigue siendo un marcador.

    Es preferible que el CV no muestre el enlace a que lo muestre roto.
    En cuanto se ponga la URL real en `cv.html`, el enlace reaparece solo.
    """
    pendientes = re.findall(r'<a href="(URL_[^"]*)">', html)
    if not pendientes:
        return html, []

    # Se retira también un separador adyacente, delante o detrás según la
    # posición del enlace, para no dejar un '·' suelto.
    html = re.sub(r'<a href="URL_[^"]*">.*?</a><span class="sep">·</span>', "", html)
    html = re.sub(r'<span class="sep">·</span><a href="URL_[^"]*">.*?</a>', "", html)
    html = re.sub(r'<a href="URL_[^"]*">.*?</a>', "", html)
    return html, pendientes


def imprimir(html: str, destino: Path, navegador: Path) -> None:
    temporal = AQUI / "_tmp_cv.html"
    temporal.write_text(html, encoding="utf-8")
    destino.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(
            [
                str(navegador),
                "--headless=new",
                "--disable-gpu",
                "--no-pdf-header-footer",
                f"--print-to-pdf={destino}",
                temporal.as_uri(),
            ],
            check=True,
            capture_output=True,
            timeout=120,
        )
    finally:
        temporal.unlink(missing_ok=True)


def main() -> int:
    if not FUENTE.exists():
        print(f"FALLO: no existe {FUENTE}")
        return 1

    html = FUENTE.read_text(encoding="utf-8")
    navegador = buscar_navegador()

    html, pendientes = quitar_enlaces_pendientes(html)
    if pendientes:
        print("AVISO: se han retirado del CV estos enlaces por no tener URL real:")
        for p in pendientes:
            print(f"  - {p}")
        print("       Pon la URL en cv.html y vuelve a ejecutar para recuperarlos.")
        print()

    # --- pública: sin teléfono
    publico = html.replace(FRAGMENTO_TEL, "").replace(MARCA_TEL, "")
    imprimir(publico, PUBLICO, navegador)
    print(f"OK  pública -> {PUBLICO.relative_to(RAIZ)}  (sin teléfono)")

    # --- privada: con teléfono
    telefono = leer_telefono()
    if telefono:
        privado = html.replace(MARCA_TEL, telefono)
        imprimir(privado, PRIVADO, navegador)
        print(f"OK  privada -> {PRIVADO.relative_to(RAIZ)}  (con teléfono, no se sube)")
    else:
        print(f"--  privada omitida: falta {PRIVADOS.name}")
        print("    Créalo con una línea:  telefono=+34 600 11 22 33")

    # --- verificación de la pública, que es la que ve un ATS
    print()
    r = subprocess.run(
        [sys.executable, str(AQUI / "verificar_cv.py")],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    print(r.stdout.strip())
    if r.stderr.strip():
        print(r.stderr.strip())
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
