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
        string_representation = "NFA(\n"
        string_representation += f"\tstates={self.states},\n"
        string_representation += f"\talphabet={self.alphabet},\n"
        string_representation += f"\tinitial_state={self.initial_state},\n"
        string_representation += f"\tacceptance_state={self.acceptance_state},\n"
        string_representation += f"\tmapping={self.mapping}\n"
        string_representation += ")"
        return string_representation
