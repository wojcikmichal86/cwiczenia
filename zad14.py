from random import randint


def get_int_from(int_range: tuple[int, int]) -> int:
    r_min, r_max = int_range
    if r_min >= r_max:
        raise ValueError("Range min should be smaller that range max")
    return randint(r_min, r_max)


def swap_digits_of(number: int) -> int:
    tens = (abs(number) // 10 ** 1) % 10
    ones = (abs(number) // 10 ** 0) % 10
    return (ones * 10) + tens


def main() -> None:
    int_range = (10, 100)
    number = get_int_from(int_range)
    print(swap_digits_of(number))


main()
