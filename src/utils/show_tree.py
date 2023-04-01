"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para la visualización del árbol.
import os
import graphviz

# Configuración de la ruta de Graphviz.
os.environ["PATH"] += os.pathsep + "C:/Program Files/Graphviz/bin"

# Función para mostrar un nodo del árbol.
def show_node(node, visual_tree):
    if (node is not None):
        label = str(node.value) if ((node.left != None) or (node.right != None)) else str(chr(int(node.value)))
        visual_tree.node(str(id(node)), label, shape="circle")
        if (node.left != None):
            visual_tree.edge(str(id(node)), str(id(node.left)))
            show_node(node.left, visual_tree)
        if (node.right != None):
            visual_tree.edge(str(id(node)), str(id(node.right)))
            show_node(node.right, visual_tree)

# Función para visualizar un árbol.
def show_expression_tree(root, view=False):
    visual_tree = graphviz.Digraph(comment="Expression Tree")
    show_node(root, visual_tree)
    visual_tree.render("./out/tree-output", format="png", view=view)
