from datetime import datetime


def log(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Формируем строку лога
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            error_type = type(e).__name__
            log_entry = f"{timestamp} | ERROR: {error_type}\n"

            # Записываем в файл
            with open('errors.log', 'a', encoding='utf-8') as f:
                f.write(log_entry)
    return wrapper

@log
def divide(a, b):
    return a / b

try:
    divide(10,0)
except:
    pass