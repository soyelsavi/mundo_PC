# llave y valor
diccionario = {
    "IDE" : "Entorno de desarrollo integrado",
    "OOP" : "Programacion orientada a objetos",
    "DBMS" : "Sistema de manejo de bases de datos"
    
}
print (diccionario)
#largo
print(len(diccionario))
#acceder a un elemento
print (diccionario["IDE"])
#Modificar valores
diccionario["IDE"] = "HOla"
print (diccionario.get("IDE")) #Otra forma mismo resultado
#iterar elementos
for termino in diccionario:
    print(termino)
for termino in diccionario:
    print(diccionario[termino], end=" ")
#comprobar existencia
print ("IDE" in diccionario)
# Agregar nuevos elementos
diccionario["pk"] = "Primary key"
#remover
diccionario.pop("pk")
#limpiar
diccionario.clear()
#Eliminar por completo
del diccionario