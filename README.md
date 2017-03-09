# Escaneador de switches

### Información
La aplicación **Escaneador de switches** se encarga de escanear la plataforma de
servidores a través de una lista de ips dada en un fichero, conectarse a dichos
servidores, y escanear los switches en las ips entre la 192.168.4.40 y 192.168.4.50
para sacar la información de las bocas físicas de dichos switches.

### Requisitos
- Python 2.7
- Paramiko (pip install paramiko)
- Paramiko expect (pip install git+https://github.com/fgimian/paramiko-expect.git)

### Instrucciones
El fichero principal de la aplicación es el **main.py**. Se ejecutará con:
```python main.py```
La aplicación tiene 2 opciones:
- Configuración de fichero: para indicar cuál es el fichero de texto con la lista de ips.
- Escaneo de switches: escaneo de los servidores en busca de los switches y guardado a CSV.

### Autores
- Mario Adrián Domínguez
- Jesús Velázquez

Versión 1.6