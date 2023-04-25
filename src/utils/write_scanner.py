"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Función para escribir el archivo scanner.py.
def write_scanner(filename, regex, yalex_code):

    # Líneas de código fijas del archivo.
    lines = [
        "import sys",
        "from utils.direct_construction import direct_construction",
        "from utils.simulate_yalex_file import simulate_yalex_file",
        "",
        "dfa = direct_construction(",
        f"    {regex},",
        f"    {yalex_code}",
        ")",
        "",
        "test_file = sys.argv[1] if (len(sys.argv) > 1) else \"./tests/slr-1-test.txt\"",
        "",
        "def return_token(found_token):",
    ]

    # Listas con el código y los tokens del archivo yalex.
    code_to_write = [entry[0] for entry in yalex_code]
    tokens_to_return = [entry[1] for entry in yalex_code]

    # Separador entre la función y la definición de los tokens.
    lines.append("")

    # Definición de los tokens.
    for token in tokens_to_return:
        lines.append(f"    {token} = \"{token}\"")

    # Separador entre los tokens y el código a retornar.
    lines.append("")

    # Escritura del código a retornar.
    for yalex_code, token in zip(code_to_write, tokens_to_return):
        lines.append(f"    if (found_token == {token}):")
        lines.append(f"        {yalex_code}")

    # Llamada final a la simulación del archivo.
    lines.append("")
    lines.append("simulate_yalex_file(test_file, dfa, return_token)")

    # Escritura del archivo scanner.py.
    with open(filename, "w+") as file:
        for line in lines:
            file.write(line + "\n")
