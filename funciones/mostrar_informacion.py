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
    (Algunos pokemones incluyen en sus ataques acciones para 
    esquivar el ataque o de defensa )
    
    4) Turnos: El jugador y el oponente se turnan para realizar ataques
    hasta que un Pokemón sea derrotado
    
    """
    
    print(reglas)


def mostrar_debilidades_de_tipos() -> None:
    """ Muestra las debilidades de cada tipo de Pokemón """
    
    debilidades = """ 
    DEBILIDADES Y FORTALEZAS DE CADA TIPO:
    
    FUEGO: Debíl contra el Agua <--> Fuerte contra el Planta
    AGUA: Debíl contra el Eléctrico/Planta <--> Fuerte contra el Fuego
    PLANTA: Debíl contra el Fuego/Veneno <--> Fuerte contra el Agua
    ELECTRICO: Debíl contra el Tierra <--> Fuerte contra el Agua
    """
    
    print(debilidades)


def mostrar_menu_opciones() -> None:
    """Muestra el menú de opciónes que hay dentro del juego  """
    
    opciones = """ 
    
    1. Volver a ver las reglas del juego
    2. Ver debilidades de los tipos de Pokemones
    3. Jugar
    4. Salir del juego
    """
    
    print(opciones)