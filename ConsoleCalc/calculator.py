import math


def add(numb_a: int, numb_b: int) -> int:
    return numb_a + numb_b

def sub(numb_a: int, numb_b: int) -> int:
    return numb_a - numb_b

def mult(numb_a: int, numb_b: int) -> int:
    return numb_a * numb_b

def div(numb_a: int, numb_b: int) -> float:
    return numb_a / numb_b

def int_div(numb_a: int, numb_b: int) -> float:
    return numb_a // numb_b

def check_int(numb_a: str, numb_b: str) -> int:
    while not numb_a.isdigit():
        numb_a = input('Enter number_a:\n')
    numb_a = int(numb_a)

    while not numb_b.isdigit():
        numb_b = input('Enter number_b:\n')
    numb_b = int(numb_b)
    return numb_a, numb_b

def main():
    OPERATIONS = ('+', '-', '*', '/', '//', 'pi')

    operation = input(f'Choose operation: {OPERATIONS}\n')
    while operation not in OPERATIONS:
        operation = input(f'Choose operation: {OPERATIONS}\n')

    match operation:
        case 'pi':
            print(math.pi)
        case _:
            number_a = input('Enter number_a:\n')
            number_b = input('Enter number_b:\n')
            int_numb_a, int_numb_b = check_int(number_a, number_b)
            match operation:
                case '+':
                    print(add(int_numb_a, int_numb_b))
                case '-':
                    print(sub(int_numb_a, int_numb_b))
                case '*':
                    print(mult(int_numb_a, int_numb_b))
                case '/':
                    print(div(int_numb_a, int_numb_b))
                case '//':
                    print(int_div(int_numb_a, int_numb_b))



if __name__ == '__main__':
    main()