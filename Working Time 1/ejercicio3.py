# 3. Crea una función llamada verificar_calificacion que reciba tres parámetros: nota1, nota2 y nota3
# ↪ Dentro de la función calcular el promedio de notas
# ↪ Si el promedio es mayor o igual a 6, entonces la función debe
# retornar un mensaje “Aprobado”, en caso contrario
# “Reprobado”
# ● Guardar en un archivo llamado ejercicio3.py

def verificar_calificacion(nota1, nota2, nota3):
    nota_total = nota1 + nota2 + nota3
    promedio = nota_total // 3

    if  promedio >= 6:
        print ( "nota:", nota_total,
              "\nPromedio: ", promedio,
              "\nCalificacion: Aprobado"
        )
        return("Aprobado")
    else:
        print ( "nota:", nota_total,
              "\nPromedio: ", promedio,
              "\nCalificacion: Reprobado"
        )
        return("Reprobado")
    
verificar_calificacion(6,7,0)