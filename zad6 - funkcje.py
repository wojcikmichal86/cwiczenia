from typing import Final


def count_elements_in_array_higher_than(number: int, int_array: list[int]) -> int:
    return len([el for el in int_array if el > number])


def main():
    INT_ARRAY: Final = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    NUMBER: Final = 5
    print(count_elements_in_array_higher_than(NUMBER, INT_ARRAY))


if __name__ == '__main__':
    main()