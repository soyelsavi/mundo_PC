import os

class CatalogoPeliculas:
    
    ruta_archivo = "peliculas.txt"
    
    @staticmethod
    def agregar_pelicula(pelicula):
            try:
                archivo = open(CatalogoPeliculas.ruta_archivo, "a")
                archivo.write(pelicula.__str__() + "\n")
            except Exception as e:
                print("Ocurrio una excepción al agregar: ", e)
            finally:
                archivo.close()
                
    @staticmethod
    def listar_peliculas():
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo, "r" )
            print("Catalogo de Peliculas: ")
            print(archivo.read())
        except Exception as e:
                print("Ocurrio una excepción al Listar peliculas: ", e)
        finally:
            archivo.close()
            
            
    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.ruta_archivo)
            print("Archivos eliminados: ")
        except Exception as e:
                print("Ocurrio una excepción al eliminar peliculas: ", e)
       