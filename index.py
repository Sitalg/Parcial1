from  crud import *
from function_basic import *

while True:
    print("Seleccione una opción: ")
    print("1. Buscar películas por fecha de emisión.")
    print("2. Buscar películas por título.")
    print("3. Insertar películas.")
    print("4. Actualizar películas.")
    print("5. Eliminar películas.")
    print("6. Salir.")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        fecha = input("Ingrese la fecha de emisión de la película: ")
        buscar_fecha(fecha)
    elif opcion == "2":
        titulo = input("Ingrese el titulo de la película: ")
        buscar_titulo(titulo)
    elif opcion == "3":
        pelicula = json_insert()
        insertar_peliculas(pelicula)
    elif opcion == "4":
        titulo = input("Ingrese el titulo de la película: ")
        pelicula = json_update()
        actualizar_peliculas(titulo, pelicula)
    elif opcion == "5":
        titulo = input("Ingrese el titulo de la película: ")
        delete_peliculas(titulo)
    elif opcion == "6":
        break
