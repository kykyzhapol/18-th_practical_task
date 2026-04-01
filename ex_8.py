"""
Decorator that logs exceptions to a file.

The decorator catches any exception raised by the decorated function,
writes a log entry with timestamp and exception type to 'errors.log',
and then re-raises the exception.
"""

from datetime import datetime


def log(func):
    """
    Decorator that logs exceptions to a file.

    Args:
        func: The function to be decorated.

    Returns:
        A wrapper function that catches exceptions and logs them.
    """
    def wrapper(*args, **kwargs):
        try:
            # Execute the original function
            return func(*args, **kwargs)
        except Exception as e:
            # Create timestamp for the log entry
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Get the exception class name
            error_type = type(e).__name__
            # Format the log entry
            log_entry = f"{timestamp} | ERROR: {error_type}\n"

            # Append the log entry to the errors file
            with open('errors.log', 'a', encoding='utf-8') as f:
                f.write(log_entry)

            # Re-raise the exception for further handling
            raise
    return wrapper


@log
def divide(a: float, b: float) -> float:
    """
    Divide two numbers.

    Args:
        a: Numerator.
        b: Denominator.

    Returns:
        The result of a divided by b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    return a / b


if __name__ == "__main__":
    try:
        divide(10, 0)
    except Exception:
        # Exception is logged by the decorator and caught here
        pass