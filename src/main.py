"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para el archivo main.py.
import sys
from utils.regex_infix_to_postfix import regex_infix_to_postfix
from utils.direct_construction import direct_construction
from utils.show_fa import show_dfa
from utils.parse_yalex import parse_yalex
from utils.write_scanner import write_scanner
from utils.simulate_yalex_file import simulate_yalex_file
from timeit import default_timer

# Inicio del cronómetro.
start = default_timer()

# Path del archivo .yal a convertir.
path = sys.argv[1] if (len(sys.argv) > 1) else "./yalex/slr-1.yal"

# Obtención de la expresión regular y los tokens del archivo .yal.
yalex_regex, yalex_parser_code = parse_yalex(path)
# print(yalex_regex)
# print(yalex_parser_code)

# Conversión de la expresión regular del archivo a postfix.
postfix_yalex_regex = regex_infix_to_postfix(yalex_regex)

# Construcción del DFA del archivo.
dfa = direct_construction(postfix_yalex_regex, yalex_parser_code)
show_dfa(dfa, type="direct", view=False)
# print(f"Direct DFA construction took {round(default_timer() - start, 4)} seconds.")

write_scanner("scanner.py", postfix_yalex_regex, yalex_parser_code)
