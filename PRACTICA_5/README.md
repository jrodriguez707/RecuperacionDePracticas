# nmap_casero.py

Escáner de puertos TCP en Python que imita el comportamiento básico de Nmap.
Intenta conectarse a cada puerto indicado y determina si está abierto o cerrado.

---

## Sintaxis de uso

```
python nmap_casero.py <ip> [-p puerto1,puerto2,...]
```

| Argumento | Obligatorio | Descripción |
|-----------|-------------|-------------|
| `<ip>` | Sí | Dirección IPv4 del host a analizar |
| `-p lista` | No | Lista de puertos separados por coma |

Si no se indica `-p`, el programa escanea un conjunto de 22 puertos habituales (HTTP, SSH, FTP, HTTPS, bases de datos, etc.).

---

## Ejemplos de ejecución

### Sin opción `-p` (puertos por defecto)

```
python nmap_casero.py 192.168.1.1
```

```
Escaneando 192.168.1.1 — 22 puerto(s)

Puerto    20: CERRADO
Puerto    21: CERRADO
Puerto    22: ABIERTO
Puerto    23: CERRADO
Puerto    25: CERRADO
Puerto    53: ABIERTO
Puerto    80: ABIERTO
...

Resumen: 3 abierto(s) de 22 analizado(s).
```

### Con opción `-p`

```
python nmap_casero.py 10.0.0.5 -p 22,80,443,3306
```

```
Escaneando 10.0.0.5 — 4 puerto(s)

Puerto    22: ABIERTO
Puerto    80: ABIERTO
Puerto   443: CERRADO
Puerto  3306: CERRADO

Resumen: 2 abierto(s) de 4 analizado(s).
```

---

## Posibles mejoras futuras

- **Soporte de rangos**: permitir `-p 20-80` además de listas por coma.
- **Escaneo UDP**: añadir un modo `-u` para puertos UDP (DNS, DHCP, NTP...).
- **Concurrencia**: usar `threading` o `asyncio` para escanear varios puertos en paralelo y reducir el tiempo total.
- **Resolución de nombres**: aceptar hostnames además de IPs y resolverlos con `socket.getaddrinfo`.
- **Detección de servicio**: mostrar el nombre del servicio asociado a cada puerto (`socket.getservbyport`).
- **Exportación de resultados**: opción `-o fichero.txt` para guardar el informe.
- **Ajuste de timeout**: opción `-T` para configurar el tiempo de espera desde la línea de comandos.
