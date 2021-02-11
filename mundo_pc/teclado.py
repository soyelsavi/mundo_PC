from dispositivos_entrada import DispositivosEntrada

class Teclado(DispositivosEntrada):
    contador_teclados = 0
    def __init__(self,tipo, marca):
        Teclado.contador_teclados += 1
        self.__id = Teclado.contador_teclados
        self._marca = marca
        self._tipo = tipo
        
    def __str__(self):
        return(
            f"ID: {self.__id},  "
            f"Marca: {self._marca}, "
            f"Tipo: {self._tipo}"
        )
        

    