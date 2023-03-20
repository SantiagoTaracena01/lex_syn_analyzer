"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Definición de la clase Node.
class Node(object):

    # Método constructor de la clase Node.
    def __init__(self, value, position=None):
        self.value = value
        self.position = position
        self.left = None
        self.right = None
        self.properties = { "firstpos": set(), "lastpos": set(), "followpos": set() }

    # Método para imprimir el árbol inorder.
    def print_tree_by_inorder(self):

        # Impresión de la parte izquierda del árbol.
        if (self.left != None):
            self.left.print_tree_by_inorder()

        # Impresión del nodo raíz del recorrido.
        print(self.value)

        # Impresión de la parte derecha del árbol.
        if (self.right != None):
            self.right.print_tree_by_inorder()

    # Representación de la clase Node.
    def __repr__(self):
        string_representation = "Node(\n"
        string_representation += f"\tvalue={self.value},\n"
        string_representation += f"\tleft={self.left},\n"
        string_representation += f"\tright={self.right},\n"
        string_representation += f"\tproperties={self.properties}\n"
        string_representation += ")"
        return string_representation
