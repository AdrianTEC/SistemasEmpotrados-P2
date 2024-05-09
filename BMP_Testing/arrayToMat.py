from PIL import Image

def lista_a_matriz(lista, filas, columnas):
    if filas * columnas != len(lista):
        print("El tamaño de la lista no coincide con el número de filas y columnas especificadas.")
        return None

    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            inicio = (i * columnas + j) * 3
            fila.append(lista[inicio:inicio + 3])
        matriz.append(fila)
    return matriz

def matriz_a_imagen(matriz):
    ancho = len(matriz[0]) * len(matriz[0][0])
    alto = len(matriz) * len(matriz[0][0])
    imagen = Image.new("RGB", (ancho, alto))

    for i, fila in enumerate(matriz):
        for j, pixel in enumerate(fila):
            imagen.putpixel((j, i), tuple(pixel))

    return imagen

# Ejemplo de uso
lista_numeros = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 192, 192, 192, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 192, 192, 192, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 192]

filas = 20
columnas = 18

matriz_resultante = lista_a_matriz(lista_numeros, filas, columnas)
if matriz_resultante:
    imagen_resultante = matriz_a_imagen(matriz_resultante)
    imagen_resultante.show()  # Muestra la imagen resultante en una ventana
    imagen_resultante.save("imagen_bitmap.bmp")  # Guarda la imagen resultante como un archivo BMP
