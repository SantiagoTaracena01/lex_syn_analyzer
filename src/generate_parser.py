"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Librerías importantes para el archivo generate_parser.py.
import sys
from utils.parse_yapar import parse_yapar
from utils.lr0_construction import lr0_construction
from utils.lr_parsing_table_construction import lr_parsing_table_construction

# Archivo a simular por parte del parser.
simulation_file = sys.argv[1] if (len(sys.argv) > 1) else "./out/parse-output.txt"

yapar_grammar = parse_yapar("./out/output.txt")
lr0_automata = lr0_construction(yapar_grammar)
print(lr0_automata)
lr_parsing_table_construction(yapar_grammar, lr0_automata)
