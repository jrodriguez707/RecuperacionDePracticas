import sys

def clase_ip(primer_octeto):
    if 1 <= primer_octeto <= 126:
        return "A"
    elif 128 <= primer_octeto <= 191:
        return "B"
    elif 192 <= primer_octeto <= 223:
        return "C"
    elif 224 <= primer_octeto <= 239:
        return "D"
    elif 240 <= primer_octeto <= 254:
        return "E"
    else:
        return "Desconocida"

def main():
    # Comprobar numero de argumentos
    if len(sys.argv) != 2:
        print("Uso: python comprueba_ip.py <IPv4>")
        sys.exit(1)

    ip = sys.argv[1]

    # Validacion ips

    partes = ip.split(".")

    # Debe tener 4 partes
    if len(partes) != 4:
        print("Error: IP no válida")
        sys.exit(2)

    octetos = []

    # Validar cada parte
    for p in partes:

        # Debe ser numerica
        if not p.isdigit():
            print("Error: IP no válida")
            sys.exit(2)

        numero = int(p)

        # Debe estar en el rango 0–255
        if numero < 0 or numero > 255:
            print("Error: IP no válida")
            sys.exit(2)

        octetos.append(numero)

    # Si llega aqui la ip es correcta
    print("IP válida")

    # Obtener clase usando solo el primer octeto
    clase = clase_ip(octetos[0])
    print("Clase:", clase)


if __name__ == "__main__":
    main()
