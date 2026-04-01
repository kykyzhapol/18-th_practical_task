"""
Decorator that converts a function's return value to JSON and saves it to a file.

The decorator `to_json` takes the result of the decorated function, serialises it
as JSON (with non‑ASCII characters preserved) and writes it to 'dump.json'.
"""

import json


def to_json(func):
    """
    Decorator that writes the function's return value as JSON to 'dump.json'.

    Args:
        func: The function to decorate.

    Returns:
        A wrapper function that executes the original function, serialises its
        return value to JSON, and writes it to a file.
    """
    def wrapper(*args, **kwargs):
        # Call the original function and get its result
        result = func(*args, **kwargs)

        # Serialise the result to a JSON string
        json_str = json.dumps(result, ensure_ascii=False)

        # Write the JSON to a file
        with open('dump.json', 'w', encoding='UTF-8') as f:
            f.write(json_str)

    return wrapper


@to_json
def simple_math(a: int, b: int) -> int:
    """
    Return the sum of two integers.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        The sum a + b.
    """
    return a + b


@to_json
def user_info(name: str, age: int, city: str) -> dict:
    """
    Return a dictionary containing user information.

    Args:
        name: User's name.
        age: User's age.
        city: User's city.

    Returns:
        A dictionary with keys 'name', 'age', 'city'.
    """
    return {
        'name': name,
        'age': age,
        'city': city
    }


if __name__ == "__main__":
    # Example usage (will write to dump.json each time)
    simple_math(5, 3)
    user_info("Alice", 30, "New York")