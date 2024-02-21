# 1. Crear un algoritmo para calcular la sumatoria de los primeros cien números (del 01 al 100) con un ciclo while.
# ● Guardar el algoritmo en un archivo llamado ejercicio1.py

def sumatoria(inicio,ultimo):
    suma = 0

    while  inicio <= ultimo:
        suma += inicio
        inicio += 1
    print("Total:",suma)

sumatoria(0,100)
