def json_insert():
    titulo = input("Ingrese el título de la película: ")
    genero = input("Ingrese el género de la película: ")
    año = input("Ingrese el año de la película: ")
    duracion = input("Ingrese el duración de la película: ")
    productor = input("Ingrese el productor de la película: ")

    pelicula = {
        "titulo": titulo,
        "genero": genero,
        "año": año,
        "duración": duracion,
        "productor": productor
    }
    return (pelicula)

def json_update():
    print("Menú de opciones")
    print("1. Modificar todo el documento.")
    print("2. Moficar un elemento del documento.")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        return json_insert()
    elif opcion == 2:
        indice = input("Ingrese el campo a modificar: ")
        valor = input("Ingrese el nuevo valor: ")
        pelicula = {indice: valor}
        return pelicula