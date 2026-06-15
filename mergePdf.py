import os
import re
import sys
from pypdf import PdfReader, PdfWriter

# Detectar si es .exe o .py
if getattr(sys, 'frozen', False):
    carpeta = os.path.dirname(sys.executable)
else:
    carpeta = os.path.dirname(os.path.abspath(__file__))

writer = PdfWriter()
archivos = []

print("Buscando PDFs en:", carpeta)  # DEBUG

for archivo in os.listdir(carpeta):
    print("Encontrado:", archivo)  # DEBUG
    
    if archivo.lower().endswith(".pdf"):
        match = re.search(r'\d+', archivo)
        if match:
            numero = int(match.group())
            archivos.append((numero, archivo))

archivos.sort(key=lambda x: x[0])

if not archivos:
    print("No se encontraron PDFs con números en el nombre.")
    input("Presioná Enter para salir...")
    exit()

print(f"Se encontraron {len(archivos)} PDFs. Uniendo...")

for numero, archivo in archivos:
    print(f"Agregando {archivo}")
    reader = PdfReader(os.path.join(carpeta, archivo))
    for page in reader.pages:
        writer.add_page(page)

salida = os.path.join(carpeta, "PDF_FINAL.pdf")

with open(salida, "wb") as f:
    writer.write(f)

print("PDF unido correctamente")
input("Presioná Enter para salir...")
