import socket
import sys

PUERTOS_DEFAULT = [
    20, 21, 22, 23, 25, 53, 80, 110, 143, 443,
    445, 465, 587, 993, 995, 1433, 1521, 3306,
    3389, 5432, 5900, 8080
]

TIMEOUT = 1.0


def mostrar_uso():
    print("Uso: nmap_casero.py <ip> [-p puerto1,puerto2,...]")
    print("Ejemplo: nmap_casero.py 192.168.1.1 -p 22,80,443")


def validar_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


def parsear_puertos(cadena):
    partes = cadena.split(",")
    puertos = []
    vistos = set()

    for parte in partes:
        parte = parte.strip()
        if not parte.isdigit():
            print(f"Error: '{parte}' no es un número de puerto válido.")
            sys.exit(1)
        numero = int(parte)
        if not (1 <= numero <= 65535):
            print(f"Error: el puerto {numero} está fuera del rango permitido (1-65535).")
            sys.exit(1)
        if numero in vistos:
            continue
        vistos.add(numero)
        puertos.append(numero)

    return puertos


def parsear_argumentos(argv):
    if len(argv) < 2:
        mostrar_uso()
        sys.exit(1)

    ip = argv[1]

    if not validar_ip(ip):
        print(f"Error: '{ip}' no es una dirección IP válida.")
        sys.exit(1)

    puertos = PUERTOS_DEFAULT

    i = 2
    while i < len(argv):
        if argv[i] == "-p":
            if i + 1 >= len(argv):
                print("Error: la opción -p requiere una lista de puertos.")
                sys.exit(1)
            puertos = parsear_puertos(argv[i + 1])
            i += 2
        else:
            print(f"Error: opción desconocida '{argv[i]}'.")
            mostrar_uso()
            sys.exit(1)

    return ip, puertos


def escanear_puerto(ip, puerto):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(TIMEOUT)
            resultado = s.connect_ex((ip, puerto))
            return resultado == 0
    except socket.error:
        return False


def escanear(ip, puertos):
    abiertos = 0

    print(f"\nEscaneando {ip} — {len(puertos)} puerto(s)\n")

    for puerto in puertos:
        abierto = escanear_puerto(ip, puerto)
        estado = "ABIERTO" if abierto else "CERRADO"
        print(f"Puerto {puerto:5d}: {estado}")
        if abierto:
            abiertos += 1

    print(f"\nResumen: {abiertos} abierto(s) de {len(puertos)} analizado(s).")


def main():
    ip, puertos = parsear_argumentos(sys.argv)
    escanear(ip, puertos)


if __name__ == "__main__":
    main()
