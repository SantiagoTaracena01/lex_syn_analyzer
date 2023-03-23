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
            regular_definitions[definition] = list_to_regex(regular_definitions[definition])
            regex_definition = ""
            for element in regular_definitions[definition]:
                if ("-" in element):
                    interval_elements = element.split("-")
                    for char in range(ord(interval_elements[0]), ord(interval_elements[1]) + 1):
                        regex_definition += f"{chr(char)}|"
                else:
                    regex_definition += f"{element}|"
            regular_definitions[definition] = regex_definition[:-1]
        print(definition + ":", regular_definitions[definition])

    yalex_file_regex = ""
    building_regex = False

    for line in file_lines:
        if (line.startswith("rule")):
            building_regex = True
            continue
        if (building_regex):
            yalex_file_regex += line

    yalex_file_regex = list(yalex_file_regex.replace(" ", ""))
    deleting_regex = False

    for index, char in enumerate(yalex_file_regex):
        if (char == "{"):
            deleting_regex = True
            yalex_file_regex[index] = "ε"
        if (char == "}"):
            deleting_regex = False
            yalex_file_regex[index] = "ε"
        if (deleting_regex):
            yalex_file_regex[index] = "ε"
        if (yalex_file_regex[index] == "(" and yalex_file_regex[index + 1] == "*"):
            deleting_regex = True
            yalex_file_regex[index] = "ε"
        if (yalex_file_regex[index] == ")" and yalex_file_regex[index - 1] == "*"):
            deleting_regex = False
            yalex_file_regex[index] = "ε"

    print("".join(yalex_file_regex).replace("ε", ""))

    splitted_yalex_file_regex = "".join(yalex_file_regex).replace("ε", "").split("|")
    regex_has_non_terminals = True

    while (regex_has_non_terminals):

        regex_has_non_terminals = False

        for regex in splitted_yalex_file_regex:
            for definition in regular_definitions:
                if (definition in regex):
                    regex_has_non_terminals = True

        splitted_yalex_file_regex_copy = splitted_yalex_file_regex.copy()

        for index, regex in enumerate(splitted_yalex_file_regex):
            for definition in regular_definitions:
                if (definition in regex):
                    splitted_yalex_file_regex_copy[index] = splitted_yalex_file_regex_copy[index].replace(regex, f"({regular_definitions[definition]})")

        splitted_yalex_file_regex = splitted_yalex_file_regex_copy.copy()

    print("Final regex", "|".join(splitted_yalex_file_regex))
