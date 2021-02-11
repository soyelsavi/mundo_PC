from empleado import Empleado
from gerente import Gerente

def imprimir_detalles(tipo_padre):
    print(tipo_padre)

emp = Empleado("Juan", 100)
imprimir_detalles(emp)