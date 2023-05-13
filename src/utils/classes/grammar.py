"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

class Grammar(object):
    def __init__(self, productions, terminals, non_terminals):
        self.productions = productions
        self.terminals = terminals
        self.non_terminals = non_terminals

    def __str__(self):
        grammar_string = ""
        for production in self.productions:
            grammar_string += f"{production.name} -> {production.rules}\n"
        return grammar_string # + "\n" + str(self.terminals) + "\n" + str(self.non_terminals) + "\n"
