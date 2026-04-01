"""
Sort a list of lists in non-increasing order based on numeric values.

The program reads a JSON file containing a list where each element is a list
with two elements: a string and a number. Sorts the list in descending order
based on the numeric values using a lambda function.
"""

import json


def main() -> None:
    """
    Main function: read JSON data from file, sort by numeric values,
    and display the result.
    """
    # Read the JSON file path from user input
    json_file = input("Enter the JSON file path: ")

    # Load the JSON data from the specified file
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Sort in non-increasing order (descending) based on numeric values
    # Uses lambda function to extract the second element (index 1) as the sorting key
    sorted_data = sorted(data, key=lambda item: item[1], reverse=True)

    # Display the sorted result
    print(sorted_data)


if __name__ == "__main__":
    main()