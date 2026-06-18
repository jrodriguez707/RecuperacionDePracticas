import zipfile
import itertools
import time
import os

# ===============================
# PROBAR UNA CONTRASEÑA LEYENDO 1 SOLO BYTE
# ===============================
def probar_contraseña(zip_name, contraseña):
    try:
        with zipfile.ZipFile(zip_name, 'r') as zf:
            archivo = zf.namelist()[0]

            # Abrimos el archivo interno y leemos SOLO 1 BYTE
            with zf.open(archivo, pwd=contraseña.encode()) as f:
                f.read(1)

        return True
    except:
        return False


# ===============================
# FUERZA BRUTA PARA DICCIONARIO.ZIP
# ===============================
def abrir_diccionario_zip():

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


# ===============================
# ATAQUE POR DICCIONARIO PARA COMPRESS.ZIP
# ===============================
def abrir_compress_zip():
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


# ===============================
# PROGRAMA PRINCIPAL
# ===============================
print("=== RECUPERADOR DE CONTRASEÑAS ZIP ===\n")

if abrir_diccionario_zip():
    abrir_compress_zip()

print("\nPrograma terminado.")
