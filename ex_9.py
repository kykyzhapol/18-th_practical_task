import json
import xml.etree.ElementTree as ET
import yaml

def to_format(form='json', output_file=None):
    """
    Декоратор для сохранения результата функции в файл указанного формата.

    :param form: Формат вывода ('json', 'xml', 'yaml')
    :param output_file: Имя файла для сохранения. Если не указано, генерируется по умолчанию.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            # Определяем имя файла
            filename = output_file if output_file is not None else f"dump.{form}"

            # Обработчики форматов
            handlers = {
                'json': lambda data: _save_json(data, filename),
                'xml': lambda data: _save_xml(data, filename),
                'yaml': lambda data: _save_yaml(data, filename),
            }

            handler = handlers.get(form)
            if handler:
                handler(result)
            else:
                raise ValueError(f"Unsupported format: {form}")

            return result
        return wrapper
    return decorator

def _save_json(data, filename):
    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def _save_xml(data, filename):
    root = ET.Element('data')
    # Преобразуем данные в строку для записи в текстовый узел
    root.text = str(data)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='UTF-8', xml_declaration=True)

def _save_yaml(data, filename):
    with open(filename, 'w', encoding='UTF-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)


# Функция, возвращающая словарь (будет сохранён в JSON)
@to_format(form='json', output_file='user.json')
def get_user(user_id):
    return {
        "id": user_id,
        "name": "Alice",
        "email": "alice@example.com"
    }

# Функция, возвращающая строку (сохранится в XML)
@to_format(form='xml', output_file='message.xml')
def get_message():
    return "Hello, world!"

# Вызов
user_data = get_user(42)
print(user_data)  # Словарь также доступен в коде

message = get_message()
print(message)