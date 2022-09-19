from random import randint


def draw_int_number(r_min: int, r_max: int) -> int:
    if r_min > r_max:
        raise ValueError('Draw range is not correct')
    return randint(r_min, r_max)


def get_digit_on(position, number: int) -> int:
    return (abs(number) // 10 ** position) % 10


def check_if_the_digits_are_bigger(int_range: tuple[int, int]) -> str:
    r_min, r_max = int_range
    number1 = draw_int_number(r_min, r_max)
    number2 = draw_int_number(r_min, r_max)
    if (get_digit_on(1, number1) > get_digit_on(1, number2)) and (get_digit_on(0, number1) > get_digit_on(0, number2)):
        return "TAK"
    return "NIE"


def main() -> None:
    int_range = (10, 31)
    print(check_if_the_digits_are_bigger(int_range))


main()
