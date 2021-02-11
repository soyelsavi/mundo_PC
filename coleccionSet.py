#Set es una colección sin orden y sin elementos repetidos
planetas = {"MArte","jupiter","Venus"}
print(planetas)
#largo
print(len(planetas))
#revisar si hay elementeso
print("jupiter" in planetas)
#agregar 
planetas.add("Tierra")
print(planetas)
#Eliminar
planetas.remove("Tierra")
print(planetas)
planetas.discard("jupiters") #No arroja error cuando no se encuentran
#Limpiar 
planetas.clear()
#Eliminar el set
del planetas