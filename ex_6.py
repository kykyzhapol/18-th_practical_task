'''
Напишите декоратор, который выводит на экран результат работы функций, имеющих один параметр.
'''


def print_dec(func):
    def wrapper(x):
        result = func(x)
        print(result)
        return result
    return wrapper


@print_dec
def simple_math(a):
    return a**2


simple_math(1)