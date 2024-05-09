import os

# Ruta del archivo de entrada
file_path = os.path.expanduser("/dev/dispositivo/pixeles.txt")

# Ruta del archivo de salida para el filtro negativo
negative_output_path = os.path.expanduser("/dev/dispositivo/pixeles_negativos.txt")

# Ruta del archivo de salida para el filtro suavizado
smoothed_output_path = os.path.expanduser("/dev/dispositivo/pixeles_suavizados.txt")

# Función para aplicar filtro negativo a un pixel
def apply_negative_filter(pixel_value):
    return 255 - pixel_value  # Calcula el valor negativo del pixel

# Función para aplicar filtro de suavizado a un pixel
def apply_smoothing_filter(pixel_value, neighbor_values):
    # Calcula el promedio de los valores de píxeles vecinos
    neighbor_sum = sum(neighbor_values) + pixel_value
    return neighbor_sum // (len(neighbor_values) + 1)  # Retorna el promedio

# Lee los valores de los píxeles del archivo de entrada
with open(file_path, 'r') as file:
    pixels = file.readlines()

# Aplica el filtro negativo y el filtro suavizado a cada valor de píxel
new_negative_pixels = [str(apply_negative_filter(int(pixel.strip()))) + '\n' for pixel in pixels]
new_smoothed_pixels = []
for i, pixel in enumerate(pixels):
    pixel_value = int(pixel.strip())
    # Selecciona los valores de los píxeles vecinos para el filtro suavizado
    neighbor_values = [int(p.strip()) for p in pixels[max(0, i-1):min(len(pixels), i+2)]]
    new_smoothed_pixels.append(str(apply_smoothing_filter(pixel_value, neighbor_values)) + '\n')

# Escribe los nuevos valores de píxeles en archivos de salida
with open(negative_output_path, 'w') as negative_output_file:
    negative_output_file.writelines(new_negative_pixels)

with open(smoothed_output_path, 'w') as smoothed_output_file:
    smoothed_output_file.writelines(new_smoothed_pixels)

print("Filtro negativo aplicado y guardado en:", negative_output_path)
print("Filtro suavizado aplicado y guardado en:", smoothed_output_path)
