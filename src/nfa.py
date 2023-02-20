class NFA(object):

    def __init__(self, states, alphabet, initial_state, acceptance_state, mapping):
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.acceptance_state = acceptance_state
        self.mapping = mapping

    def __repr__(self):
        return f"""
            NFA(
                states={self.states},
                alphabet={self.alphabet},
                initial_state={self.initial_state},
                acceptance_state={self.acceptance_state},
                mapping={self.mapping}
            )
        """
