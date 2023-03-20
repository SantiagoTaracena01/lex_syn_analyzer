"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Módulos importantes para la construcción de Thompson.
from utils.classes.nfa import NFA
from utils.classes.stack import Stack

# Función para construir un NFA a partir de una expresión regular en notación posfix.
def thompson_construction(postfix):

    # Variables importantes para la construcción.
    current_state = 0
    nfa_stack = Stack()

    # Iteración sobre cada caracter de la expresión regular en postfix.
    for char in postfix:

        # Si se encuentra un kleene, se construye un barco.
        if (char == "*"):

            # Se obtiene el NFA que se encuentra en la cima del stack.
            nfa_to_kleene = nfa_stack.pop()

            # Instancia del nuevo NFA kleeneado.
            kleene_nfa = NFA(
                states=nfa_to_kleene.states | { current_state, current_state + 1 },
                alphabet=nfa_to_kleene.alphabet,
                initial_state=current_state,
                acceptance_state=current_state + 1,
                mapping={
                    **nfa_to_kleene.mapping,
                    nfa_to_kleene.acceptance_state: {
                        "ε": set([nfa_to_kleene.initial_state, current_state + 1])
                    },
                    current_state: {
                        "ε": set([nfa_to_kleene.initial_state, current_state + 1])
                    },
                    current_state + 1: {}
                }
            )

            # Cambio de próximo estado y almacenamiento del nuevo NFA.
            current_state += 2
            nfa_stack.push(kleene_nfa)

        # Si se encuentra un nullable, se construye su NFA.
        elif (char == "?"):

            # Se obtiene el NFA que se encuentra en la cima del stack.
            nfa_to_null = nfa_stack.pop()

            # Instancia del nuevo NFA nullableado.
            nullable_nfa = NFA(
                states=nfa_to_null.states | { current_state, current_state + 1 },
                alphabet=nfa_to_null.alphabet,
                initial_state=current_state,
                acceptance_state=current_state + 1,
                mapping={
                    **nfa_to_null.mapping,
                    nfa_to_null.acceptance_state: {
                        "ε": set([current_state + 1])
                    },
                    current_state: {
                        "ε": set([nfa_to_null.initial_state, current_state + 1])
                    },
                    current_state + 1: {}
                }
            )

            # Cambio de próximo estado y almacenamiento del nuevo NFA.
            current_state += 2
            nfa_stack.push(nullable_nfa)

        # Si se encuentra una cerradura positiva, se construye su NFA.
        elif (char == "+"):

            # Se obtiene el NFA que se encuentra en la cima del stack.
            nfa_to_positive = nfa_stack.pop()

            # Instancia del nuevo NFA positivizado.
            positive_nfa = NFA(
                states=nfa_to_positive.states | { current_state, current_state + 1 },
                alphabet=nfa_to_positive.alphabet,
                initial_state=current_state,
                acceptance_state=current_state + 1,
                mapping={
                    **nfa_to_positive.mapping,
                    nfa_to_positive.acceptance_state: {
                        "ε": set([nfa_to_positive.initial_state, current_state + 1])
                    },
                    current_state: {
                        "ε": set([nfa_to_positive.initial_state])
                    },
                    current_state + 1: {}
                }
            )

            # Cambio de próximo estado y almacenamiento del nuevo NFA.
            current_state += 2
            nfa_stack.push(positive_nfa)

        # Si se encuentra una concatenación, se construye una cadena.
        elif (char == "."):

            # Se obtienen los dos últimos NFA del stack.
            second_nfa = nfa_stack.pop()
            first_nfa = nfa_stack.pop()

            # Instancia de la concatenación de los dos últimos NFAs.
            concatenation_nfa = NFA(
                states=first_nfa.states | second_nfa.states - { second_nfa.initial_state },
                alphabet=first_nfa.alphabet | second_nfa.alphabet,
                initial_state=first_nfa.initial_state,
                acceptance_state=second_nfa.acceptance_state,
                mapping={
                    **first_nfa.mapping,
                    **second_nfa.mapping,
                    first_nfa.acceptance_state: {
                        **second_nfa.mapping[second_nfa.initial_state]
                    }
                }
            )

            # Almacenamiento del nuevo NFA (no se crearon nuevos estados).
            nfa_stack.push(concatenation_nfa)

        # Si se encuentra una unión, se construye una hamburguesa.
        elif (char == "|"):

            # Se obtienen los dos últimos NFA del stack.
            second_nfa = nfa_stack.pop()
            first_nfa = nfa_stack.pop()

            # Instancia de la unión de los dos últimos NFAs.
            union_nfa = NFA(
                states=set([*first_nfa.states, *second_nfa.states, current_state, current_state + 1]),
                alphabet=set([*first_nfa.alphabet, *second_nfa.alphabet]),
                initial_state=current_state,
                acceptance_state=current_state + 1,
                mapping={
                    **first_nfa.mapping,
                    **second_nfa.mapping,
                    first_nfa.acceptance_state: {
                        "ε": set([current_state + 1])
                    },
                    second_nfa.acceptance_state: {
                        "ε": set([current_state + 1])
                    },
                    current_state: {
                        "ε": set([first_nfa.initial_state, second_nfa.initial_state])
                    },
                    current_state + 1: {}
                }
            )

            # Cambio de próximo estado y almacenamiento del nuevo NFA.
            current_state += 2
            nfa_stack.push(union_nfa)

        # Para cualquier otro caracter, se realiza un NFA simple.
        else:

            # Instancia del NFA simple.
            char_nfa = NFA(
                states=set([current_state, current_state + 1]),
                alphabet=set([char]),
                initial_state=current_state,
                acceptance_state=current_state + 1,
                mapping={
                    current_state: {
                        char: set([current_state + 1])
                    },
                    current_state + 1: {}
                }
            )

            # Cambio de próximo estado y almacenamiento del nuevo NFA.
            current_state += 2
            nfa_stack.push(char_nfa)

    # Se retorna el último NFA del stack.
    return nfa_stack.pop()
