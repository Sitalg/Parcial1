import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
base_datos = client["parcial1"]
collection = base_datos["peliculas"]
