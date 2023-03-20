"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Módulos importantes para la construcción de subconjuntos.
from utils.classes.queue import Queue
from utils.classes.dfa import DFA

# Definición de la función ε-closure.
def ε_closure(states, mapping):

    # Instancia inicial del resultado.
    result = set()

    # En primer lugar, todos los estados del conjunto se agregan al resultado.
    result |= states
    last_result = set()

    # Mientras el resultado no sea igual al último resultado, se itera sobre el último resultado.
    while (result != last_result):

        # Se actualiza el último resultado.
        last_result = result.copy()

        # Para cada estado del último resultado, se unen los estados a los que se llega con el símbolo ε.
        for state in last_result:
            if ("ε" in mapping[state]):
                result |= mapping[state]["ε"]

    # Retorno del resultado.
    return result

# Definición de movimiento de estados con un símbolo.
def move(states, symbol, mapping):

    # Instancia inicial del resultado.
    result = set()

    # Para cada estado del conjunto, se unen los estados a los que se llega con el símbolo.
    for state in states:
        if (symbol in mapping[state]):
            result |= mapping[state][symbol]

    # Retorno del resultado obtenido.
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
    initial_state = ε_closure({ nfa.initial_state }, nfa.mapping)
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

    # Conjunto inicial de estados de aceptación.
    acceptance_states = set()

    # Creación de los estados de aceptación si el estado de aceptación del NFA está en el estado actual.
    for state in states:
        if (nfa.acceptance_state in states[state]):
            acceptance_states.add(state)

    # Instancia de un mapping temporal del DFA.
    temporal_mapping = {}

    # Iteración de las transiciones en el mapping original.
    for transition in mapping:

        # Nuevo conjunto de transiciones del mapping temporal.
        temporal_mapping[transition] = {}

        # Iteración en cada entrada de la transición actual.
        for entry in mapping[transition]:

            # Si la entrada no va a un estado de atrapamiento, se agrega al nuevo mapping.
            if (mapping[transition][entry] != set()):
                temporal_mapping[transition][entry] = mapping[transition][entry]

    # Cambio del mapping del DFA.
    mapping = temporal_mapping

    # Retorno del DFA.
    return DFA(
        states=set(states.keys()),
        alphabet=alphabet,
        initial_state=0,
        acceptance_states=acceptance_states,
        mapping=mapping
    )
