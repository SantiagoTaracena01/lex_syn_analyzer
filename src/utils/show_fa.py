import os
import graphviz

os.environ["PATH"] += os.pathsep + "C:/Program Files/Graphviz/bin"

def show_nfa(nfa):

    visual_nfa = graphviz.Digraph(comment="NFA Result")

    for state in nfa.states:

        if state == nfa.initial_state:
            visual_nfa.node(str(state), str(state), shape="circle", style="filled")
        elif state == nfa.acceptance_state:
            visual_nfa.node(str(state), str(state), shape="doublecircle", style="filled")
        else:
            visual_nfa.node(str(state), str(state), shape="circle")

        for transition in nfa.mapping[state]:
            for next_state in nfa.mapping[state][transition]:
                visual_nfa.edge(str(state), str(next_state), label=transition)

    visual_nfa.render("./out/output", format="png", view=True)
