"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para el archivo lr0_construction.py.
from utils.closure import closure
from utils.goto import goto
from utils.classes.queue import Queue
from utils.classes.production import Production
from utils.classes.lr0_automata import LR0Automata
from utils.classes.lr0_state import LR0State

# Construcción del autómata LR(0) de una gramática.
def lr0_construction(grammar):

    # Lista inicial de producciones extendidas con el signo $.
    extended_productions = []

    # Instancia de las nuevas producciones extendidas.
    for production in grammar.productions:
        extended_productions.append(
            Production(production.name, " ".join(production.listed_rules + ["$"]))
        )

    # Se reemplazan las producciones de la gramática por las extendidas.
    grammar.productions = extended_productions

    # Cola de estados.
    state_queue = Queue()
    created_states = []

    # Alfabeto de la gramática.
    alphabet = grammar.non_terminals + grammar.terminals
    alphabet = [symbol for symbol in alphabet if (not symbol.endswith("'"))]

    # Agregar punto al inicio de la primera producción.
    initial_production = grammar.productions[0]
    initial_production.listed_rules.insert(0, ".")

    # Producción de aceptación a agregar.
    acceptance_listed_rules = initial_production.listed_rules.copy()
    acceptance_listed_rules.remove(".")
    acceptance_listed_rules.insert(len(acceptance_listed_rules) - 1, ".")
    acceptance_production = Production(initial_production.name, " ".join(acceptance_listed_rules))

    # Número del último estado creado.
    last_created_state = 0

    # Calcular el closure de la primera producción.
    closure_result = closure(grammar, [initial_production])

    # Crear el estado inicial.
    initial_state = LR0State(f"I{last_created_state}", closure_result)
    state_queue.push(initial_state)
    created_states.append(initial_state)

    # Estado de aceptación.
    accept_state = LR0State("ACCEPT", [])
    created_states.append(accept_state)

    # Suma del nuevo estado a last_created_state.
    last_created_state += 1

    # Ciclo que verifica que la cola no esté vacía.
    while (not state_queue.is_empty()):

        # Se obtiene el estado de la cola.
        current_state = state_queue.get()

        # Iteración sobre el alfabeto para hallar transiciones.
        for symbol in alphabet:

            # Resultado de la función goto con el estado y símbolo actuales.
            goto_result = goto(grammar, current_state, symbol)
            new_state = LR0State(f"I{last_created_state}", goto_result)

            if (goto_result):

                for state in created_states:
                    if (goto_result == state.productions):
                        new_state = state

                current_state.transitions[symbol] = new_state

                if (new_state not in created_states):

                    state_queue.push(new_state)
                    created_states.append(new_state)
                    last_created_state += 1

                if (acceptance_production in goto_result):
                    new_state.transitions["$"] = accept_state

    for state in created_states:
        if (state.name == "ACCEPT"):
            continue

    return LR0Automata(created_states)
