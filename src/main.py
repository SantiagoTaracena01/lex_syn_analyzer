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
from utils.direct_construction import direct_construction
from utils.show_fa import show_nfa, show_dfa
from timeit import default_timer

# Ingreso de la expresión regular y la cadena de entrada.
regex = input("\nPlease, input a regex: ")
w_string = input("Now please input a string: ")

# Inicio del cronómetro.
start = default_timer()

# Construcción de Thompson y obtención del NFA.
postfix = regex_infix_to_postfix(regex)
nfa = thompson_construction(postfix)
show_nfa(nfa, view=False)
print(f"\nNFA: ¿La cadena {w_string} pertenece a la expresión regular {regex}? {nfa.simulate(w_string)}")

# Construcción de Subconjuntos y obtención del DFA.
dfa = subset_construction(nfa)
show_dfa(dfa, view=False)
print(f"\nDFA: ¿La cadena {w_string} pertenece a la expresión regular {regex}? {dfa.simulate(w_string)}")

# Minimización del DFA por particiones y obtención del DFA mínimo.
minimized_dfa = dfa_minimization(dfa)
show_dfa(minimized_dfa, type="min", view=False)
print(f"\nMin-DFA: ¿La cadena {w_string} pertenece a la expresión regular {regex}? {minimized_dfa.simulate(w_string)}")

# Construcción directa del DFA de la expresión regular.
direct_dfa = direct_construction(postfix)
show_dfa(direct_dfa, type="direct", view=False)
print(f"\nDirect-DFA: ¿La cadena {w_string} pertenece a la expresión regular {regex}? {direct_dfa.simulate(w_string)}")

# Fin del cronómetro.
print(f"\nProceso terminado en {default_timer() - start} segundos.\n")
