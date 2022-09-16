from random import randint


def get_rand_int_from(target_range: tuple[int, int]) -> int:
    r_min, r_max = target_range
    if r_min > r_max:
        raise ValueError("Draw range is not correct")
    return randint(r_min, r_max)


def get_int_from_user(message: str) -> int:
    return int(input(f'{message}:\n'))


def calc_average(num1: int, num2: int) -> float:
    return (num1 + num2) / 2


def get_ints_from_user_until_average_close_to(target: int, difference) -> tuple[int, int]:
    while True:
        if (abs(calc_average(num1 := get_int_from_user('Provide first number'),
                             num2 := get_int_from_user('Provide second number'))
                - target) < difference):
            return num1, num2


def main() -> None:
    target_range = (1, 21)
    rand_num = get_rand_int_from(target_range)
    print(rand_num)
    print(get_ints_from_user_until_average_close_to(rand_num, 2))


if __name__ == '__main__':
    main()