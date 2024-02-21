# Consigna: ✍️
# Crear un pequeño programa que realice una función aritmética que permita al usuario ingresar datos por la terminal acorde a distintas opciones.  Para ellos debemos definir una función que reciba parámetros:
# Combinar funciones nativas y funciones definidas, condicionales, y bucles.
# Si el usuario ingresa el nro 1, realiza la acción A.
# Si el usuario ingresa el nro 2, realiza la acción B.

def sumar(numero):
    return 10 + numero

def restar(numero):
    return 10 - numero


def menu():
    print("Seleccione una opción:")
    print("1. Sumar 1 al 10")
    print("2. Restar 2 a 10")
    opcion = input("Ingrese el número de la opción deseada: ")
    return opcion



numero = menu()
def realizar_accion(numero):
    numero = menu()
    if numero == '1':
        print('uno')
    else:
        print('dos')


realizar_accion()