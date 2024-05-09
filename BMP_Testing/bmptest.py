import numpy as np
from PIL import Image

def create_bitmap(pixel_array, width, height, filename):
    image = Image.new('L', (width, height))
    image.putdata(pixel_array)
    image.save(filename)

def invert_colors(image_path, output_path):
    # Abrir la imagen
    image = Image.open(image_path)
    
    # Convertir la imagen a una matriz numpy
    image_array = np.array(image)
    print(image_array)
    # Invertir los colores modificando los valores de la matriz
    inverted_image_array = 255 - image_array
    
    # Crear una nueva imagen a partir de la matriz invertida
    inverted_image = Image.fromarray(inverted_image_array)
    
    # Guardar la imagen invertida como output2.bmp
    inverted_image.save(output_path)

# Ejemplo de uso
invert_colors('BMP_Testing\smile.bmp', 'BMP_Testing\output3333.bmp')

# Example usage:
#pixel_array = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)
#create_bitmap(pixel_array.flatten(), 100, 100, 'output.bmp')
