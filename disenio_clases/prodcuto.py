class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self.__id_productos = Producto.contador_productos
        self.__nombre = nombre
        self.__precio = precio
    
    def __str__(self):
        return "Id Producto: " + str(self.__id_productos) + ", Nombre: " + self.__nombre + ", Precio: " + str(self.__precio)
    def getPrecio(self):
        return self.__precio