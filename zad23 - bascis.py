from random import randint


def draw_random_int(r_min: int, r_max: int) -> int:
    if r_min >= r_max:
        raise ValueError("Range min should be lower than range max")
    return randint(r_min, r_max)


def get_digits_of_(number: int) -> list[int]:
    digits = []
    while number > 0:
        digits.append(number % 10)
        number //= 10
    return digits


def separate_max_from_the_rest_of(int_array: list[int]) -> tuple[int, list[int]]:
    ordered_list = sorted(int_array, reverse=True)
    return ordered_list[0], ordered_list[1:]


def sum_differences(minuend: int, subtrahends: list[int]) -> int:
    return sum([minuend - subtrahend for subtrahend in subtrahends])


def main():
    R_MIN = 1000
    R_MAX = 3000
    number = draw_random_int(R_MIN, R_MAX)
    print(number)
    digits = get_digits_of_(number)
    print(digits)
    max_digit, rest = separate_max_from_the_rest_of(digits)
    print(max_digit)
    print(sum_differences(max_digit, rest))


if __name__ == '__main__':
    main()