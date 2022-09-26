from random import uniform


def get_rand_float_from(float_range: tuple[float, float]) -> float:
    r_min, r_max = float_range
    if r_min >= r_max:
        raise ValueError('Range min should be lower than range max')
    return uniform(r_min, r_max)


def get_areas_and_circumference_ratio(side1: float, side2: float) -> tuple[float, float]:
    return (side1 / side2) ** 2, (side1 / side2)


def main() -> None:
    float_range = (2.5, 15.3)
    side1 = get_rand_float_from(float_range)
    side2 = get_rand_float_from(float_range)
    area_ratio, circum_ratio = get_areas_and_circumference_ratio(side1, side2)
    print(f'Area ratio: {area_ratio}, circumference ratio: {circum_ratio}')


main()
