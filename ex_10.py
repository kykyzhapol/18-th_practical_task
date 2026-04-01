import time
import threading
import functools
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FutureTimeoutError

class RateLimitExceeded(Exception):
    """Исключение, возникающее при превышении допустимого числа вызовов за период."""
    pass

def limit(max_calls=None, period=1.0, timeout=None):
    """
    Декоратор для ограничения частоты вызовов и времени выполнения функции.

    Параметры:
        max_calls (int, optional): Максимальное количество вызовов за период.
                                   None — ограничение отключено.
        period (float): Интервал времени в секундах, за который учитываются вызовы.
        timeout (float, optional): Максимальное время выполнения функции в секундах.
                                   None — ограничение отключено.

    Исключения:
        RateLimitExceeded: если превышен лимит вызовов.
        TimeoutError: если превышено время выполнения функции.
    """
    call_times = []          # список меток времени вызовов
    lock = threading.Lock()  # для потокобезопасного доступа к списку

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # --- Rate limiting (ограничение частоты) ---
            if max_calls is not None:
                now = time.monotonic()
                with lock:
                    # Удаляем записи старше периода
                    while call_times and call_times[0] <= now - period:
                        call_times.pop(0)
                    # Проверяем, не превышен ли лимит
                    if len(call_times) >= max_calls:
                        raise RateLimitExceeded(
                            f"Превышен лимит вызовов: не более {max_calls} за {period} сек."
                        )
                    call_times.append(now)

            # --- Timeout (ограничение времени выполнения) ---
            if timeout is not None:
                # Выполняем функцию в отдельном потоке с таймаутом
                with ThreadPoolExecutor(max_workers=1) as executor:
                    future = executor.submit(func, *args, **kwargs)
                    try:
                        result = future.result(timeout=timeout)
                    except FutureTimeoutError:
                        raise TimeoutError(
                            f"Превышено время выполнения функции {func.__name__}: {timeout} сек."
                        )
            else:
                result = func(*args, **kwargs)

            return result
        return wrapper
    return decorator


# Функция, ограниченная 2 вызовами за 5 секунд и временем выполнения не более 3 секунд
@limit(max_calls=2, period=5.0, timeout=3.0)
def slow_task(delay):
    time.sleep(delay)
    return "Завершено"

# Вызовы
try:
    print(slow_task(1))   # OK
    print(slow_task(1))   # OK
    print(slow_task(1))   # RateLimitExceeded
except RateLimitExceeded as e:
    print(e)

try:
    print(slow_task(5))   # TimeoutError (спит 5 сек, лимит 3 сек)
except TimeoutError as e:
    print(e)