"""
Decorator for rate limiting and timeout control.

Provides a decorator that can limit the number of function calls within a time period
and enforce a maximum execution time for the decorated function.
"""

import time
import threading
import functools
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FutureTimeoutError


class RateLimitExceeded(Exception):
    """Exception raised when the maximum number of calls within a period is exceeded."""
    pass


def limit(max_calls=None, period=1.0, timeout=None):
    """
    Decorator to limit call frequency and execution time of a function.

    Args:
        max_calls: Maximum number of calls allowed within the period.
                   If None, rate limiting is disabled.
        period: Time interval in seconds for counting calls.
        timeout: Maximum execution time in seconds for the function.
                 If None, timeout is disabled.

    Returns:
        A decorator function that wraps the original function.

    Raises:
        RateLimitExceeded: If the call limit is exceeded.
        TimeoutError: If the function execution exceeds the timeout.
    """
    # List of timestamps for recent calls (thread-safe access)
    call_times = []
    # Lock for thread-safe access to the call_times list
    lock = threading.Lock()

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # --- Rate limiting (call frequency control) ---
            if max_calls is not None:
                now = time.monotonic()
                with lock:
                    # Remove timestamps older than the current period
                    while call_times and call_times[0] <= now - period:
                        call_times.pop(0)

                    # Check if the call limit has been exceeded
                    if len(call_times) >= max_calls:
                        raise RateLimitExceeded(
                            f"Call limit exceeded: no more than {max_calls} calls per {period} sec."
                        )

                    # Record the current call timestamp
                    call_times.append(now)

            # --- Timeout (execution time control) ---
            if timeout is not None:
                # Execute the function in a separate thread with timeout
                with ThreadPoolExecutor(max_workers=1) as executor:
                    future = executor.submit(func, *args, **kwargs)
                    try:
                        result = future.result(timeout=timeout)
                    except FutureTimeoutError:
                        raise TimeoutError(
                            f"Function {func.__name__} execution timeout: {timeout} sec."
                        )
            else:
                # Execute normally without timeout
                result = func(*args, **kwargs)

            return result

        return wrapper
    return decorator


# Function with rate limit of 2 calls per 5 seconds and 3-second timeout
@limit(max_calls=2, period=5.0, timeout=3.0)
def slow_task(delay: float) -> str:
    """
    Simulate a slow task by sleeping for the specified delay.

    Args:
        delay: Number of seconds to sleep.

    Returns:
        A completion message.
    """
    time.sleep(delay)
    return "Completed"


if __name__ == "__main__":
    # Test rate limiting
    try:
        print(slow_task(1))   # OK - first call
        print(slow_task(1))   # OK - second call within limit
        print(slow_task(1))   # RateLimitExceeded - third call exceeds limit
    except RateLimitExceeded as e:
        print(e)

    # Test timeout
    try:
        print(slow_task(5))   # TimeoutError - sleeps for 5 seconds, timeout is 3 seconds
    except TimeoutError as e:
        print(e)