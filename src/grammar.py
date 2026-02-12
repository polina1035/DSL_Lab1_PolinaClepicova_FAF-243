import random


class Grammar:
    def __init__(self, Vn, Vt, P, S):
        """
        Initializes the Grammar with non-terminals, terminals, rules, and start symbol.
        Vn: set of non-terminals
        Vt: set of terminals
        P: dictionary of production rules
        S: start symbol
        """
        self.Vn = Vn
        self.Vt = Vt
        self.P = P
        self.S = S

    def generate_string(self):
        """
        Generates a valid string from the grammar using random production rules.
        """
        current_symbol = self.S

        # We loop until there are no non-terminals left in the string
        # Added a safety limit of 20 iterations to prevent infinite loops (like in state L)
        iterations = 0
        while any(s in self.Vn for s in current_symbol) and iterations < 20:
            new_string = ""
            for char in current_symbol:
                if char in self.Vn:
                    # Pick a random rule for the current non-terminal
                    rule = random.choice(self.P[char])
                    new_string += rule
                else:
                    new_string += char
            current_symbol = new_string
            iterations += 1
        return current_symbol

    def to_finite_automaton(self):
        """
        Converts the Regular Grammar (Type 3) to a Finite Automaton.
        Uses local import to avoid circular dependency.
        """
        from finite_automaton import FiniteAutomaton

        # Each non-terminal becomes a state
        states = self.Vn.copy()
        final_state = 'X'  # Special state for terminal productions (A -> a)
        states.add(final_state)

        transitions = {}
        for non_terminal, rules in self.P.items():
            for rule in rules:
                symbol = rule[0]  # The terminal character

                # If rule is A -> aB (len=2), next state is B
                # If rule is A -> a (len=1), next state is the final state X
                next_state = rule[1] if len(rule) > 1 else final_state

                key = (non_terminal, symbol)
                if key not in transitions:
                    transitions[key] = []
                transitions[key].append(next_state)

        return FiniteAutomaton(states, self.Vt, transitions, self.S, {final_state})