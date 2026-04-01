"""
Calculate the sum of numbers divisible by both c and d within a given interval.

The program reads four integers (a, b, c, d) and computes the sum of all numbers
in the range [a, b] that are divisible by both c and d.
"""


def main() -> None:
    """
    Main function: read inputs, calculate the sum, and display the result.

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

    # Filter numbers divisible by both c and d
    # Using lambda function with logical AND
    filtered = filter(lambda x: x % c == 0 and x % d == 0, numbers)

    # Calculate the sum of filtered numbers
    total = sum(filtered)

    # Display the result
    print(f"Sum of numbers divisible by {c} and {d} in interval [{a}; {b}]: {total}")


if __name__ == "__main__":
    main()