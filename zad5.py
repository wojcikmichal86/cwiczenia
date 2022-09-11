def get_int_from_user(message: str) -> int:
    return int(input(f'{message}:\n'))


def display_all_powers_of_2_lesser_than_number_minus(difference: int, number: int) -> None:
    power = 0
    while 2**power <= number - difference:
        print(2**power)
        power += 1
    return None


def main():
    display_all_powers_of_2_lesser_than_number_minus(5, get_int_from_user("Provide a number"))


if __name__ == '__main__':
    main()
