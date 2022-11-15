from typing import Final


def find_nth_biggest_int(n: int, int_array: list[int]) -> int:
    sorted_array = sorted(set(int_array))
    return sorted_array[-n]


def main():
    INT_ARRAY: Final = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
    N: Final = 3
    print(find_nth_biggest_int(N, INT_ARRAY))


if __name__ == '__main__':
    main()