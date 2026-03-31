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
    filtered = filter(lambda x: x % c == 0 and x % d == 0, numbers)
    total = sum(filtered)

    print(f"Сумма чисел, кратных {c} и {d}, на интервале [{a}; {b}]: {total}")


if __name__ == "__main__":
    main()