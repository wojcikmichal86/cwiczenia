from typing import Callable


def get_int_from_user(message: str) -> int:
    while True:
        number = input(f"{message}:\n")
        if number.isdecimal():
            return int(number)
        print("The value provided is not correct")


def a_is_smaller_than_b(a: int, b: int) -> bool:
    return a < b


def keep_getting_two_ints_until(condition: Callable) -> tuple[int, int]:
    while True:
        a = int(input('Provide the first number:\n'))
        b = int(input('Provide the second number:\n'))
        if condition(a, b):
            return a, b
        print("First number should be smaller than the second")


def find_nwd(a: int, b: int) -> int:
    return find_nwd(b, a % b) if b else a


def find_nww(a: int, b: int) -> int:
    return a * b // find_nwd(a, b)


def main():
    a, b = keep_getting_two_ints_until(a_is_smaller_than_b)
    print(find_nwd(a, b))
    print(find_nww(a, b))


if __name__ == '__main__':
    main()
