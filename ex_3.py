"""
Count natural numbers in an interval [a; b] that are not divisible by c
and end with digit d.

The program reads four integers (a, b, c, d) and counts numbers satisfying:
- x is in range [a, b] (inclusive)
- x % c != 0 (not divisible by c)
- x % 10 == d (ends with digit d)
Uses map() with a lambda function as required.
"""


def main() -> None:
    """
    Main function: read inputs, count matching numbers, and display the result.

    The interval bounds a and b are automatically swapped if a > b.
    """
    # Read input values
    a = int(input("Enter bottom: "))
    b = int(input("Enter top: "))
    c = int(input("Enter c: "))
    d = int(input("Enter d: "))

    # Swap bounds if they are given in reverse order
    if a > b:
        a, b = b, a

    # Generate range of numbers from a to b inclusive
    numbers = range(a, b + 1)

    # map returns 1 if the number matches conditions, otherwise 0
    # Conditions: not divisible by c AND ends with digit d
    count = sum(map(lambda x: 1 if (x % c != 0) and (x % 10 == d) else 0, numbers))

    # Display the result
    print(count)


if __name__ == "__main__":
    main()