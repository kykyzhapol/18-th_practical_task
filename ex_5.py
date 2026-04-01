"""
Calculate the product of natural numbers in interval [a; b] that are perfect squares
and divisible by c.

The program reads three integers (a, b, c) and computes the product of all numbers
in the range [a, b] that satisfy:
- x is a perfect square (√x is an integer)
- x is divisible by c
Uses filter() and reduce() with lambda functions as required.
"""

from functools import reduce


def main() -> None:
    """
    Main function: read inputs, filter numbers, calculate product, and display result.

    The interval bounds a and b are automatically swapped if a > b.
    """
    # Read input values
    a = int(input("Enter bottom: "))
    b = int(input("Enter top: "))
    c = int(input("Enter c: "))

    # Swap bounds if they are given in reverse order
    if a > b:
        a, b = b, a

    # Generate range of numbers from a to b inclusive
    numbers = range(a, b + 1)

    # Filter numbers that satisfy both conditions:
    # 1. Divisible by c
    # 2. Perfect square (square root is an integer)
    # Check if sqrt(x) equals its integer conversion
    filtered = filter(
        lambda x: x % c == 0 and x ** 0.5 == int(x ** 0.5),
        numbers
    )

    # Calculate the product of all filtered numbers
    # If the filtered iterator is empty, reduce will raise TypeError
    # In that case, we should handle it gracefully
    try:
        product = reduce(lambda x, y: x * y, filtered)
        print(product)
    except TypeError:
        # No numbers satisfy the conditions
        print(0)


if __name__ == "__main__":
    main()