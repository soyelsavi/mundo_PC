class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
        
    def __add__(self, otro):
        return self.__nombre + otro.__nombre
p1 = Persona("Juan")
p2 = Persona ("Karla")

print(p1 + p2)