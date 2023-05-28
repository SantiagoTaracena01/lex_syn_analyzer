"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Clase LR0Automata que modela un autómata LR(0).
class LR0Automata(object):

    # Método constructor de la clase LR0Automata.
    def __init__(self, states):
        self.states = states

    # Método que retorna la representación en string de la clase LR0Automata.
    def __repr__(self):
        repr_string = ""
        for state in self.states:
            if (state.name == "ACCEPT"):
                continue
            repr_string += f"{state}\n"
        return repr_string
