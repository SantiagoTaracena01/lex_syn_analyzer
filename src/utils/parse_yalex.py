"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

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
        if (element in ("(", ")", "+", "?", "*", ".")):
            regex_definition = regex_definition.replace(element, f"'{element}'")

    # Eliminación del último caracter de la expresión regular armada.
    return regex_definition[:-1]


# Función para parsear el archivo .yalex a expresión regular.
def parse_yalex(path):

    # * Parte 1 - Lectura del archivo.

    # Lista inicial para almacenar las líneas del archivo.
    file_lines = []

    # Lectura del archivo y almacenamiento de las líneas en la lista.
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            if (line != "\n"):
                file_lines.append(line.replace("\n", ""))

    # ! INICIA ÁREA DE DEBUG

    # print("\nParte 1 - Lectura del archivo.\n")

    # for line in file_lines:
    #     print(line)

    # print("\n")

    # ! TERMINA ÁREA DE DEBUG

    # * Parte 2 - Obtención de las definiciones regulares.

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

    # ! INICIA ÁREA DE DEBUG

    # print("\nParte 2 - Obtención de las definiciones regulares.\n")

    # for definition in regular_definitions:
    #     print(f"{definition} = {regular_definitions[definition]}")

    # print("\n")

    # ! TERMINA ÁREA DE DEBUG

    # * Parte 3 - Eliminación de las listas de las definiciones regulares.

    # Ciclo para eliminar listas de las definiciones regulares.
    for definition in regular_definitions:

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

    # ! INICIA ÁREA DE DEBUG

    # print("\nParte 3 - Eliminación de las listas de las definiciones regulares.\n")

    # for definition in regular_definitions:
    #     print(f"{definition} = {regular_definitions[definition]}")

    # print("\n")

    # ! TERMINA ÁREA DE DEBUG

    # * Parte 4 - Expresión regular del archivo.

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
    yalex_file_regex = list(yalex_file_regex.replace(" ", ""))
    deleting_regex = False
    TO_DELETE = "ε"

    # Ciclo que elimina los caracteres que no son parte de la expresión regular.
    for index, char in enumerate(yalex_file_regex):

        # Si se encuentra una llave izquierda empieza código para borrar.
        if (char == "{"):
            deleting_regex = True
            yalex_file_regex[index] = TO_DELETE

        # Si se encuentra una llave derecha finaliza código para borrar.
        if (char == "}"):
            deleting_regex = False
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

    # Expresión regular inicialmente creada a partir del archivo .yalex dividida por los ORs.
    splitted_yalex_file_regex = "".join(yalex_file_regex).replace(TO_DELETE, "").split("|")
    regex_has_regular_definitions = True

    # ! INICIA ÁREA DE DEBUG

    # print("\nParte 4 - Expresión regular del archivo.\n")
    # print("|".join(splitted_yalex_file_regex))
    # print("\n")

    # ! TERMINA ÁREA DE DEBUG

    # * Parte 5 - Reemplazo de las definiciones regulares por sus expresiones regulares.

    # Ciclo que reemplaza las definiciones regulares por sus expresiones regulares.
    while (regex_has_regular_definitions):

        # El valor de la variable es falsa hasta hallar una definición regular.
        regex_has_regular_definitions = False

        # Copia de la lista de expresiones regulares para evitar errores de índice.
        splitted_yalex_file_regex_copy = splitted_yalex_file_regex.copy()

        # Iteración sobre cada expresión regular de la definición inicial.
        for index, regex in enumerate(splitted_yalex_file_regex):

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
                splitted_yalex_file_regex_copy[index] = splitted_yalex_file_regex_copy[index].replace(found_regular_definition, f"({regular_definitions[found_regular_definition]})")

        # Reemplazo de la expresión regular por su copia limpia.
        splitted_yalex_file_regex = splitted_yalex_file_regex_copy.copy()

    # ! INICIA ÁREA DE DEBUG

    # print("\nParte 5 - Reemplazo de las definiciones regulares por sus expresiones regulares.\n")
    # print("|".join(splitted_yalex_file_regex))
    # print("\n")

    # ! TERMINA ÁREA DE DEBUG

    # * Parte 6 - Conversión a ASCII.

    # Nueva copia de la expresión regular para separar las subexpresiones en listas.
    splitted_yalex_file_regex_copy = splitted_yalex_file_regex.copy()

    # Separación de las subexpresiones en listas.
    for regex in splitted_yalex_file_regex_copy:
        regex_to_split = splitted_yalex_file_regex.pop(0)
        splitted_yalex_file_regex.append(list(regex_to_split))

    # Nueva copia de la expresión regular para convertir a ASCII.
    splitted_yalex_file_regex_copy = splitted_yalex_file_regex.copy()

    # Conversión de símbolos a ASCII.
    for index, regex in enumerate(splitted_yalex_file_regex):

        # Nueva expresión regular vacía a colocar en la expresión del archivo.
        regex_copy = []
        splitted_yalex_file_regex_copy.remove(regex)

        # Iteración sobre cada símbolo de la expresión regular.
        for jndex, char in enumerate(regex):

            # Si el símbolo es un operador entre comillas, se convierte a ASCII.
            if (jndex < (len(regex) - 1) and (char in ("(", ")", "+", "?", "*", ".", "|")) and (regex[jndex - 1] == "'") and (regex[jndex + 1] == "'")):
                regex_copy.append(str(ord(char)))

            # Si el símbolo es un operador sin comillas, se agrega sin convertir.
            elif (char in ("(", ")", "+", "?", "*", ".", "|")):
                regex_copy.append(char)

            # Si el símbolo es una comilla, sólo se ignora.
            elif (char in ("'", "\"")):
                continue

            # Para cualquier otro símbolo, se agrega convertido a ASCII.
            else:
                regex_copy.append(str(ord(char)))

        # Agregación de la nueva expresión regular formateada.
        splitted_yalex_file_regex_copy.append(regex_copy)

    # ! INICIA ÁREA DE DEBUG

    # print("\nParte 6 - Conversión a ASCII.\n")

    # for regex in splitted_yalex_file_regex_copy:
    #     print(regex)

    # print("\n")

    # ! TERMINA ÁREA DE DEBUG

    # * Parte 7 - Conversión a una sola lista de caracteres.

    # Asignación final de la expresión regular con su copia limpia.
    splitted_yalex_file_regex = splitted_yalex_file_regex_copy.copy()
    splitted_yalex_file_regex_copy = []

    # Conversión de todas las subexpresiones a una sola lista de caracteres.
    for regex in splitted_yalex_file_regex:
        for char in regex:
            splitted_yalex_file_regex_copy.append(char)
        splitted_yalex_file_regex_copy.append("|")

    # Eliminación del último OR.
    splitted_yalex_file_regex_copy.pop()

    # Último intercambio de expresiones.
    splitted_yalex_file_regex = splitted_yalex_file_regex_copy.copy()
    splitted_yalex_file_regex_copy = []

    # Eliminación de los caracteres con código 92.
    for char in splitted_yalex_file_regex:
        if (char != "92"):
            splitted_yalex_file_regex_copy.append(char)

    # Intercambio final.
    splitted_yalex_file_regex = splitted_yalex_file_regex_copy.copy()

    # ! INICIA ÁREA DE DEBUG

    # print("\nParte 7 - Conversión a una sola lista de caracteres.\n")
    # print(splitted_yalex_file_regex)
    # print("\n")

    # ! TERMINA ÁREA DE DEBUG

    # Retorno de la expresión regular del archivo yalex.
    return splitted_yalex_file_regex
