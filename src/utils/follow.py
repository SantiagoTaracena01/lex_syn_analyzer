"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Función first necesaria para el desarrollo de follow.py.
from utils.first import first

# Función que calcula el follow de un elemento.
def follow(grammar, element):

    # Resultado de la ejecución de follow.
    result = []

    # Regla para el caso de que el elemento sea el símbolo inicial.
    if (element == grammar.initial_element):
        result.append("$")

    # Cualquier otro caso.
    else:

        # Iteración sobre las producciones.
        for production in grammar.productions:

            # Índice del elemento en la producción.
            element_index = production.listed_rules.index(element)

            # Si el elemento no es el último se calcula el first de la siguiente regla.
            if (element_index < (len(production.listed_rules) - 1)):
                next_result = first(grammar, production.listed_rules[element_index + 1])
                result.append(next_result)

            # Si el elemento es el último se calcula el follow del símbolo no terminal.
            if ("ε" in first(grammar, production.listed_rules[element_index])):
                next_result = follow(grammar, production.name)
                result.append(next_result)

    # Retorno del resultado.
    return result
