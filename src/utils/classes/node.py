"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Definición de la clase Node y su constructor.
class Node(object):
    def __init__(self, value, position=None):
        self.value = value
        self.position = position
        self.left = None
        self.right = None
        self.properties = { "firstpos": set(), "lastpos": set(), "followpos": set() }

    def print_tree_by_inorder(self):
        if (self.left != None):
            self.left.print_tree_by_inorder()
        print(self.value)
        if (self.right != None):
            self.right.print_tree_by_inorder()

    def __repr__(self):
        string_representation = "Node(\n"
        string_representation += f"\tvalue={self.value},\n"
        string_representation += f"\tleft={self.left},\n"
        string_representation += f"\tright={self.right},\n"
        string_representation += f"\tproperties={self.properties}\n"
        string_representation += ")"
        return string_representation
