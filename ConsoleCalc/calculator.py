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
    number_a, number_b = [int(input(f"Enter number {number}:\n")) for number in range(1, 3)]
    print(int_div(number_a, number_b))


if __name__ == '__main__':
    main()