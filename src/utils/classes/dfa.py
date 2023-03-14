"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Definición de la clase DFA.
class DFA(object):

    # Método constructor de DFA que recibe estados, alfabeto, estado inicial, estado de aceptación y mapeo de transiciones.
    def __init__(self, states, alphabet, initial_state, acceptance_states, mapping):
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.acceptance_states = acceptance_states
        self.mapping = mapping

    # Representación en string del DFA.
    def __repr__(self):
        string_representation = "DFA(\n"
        string_representation += f"\tstates={self.states},\n"
        string_representation += f"\talphabet={self.alphabet},\n"
        string_representation += f"\tinitial_state={self.initial_state},\n"
        string_representation += f"\tacceptance_state={self.acceptance_states},\n"
        string_representation += f"\tmapping={self.mapping}\n"
        string_representation += ")"
        return string_representation
