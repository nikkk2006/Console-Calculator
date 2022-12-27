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

def main():
    OPERATIONS = ('+', '-', '*', '/', '//')

    operation = input(f'Choose operation: {OPERATIONS}\n')
    number_a, number_b = [int(input(f"Enter number {number}:\n")) for number in range(1, 3)]

    if operation == '+':
        print(add(number_a, number_b))
    elif operation == '-':
        print(sub(number_a, number_b))
    elif operation == '*':
        print(mult(number_a, number_b))
    elif operation == '/':
        print(div(number_a, number_b))
    elif operation == '//':
        print(int_div(number_a, number_b))


if __name__ == '__main__':
    main()