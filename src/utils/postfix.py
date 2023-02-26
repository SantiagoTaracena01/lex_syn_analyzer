"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Clases y archivos importantes.
from utils.errors import check_lexical_errors
from utils.classes.stack import Stack

# Constantes importantes para el archivo.
OPERATORS = ("+", "?", "*", ".", "|")
OPERATORS_AND_PARENTHESIS = ("(", ")", "+", "?", "*", ".", "|")
OPERATOR_PRECEDENCE = { "+": 3, "?": 3, "*": 3, ".": 2, "|": 1, "(": 0, ")": 0, "": 0 }
IMPOSSIBLY_HIGH_PRECEDENCE = 99

# Funciones lambda.
get_regex_operands = lambda regex: [char for char in regex if (char not in OPERATORS)]

# Función que simplifica una expresión regular a su mínima expresión.
def simplify_regex(regex):

    # Expresión regular simplificada inicial.
    simplified_regex = ""

    # Recorrido de la expresión del final al inicio.
    for i in reversed(range(1, len(regex))):

        # Si hay dos operadores kleene seguidos, la expresión se simplifica.
        if ((regex[i] == "*") and (regex[i - 1] == "*")):
            pass
        else:
            simplified_regex += regex[i]

    simplified_regex = simplified_regex.replace(" ", "")

    # Retorno de la expresión regular simplificada.
    return (regex[0] + simplified_regex[::-1])

# Función que agrega símbolos de concatenación explícitos a la expresión regular.
def check_concatenations(regex):

    # Expresión regular finalizada.
    output = ""

    # Iteración sobre el índice y caracter de una expresión regular.
    for index, char in enumerate(regex):

        # Cualquier caracter se agrega a la expresión regular convertida.
        output += char

        # Lectura de caracteres y su letra siguiente.
        try:

            # Los caracteres |, ( y . nunca llevarán una concatenación después de ellos.
            if ((char == "|") or (char == "(") or (char == ".")):
                continue

            # Condiciones para llevar una concatenación luego del caracter analizado.
            elif (((char in (")", "+", "?", "*")) or (char not in OPERATORS_AND_PARENTHESIS)) and (regex[index + 1] not in ("+", "?", "*", "|", ")"))):
                output += "."

        # Si ocurre un error buscando el siguiente caracter, el proceso finaliza.
        except:
            pass

    # Retorno de la expresión regular convertida.
    return output

# Función que convierte una expresión regular de infix a postfix.
def regex_infix_to_postfix(regex):

    # Verificación de errores léxicos.
    check_lexical_errors(regex)

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
