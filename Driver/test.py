import os
import sys
import time

# Verifica si se proporciona un mensaje como argumento al ejecutar el script
if len(sys.argv) < 2:
    sys.exit(1)

# Obtén el mensaje del primer argumento pasado al script
mensaje = sys.argv[1]

path_dispositivo = "/dev/pci_capture_chr_dev-0"

# Abre el archivo del dispositivo para escribir
fd = os.open(path_dispositivo, os.O_WRONLY)

# Escribe el mensaje en el dispositivo
os.write(fd, mensaje.encode())

# Cierra el archivo después de escribir
os.close(fd)



# Abre el archivo del dispositivo para leer
fd = os.open(path_dispositivo, os.O_RDONLY)

# Imprime un mensaje de que se está leyendo el contenido del dispositivo
print("Leyendo contenido del dispositivo...")

# Lee el contenido del dispositivo
contenido = os.read(fd, 1024).decode()

# Cierra el archivo después de leer
os.close(fd)

print("Contenido leído del dispositivo:")
print(contenido)