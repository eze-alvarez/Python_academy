# animal
# perro(animal)
# aguila(animal)

class Animal:
    def __init__(self,cantidad_patas,tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo
    
    def moverse(self):
        pass
    
class Perro(Animal):
    def __init__(self,nombre,raza):
        super().__init__(self,cantidad_patas, tipo)
        self.nombre = nombre
        self.raza = raza



    def moverse(self):
        return 'estoy corriendo'
    

class Aguila(Animal):
    def __init__(self,nombre,raza):
        self.nombre = nombre
        self.raza = raza
    
    def moverse(self):
        return 'estoy volando'
    
