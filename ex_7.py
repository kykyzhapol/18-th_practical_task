'''
Напишите декоратор to_json для преобразования возвращаемого функцией значения в формате JSON.
Приведите несколько разных примеров использования декоратора.
'''
import json


def to_json(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        json_str = json.dumps(result, ensure_ascii=False)
        with open('dump.json', 'w', encoding='UTF-8') as f:
            f.write(json_str)
    return wrapper


@to_json
def simple_m(a, b):
    return a + b


@to_json
def user_info(name, age, city):
    return {
        'name': name,
        'age': age,
        'city': city
    }
