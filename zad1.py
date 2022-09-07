def get_input(message: str) -> float:
    """
    :return: float provided by the user
    """
    return float(input(f'{message}:\n'))


def calculate_polynomial(x: float) -> float:
    """
    :return: float - polynomial W(x) = 2x**12 + 3x**5 − 4x**2.
    """
    return 2 * x ** 12 + 3 * x ** 5 - 4 * x ** 2


def main():
    print(calculate_polynomial(0))
    print(calculate_polynomial(1))
    print(calculate_polynomial(get_input('Enter argument')))


if __name__ == '__main__':
    main()
