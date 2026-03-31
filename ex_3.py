'''
Найти количество натуральных чисел на интервале
[a; b] не кратных c и оканчивающихся цифрой d. Использовать функцию map() и анонимную функцию.
'''
def main():
    # Ввод данных
    a = int(input("Enter bottom: "))
    b = int(input("Enter top: "))
    c = int(input("Enter c: "))
    d = int(input("Enter d: "))

    # Если границы заданы в обратном порядке, меняем их местами
    if a > b:
        a, b = b, a


    numbers = range(a, b + 1)
    # map возвращает 1, если число подходит под условия, иначе 0
    count = sum(map(lambda x: 1 if (x % c != 0) and (x % 10 == d) else 0, numbers))

    print(count)


if __name__ == "__main__":
    main()