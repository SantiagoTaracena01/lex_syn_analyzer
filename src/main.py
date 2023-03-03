"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para la construcción del NFA.
from utils.postfix import regex_infix_to_postfix
from utils.thompson import thompson_construction
from utils.subsets import subset_construction
from utils.show_fa import show_nfa

# Transformación de la expresión regular a postfix y construcción del NFA.
regex = input("Please, input a regex: ")
postfix = regex_infix_to_postfix(regex)
nfa = thompson_construction(postfix)
subset_construction(nfa)
show_nfa(nfa)
print(nfa)
