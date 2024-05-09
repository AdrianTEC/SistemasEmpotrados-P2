#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <input_bitmap_file>\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "rb");
    if (!file) {
        printf("Error opening file.\n");
        return 1;
    }

    // Leer el encabezado del archivo BMP
    uint8_t header[54];
    fread(header, sizeof(uint8_t), 54, file);

    // Obtener el ancho y alto de la imagen desde el encabezado
    int32_t width = *(int32_t *)&header[18];
    int32_t height = *(int32_t *)&header[22];

    // Calcular el tamaño del arreglo de píxeles
    int pixel_array_size = width * height / 2;

    // Leer los datos de los píxeles
    uint8_t *pixels = (uint8_t *)malloc(pixel_array_size * sizeof(uint8_t));
    fread(pixels, sizeof(uint8_t), pixel_array_size, file);

    // Imprimir el ancho y alto de la imagen
    printf("Width: %d\n", width);
    printf("Height: %d\n", height);

    // Imprimir los píxeles en formato decimal
    printf("4-bit pixels:\n");
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            int index = i * (width / 2) + j / 2;
            uint8_t byte = pixels[index];
            if (j % 2 == 0)
                printf("%d ", (byte >> 4) & 0x0F);
            else
                printf("%d ", byte & 0x0F);
        }
        printf("\n");
    }

    // Liberar la memoria y cerrar el archivo
    free(pixels);
    fclose(file);
    return 0;
}
