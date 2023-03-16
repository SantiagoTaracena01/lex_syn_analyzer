"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Definición de la clase Node y su constructor.
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
