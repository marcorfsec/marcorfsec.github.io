"""Verifica que el CV en PDF es legible por un ATS.

Un ATS (el sistema que filtra candidaturas antes de que las vea una persona)
extrae texto plano del PDF. Si el texto no se puede extraer, si el CV ocupa
más de una página o si faltan las palabras clave por las que buscan los
reclutadores, la candidatura se descarta sin que nadie la lea.

Uso:
    python verificar_cv.py
"""
import re
import sys
import unicodedata
from pathlib import Path

import pypdf

# La consola de Windows usa cp1252 y revienta con caracteres combinantes.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except AttributeError:
    pass

PDF = Path(__file__).resolve().parents[1] / "assets" / "cv" / "CV-Marco-Rodriguez-Fernandez.pdf"

# Términos por los que buscan los reclutadores. Si no están en el texto
# extraíble, el CV no aparece en sus búsquedas.
OBLIGATORIAS = [
    "Marco Rodríguez Fernández",
    "marcurf86@gmail.com",
    "Gijón",
    "SOC",
    "Pentesting",
    "eJPT",
    "Linux",
    "Python",
    "Hacking Web",
    "marcorfsec.github.io",
    "turnos rotativos",
]

# Marcadores que hay que sustituir antes de enviar el CV a nadie.
PROHIBIDAS = [
    "[TU TELÉFONO]",
    "URL_LINKEDIN",
    "URL_HTB",
    "TELEFONO",
]


def normalizar(t: str) -> str:
    """Deja el texto como lo dejaría un ATS antes de buscar en él.

    Al extraer de un PDF, las tildes pueden venir descompuestas ('i' más
    acento combinante) y los espacios convertidos en tabuladores o saltos
    de línea según cómo se hayan colocado los glifos. Cualquier parser
    serio normaliza ambas cosas; el verificador no debe ser más estricto
    que la realidad que simula.
    """
    t = unicodedata.normalize("NFC", t)
    t = t.replace("­", "")  # guion blando
    return re.sub(r"\s+", " ", t).strip().lower()


def urls_del_pdf(pagina) -> list[str]:
    """Devuelve los destinos de los enlaces incrustados en la página.

    Los href no aparecen en el texto extraído, así que un CV con enlaces
    rotos pasaría desapercibido si solo se mirase el texto.
    """
    urls: list[str] = []
    anotaciones = pagina.get("/Annots")
    if not anotaciones:
        return urls
    for ref in anotaciones:
        try:
            obj = ref.get_object()
            accion = obj.get("/A")
            if accion and accion.get("/URI"):
                urls.append(str(accion["/URI"]))
        except Exception:
            continue
    return urls


def main() -> int:
    if not PDF.exists():
        print(f"FALLO: no existe el PDF en {PDF}")
        print("       Exporta cv.html desde el navegador con Ctrl+P > Guardar como PDF.")
        return 1

    lector = pypdf.PdfReader(str(PDF))

    if len(lector.pages) != 1:
        print(f"FALLO: el CV ocupa {len(lector.pages)} páginas y debe ocupar 1.")
        print("       Baja el font-size del body en cv.html de 9.6pt a 9.2pt y reexporta.")
        return 1

    texto = lector.pages[0].extract_text() or ""

    if len(texto.strip()) < 400:
        print(f"FALLO: solo se extraen {len(texto.strip())} caracteres.")
        print("       El PDF se ha generado como imagen. Usa 'Guardar como PDF'")
        print("       del navegador, no 'Microsoft Print to PDF'.")
        return 1

    texto_min = normalizar(texto)

    faltan = [p for p in OBLIGATORIAS if normalizar(p) not in texto_min]
    if faltan:
        print("FALLO: faltan palabras clave en el texto extraído:")
        for p in faltan:
            print(f"  - {p}")
        return 1

    quedan = [p for p in PROHIBIDAS if normalizar(p) in texto_min]
    if quedan:
        print("FALLO: el CV todavía tiene marcadores sin sustituir:")
        for p in quedan:
            print(f"  - {p}")
        print("       Edita cv.html, sustitúyelos por los datos reales y reexporta.")
        return 1

    urls = urls_del_pdf(lector.pages[0])

    rotos = [u for u in urls if any(p.lower() in u.lower() for p in PROHIBIDAS)]
    if rotos:
        print("FALLO: hay enlaces sin sustituir en el CV:")
        for u in rotos:
            print(f"  - {u}")
        return 1

    if not any("marcorfsec.github.io" in u for u in urls):
        print("FALLO: falta el enlace a marcorfsec.github.io entre los hipervínculos.")
        print(f"       Enlaces encontrados: {urls}")
        return 1

    print(f"OK: 1 página, {len(texto.strip())} caracteres extraíbles.")
    print(f"    {len(urls)} hipervínculos, todos con destino válido.")
    print("    Todas las palabras clave presentes y ningún marcador pendiente.")
    print("    El CV es legible por un ATS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
