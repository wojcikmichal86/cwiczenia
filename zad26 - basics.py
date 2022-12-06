from typing import Final, Callable
from random import randint


def is_odd(number: int) -> bool:
    return number % 2 != 0


def draw_int_from_range_with(condition: Callable, r_min: int, r_max: int) -> int:
    if r_min >= r_max:
        raise ValueError("Range min should be lower than range max")
    while True:
        number = randint(r_min, r_max)
        if condition(number):
            return number


def get_digits_sum(number: int) -> int:
    return sum(int(char) for char in str(number))


def display_all_powers_of_2_lesser_than(limit: int) -> list[int]:
    return [2 << i for i in range(len(bin(limit)) - 3)]


def main():
    R_MIN: Final = 10
    R_MAX: Final = 40
    number = draw_int_from_range_with(is_odd, R_MIN, R_MAX)
    limit = number - get_digits_sum(number)
    print(limit)
    print(display_all_powers_of_2_lesser_than(limit))


if __name__ == '__main__':
    main()

