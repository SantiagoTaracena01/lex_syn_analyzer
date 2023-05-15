"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para el archivo goto.py.
from utils.closure import closure
from utils.classes.production import Production

# Función que obtiene el estado siguiente de un estado dado un símbolo.
def goto(grammar, state, symbol):

    # Lista de producciones del nuevo estado.
    new_state = []

    # Iteración sobre las producciones del estado.
    for production in state.productions:

        # Copia de las producciones.
        listed_rules_copy = production.listed_rules.copy()

        # Se obtiene el índice del punto.
        dot_index = listed_rules_copy.index(".")

        # Verificación de estado de aceptación.
        if ((dot_index + 1) >= len(listed_rules_copy)):
            continue

        # Verificación de que el punto no esté al final de la producción.
        if (listed_rules_copy[dot_index + 1] == symbol):

            # Se intercambian los símbolos.
            listed_rules_copy[dot_index], listed_rules_copy[dot_index + 1] = \
                listed_rules_copy[dot_index + 1], listed_rules_copy[dot_index]

            # Nuevo estado con la producción modificada.
            new_state.append(Production(production.name, " ".join(listed_rules_copy)))

    # Se calcula el closure del nuevo estado.
    return closure(grammar, new_state)
