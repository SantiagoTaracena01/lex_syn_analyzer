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
from utils.simulate_lr0 import simulate_lr0

# Archivo a simular por parte del parser.
yapar_file = sys.argv[1] if (len(sys.argv) > 1) else "./out/parser-output.txt"
simulation_file = sys.argv[2] if (len(sys.argv) > 2) else "./out/parse-output.txt"

# Obtención de la gramática del yapar y del autómata LR(0).
yapar_grammar = parse_yapar(yapar_file)
lr0_automata = lr0_construction(yapar_grammar)

# Impresión de la tabla de parseo y la tabla de la simulación del archivo dado.
parsing_table = lr_parsing_table_construction(yapar_grammar, lr0_automata)
lexical_output, syntactic_output = simulate_lr0(yapar_grammar, parsing_table, lr0_automata, simulation_file)

# Resultados generales del análisis léxico y sintáctico.
print(f"¿La cadena dentro de {simulation_file} es aceptada por las expresiones regulares? {lexical_output}")
print(f"¿La cadena dentro de {simulation_file} es aceptada por la gramática? {syntactic_output}\n")
