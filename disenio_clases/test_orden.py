from prodcuto import Producto
from orden import Orden

p1 = Producto("Camisa", 100)
p2 = Producto("Jean", 200)
p3 = Producto("Medias", 25)

productos = [p1,p2]
print(productos)


o1 = Orden(productos)

print(o1)



o2= Orden(productos)
o2.agregarProductos(p3)
print(o2)
print(o2.calcularTotal())
