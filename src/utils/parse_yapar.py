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

    getting_productions = False

    current_production = []

    # Iteración enumerada de las líneas del archivo.
    for line in lines:
        if (line.strip() == "" or line.startswith("WHITESPACE")):
            continue

        if (line.startswith("SEMICOLON")):
            productions.append(current_production)
            current_production = []
        if (getting_productions):
            current_production.append(line)

        if (line.startswith("SPLIT")):
            getting_productions = True

    print(productions, "\n")

    instanced_productions = []
    grammar_terminals, grammar_non_terminals = set(), set()

    for production in productions:
        getting_name = True
        name = ""
        rules = ""
        for element in production:
            if (element.strip() == "COLON::"):
                token_type, token = "COLON", ":"
            else:
                token_type, token = element.split(":")

            if (token_type == "COLON"):
                getting_name = False
                continue

            if (token_type == "TERMINAL"):
                grammar_terminals.add(token.strip())
            elif (token_type == "NONTERMINAL"):
                grammar_non_terminals.add(token.strip())

            if (getting_name):
                name = token.strip()
            else:
                rules += token.strip() + " "
        rules = rules.strip()
        instanced_production = Production(name, rules)
        instanced_productions.append(instanced_production)

    splitted_productions = []

    for production in instanced_productions:
        splitted_rules = production.rules.strip().split("|")
        for rule in splitted_rules:
            new_production = Production(production.name, rule.strip())
            splitted_productions.append(new_production)

    # Retorno de la gramática del archivo.
    return Grammar(
        splitted_productions,
        list(grammar_terminals),
        list(grammar_non_terminals),
    )
