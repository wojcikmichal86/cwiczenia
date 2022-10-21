import re


def get_numbers_from_user(message: str) -> str:
    while not re.match(r"^-?[1-9]*[0-9]*\.?[0-9]*[Ee]?-?[0-9]*$", number := input(f'{message}:\n')):
        print("Please provide a number")
    return number


def main():
    number = get_numbers_from_user("Please provide a number")
    print(number)


main()
