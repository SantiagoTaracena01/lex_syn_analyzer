"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Clase Grammar para modelar gramáticas.
class Grammar(object):

    # Método constructor de la clase Grammar.
    def __init__(self, productions, terminals, non_terminals):
        self.productions = productions
        self.terminals = terminals
        self.non_terminals = non_terminals
        self.initial_production = productions[0]
        self.initial_element = productions[0].name

    # Método que obtiene las producciones de un símbolo dado.
    def get_productions_by_symbol(self, symbol):
        return [production for production in self.productions if (symbol == production.name)]

    # Método que representa a la clase Grammar en forma de string.
    def __repr__(self):
        grammar_string = ""
        for production in self.productions:
            grammar_string += f"{production.name} -> {' '.join(production.listed_rules)}\n"
        return grammar_string
