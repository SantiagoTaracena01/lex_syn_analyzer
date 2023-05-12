"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para la construcción directa.
from utils.regex_infix_to_postfix import OPERATORS
from utils.classes.node import Node
from utils.classes.stack import Stack
from utils.classes.dfa import DFA

# Método para construir el árbol de expresión a partir de una expresión postfix.
def build_expression_tree(postfix):

    # Corrección de expresión regular postfix.
    if (f"{postfix[-2]}{postfix[-1]}" != "35."):
        postfix.append("35")
        postfix.append(".")

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

    # Modo pánico supongo.
    if (type(node) != Node):
        return False

    # Cálculo del caso base de nullable, es decir, una hoja.
    if ((type(node) == Node) and (node.left == None) and (node.right == None)):

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

    # Modo pánico supongo.
    if (type(node) != Node):
        return set()

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

    # Modo pánico supongo.
    if (type(node) != Node):
        return set()

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

    # Modo pánico supongo.
    if (type(node) != Node):
        return set()

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

# Método para la construcción directa de expresión postfix a DFA.
def direct_construction(postfix, tokens):

    # Obtención del árbol de expresión y del arreglo de nodos.
    expression_tree_root, node_array = build_expression_tree(postfix)

    # Cálculo de los conjuntos nullable, firstpos, lastpos y followpos para cada nodo.
    for node in node_array:
        node.properties["nullable"] = nullable(node)
        node.properties["firstpos"] = firstpos(node)
        node.properties["lastpos"] = lastpos(node)
        node.properties["followpos"] = followpos(node)

    # Variables importantes para el DFA.
    states = set()
    alphabet = set([char for char in postfix if char not in set(OPERATORS) | {"ε", "#"}])
    indexed_states = []
    mapping = {}
    state_stack = Stack()

    # Obtención del estado inicial (firspos de la raíz) y agregación del mismo al stack.
    initial_state = firstpos(expression_tree_root)
    state_stack.push(initial_state)
    indexed_states.append(initial_state)

    # Iteración en el stack de estados a meter al mapping.
    while (not state_stack.is_empty()):

        # Obtención del estado actual, su índice y creación en el mapping.
        current_state = state_stack.pop()
        current_state_index = indexed_states.index(current_state)
        mapping[current_state_index] = {}

        # Iteración en el alfabeto para obtener los estados siguientes.
        for char in alphabet:

            # Instancia inicial del próximo estado alcanzado con el caracter actual.
            next_state = set()

            # Iteración en el estado actual para obtener los estados siguientes.
            for node in current_state:

                # Si el valor del nodo es el caracter, debemos agregar los followpos del nodo al conjunto de estados siguientes.
                if (node.value == char):

                    # Unión del followpos del nodo al estado siguiente.
                    next_state |= node.properties["followpos"]

            # Si el estado siguiente no está indexado o registrado, se agrega al stack y al arreglo de estados indexados.
            if (next_state not in indexed_states):
                indexed_states.append(next_state)
                state_stack.push(next_state)

            # Se agrega el estado siguiente al mapping.
            mapping[current_state_index][char] = indexed_states.index(next_state)

    # Obtención del conjunto de estados del DFA.
    for index in range(len(indexed_states)):
        states.add(index)

    # Obtención del estado inicial del DFA.
    initial_state = indexed_states.index(initial_state)

    # Obtención del conjunto de estados de aceptación del DFA.
    acceptance_states = set([indexed_states.index(state) for state in indexed_states if (state & lastpos(expression_tree_root) != set())])
    acceptance_states = acceptance_states if (len(acceptance_states) > 0) else { initial_state }

    # Instancia de estados muertos del DFA.
    dead_states = set()

    # Copia de los estados para evitar errores de iteración.
    states_copy = states.copy()

    # Obtención de estados muertos del DFA.
    for dead_state in states_copy:
        if (all([mapping[dead_state][char] == dead_state for char in alphabet]) and (dead_state not in acceptance_states)):
            dead_states.add(dead_state)
            states.remove(dead_state)

    # Eliminación de estados muertos del mapping.
    for dead_state in dead_states:
        for state in states:
            for char in alphabet:
                entry_mapping = mapping.get(state, {})
                result = entry_mapping.get(char, False)
                if ((type(result) != bool) and (mapping[state][char] == dead_state)):
                    del mapping[state][char]
        del mapping[dead_state]

    # Arreglo de DFAs con un estado sin transiciones.
    if (len(mapping) < 2):
        states = { 0 }
        mapping = { 0: { char: 0 for char in alphabet } }

    # Agregación de los estados de aceptación y sus tokens.
    for state in states:
        for index in range(len(tokens)):
            if (f"#{index}" in mapping[state]):
                acceptance_states.add((state, tokens[index]))

    # Eliminación de los estados de aceptación y sus tokens del conjunto de estados.
    acceptance_states_copy = acceptance_states.copy()

    # Eliminación de los estados de aceptación y sus tokens del conjunto de estados si no son tuplas.
    for state in acceptance_states_copy:
        if (type(state) != tuple):
            acceptance_states.remove(state)

    # Retorno del DFA.
    return DFA(
        states=states,
        alphabet=alphabet,
        initial_state=initial_state,
        acceptance_states=acceptance_states,
        mapping=mapping
    )
