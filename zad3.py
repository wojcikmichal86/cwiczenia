from random import randint


def get_highest_number_on(position: int) -> tuple[int, tuple[int, int, int]]:

    def get_digit_on(number: int) -> int:
        return (abs(number) // 10 ** position) % 10

    def get_rand_int():
        return randint(100, 999)

    number1 = get_rand_int()
    number2 = get_rand_int()
    if get_digit_on(number1) > get_digit_on(number2):
        highest_digit_number = number1
    else:
        highest_digit_number = number2
    number3 = get_rand_int()
    if get_digit_on(number3) > get_digit_on(highest_digit_number):
        highest_digit_number = number3
    return highest_digit_number, (number1, number2, number3)


def main():
    print(get_highest_number_on(3))


if __name__ == '__main__':
    main()


