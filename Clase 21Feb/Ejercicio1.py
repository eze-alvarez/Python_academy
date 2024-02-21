class Bicicleta:
    def __init__(self,marca,rodado,precio,velocidad):
        self.marca = marca
        self.rodado = rodado
        self.precio = precio
        self.velocidad = velocidad

    def frenar(self):
        while(self.velocidad>0):
            self.velocidad-=1
            print(f'Bajando velocidad: {self.velocidad}')
        print('ya frenaste')

    


miBici = Bicicleta('Venzo', 29, 150000,25)
miBici.frenar()