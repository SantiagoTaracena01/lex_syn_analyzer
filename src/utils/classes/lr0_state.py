"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Clase LR0State que modela un estado de la construcción LR(0).
class LR0State(object):

    # Método constructor de la clase LR0State.
    def __init__(self, name, productions):
        self.name = name
        self.productions = productions
        self.transitions = {}

    # Método que compara dos estados LR(0).
    def __eq__(self, other):
        return (self.productions == other.productions)

    # Método que devuelve la representación en string de la clase LR0State.
    def __repr__(self):
        repr_string = f"{self.name}:\n"
        for production in self.productions:
            repr_string += f"{production}\n"
        return repr_string
