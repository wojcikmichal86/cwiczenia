from random import randint
from typing import Callable
from math import sqrt


def draw_n_random_ints(n: int, r_min: int, r_max: int) -> list[int]:
    if r_min >= r_max:
        raise ValueError("Range min should be lower than range max")
    return [randint(r_min, r_max) for _ in range(n)]


def get_min_max(int_array: list[int]) -> tuple[int, int]:
    return min(int_array), max(int_array)


def sum_digits_of_(number: int) -> int:
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    return digit_sum


def count_divisors_of(number: int) -> int:
    if number == 0:
        raise ValueError("Zero has infinite divisors")
    return len([i for i in range(1, (number // 2) + 1) if number % i == 0] + [number])


def count_prime_factors_of(number: int) -> int:
    result = []
    while number % 2 == 0:
        result.append(2)
        number = number // 2
    for i in range(3, int(sqrt(number)) + 1, 2):
        while number % i == 0:
            result.append(i)
            number = number // i
    if number > 2:
        result.append(number)
    return len(result)


def find_number_with(condition: Callable, int_array: list[int]) -> int:
    if len(int_array) < 1:
        raise ValueError("The list cannot be empty")
    result = int_array[0]
    best_score = condition(result)
    for i in int_array[1:]:
        i_score = condition(i)
        if i_score > best_score:
            result = i
            best_score = i_score
    return result


def main():
    int_array = draw_n_random_ints(5, 10, 100)
    print(int_array)
    minimum, maximum = get_min_max(int_array)
    print(f'The minimum is: {minimum}, the maximum: {maximum}')
    print(f'The number with biggest digit sum is {find_number_with(sum_digits_of_, int_array)}')
    print(f'The number with most divisors is {find_number_with(count_divisors_of, int_array)}')
    print(f'The number with most prime factors is {find_number_with(count_prime_factors_of, int_array)}')


if __name__ == '__main__':
    main()
