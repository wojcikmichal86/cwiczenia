def get_number_from_user(message: str) -> int:
    while not (number := input(f'{message}:\n')).isdecimal():
        print("Please provide a number")
    return int(number)


def get_text_from_user(message: str) -> str:
    return input(f'{message}:\n')


def multiply_character_in_(text: str, char: str, number: int) -> str:
    return text.replace(char, char*number)


def main():
    text = get_text_from_user("Please provide a text")
    multiplied_character = get_text_from_user("Please provide a character that you want multiplied")
    multiply_count = get_number_from_user("Please provide a number of times the character should be multiplied")
    print(multiply_character_in_(text, multiplied_character, multiply_count))


main()
