"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para la construcción del NFA.
from utils.postfix import regex_infix_to_postfix
from utils.thompson import thompson_construction
from utils.subsets import subset_construction
from utils.minimization import dfa_minimization
from utils.show_fa import show_nfa, show_dfa

# Transformación de la expresión regular a postfix y construcción del NFA.
regex = input("\nPlease, input a regex: ")
# w_string = input("Now please input a string: ")
postfix = regex_infix_to_postfix(regex)
nfa = thompson_construction(postfix)
dfa = subset_construction(nfa)
show_nfa(nfa, view=False)
# print(nfa)
show_dfa(dfa, view=False)
# print(dfa)
minimized_dfa = dfa_minimization(dfa)
print()
# print(nfa.simulate(w_string))
# print(dfa.simulate(w_string))
