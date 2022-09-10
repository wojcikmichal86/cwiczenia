def get_float_number_from_user(message: str) -> float:
    return float(input(f'{message}:\n'))


def get_triangle_sides() -> tuple[float, float]:
    side1 = get_float_number_from_user('Enter first side')
    side2 = get_float_number_from_user('Enter second side')
    return side1, side2


def get_areas_ratio(side1: float, side2: float) -> float:
    if side1 <= 0:
        raise ValueError('First side must be positive')
    if side2 <= 0:
        raise ValueError('Second side must be positive')
    return (side1 / side2) ** 2


def main() -> None:
    side1 = get_float_number_from_user('Enter first side')
    side2 = get_float_number_from_user('Enter first side')
    print(get_areas_ratio(side1, side2))


if __name__ == '__main__':
    main()








