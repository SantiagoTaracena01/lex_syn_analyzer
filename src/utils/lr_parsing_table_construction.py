"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Módulos importantes para la construcción de la tabla.
from prettytable import PrettyTable
from utils.follow import follow

# Función que genera la tabla de construcción para la simulación de un autómata LR(0).
def lr_parsing_table_construction(grammar, lr0_automata):

    # Instancia inicial de la tabla de construcción.
    table = {}
    graphic_table = PrettyTable()

    # Símbolos (columnas) y estados (filas) de la tabla de construcción.
    symbols = [symbol for symbol in grammar.terminals + ["$"] + grammar.non_terminals if (not symbol.endswith("'"))]
    states = [state for state in lr0_automata.states if (state.name != "ACCEPT")]

    # Limpieza de los puntos para armar la tabla de construcción.
    grammar.productions[0].listed_rules.remove(".")

    # Limpieza del dólar para el cálculo de follow.
    for production in grammar.productions:
        production.listed_rules.remove("$")

    # Producciones comparables en formato string.
    comparable_grammar_productions = [f"{production.name} -> {' '.join(production.listed_rules)}" for production in grammar.productions]

    # Columnas de la tabla de construcción.
    table["STATE"] = symbols.copy()

    # Campos de la tabla a imprimir.
    graphic_table.field_names = ["STATE"] + symbols.copy()

    # Iteración entre los estados del autómata (filas).
    for state in states:

        # Instancia inicial de la fila perteneciente al estado.
        table[state.name] = ["" for _ in range(len(table["STATE"]))]

        # Iteración entre los símbolos para colocar los valores de las 
        for symbol in symbols:

            # Si el símbolo está en las transiciones del estado se coloca en la tabla.
            if (symbol in state.transitions):

                # Transición con terminales o no terminales.
                symbol_index = table["STATE"].index(symbol)
                transition_name = state.transitions[symbol].name

                # Nombre de la entrada de la tabla.
                if (transition_name == "ACCEPT"):
                    table[state.name][symbol_index] = "ACCEPT"
                else:
                    table[state.name][symbol_index] = f"s{transition_name[1:]}" if (symbol in grammar.terminals) else transition_name[1:]

            # Iteración entre producciones para encontrar una con el punto al final.
            for production in state.productions:

                # Producciones con el punto como último elemento antes del $.
                if ((len(production.listed_rules) > 1) and (production.listed_rules[-2] == ".")):

                    # Cálculo del follow del nombre de la producción con el punto al final.
                    follow_result = follow(grammar, production.name)

                    # Si el símbolo está en el resultado del follow, se hace reduce con el índice de la producción.
                    if (symbol in follow_result):

                        # Copia de la producción y limpieza de símbolos innecesarios.
                        production_copy = production.listed_rules.copy()
                        production_copy.remove(".")
                        production_copy.remove("$")

                        # Producción en forma de string para comparar.
                        comparable_production = f"{production.name} -> {' '.join(production_copy)}"

                        # Índice de la producción para asignar al reduce.
                        production_index = comparable_grammar_productions.index(comparable_production)

                        # Índice del símbolo actual, que es la columna del reduce.
                        symbol_index = table["STATE"].index(symbol)

                        # Entrada de la tabla encontrada.
                        table[state.name][symbol_index] = f"r{production_index}"

    # Construcción de la tabla gráfica.
    for entry in table:
        if (entry == "STATE"):
            continue
        graphic_table.add_row([entry] + table[entry])

    # Impresión de la tabla gráfica construida.
    print("\n", graphic_table)

    # Escritura de la tabla constuida en .txt.
    with open("./out/parsing-table.txt", "w+") as file:
        file.write(str(graphic_table) + "\n")

    # Retorno de la tabla construida.
    return table
