class FiniteAutomaton:
    def __init__(self, Q, sigma, delta, q0, F):
        """
        Q: set of states
        sigma: alphabet
        delta: transition function (dict with key (state, char))
        q0: initial state
        F: set of final states
        """
        self.Q = Q
        self.sigma = sigma
        self.delta = delta
        self.q0 = q0
        self.F = F

    def string_belong_to_language(self, input_string):
        """
        Checks if the input string is accepted by the Finite Automaton by following transitions.
        """
        current_states = {self.q0}

        for char in input_string:
            next_states = set()
            for state in current_states:
                # If a transition exists for current state and symbol, move to next states
                if (state, char) in self.delta:
                    for next_s in self.delta[(state, char)]:
                        next_states.add(next_s)
            current_states = next_states

        # If any of the final positions is a terminal state, accept the string
        return any(state in self.F for state in current_states)