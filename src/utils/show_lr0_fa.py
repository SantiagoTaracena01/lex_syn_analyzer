"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para la visualización del LR(0).
import os
import graphviz

# Configuración de la ruta de Graphviz.
os.environ["PATH"] += os.pathsep + "C:/Program Files/Graphviz/bin"

# Función para mostrar un LR(0) con graphviz.
def show_lr0_fa(lr0, view=False):

    # Creación del grafo.
    visual_nfa = graphviz.Digraph(comment="LR(0) Result")
    visual_nfa.attr(rankdir="LR")

    # Iteración para dibujar los estados.
    for state in lr0.states:

        visual_nfa.node(str(state.name), str(state.name), shape="rectangle")

        # Dibujo de las transiciones del autómata.
        for transition in state.transitions:
            # for next_state in state.transitions[transition]:
            visual_nfa.edge(str(state.name), str(state.transitions[transition].name), label=transition)

    # Visualización del LR(0).
    visual_nfa.render("./out/lr0-output", format="png", view=view)
