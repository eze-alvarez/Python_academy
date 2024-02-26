"""
Enunciado
Cierta empresa requiere una aplicación informática 
para administrar los datos de su personal, del
cual se conoce:

- número de DNI
- nombre
- apellido 
- año de ingreso.

Existen dos categorías de
empleados:-
- con salario fijo
- a comisión.

Los empleados a comisión tienen
- un salario mínimo, 
- un número de clientes captados
- un monto a cobrar por cada cliente captado.
El salario = clientes captados * monto por cliente

Si el salario obtenido por los clientes
captados no llega a cubrir el salario mínimo, cobrará
el salario mínimo. 

-----

Los empleados con salario fijo
tienen un sueldo básico y un porcentaje adicional
en función del número de años que llevan la empresa: 
• Menos de 2 años: Nada
• De 2 a 5 años: 5% más.
• Más de 5 años: 10% más.

Basado en el enunciado descripto, realizá:

A) El diagrama de clases que lo modelice, con sus relaciones, atributos y métodos.
B) La implementación del método mostrarSalarios que imprima por consola el nombre
completo de cada empleado junto a su salario.
C) La implementación del método empleadoConMasClientes que devuelva al empleado con
mayor cantidad de clientes captados (se supone único).

creen 10 empleados
"""

class Empleado:
    def __init__(self, dni, nombre, apellido, anio_ingreso):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anio_ingreso = anio_ingreso

    def mostrarSalario(self):
        pass

class EmpleadoFijo(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso, sueldo_basico):
        super().__init__(dni, nombre, apellido, anio_ingreso)
        self.sueldo_basico = sueldo_basico

    def mostrarSalario(self):
        anios_en_empresa = 2024 - self.anio_ingreso
        porcentaje_adicional = 0
        if anios_en_empresa >= 5:
            porcentaje_adicional = 0.10
        elif 2 <= anios_en_empresa <= 5:
            porcentaje_adicional = 0.05

        salario_total = self.sueldo_basico * (1 + porcentaje_adicional)
        print(f"{self.nombre} {self.apellido}: ${salario_total}")

class EmpleadoComision(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso, salario_minimo, clientes_captados, monto_por_cliente):
        super().__init__(dni, nombre, apellido, anio_ingreso)
        self.salario_minimo = salario_minimo
        self.clientes_captados = clientes_captados
        self.monto_por_cliente = monto_por_cliente

    def mostrarSalario(self):
        salario = self.clientes_captados * self.monto_por_cliente
        if salario < self.salario_minimo:
            salario = self.salario_minimo
        print(f"{self.nombre} {self.apellido}: ${salario}")




    empleadoFijo1= EmpleadoFijo(11111111, "Juan", "Perez", 2018, 2000),
    empleadoFijo2= EmpleadoFijo(22222222, "Maria", "Gonzalez", 2017, 2500),
    empleadoFijo3= EmpleadoFijo(33333333, "Carlos", "Lopez", 2015, 1800),
    empleadoFijo4= EmpleadoFijo(77777777, "Diego", "Rodriguez", 2014, 2200),
    empleadoFijo5= EmpleadoFijo(88888888, "Sofia", "Fernandez", 2013, 2700),
    
       
    empleadoComision1= EmpleadoComision(44444444, "Ana", "Martinez", 2019, 1500, 10, 100),
    empleadoComision2= EmpleadoComision(55555555, "Pedro", "Sanchez", 2020, 1200, 8, 80),
    empleadoComision3= EmpleadoComision(66666666, "Laura", "Diaz", 2016, 1700, 12, 90),
    empleadoComision4= EmpleadoComision(99999999, "Julia", "Ramirez", 2018, 2000, 15, 110),
    empleadoComision5= EmpleadoComision(10101010, "Daniel", "Torres", 2017, 1900, 20, 120)


empleados = [
    empleadoFijo1,
    empleadoFijo2,
    empleadoFijo3,
    empleadoFijo4,
    empleadoFijo5,
    empleadoComision1,
    empleadoComision2,
    empleadoComision3,
    empleadoComision4,
    empleadoComision5
]



print("Salarios de los empleados:")
for empleado in empleados:
    empleado.mostrarSalario()