def validar_opciones_pokemon_inicial(opcion:str) -> str:
    while opcion != "1" and opcion != "2" and opcion != "3":
        opcion = input("Opción no válida. Elige 1, 2 o 3: ")
    return opcion