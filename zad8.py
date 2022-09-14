def get_int(message: str) -> int:
    while not (number := input(f'{message}:\n')).isdecimal():
        print("The value provided is not an integer")
    return int(number)


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


def is_prime_digit(n: int) -> bool:
    return n in [2, 3, 5, 7]


def get_digit_on(position, number: int) -> int:
    return (abs(number) // 10 ** position) % 10


def get_integers_until_a_less_than_b() -> int:
    while True:
        if (a := get_int('Provide the first number')) < (b := get_int('Provide the second number')):
            result = 1
            for number in range(a, b+1):
                if is_prime(get_digit_on(0, number)):
                    result = result * number
            return result
        print("Pierwsza liczba powinna być mniejsza od drugiej")


def main():
    print(get_integers_until_a_less_than_b())
    for i in range(100):
        print(f'I = {i} IS PRIME: {is_prime(i)}')


if __name__ == '__main__':
    main()
