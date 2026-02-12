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

    # 1. Initialize Grammar
    grammar = Grammar(Vn, Vt, P, 'S')

    # 2. Automatically generate 5 valid strings
    print("--- 5 Generated Valid Strings ---")
    for _ in range(5):
        print(f"Generated: {grammar.generate_string()}")

    # 3. Convert the Grammar to a Finite Automaton
    fa = grammar.to_finite_automaton()

    # 4. Interactive Manual Verification
    print("\n--- Manual FA Verification ---")
    print("Type a string to check if it belongs to the language.")
    print("Type 'exit' or 'q' to stop.")

    while True:
        # Get input from user and remove whitespace
        user_input = input("\nEnter string to check: ").strip()

        # Check if the user wants to close the program
        if user_input.lower() in ['exit', 'q']:
            print("Exiting program...")
            break

        # Run the FA check
        if fa.string_belong_to_language(user_input):
            print(f"Result: SUCCESS! The string '{user_input}' belongs to the language.")
        else:
            print(f"Result: REJECTED! The string '{user_input}' is NOT in the language.")


if __name__ == "__main__":
    main()