# Escaneador de switches

## Información
La aplicación se encarga de escanear la plataforma de
servidores a través de una lista de ips dada en un fichero, conectarse a dichos
servidores, y escanear los switches en las ips entre la 192.168.4.40 y 192.168.4.50
para sacar la información de las bocas físicas de dichos switches.

## Requisitos
- Python 2.7 y Python Pip (sudo apt-get install python python-pip)
- Paramiko (sudo pip install paramiko)
- Paramiko expect (sudo pip install git+https://github.com/fgimian/paramiko-expect.git)

## Instrucciones
El fichero principal de la aplicación es el **main.py**. Se ejecutará con:

```python main.py```

La aplicación tiene 2 opciones:
- Configuración de fichero: para indicar cuál es el fichero de texto con la lista de ips.
- Escaneo de switches: escaneo de los servidores en busca de los switches y guardado a CSV.

Al ejecutable se le puede pasar como parámetro el fichero con la lista de IPs:

```python main.py fichero_con_ips```

En el caso de que de error en la lectura de fichero, asegurar que tras la última IP
de la lista hay una línea en blanco.

## Autores
- Mario Adrián Domínguez
- Jesús Velázquez

## Cambios
**1.6.03**
- Se permite pasar por parámetro el fichero de IPs
- Añadido método de detección del Dlink DGS-1210-24 por Telnet
- Fix para la conexión a servidores
- Subido el timeout para ejecución de comandos SSH y Telnet a 5 segundos
- Fixes varios