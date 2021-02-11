class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return "Color: "+ self.color + " Ruedas: " + str(self.ruedas)
    
class Coche(Vehiculo):
    def __init__ (self, color, ruedas, velocidad):
        super().__init__(color,ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
        return super().__str__() + " Velocidad: " + str(self.velocidad) +" Km/H"
    
class Bicicleta(Vehiculo):
    def __init__(self,color, ruedas, tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + " Tipo: " + self.tipo
    
v1 = Vehiculo("Rojo", 3)
print(v1)
v2 = Coche("Verde", 4, 300)
print(v2)
v3 = Bicicleta("Azul", 2, "Urbana")
print(v3)

