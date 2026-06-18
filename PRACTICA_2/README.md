## 1) Descripción breve

`comprueba_ip.py` es un modulo simple de línea de comandos que:
- Valida direcciones IPv4 (formato `X.X.X.X` y rango `0–255` en cada octeto).
- Informa de la clase (A, B, C, D o E) según el primer octeto.

---

## 2) Sintaxis y ejemplos

**Sintaxis:**
```bash
python comprueba_ip.py <IPv4>
Ejemplos:

bash
python comprueba_ip.py 192.168.68.1
# IP válida
# Clase: C

python comprueba_ip.py 10.0.0.1
# IP válida
# Clase: A

python comprueba_ip.py 255.255.255.255
# IP válida
# Clase: Desconocida

python comprueba_ip.py 300.1.1.1
# IP no válida