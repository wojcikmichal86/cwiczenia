def sum_digits(number: int) -> int:
    digit_sum = 0
    for digit in str(number):
        digit_sum += int(digit)
    return digit_sum


def get_number(message: str) -> int:
    return int(input(f'{message}:\n'))


def compare_with_(highest_digit_sum, number) -> int:
    return max(highest_digit_sum, sum_digits(number))


def get_number_until_bigger_than(minimum: int) -> int:
    number = get_number("Please provide a number")
    highest_digit_sum_number = number
    while number <= minimum:
        highest_digit_sum_number = compare_with_(highest_digit_sum_number, number)
        number = get_number("Number not bigger than 100, please provide another number")
    highest_digit_sum_number = compare_with_(highest_digit_sum_number, number)
    return highest_digit_sum_number


def main():
    print(f'The number with the highest sum of digits was: '
          f'{get_number_until_bigger_than(100)}')


if __name__ == '__main__':
    main()