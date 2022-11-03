def count_solutions_of_squared_polynomial(a: float, b: float, c: float) -> int:
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        return 0
    if delta == 0:
        return 1
    return 2


def main():
    print(count_solutions_of_squared_polynomial(3.0, 2.7, -6.9))


main()
