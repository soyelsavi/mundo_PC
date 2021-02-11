from dominio.pelicula import Pelicula
from servicio.catalogoPeliculas import CatalogoPeliculas

opcion = None

while opcion != "4":
    print("Opciones:")
    print("1. Agregar Pelicula")
    print("2. Listar Pelicula")
    print("3. Eliminar Catalogo")
    print("Salir")
    opcion = input("Escribe tu opcion (1-4): ")
    if opcion == "1":
        nombre = input("Proporciona nombre de plicula")
        pelicula = Pelicula(nombre)
        CatalogoPeliculas.agregar_pelicula(pelicula)
    elif opcion == "2":
        CatalogoPeliculas.listar_peliculas()
    elif opcion == "3":
        CatalogoPeliculas.eliminar()
else:
    print("Salimos del programa")
    
