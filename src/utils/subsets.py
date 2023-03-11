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

    # Stack para almacenar los estados del conjunto.
    state_stack = Stack()

    # Push de todos los estados del conjunto al stack.
    for state in element:
        state_stack.push(state)

    # Instancia inicial del resultado.
    result = set()

    for state in element:
        result.add(state)

    # Mientras el stack no esté vacío, se obtiene el estado en el tope y se calcula su ε-closure.
    while (not state_stack.is_empty()):
        state = state_stack.pop()
        if ("ε" in mapping[state]):
            new_element = mapping[state]["ε"]
            for reachable_state in new_element:
                state_stack.push(reachable_state)
            result |= new_element

    # Retorno del resultado.
    return result

# Definición de movimiento de estados con un símbolo.
def move(element, symbol, mapping):

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

def subset_construction(nfa):
    print(ε_closure({ nfa.initial_state, 1, 3 }, nfa.mapping))
    print(move({ 0, 2 }, "a", nfa.mapping))
    pass
