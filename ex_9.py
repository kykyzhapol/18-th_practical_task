"""
Decorator for saving function results to files in different formats.

Provides a decorator that can save the return value of a function to a file
in JSON, XML, or YAML format.
"""

import json
import xml.etree.ElementTree as ET
import yaml


def to_format(form='json', output_file=None):
    """
    Decorator to save function result to a file in the specified format.

    Args:
        form: Output format ('json', 'xml', or 'yaml').
        output_file: Filename to save the result. If None, generates a default name.

    Returns:
        A decorator function that wraps the original function.

    Raises:
        ValueError: If the specified format is not supported.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Execute the original function to get the result
            result = func(*args, **kwargs)

            # Determine the output filename
            filename = output_file if output_file is not None else f"dump.{form}"

            # Map formats to their save handlers
            handlers = {
                'json': lambda data: _save_json(data, filename),
                'xml': lambda data: _save_xml(data, filename),
                'yaml': lambda data: _save_yaml(data, filename),
            }

            # Get the appropriate handler for the requested format
            handler = handlers.get(form)

            if handler:
                # Save the result to file
                handler(result)
            else:
                # Unsupported format
                raise ValueError(f"Unsupported format: {form}")

            # Return the original result for further use in code
            return result

        return wrapper
    return decorator


def _save_json(data, filename):
    """
    Save data to a JSON file.

    Args:
        data: Data to be serialised.
        filename: Output file path.
    """
    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _save_xml(data, filename):
    """
    Save data to an XML file.

    Args:
        data: Data to be serialised (converted to string).
        filename: Output file path.
    """
    # Create root element and set the data as text content
    root = ET.Element('data')
    root.text = str(data)

    # Create element tree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='UTF-8', xml_declaration=True)


def _save_yaml(data, filename):
    """
    Save data to a YAML file.

    Args:
        data: Data to be serialised.
        filename: Output file path.
    """
    with open(filename, 'w', encoding='UTF-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)


# Example 1: Function returning a dictionary (saved as JSON)
@to_format(form='json', output_file='user.json')
def get_user(user_id: int) -> dict:
    """
    Get user information.

    Args:
        user_id: User identifier.

    Returns:
        Dictionary with user data.
    """
    return {
        "id": user_id,
        "name": "Alice",
        "email": "alice@example.com"
    }


# Example 2: Function returning a string (saved as XML)
@to_format(form='xml', output_file='message.xml')
def get_message() -> str:
    """
    Get a greeting message.

    Returns:
        A string containing the message.
    """
    return "Hello, world!"


if __name__ == "__main__":
    # Call the decorated functions
    user_data = get_user(42)
    print(user_data)  # Dictionary is also available in code

    message = get_message()
    print(message)