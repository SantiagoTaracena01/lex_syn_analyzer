"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para la construcción del NFA.
# from utils.check_lexical_errors import check_lexical_errors
# from utils.regex_infix_to_postfix import regex_infix_to_postfix
# from utils.thompson_construction import thompson_construction
# from utils.subset_construction import subset_construction
# from utils.dfa_minimization import dfa_minimization
# from utils.direct_construction import direct_construction, build_expression_tree
# from utils.show_fa import show_nfa, show_dfa
# from utils.show_tree import show_expression_tree
# from utils.parse_yalex import parse_yalex
# from timeit import default_timer

# Módulos necesarios para la construcción del árbol del archivo .yal.
from utils.parse_yalex import parse_yalex
from utils.regex_infix_to_postfix import regex_infix_to_postfix
from utils.direct_construction import build_expression_tree
from utils.show_tree import show_expression_tree
from timeit import default_timer

# Inicio del cronómetro.
start = default_timer()

path = "./yalex/slr-4.yal"

# Construcción del árbol de la expresión regular del archivo .yal.
yalex_regex = parse_yalex(path)
# print("\nYalex regex", yalex_regex)
postfix_yalex_regex = regex_infix_to_postfix(yalex_regex)
yalex_expression_root, _ = build_expression_tree(postfix_yalex_regex)
show_expression_tree(yalex_expression_root)

# Fin del cronómetro.
print(f"\nYalex regex and tree from file \"{path}\" took {round(default_timer() - start, 4)} seconds.\n")

# # Ejemplo de la construcción del árbol.
# initial_regex = ["(", "97", "|", "98", ")", "*", "97", "98", "98"]
# postfix = regex_infix_to_postfix(initial_regex)
# print("Expresión postfix", postfix)
# expression_root, _ = build_expression_tree(postfix)
# show_expression_tree(expression_root)

# # Ingreso de la expresión regular y la cadena de entrada.
# regex = input("\nPlease, input a regex: ")

# # Verificación de errores léxicos.
# check_lexical_errors(regex)

# # Ingreso de la cadena de entrada.
# w_string = input("Now please input a string: ")

# # Inicio del cronómetro.
# start = default_timer()

# # Obtención de la expresión postfix de la expresión regular.
# postfix = regex_infix_to_postfix(regex)
# print(f"\nPostfix: {postfix}")
# print(f"Regex to postfix took {round(default_timer() - start, 4)} seconds.")
# start = default_timer()

# # Construcción de Thompson y obtención del NFA.
# nfa = thompson_construction(postfix)
# show_nfa(nfa, view=False)
# print(f"\nNFA: Does string \"{w_string}\" belongs to the language of \"{regex}\"? {nfa.simulate(w_string)}")
# print(f"NFA construction took {round(default_timer() - start, 4)} seconds.")
# start = default_timer()

# # Construcción de Subconjuntos y obtención del DFA.
# dfa = subset_construction(nfa)
# show_dfa(dfa, view=False)
# print(f"\nDFA: Does string \"{w_string}\" belongs to the language of \"{regex}\"? {dfa.simulate(w_string)}")
# print(f"DFA construction took {round(default_timer() - start, 4)} seconds.")
# start = default_timer()
# # Construcción directa del DFA de la expresión regular.

# direct_dfa = direct_construction(postfix)
# show_dfa(direct_dfa, type="direct", view=False)
# print(f"\nDirect-DFA: Does string \"{w_string}\" belongs to the language of \"{regex}\"? {direct_dfa.simulate(w_string)}")
# print(f"Direct DFA construction took {round(default_timer() - start, 4)} seconds.")
# start = default_timer()

# # Minimización del DFA por particiones y obtención del DFA mínimo.
# minimized_dfa = dfa_minimization(dfa)
# show_dfa(minimized_dfa, type="min", view=False)
# print(f"\nMin-DFA: Does string \"{w_string}\" belongs to the language of \"{regex}\"? {minimized_dfa.simulate(w_string)}")
# print(f"DFA minimization took {round(default_timer() - start, 4)} seconds.")
# start = default_timer()

# # Minimización del DFA directo y obtención del DFA mínimo.
# minimized_direct_dfa = dfa_minimization(direct_dfa)
# show_dfa(minimized_direct_dfa, type="min-direct", view=False)
# print(f"\nMin-Direct-DFA: Does string \"{w_string}\" belongs to the language of \"{regex}\"? {minimized_direct_dfa.simulate(w_string)}")
# print(f"Direct DFA minimization took {round(default_timer() - start, 4)} seconds.")
