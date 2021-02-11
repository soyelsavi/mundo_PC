from dispositivos_entrada import DispositivosEntrada



class Raton(DispositivosEntrada):
    contador_ratones = 0
    def __init__(self, tipo, marca):
        Raton.contador_ratones = +1
        self.__id = Raton.contador_ratones
        self._marca = marca
        self._tipo = tipo
        
        
    def __str__ (self):
        return (
            f"Id: {self.__id},  "
            f"Marca: {self._marca}"
            f" Tipo: {self._tipo}"
        )
