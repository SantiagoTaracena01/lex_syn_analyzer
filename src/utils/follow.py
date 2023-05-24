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
    result = set()

    # Regla para el caso de que el elemento sea el símbolo inicial.
    if (element == grammar.initial_production.rules):
        result |= { "$" }

    # Iteración sobre las producciones.
    for production in grammar.productions:

        # Ejecución si el elemento está en las reglas de la producción.
        if (element in production.listed_rules):

            # Índice del elemento en la producción.
            element_index = production.listed_rules.index(element)

            # Si el elemento no es el último se calcula el first del siguiente elemento.
            if (element_index < (len(production.listed_rules) - 1)):

                # Unión del resultado del first del siguiente elemento.
                result |= first(grammar, production.listed_rules[element_index + 1])

            # Si el elemento es el último de la regla se obtiene el follow del nombre de la producción.
            elif (element_index == (len(production.listed_rules) - 1)):

                # Unión del resultado del follow del nombre de la producción.
                result |= follow(grammar, production.name)

    # Retorno del resultado.
    return result
