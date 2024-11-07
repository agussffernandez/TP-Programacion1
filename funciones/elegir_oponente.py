import random


def elegir_oponente() -> str:
    """ 
    Elige un oponente aleatorio para el jugador desde un diccionario.
    """
    oponentes = {
        "1": {
            "nombre": "Cyndaquil",
            "tipo": "Fuego"
        },
        "2": {
            "nombre": "Totodile",
            "tipo": "Agua"
        },
        "3": {
            "nombre": "Chikorita",
            "tipo": "Planta"
        },
        "4": {
            "nombre": "Pikachu",
            "tipo": "Electrico"
        }
    }
    
    
    # Elegir una opción aleatoria de entre las claves del diccionario
    # explicación ----->
    # oponentes.keys(): es un objeto de tipo dict_keys, que se ve como una lista, pero no es una lista propiamente dicha. Keys() es un método de los diccionarios en Python que devuelve una vista de todas las claves en el diccionario
    # a función list() convierte el objeto dict_keys en una lista estándar de Python
    # list(oponentes.keys()): ['1', '2', '3', '4']
    opcion = random.choice(list(oponentes.keys()))
    
    # Obtener el oponente elegido usando la clave aleatoria
    oponente_elegido = oponentes[opcion]
    
    # Imprimir el nombre y tipo del oponente elegido
    print(f"Tu oponente es: {oponente_elegido["nombre"]} (Tipo: {oponente_elegido["tipo"]})")
    
    return oponente_elegido['nombre']
