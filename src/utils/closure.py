"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para el archivo closure.py.
from utils.classes.stack import Stack
from utils.classes.production import Production

# Función que calcula el closure de una producción.
def closure(grammar, productions):

    # Paso inicial del cálculo del closure.
    closure_list = [*productions]

    # Stack de símbolos para el cálculo del closure.
    symbol_stack = Stack()

    # Lista de símbolos ya guardados.
    saved_symbols = []

    # Iteración sobre las producciones para obtener el siguiente símbolo.
    for production in productions:

        # Obtención del siguiente símbolo a insertar.
        next_symbol_index = production.listed_rules.index(".") + 1

        # Verificación de que el símbolo no esté al final de la producción.
        if (next_symbol_index >= len(production.listed_rules)):
            continue

        # Obtención del siguiente símbolo.
        next_symbol = production.listed_rules[next_symbol_index]

        # Inserción del símbolo en el stack.
        symbol_stack.push(next_symbol)

        # Ciclo que verifica que el stack no esté vacío.
        while (not symbol_stack.is_empty()):

            # Se obtienen las producciones que contienen al símbolo.
            productions = grammar.get_productions_by_symbol(next_symbol)

            # Parseo de las producciones para tener el punto inicial.
            parsed_productions = [Production(production.name, f". {production.rules}") for production in productions]

            # Se itera sobre las producciones.
            for production in parsed_productions:

                # Se verifica que la producción no esté en el closure.
                if (production not in closure_list):

                    # Se agrega la producción al closure.
                    closure_list.append(production)

                # Se obtiene el siguiente símbolo de la producción.
                next_symbol_index = production.listed_rules.index(".") + 1
                next_symbol = production.listed_rules[next_symbol_index]

                # Se verifica que el símbolo no esté en el stack ni en el closure.
                if ((next_symbol not in saved_symbols) and (next_symbol not in grammar.terminals)):

                    # Agregación del símbolo al stack.
                    symbol_stack.push(next_symbol)
                    saved_symbols.append(next_symbol)

            # Se obtiene el siguiente símbolo de la pila.
            next_symbol = symbol_stack.pop()

    # Lista de producciones ya guardadas.
    saved_rules, closure_result = [], []

    # Eliminación de producciones repetidas.
    for production in closure_list:
        if (production.listed_rules not in saved_rules):
            saved_rules.append(production.listed_rules)
            closure_result.append(production)

    # Retorno del resultado del closure.
    return closure_result
