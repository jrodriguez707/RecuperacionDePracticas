# Recuperador de Contraseñas ZIP en Python

Este módulo permite recuperar contraseñas de archivos ZIP protegidos mediante dos técnicas principales:

1. Ataque por fuerza bruta sobre un ZIP con contraseña de longitud fija.
2. Ataque por diccionario usando palabras contenidas en un archivo `diccionario.txt`.

El sistema está optimizado para probar contraseñas rápidamente leyendo solo un byte del archivo interno del ZIP, evitando descompresiones completas.

---

## Contenido del proyecto

- `recuperador.py`: Script principal que ejecuta ambos ataques.
- `diccionario.zip`: Archivo ZIP con una contraseña sencilla que se descifra por fuerza bruta.
- `compress.zip`: Archivo ZIP protegido con una contraseña que debe buscarse mediante diccionario.
- `README.md`: Documento explicativo del funcionamiento del proyecto.

---

## Funcionamiento del módulo

### 1. Ataque por fuerza bruta (`abrir_diccionario_zip()`)

El script genera todas las combinaciones posibles de un conjunto de caracteres (alfabeto personalizado) con longitud fija (4 caracteres).  
Cada combinación se prueba automáticamente llamando a la función `probar_contraseña()`.

Cuando se encuentra la contraseña correcta:
- Se muestra la contraseña.
- Se indica el tiempo empleado.
- Se extrae automáticamente el fichero `diccionario.txt` del ZIP.

Ese archivo será utilizado posteriormente en el ataque por diccionario.

---

### 2. Ataque por diccionario (`abrir_compress_zip()`)

Una vez generado `diccionario.txt`, el módulo lo utiliza línea por línea para intentar abrir `compress.zip`.

Para cada línea:
- Se elimina el salto de línea.
- Se intenta usarla como contraseña.
- Si coincide, se muestra la contraseña y el tiempo de ejecución.

---

### 3. Optimización: lectura de un solo byte

La función `probar_contraseña()` abre el ZIP e intenta leer un único byte del archivo interno:

```python
with zf.open(archivo, pwd=contraseña.encode()) as f:
    f.read(1)
```
### Requisitos

- El script requiere Python 3 y las siguientes librerías estándar:

itertools
zipfile
time
os

No es necesario instalar bibliotecas adicionales.

### Cómo ejecutar el programa

Coloca en la misma carpeta:

fuerza_bruta_diccionario.py

diccionario.zip

compress.zip

Ejecuta el script desde consola:
```bash
python fuerza_bruta_diccionario.py
```

- El programa:

Recuperará la contraseña de diccionario.zip mediante fuerza bruta.

- Extraerá automáticamente diccionario.txt.

Usará el diccionario para buscar la contraseña de compress.zip.