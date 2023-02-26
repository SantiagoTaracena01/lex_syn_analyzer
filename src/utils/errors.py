"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Librería sys para salir del programa en caso de error.
import sys

OPERATORS = ("+", "?", "*", ".", "|")

# Función para checar errores léxicos de la expresión regular.
def check_lexical_errors(regex):

    # Verificación de que la expresión regular no esté vacía.
    if (regex == ""):
        sys.exit("Error: The regex can't be empty.")

    # Verificación de que no haya un operador or al final.
    if (regex.endswith("|")):
        sys.exit("Error: The regex can't end with a | operator.")

    # Verificación de que no haya un operador al inicio.
    for operator in OPERATORS:
        if (regex == operator):
            sys.exit(f"Error: The regex can't be only a {operator} operator.")
        elif (regex.startswith(operator)):
            sys.exit(f"Error: The regex can't start with a {operator} operator.")

    # Cuenta de paréntesis izquierdos y derechos.
    left_parenthesis = regex.count("(")
    right_parenthesis = regex.count(")")

    # Verificación de que la cantidad de paréntesis izquierdos y derechos sea la misma.
    if (left_parenthesis != right_parenthesis):
        sys.exit("Error: The regex has a wrong number of parenthesis.")

    # Expresión regular separada.
    splitted_regex = list(regex)

    # Recorrido de la expresión regular.
    for i in reversed(range(1, len(splitted_regex))):
        if ((splitted_regex[i] in OPERATORS) and (splitted_regex[i - 1] == "|")):
            sys.exit(f"Error: The regex has a wrong operator placement at indexes {i - 1} and {i}.")
