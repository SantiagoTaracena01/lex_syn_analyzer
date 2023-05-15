"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Clase Production que modela producciones de una gramática.
class Production(object):

    # Método constructor de la clase Production.
    def __init__(self, name, rules):
        self.name = name
        self.rules = rules
        self.listed_rules = rules.split(" ")

    # Método que compara dos producciones.
    def __eq__(self, other):
        return ((self.name == other.name) and (self.rules == other.rules))

    # Método que devuelve la representación en string de la clase Production.
    def __repr__(self):
        return f"{self.name} -> {' '.join(self.listed_rules)}"
