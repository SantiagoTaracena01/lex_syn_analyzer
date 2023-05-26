"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

from utils.parse_yapar import parse_yapar
from utils.lr0_construction import lr0_construction
from utils.lr_parsing_table_construction import lr_parsing_table_construction
# from utils.show_lr0_fa import show_lr0_fa

yapar_grammar = parse_yapar("./out/output.txt")
lr0_automata = lr0_construction(yapar_grammar)
# show_lr0_fa(lr0_automata)
print(lr0_automata)
lr_parsing_table_construction(yapar_grammar, lr0_automata)
