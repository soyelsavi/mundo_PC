from computadora import Computadora

class Orden:
    contador_orden = 0
    def __init__ (self, computadora):
        Computadora.contador_computadoras += 1
        self.__id = Computadora.contador_computadoras
        self.__computadora = computadora
        
    def agregar_computadoras(self,computadora):
        self.__computadora.append(computadora)
        
    def __str__(self):
        computadora_str = ""
        for computadora in self.__computadora:
            computadora_str += computadora.__str__()
        
        return (
            f"Orden: {self.__id} "
            f"Computadoras: {computadora_str} "
        )