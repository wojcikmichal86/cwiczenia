from random import randint
from typing import Final


def draw_int_number(r_min: int, r_max: int) -> int:
    if r_min > r_max:
        raise ValueError('Draw range is not correct')
    return randint(r_min, r_max)


def display_range(number):
    print(f"Selected number {number} belongs to the range:")
    if number < -40:
        print("<-∞, -40)")
    elif number < -20:
        print("<-40, -20)")
    elif number <= 20:
        print("<-20, 20>")
    else:
        print("(20, ∞)")


def display_range_km(number: int) -> int:
    if number < -40:
        return 1
    if number < -20:
        return 2
    if number <= 20:
        return 3
    return 4


def main():
    r_min: Final = -50
    r_max: Final = 50
    number = draw_int_number(r_min, r_max)
    print(f'{number = }')
    print(display_range_km(number))


if __name__ == '__main__':
    main()