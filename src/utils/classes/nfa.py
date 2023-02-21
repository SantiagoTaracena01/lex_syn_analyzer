"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Definición de la clase NFA.
class NFA(object):

    # Método constructor de NFA que recibe estados, alfabeto, estado inicial, estado de aceptación y mapeo de transiciones.
    def __init__(self, states, alphabet, initial_state, acceptance_state, mapping):
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.acceptance_state = acceptance_state
        self.mapping = mapping

    # Representación en string del NFA.
    def __repr__(self):
        return f"""
            NFA(
                states={self.states},
                alphabet={self.alphabet},
                initial_state={self.initial_state},
                acceptance_state={self.acceptance_state},
                mapping={self.mapping}
            )
        """
