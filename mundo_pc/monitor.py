class Monitor:
    contador_monitores = 0
    def __init__(self, marca, size):
        Monitor.contador_monitores += 1
        self.__id = Monitor.contador_monitores
        self.__marca = marca
        self.__size = size
    
    def get_marca(self):
        return self.__marca
    
    def set_marca(self, marca):
        self.__marca = marca
        
    def get_size(self):
        return self.__size
    
    def set_size(self,size):
        self.__size = size
    
    def __str__(self):
        return (
            f"Id: {self.__id}, "
            f"Marca: {self.__marca}, "
            f"Tamaño: {self.__size}\" "
        )
        


