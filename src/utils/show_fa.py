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
def show_nfa(nfa):

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
    visual_nfa.render("./out/output", format="png", view=True)
