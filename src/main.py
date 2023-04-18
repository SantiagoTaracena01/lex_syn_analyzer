"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para el archivo main.py.
import sys
from utils.regex_infix_to_postfix import regex_infix_to_postfix
from utils.direct_construction import direct_construction, build_expression_tree
from utils.show_fa import show_dfa
from utils.show_tree import show_expression_tree
from utils.parse_yalex import parse_yalex
from timeit import default_timer

# Inicio del cronómetro.
start = default_timer()

# Path del archivo .yal a convertir.
path = sys.argv[1] if (len(sys.argv) > 1) else "./yalex/slr-1.yal"

# Construcción del árbol de la expresión regular del archivo .yal.
yalex_regex = parse_yalex(path)
print(yalex_regex)
postfix_yalex_regex = regex_infix_to_postfix(yalex_regex)
yalex_expression_root, _ = build_expression_tree(postfix_yalex_regex)
show_expression_tree(yalex_expression_root)

# Fin del cronómetro.
print(f"\nYalex regex and tree from file \"{path}\" took {round(default_timer() - start, 4)} seconds.\n")

# # Ingreso de la cadena de entrada.
# w_string = input("Please input a string to match in the Yalex file: ")

# # Inicio del cronómetro.
# start = default_timer()

# # Obtención de la expresión postfix de la expresión regular.
# postfix = regex_infix_to_postfix(yalex_regex)
# print(f"\nPostfix: {postfix}")
# print(f"Regex to postfix took {round(default_timer() - start, 4)} seconds.")
# start = default_timer()

# # Construcción del DFA del archivo.
# direct_dfa = direct_construction(postfix)
# show_dfa(direct_dfa, type="direct", view=False)
# print(f"\nDirect-DFA: Does string \"{w_string}\" belongs to the language of \"{yalex_regex}\"? {direct_dfa.simulate(w_string)}")
# print(f"Direct DFA construction took {round(default_timer() - start, 4)} seconds.")
# start = default_timer()
