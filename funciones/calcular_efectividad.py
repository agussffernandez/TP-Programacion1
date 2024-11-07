# Según la regla de efectividad de tipos

def calcular_efectividad(tipo_atacante: str, tipo_oponente: str) -> tuple:
    """ 
    Calcula la efetividad de un ataque basado en los tipos
    
    Args:
        tipo_atacante(str): El nombre del tipo de Pokemon atacante a calcular efectividad.
        tipo_oponente(str): El nombre del tipo de Pokemon oponente.
    
    Return:
        (tuple) -> (int,str): Retorna el puntaje de efectividad, un mensaje
    """
    #tipo fuego
    if tipo_atacante == "Fuego" and tipo_oponente == "Planta":
        efectividad = 2
        mensaje_efectividad = "Muy Efectivo"
    elif tipo_atacante == "Fuego" and tipo_oponente == "Agua":
        efectividad = 0.5
        mensaje_efectividad = "Poco Efectivo"
    # tipo agua
    elif tipo_atacante == "Agua" and tipo_oponente == "Fuego":
        efectividad = 2
        mensaje_efectividad = "Muy Efectivo"
    elif tipo_atacante == "Agua" and tipo_oponente == "Planta":
        efectividad = 0.5
        mensaje_efectividad = "Poco Efectivo"
    # tipo planta
    elif tipo_atacante == "Planta" and tipo_oponente == "Agua":
        efectividad = 2
        mensaje_efectividad = "Muy Efectivo"
    elif tipo_atacante == "Planta" and tipo_oponente == "Fuego":
        efectividad = 0.5
        mensaje_efectividad = "Poco Efectivo"
    # tipo electrico
    elif tipo_atacante == "Electrico" and tipo_oponente == "Agua":
        efectividad = 2
        mensaje_efectividad = "Muy Efectivo"
    # tipos de igual tipo, o contra alguno que no sean ni muy ni poco efectivos
    else:
        efectividad = 1
        mensaje_efectividad = "Efectivo"
    
    return efectividad , mensaje_efectividad
