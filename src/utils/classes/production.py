"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

class Production(object):
    def __init__(self, name, rules):
        self.name = name
        self.rules = rules
        self.listed_rules = rules.split(" ")

    def __repr__(self):
        return f"{self.name} -> {self.rules}"
