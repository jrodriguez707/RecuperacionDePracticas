# Proyecto: Comprobador de Ping

Este proyecto contiene un programa en Python que envía un único ping a una dirección IP y comprueba si responde o no.

## Características

* Validación de direcciones IP IPv4 e IPv6.
* Compatibilidad con Windows, Linux y macOS.
* Manejo básico de errores.
* Muestra únicamente el resultado final de la comprobación.

## Requisitos

* Python 3.8 o superior.

## Instalación

1. Descarga o clona este proyecto.
2. Asegúrate de tener Python instalado ejecutando:

```bash
python --version
```

## Ejecución

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
python ping.py 8.8.8.8
```

Sustituye `8.8.8.8` por la dirección IP que quieras comprobar.

## Ejemplos

Si la IP responde:

```text
La IP 8.8.8.8 responde.
```

Si la IP no responde:

```text
La IP 192.168.1.250 no responde.
```

Si la dirección introducida no es una IP válida:

```text
Error: 'abc.def' no es una dirección IP válida.
```

## Manejo de errores

El programa informa de los siguientes errores:

* Número incorrecto de argumentos.
* Dirección IP con formato inválido.
* Comando `ping` no disponible en el sistema.
* Errores inesperados durante la ejecución.

## Autor

Proyecto realizado como práctica de Python.
