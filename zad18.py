from random import randint
from math import sqrt


def get_rand_int_from(int_range: tuple[int, int]) -> int:
    r_min, r_max = int_range
    if r_min >= r_max:
        raise ValueError("Lower range must be lower than higher range")
    return randint(r_min, r_max)


def calculate_divisors_of(smaller: int, bigger: int) -> tuple[int, int]:
    counter = 0
    divisor_sum = 0
    for i in range(2, int(sqrt(bigger)) + 1):
        match smaller % i == 0, bigger % i == 0:
            case True, True: counter += 1
            case False, False: pass
            case _: divisor_sum += i
    return counter, divisor_sum


def keep_drawing_ints_until_num2_bigger_than_num1(int_range: tuple[int, int]) -> tuple[int, int]:
    while (num1 := get_rand_int_from(int_range)) >= (num2 := get_rand_int_from(int_range)):
        continue
    return num1, num2


def main():
    int_range = 100, 1000
    a, b = keep_drawing_ints_until_num2_bigger_than_num1(int_range)
    counter, divisor_sum = calculate_divisors_of(a, b)
    print(f'Number of common divisors: {counter}, sum of uncommon divisors: {divisor_sum}')


main()
