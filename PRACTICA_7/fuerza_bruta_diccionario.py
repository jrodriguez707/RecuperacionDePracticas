import zipfile
import itertools
import time
import os
import zlib


def probar_contraseña(zip_name, contraseña):
    try:
        with zipfile.ZipFile(zip_name, 'r') as zf:
            archivo = zf.namelist()[0]
            with zf.open(archivo, pwd=contraseña.encode()) as f:
                f.read(1)
        return True
    except (RuntimeError, zipfile.BadZipFile, zlib.error):
        return False


def validar_archivo(zip_name):
    if not os.path.exists(zip_name):
        raise FileNotFoundError(f"El archivo '{zip_name}' no existe.")
    if not zipfile.is_zipfile(zip_name):
        raise ValueError(f"El archivo '{zip_name}' no es un ZIP válido.")


def abrir_diccionario_zip():
    validar_archivo("diccionario.zip")

    alfabeto = "eEaAoOlLsSnNrRiIdDtTcCuUmMpPbBgGvVqQhHfFzZjJyYñÑkKwWxX0123456789"
    longitud = 4

    print("Buscando contraseña de diccionario.zip...")
    inicio = time.time()

    for comb in itertools.product(alfabeto, repeat=longitud):
        pwd = "".join(comb)

        if probar_contraseña("diccionario.zip", pwd):
            fin = time.time()
            print("Contraseña encontrada:", pwd)
            print("Tiempo:", round(fin - inicio, 2), "segundos")

            with zipfile.ZipFile("diccionario.zip", "r") as zf:
                zf.extract("diccionario.txt", pwd=pwd.encode())

            print("diccionario.txt extraído.\n")
            return True

    print("No se encontró la contraseña.")
    return False


def abrir_compress_zip():
    validar_archivo("compress.zip")

    if not os.path.exists("diccionario.txt"):
        print("El archivo diccionario.txt no está disponible.")
        return

    print("Probando contraseñas para compress.zip...")
    inicio = time.time()

    with open("diccionario.txt", "r", encoding="utf-8", errors="ignore") as f:
        for linea in f:
            pwd = linea.strip()

            if probar_contraseña("compress.zip", pwd):
                fin = time.time()
                print("Contraseña encontrada para compress.zip:", pwd)
                print("Tiempo:", round(fin - inicio, 2), "segundos")
                return

    print("No se encontró la contraseña en el diccionario.")


print("=== RECUPERADOR DE CONTRASEÑAS ZIP ===\n")

try:
    if abrir_diccionario_zip():
        abrir_compress_zip()
except FileNotFoundError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error: {e}")

print("\nPrograma terminado.")