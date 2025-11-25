from collections import deque

bracket_pairs = {")": "(", "}": "{", "]": "["}


def is_symmetric(input_string):
    """Перевіряє, чи є вхідний рядок симетричним за дужками."""

    opening_brackets = set(bracket_pairs.values())
    closing_brackets = set(bracket_pairs.keys())

    char_deque = deque()

    for char in input_string:
        if char in opening_brackets:
            char_deque.append(char)
        elif char in closing_brackets:
            if not char_deque or char_deque.pop() != bracket_pairs[char]:
                return False

    return len(char_deque) == 0


if __name__ == "__main__":
    test_strings = ["( ){[ 1 ]( 1 + 3 )( ){ }}",
                    "( 23 ( 2 - 3);",
                    "( 11 }",
                    "({ )} ",
                    ]
    for s in test_strings:
        print(f"'{s}' : {"Симетрично" if is_symmetric(s) else "Несиметрично"}")
