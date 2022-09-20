from random import randint


def get_int_from(int_range: tuple[int, int]) -> int:
    r_min, r_max = int_range
    if r_min >= r_max:
        raise ValueError("Range min should be bigger than max")
    return randint(r_min, r_max)


def get_min_max_from(ints: tuple[int, int, int]) -> tuple[int, int]:
    return min(ints), max(ints)


def sum_last_digits(number1: int, number2: int) -> int:
    return ((abs(number1) // 10 ** 0) % 10) + ((abs(number2) // 10 ** 0) % 10)


def main() -> None:
    int_range = (5, 232)
    num1 = get_int_from(int_range)
    num2 = get_int_from(int_range)
    num3 = get_int_from(int_range)
    random_ints = num1, num2, num3
    minint, maxint = get_min_max_from(random_ints)
    last_digit_sum = sum_last_digits(minint, maxint)
    print(minint, maxint, last_digit_sum)


main()
