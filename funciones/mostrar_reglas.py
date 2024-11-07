def mostrar_reglas() -> None :
    """ 
    Muestra las reglas del juego
    """
    reglas = """
    REGLAS DEL JUEGO:
    
    1) El jugador debera elegir un pokemon incial para jugar:
    * Charmander: tipo Fuego
    * Squirtle: tipo Agua
    * Bulbasaur: Tipo Planta y Veneno
    
    2) Se jugara contra un oponente aleatorio que puede tener cualquiera de los siguientes pokemones iniciales:
    * Cyndaquil: tipo Fuego
    * Totodile: tipo Agua
    * Chikorita: tipo Planta
    * Pikachu: tipo Electrico
    
    3) Acciones: El jugador puede elgir entre atacar o curar.
    
    4) Turnos: El jugador y el oponente se turnan para realizar ataques
    hasta que un Pokemón sea derrotado
    
    """
    
    print(reglas)
