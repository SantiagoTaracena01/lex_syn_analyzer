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
        string_representation += f"\tacceptance_states={self.acceptance_states},\n"
        string_representation += f"\tmapping={self.mapping}\n"
        string_representation += ")"
        return string_representation

    # Método para simular un DFA.
    def simulate(self, input_string):
            
        # Se obtiene el estado actual.
        current_state = self.initial_state

        # Se recorre la cadena de entrada.
        for symbol in input_string:

            # Se obtiene el estado actual con el símbolo actual.
            current_transition = self.mapping.get(current_state, False)

            if (current_transition == False):
                return False

            current_state = current_transition.get(symbol, False)

            if (current_state == False):
                return False

        # Se retorna si el estado actual es de aceptación.
        return (current_state in self.acceptance_states)
