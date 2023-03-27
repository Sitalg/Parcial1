from parameters import collection

def buscar_fecha(fecha):
    query = {"año": fecha}
    document = collection.find_one(query)
    print("Título:", document["titulo"])
    print("Género:", document["genero"])
    print("Año:", document["año"])
    print("Duración:", document["duración"])
    print("Productor:", document["productor"])

def buscar_titulo(titulo):
    query = {"titulo": titulo}
    document = collection.find_one(query)
    print("Título:", document["titulo"])
    print("Género:", document["genero"])
    print("Año:", document["año"])
    print("Duración:", document["duración"])
    print("Productor:", document["productor"])

def insertar_peliculas(pelicula):
    result = collection.insert_one(pelicula)
    print(result.inserted_id)

def actualizar_peliculas(titulo, json_up):
    query = {"titulo": titulo}
    new_val = {"$set": json_up}
    result = collection.update_one(query, new_val)
    print(result.modified_count)

def delete_peliculas(titulo):
    query = {"titulo": titulo}
    result = collection.delete_one(query)
    print(result.deleted_count)
