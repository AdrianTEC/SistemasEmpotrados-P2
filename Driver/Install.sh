#!/bin/bash

# Compilar el módulo del kernel
make

# Cargar el módulo del kernel
sudo insmod PCI-Driver.ko

# Verificar si la carga del módulo fue exitosa
if [ $? -eq 0 ]; then
    echo "El módulo del kernel se ha cargado correctamente."
else
    echo "Error: No se pudo cargar el módulo del kernel."
fi
