from random import randint


def get_rand_int_from(int_range: tuple[int, int]) -> int:
    r_min, r_max = int_range
    if r_min > r_max:
        raise ValueError("Draw range is not correct")
    return randint(r_min, r_max)


def get_three_rand_ints(range1: tuple, range2: tuple, range3: tuple) -> tuple[int, int, int]:
    number1 = get_rand_int_from(range1)
    number2 = get_rand_int_from(range2)
    number3 = get_rand_int_from(range3)
    return number1, number2, number3


def calc_average(number1, number2, number3) -> int:
    return (number1 + number2 + number3) / 3


def find_num_closes_to(average: int, number1, number2, number3) -> int:
    closest_num = number1
    if abs(average - number2) < abs(average - closest_num):
        closest_num = number2
    if abs(average - number3) < abs(average - closest_num):
        closest_num = number3
    return closest_num


def main() -> None:
    a, b, c = get_three_rand_ints((0, 11), (-13, 24), (34, 88))
    average = calc_average(a, b, c)
    print(find_num_closes_to(average, a, b, c))


if __name__ == '__main__':
    main()