import inspect


def introspection_info(obj):

    # определяем тип объекта
    obj_type = type(obj).__name__

    # получаем список атрибутов и методов
    obj_dir = dir(obj)

    # создаем списки методов и атрибутов
    obj_methods = [attr for attr in obj_dir if callable(getattr(obj, attr))]
    obj_attr = [attr for attr in obj_dir if not callable(getattr(obj, attr))]

    # Определяем модуль объекта
    if callable(obj):
        module = inspect.getmodule(obj).__name__
    else:
        module = None

    # Создаем словарь с информацией
    introspection_info = {'type': obj_type, 'attributes': obj_attr, 'methods': obj_methods, 'module': module}

    return introspection_info

# Проверочный код

number_info = introspection_info(42)
print(number_info)

list_info = introspection_info([1, 2, 3])
print(list_info)

list_info = introspection_info(introspection_info)
print(list_info)

list_info = introspection_info(inspect)
print(list_info)