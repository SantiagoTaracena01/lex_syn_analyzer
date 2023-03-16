"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

from utils.classes.node import Node

def nullable(char):
    return (char == "ε")

def direct_construction(postfix):

    postfix = postfix + "#."

    print(postfix)
