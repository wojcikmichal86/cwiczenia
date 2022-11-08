def check_if_triangle_is_right(side1: float, side2: float, side3: float) -> bool:
    longest = max(side1, side2, side3)
    shortest = min(side1, side2, side3)
    middle = (side1 + side2 + side3) - (longest + shortest)
    return longest ** 2 == middle ** 2 + shortest ** 2


def main():
    print(check_if_triangle_is_right(10.0, 8.0, 6.0))


main()
