"""
Count uppercase letters in a substring.

The program reads a string and two indices (1‑based) i and j,
then prints the number of uppercase characters in the substring
from i to j inclusive, using filter().
"""


def is_uppercase(char: str) -> bool:
    """
    Check if a single character is uppercase.

    Args:
        char: A string containing exactly one character.

    Returns:
        True if the character is an uppercase letter, False otherwise.
    """
    return char.isupper()


def main() -> None:
    """
    Main function: read input, count uppercase letters in the substring,
    and print the result.
    """
    # Read the string
    in_str = input('Enter string --> ')
    # Read 1‑based indices
    i = int(input('Enter bottom: '))
    j = int(input('Enter up: '))

    # Extract substring (convert to 0‑based indices)
    substring = in_str[i - 1:j]   # j is inclusive, so slice end is j (exclusive)

    # Use filter to keep only uppercase characters
    uppercase_chars = list(filter(is_uppercase, substring))

    # Output the count
    print(len(uppercase_chars))


if __name__ == '__main__':
    main()