"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

def list_to_regex(list_to_parse):

    quotation_marks_counter = 0
    interval = False

    for char in list_to_parse:
        if (char == "-"):
            interval = True

    if (interval):
        print("Detected interval.")
    else:

        actual_list = []
        new_element = ""

        for char in list_to_parse:
            if (char == "'"):
                quotation_marks_counter += 1
            if ((quotation_marks_counter % 2) != 0):
                new_element += char if (char != "'") else ""
            elif (((quotation_marks_counter % 2) == 0) and (0 < quotation_marks_counter)):
                actual_list.append(new_element)
                new_element = ""

        return actual_list[:-1]

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

    for regular_definition in unparsed_regular_definitions:
        clean_regular_definition = regular_definition.replace("let ", "")
        key_value_definition = [string.strip() for string in clean_regular_definition.split("=")]
        regular_definitions[key_value_definition[0]] = key_value_definition[1]

    for definition in regular_definitions:
        if (regular_definitions[definition].startswith("[")):
            regular_definitions[definition] = list_to_regex(regular_definition[definition])
