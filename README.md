# Laboratory Work No. 1: Intro to Formal Languages. Regular Grammars. Finite Automata.

### Course: Formal Languages & Finite Automata

### Author: Polina Clepicova FAF-243

### Variant 7

---
## Theory

A formal language is a fundamental concept in computer science, acting as a structured medium used to convey information through a specific, mathematically defined format. In the most general sense, a language consists of an **alphabet** ($\Sigma$), which is a finite, non-empty set of symbols. From this alphabet, we can form **strings** (or words), which are finite sequences of symbols. The set of all possible strings over an alphabet $\Sigma$, including the empty string $\epsilon$, is denoted as the Kleene star closure, $\Sigma^*$.

To formally define which strings are valid within a specific language, we utilize a **Grammar** ($G$). A grammar is defined as an ordered quadruple $G = (V_N, V_T, P, S)$, where:

* **$V_N$ (Non-terminal symbols):** A finite set of internal symbols used as placeholders for patterns or structures.
* **$V_T$ (Terminal symbols):** A finite set of symbols that form the actual content of the strings. $V_N \cap V_T = \emptyset$.
* **$P$ (Production rules):** A finite set of rules that define how symbols can be replaced.
* **$S$ (Start symbol):** A special non-terminal ($S \in V_N$) from which all derivations begin.



According to the **Chomsky Classification**, the grammar in this work (**Variant 7**) is a **Type 3: Regular Grammar**. These are the most restricted grammars, where rules follow the format $A \rightarrow aB$ or $A \rightarrow a$. Type 3 languages are equivalent to **Finite Automata (FA)**.

---

##  Objectives

* **Theoretical Foundations:** Understand the components of formal languages: alphabet, vocabulary, and grammar structures.
* **Software Design:** Implement a modular `Grammar` class representing the quadruple $(V_N, V_T, P, S)$.
* **String Generation:** Develop a stochastic derivation engine to generate valid strings by following production rules.
* **Mathematical Conversion:** Implement an algorithm to transform a Regular Grammar into an equivalent Finite Automaton.
* **Automata Simulation:** Develop a `FiniteAutomaton` class to process input strings and determine their membership in the language.

---

## Implementation Description

The implementation is designed using **Object-Oriented Programming (OOP)** principles in Python.

### Grammar Class (`grammar.py`)
This class acts as the "producer." It stores production rules in a dictionary.
* **`generate_string`**: Implements a random walk through the grammar starting from $S$. It replaces non-terminals using `random.choice`. A safety threshold (20 iterations) is implemented to prevent infinite loops caused by cycles.
* **`to_finite_automaton`**: Acts as a bridge. It maps each non-terminal to a state in the FA. $A \rightarrow aB$ creates a transition $\delta(A, a) = B$, while $A \rightarrow a$ creates a transition to a specialized "Final State" (labeled 'X').

### Finite Automaton Class (`finite_automaton.py`)
This class acts as the "recognizer."
* **`string_belong_to_language`**: Simulates the transition process. It maintains a set of "current states" and updates them for every character in the input string. If any reached state is in the final states set after processing the string, the input is accepted.
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
    
    return to_finite_automaton(states, self.Vt, transitions, self.S, {final_state})

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

## Challenges and Difficulties
During the implementation of this project, several technical and conceptual challenges were encountered:
* Handling Recursive Productions: One of the main challenges was managing the stochastic string generation for rules like $L \rightarrow aL$ or $D \to E \to F \to D$. Without a proper stopping condition, the recursive nature of these rules could lead to an infinite derivation tree or a RecursionError. To solve this, a loop-limit (iteration threshold) was implemented to ensure all generated strings are of a reasonable and finite length.
* Mapping Terminating Rules: Converting a grammar production like $L \rightarrow c$ to a Finite Automaton transition was initially non-obvious. Unlike $S \rightarrow aD$, which clearly moves from state $S$ to $D$, terminal rules end the process. I overcame this by introducing a conceptual "Sink/Final State" (X), which serves as the destination for all productions that do not lead to another non-terminal.
* Non-Determinism Management: Although the variant provided is largely linear, the structure of a Finite Automaton must inherently support potential non-determinism. Implementing the current_states as a set rather than a single variable allowed the recognizer to track all possible active paths simultaneously, making the FA robust and mathematically accurate according to NFA (Non-deterministic Finite Automata) standards.
* Software Architecture (Circular Imports): In Python, having the Grammar class know about FiniteAutomaton and vice versa created a circular dependency. I resolved this by utilizing local imports within the conversion method, which ensured a clean separation of concerns while maintaining the ability to transform one object into another.

## Conclusions / Results
Analytical Derivation Example (Manual Trace)
1. Start: $S$
2. Rule $S \rightarrow aD$: string is a, state $D$.
3. Rule $D \rightarrow bE$: string is ab, state $E$.
4. Rule $E \rightarrow dL$: string is abd, state $L$.
5. Rule $L \rightarrow c$: string is abdc, state Terminal.Result: abdc is a valid word.

### System Results
The system successfully generated samples and validated inputs for Variant 7.
### Generated Samples:
* abdc (Minimum length)
* abcdbdc (Cycle $D-E-F$)
* abdcabc (Cycle in state $L$)
### FA Testing:
* abdc: Accepted (Valid path: $S \xrightarrow{a} D \xrightarrow{b} E \xrightarrow{d} L \xrightarrow{c} X$)
* abcc: Rejected (No valid transition after the first c from state $E$)


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
