import json

class ModeloIndex:
    def __init__(self):
        pass

    def consultaProductos(self):
        try:
            with open('contactos.json', 'r') as file:
                datos = json.load(file)
            return datos
        except FileNotFoundError:
            print("El archivo 'contactos.json' no se encontró.")
            return []