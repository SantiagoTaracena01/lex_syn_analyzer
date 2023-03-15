"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para la minimización del DFA.
from utils.classes.dfa import DFA
from utils.classes.stack import Stack
from utils.classes.queue import Queue

# Función que minimiza un DFA.
def dfa_minimization(dfa):

    states = dfa.states
    alphabet = dfa.alphabet
    initial_state = [dfa.initial_state]
    acceptance_states = dfa.acceptance_states
    mapping = dfa.mapping

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

        for entry in mapping:
            partition_table[entry] = {}
            for index, actual_partition in enumerate(partitions):
                for char in alphabet:
                    result = mapping[entry][char]
                    if (result in actual_partition):
                        partition_table[entry][char] = index

        splitted_tables = []

        for partition in partitions:
            splitted_partition_table = {}
            for entry in partition_table:
                if entry in partition:
                    splitted_partition_table[entry] = partition_table[entry]
            splitted_tables.append(splitted_partition_table)

        partition_types = []

        for index, table in enumerate(splitted_tables):
            for entry in table:
                values = [str(value) for value in list(table[entry].values())]
                partition_type = f"{index}{str().join(values)}"
                partition_types.append(partition_type)

        partition_types = set(partition_types)

        new_partitions = [[] for _ in partition_types]

        for index, partition_type in enumerate(partition_types):
            for jndex, table in enumerate(splitted_tables):
                for entry in table:
                    values = [str(value) for value in list(table[entry].values())]
                    if (f"{jndex}{str().join(values)}" == partition_type):
                        new_partitions[index].append(entry)

        print("Comparing", partitions, new_partitions)

        last_partitions = sorted(partitions)
        partitions = sorted(new_partitions)

    print("Partitions", partitions)
