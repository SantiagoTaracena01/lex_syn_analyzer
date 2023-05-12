"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

def parse_yapar(output_path):

    lines, tokens, productions = [], [], []

    with open(output_path, "r", newline="") as file:
        for line in file:
            lines.append(line)

    getting_productions = False

    current_production = []

    for line in lines:
        if (line.strip() == "" or line.startswith("WHITESPACE")):
            continue

        if (line.startswith("SEMICOLON")):
            productions.append(current_production)
            current_production = []
        if (getting_productions):
            print(line, end="")
            current_production.append(line)

        if (line.startswith("SPLIT")):
            getting_productions = True

    print("\n\n\n")
    print(productions)
