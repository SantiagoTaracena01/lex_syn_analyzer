"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Clases y archivos importantes.
from utils.classes.stack import Stack

# Constantes importantes para el archivo.
OPERATORS = ("+", "?", "*", ".", "|")
OPERATORS_AND_PARENTHESIS = ("(", ")", "+", "?", "*", ".", "|")
OPERATOR_PRECEDENCE = { "+": 3, "?": 3, "*": 3, ".": 2, "|": 1, "(": 0, ")": 0, "": 0 }
IMPOSSIBLY_HIGH_PRECEDENCE = 99

# Función que agrega símbolos de concatenación explícitos a la expresión regular.
def check_concatenations(regex):

    # Expresión regular finalizada.
    output = ""

    # Iteración sobre el índice y caracter de una expresión regular.
    for index, char in enumerate(regex):

        # Cualquier caracter se agrega a la expresión regular convertida.
        output += char

        # Los caracteres |, ( y . nunca llevarán una concatenación después de ellos.
        if ((char == "|") or (char == "(") or (char == ".")):
            continue

        # Condiciones para llevar una concatenación luego del caracter analizado.
        elif ((index < (len(regex) - 1)) and ((char in (")", "+", "?", "*")) or (char not in OPERATORS_AND_PARENTHESIS)) and (regex[index + 1] not in ("+", "?", "*", "|", ")"))):
            output += "."

    # Retorno de la expresión regular convertida.
    return output

# Función que convierte una expresión regular de infix a postfix.
def regex_infix_to_postfix(regex):

    # Conversión a una expresión con concatenaciones explícitas.
    regex = check_concatenations(regex)

    # Expresión postfix y stack de operaciones.
    postfix = ""
    operator_stack = Stack()

    # Análisis de cada caracter de la expresión regular.
    for char in regex:

        # Si el caracter es un paréntesis izquierdo, se agrega al stack.
        if (char == "("):
            operator_stack.push(char)

        # Si el caracter es un paréntesis derecho, se busca su par izquierdo.
        elif (char == ")"):
            while (operator_stack.peek() and (operator_stack.peek() != "(")):
                postfix += operator_stack.pop()
            operator_stack.pop()

        # Si el caracter es un operador en el conjunto {*, ., |} o un símbolo.
        else:

            # Mientras el stack no esté vacío se analiza la expresión.
            while (not operator_stack.is_empty()):

                # Obtención de los caracteres y precedencias de los operadores.
                peeked_char = operator_stack.peek()
                peeked_precedence = OPERATOR_PRECEDENCE.get(peeked_char, IMPOSSIBLY_HIGH_PRECEDENCE)
                char_precedence = OPERATOR_PRECEDENCE.get(char, IMPOSSIBLY_HIGH_PRECEDENCE)

                # Si la precedencia del operador en el stack es mayor o igual a la del caracter actual, se agrega a la expresión.
                if (peeked_precedence >= char_precedence):
                    postfix += operator_stack.pop()

                # Si no, se rompe el ciclo.
                else:
                    break

            # El caracter actual se agrega al stack.
            operator_stack.push(char)

    # Si el stack aún no está vacío, todos los demás operadores se agregan a la expresión.
    while (not operator_stack.is_empty()):
        postfix += operator_stack.pop()

    # Retorno de la expresión postfix.
    return postfix
