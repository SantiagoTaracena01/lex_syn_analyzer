"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Módulos importantes para la construcción de subconjuntos.
from utils.classes.stack import Stack
from utils.classes.dfa import DFA

# Definición de la función ε-closure.
def ε_closure(element, mapping):

    # Si el elemento es un conjunto, se calcula ε-closure de todos sus elementos.
    if (type(element) == set):

        # Stack para almacenar los estados del conjunto.
        state_stack = Stack()

        # Push de todos los estados del conjunto al stack.
        for state in element:
            state_stack.push(state)

        # Instancia inicial del resultado.
        result = set()

        # Mientras el stack no esté vacío, se obtiene el estado en el tope y se calcula su ε-closure.
        while (not state_stack.is_empty()):
            state = state_stack.pop()
            if ("ε" in mapping[state]):
                result |= mapping[state]["ε"]

        # Retorno del resultado.
        return result

    # Si el elemento es un estado, se calcula su ε-closure.
    else:

        # Retorno del ε-closure del resultado.
        return mapping[element]["ε"]

# Definición de movimiento de estados con un símbolo.
def move(element, symbol, mapping):

    # Si el elemento es un conjunto, se calcula move de todos sus elementos.
    if (type(element) == set):

        # Stack para almacenar los estados del conjunto.
        state_stack = Stack()

        # Push de todos los estados del conjunto al stack.
        for state in element:
            state_stack.push(state)

        # Instancia inicial del resultado.
        result = set()

        # Mientras el stack no esté vacío, se obtiene el estado en el tope y se calcula su move.
        while (not state_stack.is_empty()):
            state = state_stack.pop()
            if (symbol in mapping[state]):
                result |= mapping[state][symbol]

        # Retorno del resultado.
        return result

    # Si el elemento es un estado, se calcula su move.
    else:

        # Retorno del move del resultado.
        return mapping[element][symbol]

def subset_construction(nfa):
    pass
