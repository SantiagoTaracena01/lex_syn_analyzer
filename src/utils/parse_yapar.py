"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Clases importantes para la definición de la gramática.
from utils.classes.production import Production
from utils.classes.grammar import Grammar

# Función que obtiene el resultado del análisis del yapar y lo transforma a gramática.
def parse_yapar(output_path):

    # Líneas del archivo, tokens y producciones.
    lines, tokens, productions = [], [], []

    # Lectura del archivo de salida del análisis del yapar.
    with open(output_path, "r", newline="") as file:
        for line in file:
            lines.append(line)

    # Variables importantes para el parseo del yapar.
    getting_productions = False
    current_production = []

    # Iteración enumerada de las líneas del archivo.
    for line in lines:

        # Se ignora la línea si está vacía o si es un WHITESPACE (por ahora).
        if (line.strip() == "" or line.startswith("WHITESPACE")):
            continue

        # Si la línea empieza con SEMICOLON, se reinicia el proceso de obtención de producciones.
        if (line.startswith("SEMICOLON")):
            productions.append(current_production)
            current_production = []

        # Si se está obteniendo una producción, se agrega la línea iterada.
        if (getting_productions):
            current_production.append(line)

        # Si la línea empieza con SPLIT, se empieza a obtener las producciones.
        if (line.startswith("SPLIT")):
            getting_productions = True

    # Lista para almacenar producciones instanciadas y conjuntos del alfabeto.
    instanced_productions = []
    grammar_terminals, grammar_non_terminals = set(), set()

    # Iteración en las producciones sin parsear.
    for production in productions:

        # Variables importantes para el parseo de la producción.
        getting_name = True
        name = ""
        rules = ""

        # Iteración en los elementos de la producción.
        for element in production:

            # Tipo de token y token encontrados por el scanner.
            if (element.strip() == "COLON::"):
                token_type, token = "COLON", ":"
            else:
                token_type, token = element.split(":")

            # Si se encuentra un token COLON, se deja de obtener el nombre de la producción.
            if (token_type == "COLON"):
                getting_name = False
                continue

            # Almacenamiento de terminales y no terminales de la gramática.
            if (token_type == "TERMINAL"):
                grammar_terminals.add(token.strip())
            elif (token_type == "NONTERMINAL"):
                grammar_non_terminals.add(token.strip())

            # Si se está obteniendo un nombre, se almacena, si no, se almacena una regla.
            if (getting_name):
                name = token.strip()
            else:
                rules += token.strip() + " "

        # Eliminación del espacio que queda al final de la regla (y cualquier otro).
        rules = rules.strip()
        instanced_production = Production(name, rules)
        instanced_productions.append(instanced_production)

    # Producciones de la gramática sin operadores OR.
    splitted_productions = []

    # Iteración sobre las producciones instanciadas.
    for production in instanced_productions:

        # Separación de las reglas de la producción.
        splitted_rules = production.rules.strip().split("|")

        # Iteración sobre las reglas obtenidas luego de separar por el OR.
        for rule in splitted_rules:

            # Se crea una nueva producción con el nombre de la producción original y la regla separada.
            new_production = Production(production.name, rule.strip())
            splitted_productions.append(new_production)

    # Limpieza de producciones repetidas.
    splitted_productions_copy = splitted_productions.copy()
    splitted_productions = []

    for production in splitted_productions_copy:
        if (production.name.strip() == "" or production.rules.strip() == ""):
            continue
        splitted_productions.append(production)

    # Producción inicial de la gramática.
    initial_production = splitted_productions[0]

    # Producciones junto con la producción inicial de la gramática extendida.
    splitted_productions = [
        Production(f"{initial_production.name}'", initial_production.name),
        *splitted_productions,
    ]

    # Retorno de la gramática del archivo.
    return Grammar(
        splitted_productions,
        list(grammar_terminals),
        list(grammar_non_terminals | {f"{initial_production.name}'"}),
    )
