import sys
import ipaddress
import platform
import subprocess


# comprobacion de argumentos
if len(sys.argv) != 2:
    print("Uso: python ping.py <IP>")
    sys.exit(1)

ip = sys.argv[1]

# validar la ip antes de ejecutar el ping
try:
    ipaddress.ip_address(ip)
except ValueError:
    print(f"Error: '{ip}' no es una dirección IP válida.")
    sys.exit(1)

# ejecutar el comando segun el os
if platform.system() == "Windows":
    comando = ["ping", "-n", "1", ip]
else:
    comando = ["ping", "-c", "1", ip]

try:
    resultado = subprocess.run(
        comando,
        capture_output=True,
        text=True
    )

    if resultado.returncode == 0:
        print(f"La IP {ip} responde.")
    else:
        print(f"La IP {ip} no responde.")

except FileNotFoundError:
    print("Error: el comando 'ping' no está disponible en este sistema.")
    sys.exit(1)

except Exception as e:
    print(f"Ha ocurrido un error inesperado: {e}")
    sys.exit(1)