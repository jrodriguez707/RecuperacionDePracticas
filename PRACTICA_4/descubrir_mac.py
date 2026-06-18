import sys
import ipaddress
from scapy.all import srp, Ether, ARP


def obtener_mac(ip):
    mac_broadcast = "ff:ff:ff:ff:ff:ff"

    try:
        paquete = Ether(dst=mac_broadcast) / ARP(pdst=ip)

        respuesta, _ = srp(paquete, timeout=2, verbose=False)

        if respuesta:
            return respuesta[0][1].hwsrc
        else:
            return None

    except Exception as e:
        print(f"Error al enviar paquete ARP: {e}")
        return None


def main():
    
    if len(sys.argv) != 2:
        print("Uso: python descubrir_mac.py <IP>")
        sys.exit(1)

    ip = sys.argv[1]

    # Validación de IP
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print("Error: La IP no tiene un formato válido.")
        sys.exit(1)

    mac = obtener_mac(ip)

    if mac:
        print(f"MAC encontrada: {mac}")
    else:
        print("MAC no encontrada o el host no responde")


if __name__ == "__main__":
    main()