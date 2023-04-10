class AlimentoDeGrano:
    def __init__(self, calorias, fibras, azucares):
        self.calorias = calorias
        self.fibras = fibras
        self.azucares = azucares
    
    def ver_calorias(self):
        return self.calorias
    
    def ver_fibras(self):
        return self.fibras
    
    def ver_azucares(self):
        return self.azucares

class Cereal(AlimentoDeGrano):
    def __init__(self, calorias, fibras, azucares):
        super().__init__(calorias, fibras, azucares)
    
    def __getitem__(self, index):
        if index == "fibras":
            return self.fibras

    def __str__(self):
        return f"Cereal: {self.calorias} cal, {self.fibras} g de fibra, {self.azucares} g de azúcares"

class Snack(AlimentoDeGrano):
    def __init__(self, calorias, fibras, azucares):
        super().__init__(calorias, fibras, azucares)
    
    def __str__(self):
        return f"Snack: {self.calorias} cal, {self.fibras} g de fibra, {self.azucares} g de azúcares"

    def __add__(self, other):
        if isinstance(other, Snack):
            new_calorias = f"{self.calorias} Cal."
            new_fibras = self.fibras + other.fibras
            new_azucares = self.azucares + other.azucares
            return Snack(new_calorias, new_fibras, new_azucares)

# Crear instancias de Cereal y Snack con los datos de la tabla
cereal_abril_2023 = Cereal(300, 5.5, 10)
snack_abril_2023 = Snack(200, 1.5, 8)

# Imprimir los datos de las instancias
print(cereal_abril_2023)
print(snack_abril_2023)

# Crear una nueva instancia de Snack y agregarla a la primera instancia
snack_abril_2023_2 = snack_abril_2023 + snack_abril_2023

# Imprimir los datos de la nueva instancia de Snack
print(snack_abril_2023_2)

# Obtener el valor de las fibras de la instancia de Cereal
print(cereal_abril_2023["fibras"])




cereal_abril_2023 = Cereal(300, 5.5, 10)
snack_abril_2023 = Snack(200, 1.5, 8)
print(cereal_abril_2023)
print(snack_abril_2023)
snack_abril_2023_2 = snack_abril_2023 + snack_abril_2023
print(snack_abril_2023_2)
print(cereal_abril_2023["fibras"])