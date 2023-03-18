"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para la construcción directa.
from utils.classes.node import Node
from utils.classes.stack import Stack

# Método para construir el árbol de expresión a partir de una expresión postfix.
def build_expression_tree(postfix):

    # Variables necesarias para la construcción del árbol.
    node_stack = Stack()
    node_array = []
    position = 1

    # Iteración en la expresión postfix aumentada.
    for char in postfix:

        # Construcción de un nodo con operador kleene.
        if (char == "*"):

            # Obtención del nodo hijo del operador kleene.
            operand = node_stack.pop()
            node = Node(char)
            node.left = operand
            node_stack.push(node)
            node_array.append(node)

        # Construcción de un nodo con operador positivo.
        elif (char == "+"):

            # Obtención del nodo hijo del operador positivo.
            operand = node_stack.pop()
            node = Node(char)
            node.left = operand
            node_stack.push(node)
            node_array.append(node)

        # Construcción de un nodo con operador nullable.
        elif (char == "?"):

            # Obtención del nodo hijo del operador nullable.
            operand = node_stack.pop()
            node = Node(char)
            node.left = operand
            node_stack.push(node)
            node_array.append(node)

        # Construcción de un nodo con operador concatenación.
        elif (char == "."):

            # Obtención de los nodos hijos del operador concatenación.
            right_operand = node_stack.pop()
            left_operand = node_stack.pop()
            node = Node(char)
            node.left = left_operand
            node.right = right_operand
            node_stack.push(node)
            node_array.append(node)

        # Construcción de un nodo con operador or.
        elif (char == "|"):

            # Obtención de los nodos hijos del operador or.
            right_operand = node_stack.pop()
            left_operand = node_stack.pop()
            node = Node(char)
            node.left = left_operand
            node.right = right_operand
            node_stack.push(node)
            node_array.append(node)

        # Construcción de una hoja del árbol (símbolo del alfabeto, epsilon o #).
        else:

            # Creación de la hoja.
            node = Node(char, position)
            node_stack.push(node)
            node_array.append(node)
            position += 1

    # Retorno del nodo raíz del árbol y del arreglo de nodos.
    return node_stack.pop(), node_array

# Método para calcular si un nodo es nullable o no.
def nullable(node):
    
    # Cálculo del caso base de nullable, es decir, una hoja.
    if ((node.left == None) and (node.right == None)):

        # Retorno del valor de nullable según la hoja es epsilon o no.
        return (node.value == "ε")

    # Cálculo del caso inductivo del nullable, es decir, un operador.
    else:

        # Retorno del valor de nullable.
        if (node.value == "*"):
            return True
        elif (node.value == "+"):
            return nullable(node.left)
        elif (node.value == "?"):
            return True
        elif (node.value == "."):
            return (nullable(node.left) and nullable(node.right))
        elif (node.value == "|"):
            return (nullable(node.left) or nullable(node.right))

# Método para calcular el conjunto de firstpos de un nodo.
def firstpos(node):

    # Cálculo del caso base de firstpos, es decir, una hoja.
    if ((node.left == None) and (node.right == None)):

        # Retorno del valor de firstpos según la hoja es epsilon o no.
        if (node.value == "ε"):
            return set()
        else:
            return { node }

    # Cálculo del caso inductivo de firstpos, es decir, un operador.
    else:

        # Retorno del valor de firstpos.
        if (node.value == "*"):
            return firstpos(node.left)
        elif (node.value == "+"):
            return firstpos(node.left)
        elif (node.value == "?"):
            return firstpos(node.left)
        elif (node.value == "."):
            if (nullable(node.left)):
                return firstpos(node.left) | firstpos(node.right)
            else:
                return firstpos(node.left)
        elif (node.value == "|"):
            return firstpos(node.left) | firstpos(node.right)

# Método para calcular el conjunto de lastpos de un nodo.
def lastpos(node):

    # Cálculo del caso base de lastpos, es decir, una hoja.
    if ((node.left == None) and (node.right == None)):

        # Retorno del valor de lastpos según la hoja es epsilon o no.
        if (node.value == "ε"):
            return set()
        else:
            return { node }

    # Cálculo del caso inductivo de lastpos, es decir, un operador.
    else:

        # Retorno del valor de lastpos.
        if (node.value == "*"):
            return lastpos(node.left)
        elif (node.value == "+"):
            return lastpos(node.left)
        elif (node.value == "?"):
            return lastpos(node.left)
        elif (node.value == "."):
            if (nullable(node.right)):
                return lastpos(node.left) | lastpos(node.right)
            else:
                return lastpos(node.right)
        elif (node.value == "|"):
            return lastpos(node.left) | lastpos(node.right)

# Método para calcular el conjunto de followpos de un nodo.
def followpos(node):

    # Cálculo del caso base de followpos, es decir, una hoja.
    if ((node.left == None) and (node.right == None)):

        # Retorno del valor de followpos según la hoja es epsilon o no.
        return set()

    # Cálculo del caso inductivo de followpos, es decir, un operador.
    else:

        # Retorno del valor de followpos.
        if ((node.value == "*") or (node.value == "+")):
            first_step = lastpos(node)
            for state in first_step:
                state.properties["followpos"] |= firstpos(node)
        elif (node.value == "."):
            first_step = lastpos(node.left)
            for state in first_step:
                state.properties["followpos"] |= firstpos(node.right)
        else:
            return set()

def direct_construction(postfix):

    postfix = postfix + "#."
    expression_tree_root, node_array = build_expression_tree(postfix)

    for node in node_array:
        node.properties["nullable"] = nullable(node)
        node.properties["firstpos"] = firstpos(node)
        node.properties["lastpos"] = lastpos(node)
        node.properties["followpos"] = followpos(node)

    expression_tree_root.print_tree_by_inorder()

    for node in node_array:
        if (node.position != None):
            print(node.value, node.position, set([node.position for node in node.properties["followpos"]]))

    print(postfix)
