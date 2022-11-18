from typing import Final


def get_max_of_array_with_highest_average(array1: list[int], array2: list[int]) -> int:

    def get_array_average(array: list[int]) -> float:
        if len(array) == 0:
            raise ValueError("The list is empty!")
        return sum(array) / len(array)

    array1_avg = get_array_average(array1)
    array2_avg = get_array_average(array2)
    if array1_avg == array2_avg:
        raise ValueError("Both lists have the same average")
    if array1_avg > array2_avg:
        return max(array1)
    return max(array2)


def main():
    ARRAY1: Final = [1, 2, 3, 4, 5]
    ARRAY2: Final = [21, 1, 1, 1, 1, 1, 1, 1, 1]
    print(get_max_of_array_with_highest_average(ARRAY1, ARRAY2))


if __name__ == '__main__':
    main()

