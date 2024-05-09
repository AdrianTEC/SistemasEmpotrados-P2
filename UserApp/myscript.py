import os
import sys

# Verifica si se proporciona un mensaje como argumento al ejecutar el script
if len(sys.argv) < 2:
    print("Por favor, proporciona un mensaje como argumento al ejecutar el script.")
    sys.exit(1)

# Obtén el mensaje del primer argumento pasado al script
mensaje = sys.argv[1]

path_dispositivo = "/dev/pci_capture_chr_dev-0"

# Escribe el mensaje en el dispositivo
with open(path_dispositivo, 'w') as dispositivo:
    dispositivo.write(mensaje)
    print("El mensaje ha sido escrito")

dispositivo.close()

# Lee el contenido del dispositivo
with open(path_dispositivo, 'r') as dispositivo:
    contenido = dispositivo.read()
    print("El contenido del dispositivo es: ", contenido)

dispositivo.close()
