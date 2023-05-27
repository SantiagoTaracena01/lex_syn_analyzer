"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Función para checar erroes léxicos en las expresiones regulares.
from utils.check_lexical_errors import check_lexical_errors

# Función para encontrar todas las ocurrencias de un substring dentro de un string y devolver sus índices.
find_all = lambda string, substring: [i for i in range(len(string)) if string.startswith(substring, i)]

# Función para leer y retornar las líneas del archivo yalex.
def read_file_lines(file_path):

    # Lista inicial para almacenar las líneas del archivo.
    file_lines = []

    # Lectura del archivo y almacenamiento de las líneas en la lista.
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            if (line != "\n"):
                file_lines.append(line.replace("\n", "").strip())

    # Retorno de las líneas del archivo.
    return file_lines

# Función para convertir expresiones regulares entre corchetes [] en expresiones regulares procesables.
def list_to_regex(list_to_parse):

    # Variables para contar las comillas simples y verificar si hay intervalos.
    quotation_marks_counter = 0
    double_quotation_marks_counter = 0
    interval = False

    # Verificación de existencia de intervalos.
    for index, char in enumerate(list_to_parse):
        if ((char == "-") and ((index - 2) >= 0) and ((index + 2) < (len(list_to_parse) - 1))):
            interval = True

    # Variable para determinar el paso de la iteración.
    step = 4 if (interval) else 2

    # Variables para almacenar la expresión regular.
    actual_list = []
    new_element = ""

    # Iteración de los caracteres de la futura lista.
    for char in list_to_parse:

        # Aumento de la cuenta de comillas simples.
        if (char == "'"):
            quotation_marks_counter += 1

        # Aumento de la cuenta de comillas dobles.
        if (char == "\""):
            double_quotation_marks_counter += 1

        # Verificación de la cuenta de comillas simples.
        if ((quotation_marks_counter % step) != 0):
            new_element += char if (char != "'") else ""
        elif (((quotation_marks_counter % 2) == 0) and (0 < quotation_marks_counter)):
            actual_list.append(new_element)
            new_element = ""

        # Verificación de la cuenta de comillas dobles.
        elif (double_quotation_marks_counter == 1):
            new_element += char if (char != "\"") else ""
        elif (double_quotation_marks_counter == 2):

            # Agregación de cada elemento del rango a la lista.
            for element in list(new_element):
                actual_list.append(element)

            # Lista a utilizar si se encuentran caracteres de escape.
            future_actual_list = []

            # Iteración de los elementos de la lista.
            for index, element in enumerate(actual_list):

                # Verificación de caracteres de escape.
                if (actual_list[index - 1] == "\\"):
                    continue
                elif (element == "\\"):
                    future_actual_list.append(f"\\{actual_list[index + 1]}")
                else:
                    future_actual_list.append(element)

            # Actualización de la lista.
            actual_list = future_actual_list.copy()
            actual_list.append("")
            new_element = ""
            double_quotation_marks_counter = 0

    # Eliminación del último elemento de la lista.
    partial_result = actual_list[:-1]
    regex_definition = ""

    # Iteración de los elementos de la lista parseada.
    for index, element in enumerate(partial_result):

        # Verificación de intervalos.
        if (("-" in element) and (len(element) > 2)):

            # Conversión de intervalos a expresiones regulares.
            interval_elements = element.split("-")

            # Verificación de elementos vacíos.
            if (interval_elements[1] == ""):
                continue

            # Iteración de los caracteres del intervalo en ASCII.
            for char in range(ord(interval_elements[0]), ord(interval_elements[1]) + 1):

                # Concatenación de los caracteres del intervalo.
                regex_definition += f"{chr(char)}|"

        # Concatenación de los elementos de la lista.
        else:
            regex_definition += f"{element}|"

    for element in regex_definition:
        if (element in ("(", ")", "+", "?", "*")):
            regex_definition = regex_definition.replace(element, f"'{element}'")

    # Eliminación del último caracter de la expresión regular armada.
    return regex_definition[:-1]

# Función para obtener las definiciones regulares del archivo.
def get_regular_definitions(file_lines):

    # Lista para almacenar las definiciones regulares.
    unparsed_regular_definitions = []

    # Obtención de las definiciones regulares.
    for line in file_lines:
        if (line.startswith("let")):
            unparsed_regular_definitions.append(line)

    # Instancia inicial de las definiciones regulares.
    regular_definitions = {}

    # Proceso de armado de las definiciones regulares.
    for regular_definition in unparsed_regular_definitions:
        clean_regular_definition = regular_definition.replace("let ", "")
        key_value_definition = [string.strip() for string in clean_regular_definition.split("=")]
        regular_definitions[key_value_definition[0]] = key_value_definition[1]

    # Conversión de intervalos a expresiones regulares.
    for definition in regular_definitions:

        # Cambio de listas a expresiones regulares.
        if (regular_definitions[definition].startswith("[")):

            # Conversión de listas a expresiones regulares e instancia de nueva definición.
            regular_definitions[definition] = list_to_regex(regular_definitions[definition])

        # Expresiones regulares que posiblemente tengan listas dentro.
        else:

            # Listas a eliminar de la expresión regular.
            lists_in_definition = []
            list_to_delete = ""
            getting_list = False

            # Obtención de las listas a eliminar.
            for char in regular_definitions[definition]:

                # Si nos topamos un corchete, comenzamos a obtener la lista.
                if (char == "["):
                    getting_list = True

                # Si estamos obteniendo una lista, concatenamos los caracteres.
                if (getting_list):
                    list_to_delete += char

                # Si encontramos un corchete cerrado, terminamos de obtener la lista.
                if (char == "]"):
                    getting_list = False
                    lists_in_definition.append(list_to_delete)
                    list_to_delete = ""

            # Eliminación de las listas de la expresión regular.
            for list_to_delete in lists_in_definition:
                regular_definitions[definition] = regular_definitions[definition].replace(list_to_delete, f"({list_to_regex(list_to_delete)})")

    # Retorno de las definiciones regulares.
    return regular_definitions

# Función para obtener la expresión regular inicial del archivo.
def get_file_initial_regex_and_tokens(file_lines):

    # Instancia de la futura expresión regular.
    yalex_file_regex = ""
    building_regex = False

    # Obtención de la expresión regular inicial.
    for line in file_lines:

        # Verificación de la línea de inicio de la expresión regular.
        if (line.startswith("rule")):
            building_regex = True
            continue

        # Se agrega texto sólo después de la línea que inicia con rule.
        if (building_regex):
            yalex_file_regex += line

    # Eliminación de espacios en blanco.
    yalex_file_regex = list(yalex_file_regex)
    deleting_regex = False
    TO_DELETE = "ε"

    # Instancia del token de la expresión regular.
    regex_actual_code = ""
    regex_associated_code = []
    getting_code = False

    # Ciclo que elimina los caracteres que no son parte de la expresión regular.
    for index, char in enumerate(yalex_file_regex):

        # Si se encuentra una llave derecha finaliza código para borrar.
        if (char == "}"):
            deleting_regex = False
            getting_code = False
            regex_associated_code.append(regex_actual_code)
            regex_actual_code = ""
            yalex_file_regex[index] = TO_DELETE

        # Si se está recorriendo un token, se guarda en su variable.
        if getting_code:
            regex_actual_code += char

        # Si se encuentra una llave izquierda empieza código para borrar.
        if (char == "{"):
            deleting_regex = True
            getting_code = True
            yalex_file_regex[index] = TO_DELETE

        # Si se encuentra un paréntesis izquierdo y un asterisco, empiezan comentarios para borrar.
        if (yalex_file_regex[index] == "(" and yalex_file_regex[index + 1] == "*"):
            deleting_regex = True
            yalex_file_regex[index] = TO_DELETE

        # Si se encuentra un paréntesis derecho y un asterisco, finalizan comentarios para borrar.
        if (yalex_file_regex[index] == "*" and yalex_file_regex[index + 1] == ")"):
            deleting_regex = False
            yalex_file_regex[index] = TO_DELETE
            yalex_file_regex[index + 1] = TO_DELETE

        # Si la regex se está borrando, se reemplaza el caracter por epsilon.
        if (deleting_regex):
            yalex_file_regex[index] = TO_DELETE

    # Limpieza final de los datos a retornar.
    clean_yalex_file_regex = "".join(yalex_file_regex).replace(TO_DELETE, "").split("|")
    yalex_file_regex = [char.replace(" ", "") for char in clean_yalex_file_regex]
    regex_associated_code = [token.strip() for token in regex_associated_code]

    # Fix para el or.
    if (yalex_file_regex.count("'") == 2):
        yalex_file_regex_copy = []
        for regex in yalex_file_regex:
            if (regex == "'"):
                continue
            else:
                yalex_file_regex_copy.append(regex)
        yalex_file_regex_copy.append("'|'")
        yalex_file_regex = yalex_file_regex_copy.copy()

    # Fix para el or.
    if ("return OR" in regex_associated_code):
        regex_associated_code.remove("return OR")
        regex_associated_code.append("return OR")

    # Obtención de los tokens de la expresión regular.
    regex_code_and_tokens = []
    code_return_positions = [find_all(code, "return") for code in regex_associated_code]
    token_to_return = ""

    # Iteración de los códigos y posiciones.
    for code, positions in zip(regex_associated_code, code_return_positions):
        for position in positions:

            # Inicio de la lectura del token sumando los caracteres de "return "
            RETURN_CHARACTERS = 7
            token_recognition_position = (position + RETURN_CHARACTERS)

            # Lectura del token mientras el índice no supere la longitud del código y no se encuentre un espacio.
            while ((token_recognition_position < len(code)) and (code[token_recognition_position] != " ")):
                token_to_return += code[token_recognition_position]
                token_recognition_position += 1

            # Agregado del código y token a la lista, y eliminación del token agregado.
            regex_code_and_tokens.append((code, token_to_return))
            token_to_return = ""

    if (len(yalex_file_regex) != len(regex_code_and_tokens)):
        actual_regex_code_and_tokens = regex_code_and_tokens.copy()
        regex_code_and_tokens = []
        for entry in actual_regex_code_and_tokens:
            regex_code_and_tokens.append(entry)

    # Retorno de la expresión regular inicialmente creada a partir del archivo .yalex dividida por los ORs (y de los tokens).
    return yalex_file_regex, regex_code_and_tokens

# Función para obtener la expresión regular final del archivo.
def get_full_yalex_regex(file_regex, regular_definitions):

    # Variable que indica si se encontró una definición regular en la expresión regular.
    regex_has_regular_definitions = True

    # Ciclo que reemplaza las definiciones regulares por sus expresiones regulares.
    while (regex_has_regular_definitions):

        # El valor de la variable es falsa hasta hallar una definición regular.
        regex_has_regular_definitions = False

        # Copia de la lista de expresiones regulares para evitar errores de índice.
        file_regex_copy = file_regex.copy()

        # Iteración sobre cada expresión regular de la definición inicial.
        for index, regex in enumerate(file_regex):

            # Posibles expresiones regulares a reemplazar.
            possible_regular_definitions = []

            # Iteración en las definiciones regulares para encontrar una en la expresión del archivo.
            for definition in regular_definitions:

                # Si se encuentra una definición en la expresión regular, se cambia el valor de la variable y se reemplaza.
                if (definition in regex):
                    regex_has_regular_definitions = True
                    possible_regular_definitions.append(definition)

            # Reemplazo por la expresión regular de mayor jerarquía.
            if (len(possible_regular_definitions) > 0):
                found_regular_definition = possible_regular_definitions[-1]
                file_regex_copy[index] = file_regex_copy[index].replace(found_regular_definition, f"({regular_definitions[found_regular_definition]})")

        # Reemplazo de la expresión regular por su copia limpia.
        file_regex = file_regex_copy.copy()

    # Chequeo de posibles errores léxicos.
    for regex in file_regex:
        check_lexical_errors(regex)

    # Retorno de la expresión regular final.
    return file_regex

# Función para convertir los símbolos de la expresión regular a ASCII.
def regex_chars_to_ascii(file_regex):

    # Nueva copia de la expresión regular para separar las subexpresiones en listas.
    file_regex_copy = file_regex.copy()

    # Separación de las subexpresiones en listas.
    for regex in file_regex_copy:
        regex_to_split = file_regex.pop(0)
        file_regex.append(list(regex_to_split))

    # Nueva copia de la expresión regular para convertir a ASCII.
    file_regex_copy = file_regex.copy()

    # Conversión de símbolos a ASCII.
    for regex in file_regex:

        # Nueva expresión regular vacía a colocar en la expresión del archivo.
        regex_copy = []
        file_regex_copy.remove(regex)

        # Variable que indica si se está en una expresión entre comillas.
        on_double_quotes = False

        # Iteración sobre cada símbolo de la expresión regular.
        for jndex, char in enumerate(regex):

            # Si el símbolo es un operador entre comillas, se convierte a ASCII.
            if (jndex < (len(regex) - 1) and (char in ("(", ")", "+", "?", "*", "|")) and (regex[jndex - 1] == "'") and (regex[jndex + 1] == "'")):
                regex_copy.append(str(ord(char)))

            # Si el símbolo es un operador con \, se convierte a ASCII junto con el \.
            elif (regex[jndex - 1] == "\\"):
                regex_copy.pop()
                if (char == "n"):
                    regex_copy.append(str(ord("\n")))
                elif (char == "t"):
                    regex_copy.append(str(ord("\t")))
                elif (char == "r"):
                    regex_copy.append(str(ord("\r")))
                elif (char == "f"):
                    regex_copy.append(str(ord("\f")))
                elif (char == "v"):
                    regex_copy.append(str(ord("\v")))
                elif (char == "b"):
                    regex_copy.append(str(ord("\b")))
                elif (char == "a"):
                    regex_copy.append(str(ord("\a")))
                elif (char == "0"):
                    regex_copy.append(str(ord("\0")))
                elif (char == "s"):
                    regex_copy.append(str(ord(" ")))

            # Si el símbolo es un operador sin comillas, se agrega sin convertir.
            elif (char in ("(", ")", "+", "?", "*", "|")):
                regex_copy.append(char)

            # Si el símbolo es una comilla, sólo se ignora.
            elif (char == "'"):
                continue

            # Si el símbolo es una comilla simple, se cambia a paréntesis.
            elif ((char == "\"") and (not on_double_quotes)):
                on_double_quotes = True
                regex_copy.append("(")
                continue

            # Si el símbolo es una comilla doble, se cambia a paréntesis.
            elif ((char == "\"") and (on_double_quotes)):
                on_double_quotes = False
                regex_copy.append(")")
                continue

            # Para cualquier otro símbolo, se agrega convertido a ASCII.
            else:
                regex_copy.append(str(ord(char)))

        # Agregación de la nueva expresión regular formateada.
        file_regex_copy.append(regex_copy)

    # Símbolo final de la expresión regular.
    regex_token_position = 0

    # Proceso de agregación de los símbolos finales
    for regex in file_regex_copy:
        regex.append(f"#{regex_token_position}")
        regex_token_position += 1

    # Retorno de la expresión regular final.
    return file_regex_copy

# Función para finalizar la estructuración de la expresión regular.
def finish_file_regex(file_regex):

    # Asignación final de la expresión regular con su copia limpia.
    file_regex_copy = file_regex.copy()
    file_regex = []

    # Conversión de todas las subexpresiones a una sola lista de caracteres.
    for regex in file_regex_copy:
        for char in regex:
            file_regex.append(char)
        file_regex.append("|")

    # Eliminación del último OR.
    file_regex.pop()

    # Último intercambio de expresiones.
    file_regex_copy = file_regex.copy()
    file_regex = []

    # Eliminación de los caracteres con código 92.
    for char in file_regex_copy:
        if (char != "92"):
            file_regex.append(char)

    # Retorno de la expresión regular final.
    return file_regex

# Función para parsear el archivo .yalex a expresión regular.
def parse_yalex(path):

    # * Parte 1 - Lectura del archivo.

    # Lista inicial para almacenar las líneas del archivo.
    file_lines = read_file_lines(path)

    # ! INICIA ÁREA DE DEBUG

    # print("\nParte 1 - Lectura del archivo.\n")

    # for line in file_lines:
    #     print(line)

    # print("\n")

    # ! TERMINA ÁREA DE DEBUG

    # * Parte 2 - Obtención de las definiciones regulares.

    regular_definitions = get_regular_definitions(file_lines)

    # ! INICIA ÁREA DE DEBUG

    # print("\nParte 2 - Obtención de las definiciones regulares.\n")

    # for definition in regular_definitions:
    #     print(f"{definition} = {regular_definitions[definition]}")

    # print("\n")

    # ! TERMINA ÁREA DE DEBUG

    # * Parte 3 - Expresión regular del archivo.

    # Expresión regular inicialmente creada a partir del archivo .yalex dividida por los ORs.
    file_regex, regex_code_and_tokens = get_file_initial_regex_and_tokens(file_lines)

    # ! INICIA ÁREA DE DEBUG

    # print("\nParte 3 - Expresión regular del archivo.\n")
    # print("|".join(file_regex))
    # print(regex_code_and_tokens)
    # print("\n")

    # ! TERMINA ÁREA DE DEBUG

    # * Parte 4 - Reemplazo de las definiciones regulares por sus expresiones regulares.

    # Expresión regular final del archivo.
    complete_file_regex = get_full_yalex_regex(file_regex, regular_definitions)

    # ! INICIA ÁREA DE DEBUG

    # print("\nParte 4 - Reemplazo de las definiciones regulares por sus expresiones regulares.\n")
    # print("|".join(complete_file_regex))
    # print("\n")

    # ! TERMINA ÁREA DE DEBUG

    # * Parte 5 - Conversión a ASCII.

    # Expresión regular final del archivo en ASCII.
    complete_file_regex = regex_chars_to_ascii(complete_file_regex)

    # ! INICIA ÁREA DE DEBUG

    # print("\nParte 5 - Conversión a ASCII.\n")

    # for regex in complete_file_regex:
    #     print(regex)

    # print("\n")

    # ! TERMINA ÁREA DE DEBUG

    # * Parte 6 - Conversión a una sola lista de caracteres.

    # Expresión regular final del archivo en ASCII y en una sola lista de caracteres.
    complete_file_regex = finish_file_regex(complete_file_regex)

    # ! INICIA ÁREA DE DEBUG

    # print("\nParte 6 - Conversión a una sola lista de caracteres.\n")
    # print(complete_file_regex)
    # print("\n")

    # ! TERMINA ÁREA DE DEBUG

    # Retorno de la expresión regular del archivo yalex.
    return complete_file_regex, regex_code_and_tokens
