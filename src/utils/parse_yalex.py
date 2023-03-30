"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

from utils.regex_infix_to_postfix import OPERATORS_AND_PARENTHESIS

def list_to_regex(list_to_parse):

    quotation_marks_counter = 0
    interval = False

    for char in list_to_parse:
        if (char == "-"):
            interval = True

    step = 4 if (interval) else 2

    actual_list = []
    new_element = ""

    for char in list_to_parse:
        if (char == "'"):
            quotation_marks_counter += 1
        if ((quotation_marks_counter % step) != 0):
            new_element += char if (char != "'") else ""
        elif (((quotation_marks_counter % 2) == 0) and (0 < quotation_marks_counter)):
            actual_list.append(new_element)
            new_element = ""

    return actual_list[:-1]

# Función para parsear el archivo .yalex a expresión regular.
def parse_yalex(path):

    # Lista inicial para almacenar las líneas del archivo.
    file_lines = []

    # Lectura del archivo y almacenamiento de las líneas en la lista.
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            if (line != "\n"):
                file_lines.append(line.replace("\n", ""))

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
            regex_definition = ""

            # Iteración de los elementos de la lista parseada.
            for element in regular_definitions[definition]:

                # Verificación de intervalos.
                if ("-" in element):

                    # Conversión de intervalos a expresiones regulares.
                    interval_elements = element.split("-")

                    # Iteración de los caracteres del intervalo en ASCII.
                    for char in range(ord(interval_elements[0]), ord(interval_elements[1]) + 1):

                        # Concatenación de los caracteres del intervalo.
                        regex_definition += f"{chr(char)}|"

                # Concatenación de los elementos de la lista.
                else:
                    regex_definition += f"{element}|"

            # Eliminación del último caracter de la expresión regular armada.
            regular_definitions[definition] = regex_definition[:-1]

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

        # Si la regex se está borrando, se reemplaza el caracter por epsilon.
        if (deleting_regex):
            yalex_file_regex[index] = TO_DELETE

        # Si se encuentra un paréntesis izquierdo y un asterisco, empiezan comentarios para borrar.
        if (yalex_file_regex[index] == "(" and yalex_file_regex[index + 1] == "*"):
            deleting_regex = True
            yalex_file_regex[index] = TO_DELETE

        # Si se encuentra un paréntesis derecho y un asterisco, finalizan comentarios para borrar.
        if (yalex_file_regex[index] == ")" and yalex_file_regex[index - 1] == "*"):
            deleting_regex = False
            yalex_file_regex[index] = TO_DELETE

    # Expresión regular inicialmente creada a partir del archivo .yalex dividida por los ORs.
    splitted_yalex_file_regex = "".join(yalex_file_regex).replace(TO_DELETE, "").split("|")
    regex_has_regular_definitions = True

    # Ciclo que reemplaza las definiciones regulares por sus expresiones regulares.
    while (regex_has_regular_definitions):

        # El valor de la variable es falsa hasta hallar una definición regular.
        regex_has_regular_definitions = False

        # Copia de la lista de expresiones regulares para evitar errores de índice.
        splitted_yalex_file_regex_copy = splitted_yalex_file_regex.copy()

        # Iteración sobre cada expresión regular de la definición inicial.
        for index, regex in enumerate(splitted_yalex_file_regex):

            # Iteración en las definiciones regulares para encontrar una en la expresión del archivo.
            for definition in regular_definitions:

                # Si se encuentra una definición en la expresión regular, se cambia el valor de la variable y se reemplaza.
                if (definition in regex):
                    regex_has_regular_definitions = True
                    splitted_yalex_file_regex_copy[index] = splitted_yalex_file_regex_copy[index].replace(definition, f"({regular_definitions[definition]})")

        # Reemplazo de la expresión regular por su copia limpia.
        splitted_yalex_file_regex = splitted_yalex_file_regex_copy.copy()

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

    print("Final regex", splitted_yalex_file_regex)

    return splitted_yalex_file_regex
