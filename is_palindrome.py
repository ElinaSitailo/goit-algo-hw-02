# Необхідно розробити функцію,
# яка приймає рядок як вхідний параметр,
# додає всі його символи до двосторонньої черги (deque з модуля collections в Python),
# а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом.
# Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів,
# а також бути нечутливою до регістру та пробілів.

from collections import deque


def is_palindrome(input_string):
    """Перевіряє, чи є вхідний рядок паліндромом."""
    
    cleaned_string = "".join(input_string.split()).lower()
    cleaned_string = ''.join(char for char in cleaned_string if char.isalnum()) 
    char_deque = deque(cleaned_string)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True


if __name__ == "__main__":
    test_strings = [
        "A man a plan a canal Panama",
        "Cigar? Toss it in a can. It is so tragic.",
        "racecar",
        "hello",
        "Was it a car or a cat I saw",
        "No 'x' in Nixon",
        "Жарт – суму страж",
        "кит на морі романтик",
        "Не паліндром"
    ]
    for s in test_strings:
        print(f"'{s}' -> {"Це паліндром" if is_palindrome(s) else "Не паліндром"}")
