"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Módulos importantes para la construcción de subconjuntos.
from utils.classes.stack import Stack
from utils.classes.queue import Queue
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

# Definición de la función de construcción de subconjuntos.
def subset_construction(nfa):

    # El alfabeto del DFA es el mismo que el del NFA. También se instancia el mapping.
    alphabet = nfa.alphabet
    mapping = {}
    states = {}
    current_state = 0
    state_queue = Queue()

    # Inicio de la construcción de subconjuntos.
    initial_state = ε_closure({nfa.initial_state}, nfa.mapping)
    states[current_state] = initial_state
    state_queue.push(current_state)
    current_state += 1

    # Iteración del algoritmo de construcción de subconjuntos mientras haya estados qué analizar en el stack.
    while (not state_queue.is_empty()):

        # Estado a crear sus transiciones.
        state = state_queue.get()

        # Iteración de los símbolos del alfabeto.
        for symbol in alphabet:

            # Nuevo estado a partir del move del estado actual con el símbolo iteratdo.
            new_state = ε_closure(move(states[state], symbol, nfa.mapping), nfa.mapping)

            # Si el nuevo estado no es vacío y no está en los estados ya creados, se crea un nuevo estado.
            if ((new_state != set()) and (new_state not in states.values())):
                states[current_state] = new_state
                state_queue.push(current_state)
                current_state += 1

            # Se crea la transición del estado actual con el símbolo iterado al nuevo estado.
            for key in states:
                if (states[key] == new_state):
                    new_state = key

            # Creación del nuevo estado en el mapping.
            if (state not in mapping):
                mapping[state] = {}

            # Creación de la nueva transición en el mapping.
            mapping[state][symbol] = new_state

    acceptance_states = set()

    for state in states:
        if (nfa.acceptance_state in states[state]):
            acceptance_states.add(state)

    return DFA(
        states=set(states.keys()),
        alphabet=alphabet,
        initial_state=0,
        acceptance_states=acceptance_states,
        mapping=mapping
    )
