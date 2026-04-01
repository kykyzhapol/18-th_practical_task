"""
Decorator that prints the result of a function taking a single argument.

The decorator wraps the target function, prints its return value,
and then returns the value unchanged.
"""


def print_result(func):
    """
    Decorator that prints the result of the decorated function.

    Args:
        func: The function to be decorated. It must accept exactly one argument.

    Returns:
        A wrapper function that prints the result before returning it.
    """
    def wrapper(x):
        # Call the original function
        result = func(x)
        # Print the returned value
        print(result)
        # Return the result unchanged
        return result
    return wrapper


@print_result
def simple_math(a: int) -> int:
    """
    Compute the square of a number.

    Args:
        a: An integer.

    Returns:
        The square of a.
    """
    return a ** 2


if __name__ == "__main__":
    simple_math(1)   # Should print 1