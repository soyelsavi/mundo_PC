from orden import Orden
from computadora import Computadora
from monitor import Monitor
from teclado import Teclado
from raton import Raton

#Teclados
t1 = Teclado("Usb", "Hp")
t2 = Teclado("Mecanico","Razer")
t3 = Teclado("Mariposa", "MAc")

#Ratones
r1 = Raton("Usb","Genius")
r2 = Raton("Wireless", "Logitech")
r3 = Raton("Gamer", "RedDragon")

#Monitor
m1 = Monitor("lg", 22)
m2 = Monitor("Samsung", 27)
m3 = Monitor("Aoc", 32)

#Computadora
c1 = Computadora("Pc1", m1,t1,r1)
c2 = Computadora("pc2",m2,t2,r2)
c3 = Computadora("pc3",m2,t1,t3)

computadoras = [c1,c2]

o1 = Orden(computadoras)
o1.agregar_computadoras(c3)
print(o1)




