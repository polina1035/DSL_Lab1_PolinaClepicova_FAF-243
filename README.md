# Laboratory Work No. 1: Intro to Formal Languages. Regular Grammars. Finite Automata.

### Course: Formal Languages & Finite Automata

### Author: Polina Clepicova FAF-243

---

## Theory

A formal language is essentially a medium used to convey information through a specific format. It consists of an **alphabet**, which is a finite, non-empty set of symbols. From this alphabet, we can form **strings** (or words), which are finite sequences of symbols. The set of all possible strings over an alphabet $\Sigma$ is denoted as $\Sigma^*$.

To define which strings are valid in a specific language, we use a **Grammar** (), defined as an ordered quadruple $G = (V_N, V_T, P, S)$:


$V_N$ : A finite set of non-terminal symbols.


$V_T$: A finite set of terminal symbols.


$P$: A finite set of production rules.


$S$: The start symbol.



According to the **Chomsky Classification**, the grammar in this laboratory work (Variant 7) is a **Type 3: Regular Grammar**. This is the most restricted type, where rules typically follow the format $A \rightarrow aB$ or $A \rightarrow a$, where $a \in V_T$ and $B \in V_N$ .

---

## Objectives:

* Understand the basic components of a formal language: alphabet, vocabulary, and grammar.
* Implement a `Grammar` class to represent the mathematical quadruple $(V_N, V_T, P, S)$.
* Develop a function to generate 5 valid strings from the language defined by the grammar.
* Implement a `FiniteAutomaton` class and a method to convert the `Grammar` into a `FiniteAutomaton`.
* Implement a string verification method in the Finite Automaton to check if an input string belongs to the language.

---

## Implementation Description

* **Grammar Class**: This class stores the sets of non-terminals, terminals, and production rules. The `generate_string` method uses a `while` loop to repeatedly replace non-terminal symbols with their corresponding production options chosen randomly until no non-terminals remain.
* **Conversion Logic**: The `to_finite_automaton` method maps each non-terminal symbol to a state in the Finite Automaton (FA). Since regular grammars have rules like $A \rightarrow aB$, these are directly converted into transitions $\delta(A, a) = B$. For rules ending in a terminal like $L \rightarrow c$, a special "Final" state is created.
* **Finite Automaton Class**: This class manages the state transitions. The `string_belong_to_language` method iterates through the characters of an input string, updating the "current state" based on the transition function . If the final character leads to a designated "Final State," the string is accepted.

### Code Snippets

**Grammar to FA Conversion:**

```python
def to_finite_automaton(self):
    states = self.Vn.copy()
    final_state = 'FINAL' 
    states.add(final_state)
    
    transitions = {}
    for non_terminal, rules in self.P.items():
        for rule in rules:
            symbol = rule[0] # The terminal
            # If rule is A -> aB, next state is B. If A -> a, next state is FINAL.
            next_state = rule[1] if len(rule) > 1 else final_state
            
            if (non_terminal, symbol) not in transitions:
                transitions[(non_terminal, symbol)] = []
            transitions[(non_terminal, symbol)].append(next_state)
    
    return FiniteAutomaton(states, self.Vt, transitions, self.S, {final_state})

```

**FA String Verification:**

```python
def string_belong_to_language(self, input_string):
    current_states = {self.q0}
    for char in input_string:
        next_states = set()
        for state in current_states:
            if (state, char) in self.delta:
                next_states.update(self.delta[(state, char)])
        current_states = next_states
    return any(state in self.F for state in current_states)

```

---

## Conclusions / Results

Through this implementation, I successfully modeled the generation and recognition of a formal language. The conversion from a Regular Grammar to a Finite Automaton is seamless because their structures are mathematically equivalent.

**Generated Samples (Variant 7):**

1. `abdc`
2. `abcdbdc`
3. `abdcabc`
4. `abcdbdabdc`
5. `abdcac`

**Test Results:**

* String `abdc`: **Accepted** (Follows $S \rightarrow D \rightarrow E \rightarrow L \rightarrow \text{Final}$) )
* String `abcc`: **Rejected** (No rule allows $L \rightarrow c$ followed by another $c$)

---

## References

1. Chapter 1: Words and Languages*, provided course materials.
2. Chomsky, N. (1956). *Three models for the description of language*.
3. Vasile Drumea & Irina Cojuhari, *Formal Languages & Finite Automata Lab Guide*.
