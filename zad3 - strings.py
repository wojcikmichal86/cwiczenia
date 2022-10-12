import re


def get_text_from_user(message: str) -> str:
    return input(f'{message}:\n')


def count_regex_in(text: str, regex: str) -> int:
    return re.subn(regex, '', text)[1]


def main():
    text = get_text_from_user('Please provide a string')
    lower_count = count_regex_in(text, r'[a-z]')
    upper_count = count_regex_in(text, r'[A-Z]')
    digit_count = count_regex_in(text, r'[0-9]')
    print(f'Number of lower cases: {lower_count}, upper case: {upper_count} and digits: {digit_count}')


main()
