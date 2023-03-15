from utils.classes.dfa import DFA
from utils.classes.stack import Stack
from utils.classes.queue import Queue

def dfa_minimization(dfa):
    partitions = [
        [state for state in dfa.states if state not in dfa.acceptance_states],
        [state for state in dfa.acceptance_states]
    ]
    temporal_partitions = []
    while (partitions != temporal_partitions):
        print()
        break
    print("Partitions", partitions)
