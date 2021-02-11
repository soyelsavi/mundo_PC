class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return "Nombre: " + self.nombre + " Edad: " + str(self.edad)
        
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre,edad)
        self.sueldo = sueldo
    def __str__(self):
        return super().__str__() + " Sueldo: " + str(self.sueldo)
    
persona = Persona("juan", 28)
print(persona)

empleado = Empleado("Jesus", 22, 50000)
print(empleado)