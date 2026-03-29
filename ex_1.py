'''
В заданной строке найти количество символов  в верхнем регистре начиная
с символа с номером i до символа с номером j включительно. Использовать функцию filter().
Нумерацию символов строки считать с 1.
'''

def find_let(in_let: str):
    if in_let == in_let.upper():
        return True
    return False


def main():
    in_str = input('Enter string -->')
    i = int(input('Enter bottom:'))
    j = int(input('Enter up:'))
    capit = list(filter(find_let, in_str[i:j+1]))
    print(len(capit))


if __name__ == '__main__':
    main()