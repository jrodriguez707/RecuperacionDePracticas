# Recuperador de Contraseñas ZIP en Python

Este módulo permite recuperar contraseñas de archivos ZIP protegidos mediante dos técnicas principales:

1. Ataque por fuerza bruta sobre un ZIP con contraseña de longitud fija.
2. Ataque por diccionario usando palabras contenidas en un archivo `diccionario.txt`.

El sistema está optimizado para probar contraseñas rápidamente leyendo solo un byte del archivo interno del ZIP, evitando descompresiones completas.

---

## Contenido del proyecto

- `fuerza_bruta_diccionario.py`: Script principal que ejecuta ambos ataques.
- `diccionario.zip`: Archivo ZIP con una contraseña sencilla que se descifra por fuerza bruta.
- `compress.zip`: Archivo ZIP protegido con una contraseña que debe buscarse mediante diccionario.
- `README.md`: Documento explicativo del funcionamiento del proyecto.

---

## Funcionamiento del módulo

### 1. Validación previa de archivos (`validar_archivo()`)

Antes de iniciar cualquier ataque, el script verifica que el archivo ZIP objetivo exista y sea válido:

```python
def validar_archivo(zip_name):
    if not os.path.exists(zip_name):
        raise FileNotFoundError(f"El archivo '{zip_name}' no existe.")
    if not zipfile.is_zipfile(zip_name):
        raise ValueError(f"El archivo '{zip_name}' no es un ZIP válido.")
```

Esta validación es crítica. Sin ella, un `except` genérico silenciaría el error de archivo inexistente,
haciendo creer al programa que simplemente no existe contraseña correcta, y continuaría probando
millones de combinaciones en vano hasta terminar con "No se encontró la contraseña".

Los errores `FileNotFoundError` y `ValueError` se propagan hacia el bloque principal, donde se
capturan y muestran al usuario de forma clara.

---

### 2. Ataque por fuerza bruta (`abrir_diccionario_zip()`)

El script genera todas las combinaciones posibles de un alfabeto personalizado con longitud fija de 4 caracteres:

```python
alfabeto = "eEaAoOlLsSnNrRiIdDtTcCuUmMpPbBgGvVqQhHfFzZjJyYñÑkKwWxX0123456789"
longitud = 4

for comb in itertools.product(alfabeto, repeat=longitud):
    pwd = "".join(comb)
```

Cada combinación se prueba automáticamente llamando a `probar_contraseña()`.

Cuando se encuentra la contraseña correcta:
- Se muestra la contraseña encontrada.
- Se indica el tiempo empleado en segundos.
- Se extrae automáticamente `diccionario.txt` del ZIP.

Ese archivo será utilizado posteriormente en el ataque por diccionario.

---

### 3. Ataque por diccionario (`abrir_compress_zip()`)

Una vez generado `diccionario.txt`, el módulo lo utiliza línea por línea para intentar abrir `compress.zip`.

Para cada línea:
- Se elimina el salto de línea con `.strip()`.
- Se intenta usarla como contraseña.
- Si coincide, se muestra la contraseña y el tiempo de ejecución.

```python
with open("diccionario.txt", "r", encoding="utf-8", errors="ignore") as f:
    for linea in f:
        pwd = linea.strip()
        if probar_contraseña("compress.zip", pwd):
            ...
```

---

### 4. Optimización: lectura de un solo byte (`probar_contraseña()`)

La función `probar_contraseña()` abre el ZIP e intenta leer únicamente un byte del archivo interno:

```python
with zf.open(archivo, pwd=contraseña.encode()) as f:
    f.read(1)
```

Si la contraseña es incorrecta, Python lanza una excepción antes de leer nada. Esto evita
descomprimir el archivo completo en cada intento, haciendo el proceso mucho más rápido.

Solo se capturan las excepciones propias de contraseña incorrecta:

```python
except (RuntimeError, zipfile.BadZipFile):
    return False
```

`FileNotFoundError` queda fuera del `except` deliberadamente, para que se propague y sea
gestionado por `validar_archivo()` antes de que el ataque comience.

---

## Requisitos

El script requiere Python 3 y las siguientes librerías estándar (no es necesario instalar nada adicional):

- `zipfile`
- `itertools`
- `time`
- `os`

---

## Cómo ejecutar el programa

Coloca en la misma carpeta:

- `fuerza_bruta_diccionario.py`
- `diccionario.zip`
- `compress.zip`

Ejecuta el script desde consola:

```bash
python fuerza_bruta_diccionario.py
```

El programa:

1. Validará que ambos archivos ZIP existan y sean válidos antes de comenzar.
2. Recuperará la contraseña de `diccionario.zip` mediante fuerza bruta.
3. Extraerá automáticamente `diccionario.txt`.
4. Usará el diccionario para buscar la contraseña de `compress.zip`.

---

## Ejemplo de salida

```
=== RECUPERADOR DE CONTRASEÑAS ZIP ===

Buscando contraseña de diccionario.zip...
Contraseña encontrada: Lov3
Tiempo: 482.56 segundos
diccionario.txt extraído.

Probando contraseñas para compress.zip...
Contraseña encontrada para compress.zip: huangguanwang
Tiempo: 65.27 segundos

Programa terminado.
```