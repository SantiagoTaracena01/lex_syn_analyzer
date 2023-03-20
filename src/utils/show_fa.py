"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para la visualización del NFA.
import os
import graphviz

# Configuración de la ruta de Graphviz.
os.environ["PATH"] += os.pathsep + "C:/Program Files/Graphviz/bin"

# Función para mostrar un NFA con graphviz.
def show_nfa(nfa, view=False):

    # Creación del grafo.
    visual_nfa = graphviz.Digraph(comment="NFA Result")
    visual_nfa.attr(rankdir="LR")

    # Iteración para dibujar los estados.
    for state in nfa.states:

        # Dibujo de los estados del autómata.
        if (state == nfa.initial_state):
            visual_nfa.node(str(state), str(state), shape="circle", style="filled")
        elif (state == nfa.acceptance_state):
            visual_nfa.node(str(state), str(state), shape="doublecircle", style="filled")
        else:
            visual_nfa.node(str(state), str(state), shape="circle")

        # Dibujo de las transiciones del autómata.
        for transition in nfa.mapping[state]:
            for next_state in nfa.mapping[state][transition]:
                visual_nfa.edge(str(state), str(next_state), label=transition)

    # Visualización del NFA.
    visual_nfa.render("./out/nfa-output", format="png", view=view)

# Función para mostrar un DFA con graphviz.
def show_dfa(dfa, type="normal", view=False):

    # Diccionario para el nombre de los archivos de salida.
    output_name = {
        "normal": "dfa-output",
        "min": "min-dfa-output",
        "direct": "direct-dfa-output",
        "min-direct": "min-direct-dfa-output"
    }

    # Creación del grafo.
    visual_dfa = graphviz.Digraph(comment="DFA Result")
    visual_dfa.attr(rankdir="LR")

    # Iteración para dibujar los estados.
    for state in dfa.states:

        # Dibujo de los estados del autómata.
        if (state in dfa.acceptance_states):
            visual_dfa.node(str(state), str(state), shape="doublecircle", style="filled")
        elif (state == dfa.initial_state):
            visual_dfa.node(str(state), str(state), shape="circle", style="filled")
        else:
            visual_dfa.node(str(state), str(state), shape="circle")

        # Dibujo de las transiciones del autómata.
        for transition in dfa.mapping[state]:
            next_state = dfa.mapping[state][transition]
            visual_dfa.edge(str(state), str(next_state), label=transition)

    # Visualización del DFA.
    visual_dfa.render(f"./out/{output_name[type]}", format="png", view=view)
