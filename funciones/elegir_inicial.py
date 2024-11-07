from funciones.crear_ataques import crear_ataques
from funciones.validaciones import validar_opciones_pokemon_inicial


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