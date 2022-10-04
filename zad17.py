def get_int_from_user(message: str) -> int:
    while number := input(message).isdigit() is False:
        print('The value provided is not a positive integer')
    return number


def sum_digits_of_(number) -> int:
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    return digit_sum


def main():
    number1 = get_int_from_user("Please provide a positive integer:\n")
    number2 = get_int_from_user("Please provide another positive integer:\n")
    print(max(sum_digits_of_(number1), sum_digits_of_(number2)))


main()

