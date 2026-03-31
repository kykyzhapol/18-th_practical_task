'''
Найти произведение натуральных чисел на интервале [a; b], которые являются полными квадратами,
кратными числу с .
Использовать функцию reduce() и анонимную функцию
'''
from functools import reduce


def main():
    # Ввод данных
    a = int(input("Enter bottom: "))
    b = int(input("Enter top: "))
    c = int(input("Enter c: "))

    # Если границы заданы в обратном порядке, меняем их местами
    if a > b:
        a, b = b, a

    numbers = range(a, b + 1)
    filtered = filter(lambda x: x % c == 0 and x**0.5 == int(x**0.5), numbers)
    print(reduce(lambda x, y: x*y, filtered))


if __name__ == '__main__':
    main()