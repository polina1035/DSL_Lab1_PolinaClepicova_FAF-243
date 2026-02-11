from grammar import Grammar


def main():
    # Grammar definition for Variant 7
    # Vn - Non-terminals, Vt - Terminals, P - Productions, S - Start symbol
    Vn = {'S', 'D', 'E', 'F', 'L'}
    Vt = {'a', 'b', 'c', 'd'}
    P = {
        'S': ['aD'],
        'D': ['bE'],
        'E': ['cF', 'dL'],
        'F': ['dD'],
        'L': ['aL', 'bL', 'c']
    }

    # Instantiate the Grammar
    grammar = Grammar(Vn, Vt, P, 'S')

    # 1. Generate 5 valid strings
    print("--- 5 Generated Valid Strings ---")
    generated_words = []
    for _ in range(5):
        word = grammar.generate_string()
        generated_words.append(word)
        print(f"Generated: {word}")

    # 2. Convert Grammar to Finite Automaton
    fa = grammar.to_finite_automaton()

    # 3. Verify the generated strings using the FA
    print("\n--- Finite Automaton Verification ---")
    for word in generated_words:
        is_valid = fa.string_belong_to_language(word)
        print(f"Checking word '{word}': {'ACCEPTED' if is_valid else 'REJECTED'}")

    # 4. Manual tests
    print("\n--- Manual Tests ---")
    test_cases = ["abdc", "abcdbdc", "abcc", "aaaa"]
    for test in test_cases:
        result = "VALID" if fa.string_belong_to_language(test) else "INVALID"
        print(f"Manual test '{test}': {result}")


if __name__ == "__main__":
    main()