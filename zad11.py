from random import uniform


def get_rand_float_from(float_range: tuple[float, float]) -> float:
    r_min, r_max = float_range
    if r_min > r_max:
        raise ValueError('Incorrect range provided')
    return uniform(r_min, r_max)


def get_minimum_int(float_range: tuple[float, float]) -> int:
    r_min, r_max = float_range
    return int(r_min)


def main() -> None:
    float_range = (-0.45, 6.24)
    rand_float = get_rand_float_from(float_range)
    print(rand_float)
    min_int = get_minimum_int(float_range)
    print(min_int)
    print(len(range(min_int, int(rand_float))))


if __name__ == '__main__':
    main()