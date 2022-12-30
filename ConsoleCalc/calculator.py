import math


class Calculator:

    def add(self, numb_a: int, numb_b: int) -> int:
        return numb_a + numb_b

    def sub(self, numb_a: int, numb_b: int) -> int:
        return numb_a - numb_b

    def mult(self, numb_a: int, numb_b: int) -> int:
        return numb_a * numb_b

    def div(self, numb_a: int, numb_b: int) -> float:
        return numb_a / numb_b

    def int_div(self, numb_a: int, numb_b: int) -> float:
        return numb_a // numb_b

    def pi(self):
        return math.pi

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

    calculator = Calculator()

    match operation:
        case 'pi':
            print(calculator.pi())
        case _:
            number_a = input('Enter number_a:\n')
            number_b = input('Enter number_b:\n')
            int_numb_a, int_numb_b = check_int(number_a, number_b)
            match operation:
                case '+':
                    print(calculator.add(int_numb_a, int_numb_b))
                case '-':
                    print(calculator.sub(int_numb_a, int_numb_b))
                case '*':
                    print(calculator.mult(int_numb_a, int_numb_b))
                case '/':
                    print(calculator.div(int_numb_a, int_numb_b))
                case '//':
                    print(calculator.int_div(int_numb_a, int_numb_b))



if __name__ == '__main__':
    main()