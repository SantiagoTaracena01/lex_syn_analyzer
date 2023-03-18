"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para la minimización del DFA.
from utils.classes.dfa import DFA

# Función que minimiza un DFA.
def dfa_minimization(dfa):

    initial_state = [dfa.initial_state]
    min_acceptance_states = dfa.acceptance_states

    # Particiones iniciales (estados que son de aceptación y estados que no lo son).
    partitions = [
        [state for state in dfa.states if state not in dfa.acceptance_states],
        [state for state in dfa.acceptance_states]
    ]

    # Partición temporal para comparar el proceso.
    last_partitions = []

    # Ciclo que se ejecuta hasta que las particiones no cambien.
    while (partitions != last_partitions):

        # Tabla de particiones.
        partition_table = {}

        # Iteración sobre las entradas del mapping.
        for entry in dfa.mapping:

            # Cada entrada del mapping debe tener una entrada en la tabla de particiones.
            partition_table[entry] = {}

            # Iteración sobre cada partición actual y cada caracter del alfabeto.
            for index, actual_partition in enumerate(partitions):
                for char in dfa.alphabet:

                    # Cálculo del resultado de la función de transición con una entrada y caracter.
                    entry_mapping = dfa.mapping.get(entry, {})
                    result = entry_mapping.get(char, 0)

                    # Si el resultado está en la partición actual, se agrega a la tabla de particiones.
                    if (result in actual_partition):

                        # El valor de la fila en la tabla de particiones es el índice de la partición actual.
                        partition_table[entry][char] = index

        # Instancia de una lista para las tablas según particiones.
        splitted_tables = []

        # Iteración sobre cada partición actual.
        for partition in partitions:

            # Cada partición tiene su propia tabla.
            splitted_partition_table = {}

            # Iteración sobre cada entrada en la tabla de particiones.
            for entry in partition_table:

                # Si la entrada está en la partición actual, se agrega a la tabla de particiones respectiva.
                if (entry in partition):

                    # Agregación de la entrada a la tabla de particiones respectiva.
                    splitted_partition_table[entry] = partition_table[entry]

            # La tabla terminada se agrega a la lista de tablas.
            splitted_tables.append(splitted_partition_table)

        # Lista de tipos de particiones para su posterior separación.
        partition_types = []

        # Iteración sobre cada tabla de particiones y entrada de la tabla.
        for index, table in enumerate(splitted_tables):
            for entry in table:

                # Creación del tipo de partición con la sintáxis <índice><valores de la fila>.
                values = [str(value) for value in list(table[entry].values())]
                partition_type = f"{index}{str().join(values)}"
                partition_types.append(partition_type)

        # Eliminación de valores repetidos en los tipos de particiones..
        partition_types = set(partition_types)

        # Lista de nuevas particiones, conformada por una lista vacía por cada tipo de partición.
        new_partitions = [[] for _ in partition_types]

        # Iteración sobre cada tipo de partición, tabla de particiones y entrada de la tabla.
        for index, partition_type in enumerate(partition_types):
            for jndex, table in enumerate(splitted_tables):
                for entry in table:

                    # Nuevo cálculo del tipo de partición de la entrada.
                    values = [str(value) for value in list(table[entry].values())]

                    # Si el tipo de partición de la entrada es igual al tipo de partición actual, se agrega a su respectiva partición.
                    if (f"{jndex}{str().join(values)}" == partition_type):
                        new_partitions[index].append(entry)

        # Actualización de las particiones.
        last_partitions = sorted(partitions)
        partitions = sorted(new_partitions)

    # Estados y estado inicial del DFA minimizado.
    states = [index for index in range(len(partitions))]
    initial_state = [index for index, partition in enumerate(partitions) if (dfa.initial_state in partition)][0]

    # Instancia de los estados de aceptación del DFA minimizado.
    min_acceptance_states = []

    # Obtención de los estados de aceptación del DFA minimizado.
    for index, partition in enumerate(partitions):
        for state in partition:
            if (state in dfa.acceptance_states):
                min_acceptance_states.append(index)

    # Instancia del mapping del DFA minimizado.
    mapping = {}

    # Obtención del mapping del DFA minimizado.
    for state in states:
        for entry in dfa.mapping:
            if (state == entry):
                new_mapping_entry = {}
                for char in dfa.alphabet:
                    for other_state in states:
                        entry_mapping = dfa.mapping.get(entry, {})
                        result = entry_mapping.get(char, 0)
                        if (result == other_state):
                            new_mapping_entry[char] = other_state
                mapping[state] = new_mapping_entry

    # Finalización de la construcción del mapping.
    for entry in mapping:
        for char in dfa.alphabet:
            if (char not in mapping[entry]):
                mapping[entry][char] = entry

    # Arreglo de DFAs con un estado sin transiciones.
    if (len(mapping) < 2):
        for entry in mapping:
            if (mapping[entry] == {}):
                mapping[entry] = { char: entry for char in dfa.alphabet }

    # Retorno del DFA minimizado.
    return DFA(
        states=set(states),
        alphabet=dfa.alphabet,
        initial_state=initial_state,
        acceptance_states=set(min_acceptance_states),
        mapping=mapping,
    )
