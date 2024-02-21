# 2. Crear una lista con 5 elementos y luego aplica los siguientes accionables:
# ↪ Imprimir el último elemento
# ↪ Modificar el valor del tercer elemento
# ↪ Agregar dos elementos
# ↪ Eliminar algún elemento
# ● Guardar en un archivo llamado ejercicio2.py

vocales = [1,2,3,4,5]

# ↪ Imprimir el último elemento
pos_ultimo_elemento = len(vocales)-1
print("ultimo elemento", vocales[pos_ultimo_elemento])

# modificamos el valor del tercer elemento
vocales[2]=9
print("lista modificada en pos 3:",vocales)

# ↪ Agregar dos elementos
vocales.extend([6,7])
print("lista agregada 2 elementos:",vocales)

# ↪ Eliminar algún elemento
eliminado = vocales.pop(2)
print("elemento eliminado de la posicion 2: ", eliminado)
print("lista despues de eliminar:",vocales)