"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Librería sys para salir del programa en caso de error.
import sys

# Operadores de una expresión regular.
OPERATORS = ("+", "?", "*", ".", "|")

# Función para checar errores léxicos de la expresión regular.
def check_lexical_errors(regex):

    # Verificación de que la expresión regular pueda ser sólo los caracteres '(' y ')'.
    if ((regex == "'('") or (regex == "')'")):
        return

    # Verificación de que la expresión regular no esté vacía.
    if ((regex == "") or (regex == [])):
        sys.exit(f"Error: The regex \"{regex}\" can't be empty.")

    # Verificación de que no haya un operador or al final.
    if (regex[-1] == "|"):
        sys.exit(f"Error: The regex \"{regex}\" can't end with a \"|\" operator.")

    # Verificación de que no haya un operador al inicio.
    for operator in OPERATORS:
        if ((regex == operator) or (regex == [operator]) or (regex == ["(", operator, ")"])):
            sys.exit(f"Error: The regex \"{regex}\" can't be only a \"{operator}\" operator.")
        elif (regex[0] == operator):
            sys.exit(f"Error: The regex \"{regex}\" can't start with a \"{operator}\" operator.")

    # Cuenta de paréntesis izquierdos y derechos.
    left_parenthesis = regex.count("(")
    right_parenthesis = regex.count(")")

    # Verificación de que la cantidad de paréntesis izquierdos y derechos sea la misma.
    if (left_parenthesis != right_parenthesis):
        sys.exit(f"Error: The regex \"{regex}\" has a wrong number of parenthesis.")

    # Cuenta de paréntesis.
    only_parenthesis = True

    # Iteración para encontrar un carácter que no sea paréntesis.
    for char in regex:
        if char not in ("(", ")"):
            only_parenthesis = False
            break

    # Verificación de que no haya solo paréntesis.
    if (only_parenthesis):
        sys.exit(f"Error: The regex \"{regex}\" can't be only parenthesis.")

    # Recorrido de la expresión regular.
    for i in reversed(range(1, len(regex))):
        if ((regex[i] in OPERATORS) and (regex[i - 1] == "|")):
            sys.exit(f"Error: The regex \"{regex}\" has a wrong operator placement at indexes {i - 1} and {i}.")
