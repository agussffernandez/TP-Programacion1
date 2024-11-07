from validaciones import *
import random

# Función para crear los ataques de los pokemones
def crear_ataques(tipo) -> list:
    """Genera ataques según el tipo del Pokémon.
    
    Arguments:
        tipo(str): el tipo de pokemón
    
    Return:
        (list): Lista con los ataques del tipo del pokemon
    
    """
    if tipo == "Fuego":
        return ["Lanzallamas", "Ember", "Puño fuego", "Golpe ardiente"]
    elif tipo == "Agua":
        return ["Hidrobomba", "Pistola de agua", "Surf", "Golpe acuario"]
    elif tipo == "Planta":
        return ["Rayo solar", "Hoja afilada", "Latigo cepa", "Drenaje"]
    elif tipo == "Eléctrico":
        return ["Rayo", "Trueno", "Impactrueno", "Puño trueno"]



def elegir_pokemon_inicial() -> str:
    """ 
    Pemite a jugador elegir su pokemon inicial: 
    Charmander, Squirtle o Bulbasaur
    
    Return:
        (str): El pokemón elegido
    """
    
    # Diccionario de Pokemones con sus tipos
    pokemones = {
        "1": {
            "nombre": "Charmander",
            "tipo" : "Fuego",
            "ataques": crear_ataques("Fuego")
        },
        "2": {
            "nombre": "Squirtle",
            "tipo" : "Agua",
            "ataques": crear_ataques("Agua")
        },
        "3": {
            "nombre": "Bulbasaur",
            "tipo" : "Planta y Veneno",
            "ataques": crear_ataques("Planta")
        }
    }
    
    print("Elige tu Pokémon inicial:")
    
    # Mostrar todos los Pokémon disponibles para elegir
    for opcion, pokemon in pokemones.items():
        print(f"{opcion}: {pokemon["nombre"]} (Tipo: {pokemon["tipo"]})")
    
    opcion = validar_opciones_pokemon_inicial(input("Elige 1, 2 o 3: "))
    
    # Obtener el Pokémon elegido usando la opción validada
    pokemon_elegido = pokemones[opcion]
    
    # Imprimir el nombre del Pokémon elegido 
    print(f"Has elegido a {pokemon_elegido["nombre"]}")
    # Imprimir los ataques del pokemon
    # "str".join():  Es un método de cadenas que se usa para unir los elementos de una lista (o cualquier iterable) en una sola cadena, usando el valor dentro de la cadena de la cual se llama el método como separador.
    # Los elementos de la lista de ataques estarán separados por una coma y un espacio cuando los unamos.
    print(f"Sus ataques son: {", ".join(pokemon_elegido["ataques"])}")
    
    return pokemon_elegido["nombre"]


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
            "tipo": "Eléctrico"
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

