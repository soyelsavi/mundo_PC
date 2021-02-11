class Orden:
    contador_ordenes = 0
    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__productos = productos
    
    def __str__(self):
        productos_str = ""
        for producto in self.__productos:
            productos_str += producto.__str__() + " , "
        return "Orden: " + str(self.__id_orden) + ", Productos: " + productos_str
    
    def agregarProductos(self,producto):
        self.__productos.append(producto)
        
    def calcularTotal(self):
        contador = 0
        for suma in self.__productos:
            contador += suma.getPrecio()
        return contador