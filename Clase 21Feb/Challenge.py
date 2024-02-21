class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Libro(Producto):
    def __init__(self, nombre, precio, autor, num_paginas, genero):
        super().__init__(nombre, precio)
        self.autor = autor
        self.num_paginas = num_paginas
        self.genero = genero

    def mostrar(self):
        print(f"Libro: {self.nombre}, Autor: {self.autor}, Páginas: {self.num_paginas}, Género: {self.genero}, Precio: {self.precio}")


class Pelicula(Producto):
    def __init__(self, nombre, precio, director, duracion, genero):
        super().__init__(nombre, precio)
        self.director = director
        self.duracion = duracion
        self.genero = genero

    def mostrar(self):
        print(f"Película: {self.nombre}, Director: {self.director}, Duración: {self.duracion} min, Género: {self.genero}, Precio: {self.precio}")


class Disco(Producto):
    def __init__(self, nombre, precio, artista, num_canciones, genero):
        super().__init__(nombre, precio)
        self.artista = artista
        self.num_canciones = num_canciones
        self.genero = genero

    def mostrar(self):
        print(f"Disco: {self.nombre}, Artista: {self.artista}, Número de canciones: {self.num_canciones}, Género: {self.genero}, Precio: {self.precio}")

libro1 = Libro("Cien años de soledad", 20000, "Gabriel García Márquez", 1000, "Novela")
libro2 = Libro("Señor de los anillos", 15000, "Tolkien", 477, "Aventura")
libro3 = Libro("El principito", 10000, "Antoine de Saint-Exupéry", 300, "Novela")

pelicula1 = Pelicula("Rey Leon", 2000, "Disney", 120, "infantil")
pelicula2 = Pelicula("Titanic", 2500, "James Cameron", 210, "Suspenso")
pelicula3 = Pelicula("El secreto de sus ojos", 1500, "Campanola", 110, "Suspenso")

disco1 = Disco("Thriller", 5000, "Michael Jackson", 9, "Pop")
disco2 = Disco("Back in Black", 5000, "AC/DC", 10, "Rock")
disco3 = Disco("The Dark Side of the Moon", 7000, "Pink Floyd", 11, "Rock Progresivo")

# Llamada al método mostrar para cada instancia
libro1.mostrar()
pelicula1.mostrar()
disco1.mostrar()
