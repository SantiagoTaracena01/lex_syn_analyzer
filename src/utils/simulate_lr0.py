"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Módulos importantes para la simulación del LR(0).
from prettytable import PrettyTable

# Función que simula un autómata LR(0) con un archivo de prueba dado.
def simulate_lr0(grammar, parsing_table, lr0, test_path):

    # Separación entre la tabla de parseo y la tabla de simulación.
    print()

    # Instancia inicial del string a simular (que realmente es un array).
    string_to_simulate = ""

    # Apertura del archivo a simular (escaneado).
    with open(test_path, "r") as file:

        # Archivo en formato string.
        stringified_file = ""

        # Proceso de llenar el string a separar con las líneas del archivo.
        for line in file:
            stringified_file += line

        # Separación y limpieza del archivo para obtener la lista de tokens a simular.
        splitted_file = stringified_file.split(" ")
        string_to_simulate = splitted_file[:-1] if (splitted_file[-1] == "") else splitted_file

        # Agregación final del símbolo de aceptación.
        string_to_simulate.append("$")

    # Resultado del análisis léxico de la oración.
    is_string_lexically_correct = not "ERROR" in string_to_simulate

    # Si la oración no es correcta léxicamente, se rechaza la cadena por razones léxicas.
    if (not is_string_lexically_correct):
        return False, False

    # Tabla que indica los pasos de la simulación.
    graphic_table = PrettyTable()
    graphic_table.field_names = ["Line", "Stack", "Symbols", "Input", "Action"]

    # Instancia inicial de los datos de la simulación.
    iteration = 1
    state_stack = [lr0.states[0]]
    symbols = ["$"]
    simulation_input = string_to_simulate.copy()
    action = ""

    # Ciclo que realiza la simulación.
    while (True):

        # Copia de los estados, símbolos e input para la tabla.
        last_state_stack = state_stack.copy()
        last_symbols = symbols.copy()
        last_simulation_input = simulation_input.copy()

        # Acción textual a meter a la tabla gráfica.
        textual_action = ""

        # Estado a utilizar para la obtención de la acción siguiente.
        current_state = state_stack[-1]

        # Símbolo a utilizar para la obtención de la acción siguiente.
        symbol = simulation_input[0]
        symbol_index = parsing_table["STATE"].index(symbol)

        # Acción siguiente a tomar en cuenta para la simulación.
        action = parsing_table[current_state.name][symbol_index]

        # Si la acción empieza con s, es un shift.
        if (action.startswith("s")):

            # Obtención del estado a agregar en el stack de estados.
            state_name_to_add = f"I{action[1:]}"
            filtered_state_to_add = list(filter(lambda state: state.name == state_name_to_add, lr0.states))
            state_to_add = filtered_state_to_add[0]

            # Agregación del nuevo estado al stack.
            state_stack.append(state_to_add)

            # Agregación del símbolo obtenido del shift al stack de símbolos.
            symbol_to_add = simulation_input.pop(0)
            symbols.append(symbol_to_add)

            # Acción textual del shift.
            textual_action = f"Shift to {state_name_to_add}"

        # Si la acción empieza con r, es un reduce.
        if (action.startswith("r")):

            # Producción a utilizar para la reducción.
            production_index = int(action[1:])
            production = grammar.productions[production_index]

            # Cantidad de estados a sacar del stack de estados.
            states_to_pop = len(production.listed_rules)

            # Lista de símbolos a reemplazar.
            symbols_to_reduce = []

            # Ciclo para eliminar los estados necesarios del stack.
            for _ in range(states_to_pop):
                state_stack.pop(-1)
                symbols_to_reduce.append(symbols.pop(-1))

            # Intercambio de símbolos si se sacaron los símbolos correctos.
            if (sorted(symbols_to_reduce) == sorted(production.listed_rules)):
                symbols.append(production.name)

            # Índice de la transición a ejecutar y obtención del estado. 
            transition_index = parsing_table["STATE"].index(production.name)
            new_state_to_push_number = parsing_table[state_stack[-1].name][transition_index]

            # Filtración del estado y agregación al stack de estados.
            filtered_state_to_add = list(filter(lambda state: state.name == f"I{new_state_to_push_number}", lr0.states))
            state_to_add = filtered_state_to_add[0]
            state_stack.append(state_to_add)

            # Acción textual del reduce.
            textual_action = f"Reduce by {production}"

        # Acción de aceptación de la cadena.
        if (action == "ACCEPT"):

            # Aceptación de la cadena.
            textual_action = "Accept"

        # Si no hay acción, la simulación finaliza.
        if (not action):

            # Error en la simulación.
            textual_action = f"ERROR: No action with {current_state.name} and {symbol}"

        # Nueva fila para la tabla de simulación.
        graphic_table.add_row([
            iteration,
            [state.name for state in last_state_stack],
            last_symbols,
            last_simulation_input,
            textual_action
        ])

        # Aumento de la iteración y reinicio del ciclo.
        iteration += 1

        # Si la acción es ACCEPT, la cadena es aceptada.
        if (action == "ACCEPT"):

            # Escritura de la tabla constuida en .txt.
            with open("./out/simulation-table.txt", "w+") as file:
                file.write(str(graphic_table) + "\n")

            # Impresión de la tabla de la simulación.
            print(graphic_table, "\n")

            # Aceptación de la cadena.
            return True, True

        # Si la acción es ERROR, la cadena es rechazada.
        if (textual_action.startswith("ERROR")):

            # Escritura de la tabla constuida en .txt.
            with open("./out/simulation-table.txt", "w+") as file:
                file.write(str(graphic_table) + "\n")

            # Impresión de la tabla de la simulación.
            print(graphic_table, "\n")

            # Rechazo de la cadena por razones sintácticas.
            return True, False
