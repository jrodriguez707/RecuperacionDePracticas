# Proyecto: Descubridor de MAC

Este proyecto permite obtener la dirección MAC de una máquina en la misma red local (LAN) a partir de su dirección IP.  
Utiliza el protocolo ARP para enviar una petición a la IP objetivo y recibir la MAC.

## Requisitos

- Python 3.8 o superior  
- Librería `scapy`

## Instalación de Scapy

```bash
pip install scapy
```
## Instalación

Descarga este proyecto o copia los archivos en una carpeta.
Asegúrate de tener Python instalado ejecutando:

```bash
python --version
```
## Ejecución

Desde la terminal, ejecútalo como administrador (recomendado), sitúate en la carpeta del proyecto y ejecuta:
```bash
python descubrir_mac.py 192.168.1.5
```
Sustituye 192.168.1.5 por la IP de tu red local (LAN).

### Ejemplo de salida

Si hay respuesta: 
```bash
MAC encontrada: aa:bb:cc:dd:ee:ff
```
Si no responde (IP inactiva o fuera de la LAN):
```bash
MAC no encontrada o el host no responde
```
