class Usuario:
    
    __slots__ = ['nombre', 'edad', 'intereses', 'indice_actual']

    def __init__(self, nombre, edad, intereses):
        self.nombre = nombre
        self.edad = edad
        self.intereses = intereses
        self.indice_actual = 0
    
    def __getitem__(self, index):
        return self.intereses[index]
    
    def __setitem__(self, index, valor):
        self.intereses[index] = valor
    
    def __iter__(self):
        self.indice_actual = 0
        return self
    
    def __next__(self):
        if self.indice_actual >= len(self.intereses):
            raise StopIteration
        interes = self.intereses[self.indice_actual]
        self.indice_actual += 1
        return interes
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Intereses: {self.intereses}"



# Crear una instancia de la clase Usuario __init__
usuario = Usuario("Juan", 28, ["deportes", "lectura", "viajes"])

# Imprimir atributos del usuario 
print(usuario.nombre)
print(usuario.edad)
print(usuario.intereses)

# Acceder a intereses del usuario mediante índices __getitem__
print(usuario[0])
print(usuario[1])
print(usuario[2])

# Modificar intereses del usuario mediante índices __setitem__
usuario[0] = "cine"
print(usuario[0])
print(usuario.intereses)

# Iterar sobre los intereses del usuario __iter__
for interes in usuario:
    print(interes)

# Imprimir el usuario como una cadena de texto __str__
print(str(usuario))

# Iterar sobre los intereses del usuario otra vez (para demostrar que el iterador funciona correctamente) __iter__
for interes in usuario:
    print(interes)