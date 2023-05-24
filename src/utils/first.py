"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Función que calcula el first de un elemento.
def first(grammar, element):

    # Instancia inicial del resultado.
    result = set()

    # Verificación del caso base (terminal).
    if (element in grammar.terminals):
        result |= { element }

    # Caso inductivo (no terminal).
    else:

        # Iteración sobre las producciones.
        for production in grammar.productions:

            # Regla para el caso de que el elemento sea el símbolo inicial.
            if ((element == production.name) and (element != production.listed_rules[0])):
                result |= first(grammar, production.listed_rules[0])

    # Retorno del resultado.
    return result
