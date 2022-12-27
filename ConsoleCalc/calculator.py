
def add(numb_a: int, numb_b: int) -> int:
    return numb_a + numb_b

def main():
    number_a = int(input('Enter number a:\n'))
    number_b = int(input('Enter number b:\n'))
    print(add(number_a, number_b))


if __name__ == '__main__':
    main()