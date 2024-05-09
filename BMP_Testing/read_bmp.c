#include <stdio.h>
#include <stdint.h>

#define BUFFER_SIZE 256

int main() {
    FILE *file;
    uint16_t buffer[BUFFER_SIZE];
    
    // Abre el archivo BMP para lectura binaria
    file = fopen("/home/adriii/Documents/GitHub/SistemasEmpotrados-P2/BMP_Testing/smile.bmp", "rb");
    if (file == NULL) {
        printf("No se pudo abrir el archivo.\n");
        return 1;
    }

    // Salta la cabecera del archivo BMP (tamaño fijo de 54 bytes)
    fseek(file, 54, SEEK_SET);

    // Lee los valores de los píxeles y los guarda en el buffer
    uint32_t index = 0;
    while (index < BUFFER_SIZE) {
        // Leer dos bytes del archivo BMP para formar un valor de píxel de 16 bits
        uint8_t bytes[2];
        if (fread(bytes, sizeof(uint8_t), 2, file) != 2) {
            break; // Error al leer el archivo o llegada al final del archivo
        }
        // Combina los bytes en un valor de píxel de 16 bits
        uint16_t pixel_value = (bytes[1] << 8) | bytes[0];
        buffer[index++] = pixel_value;
    }

    // Cierra el archivo
    fclose(file);

    // Imprime los valores de los píxeles del buffer
    printf("Valores de los pixeles:\n");
    for (uint32_t i = 0; i < index; i++) {
        printf("%d ", buffer[i]);
    }
    printf("\n");

    return 0;
}
