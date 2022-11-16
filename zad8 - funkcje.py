import re
from typing import Final


def get_number_of_vowels_in(text: str) -> int:
    return re.subn('[aeiouyAEIOUY]', '*', text)[1]


def find_string_with_more_vowels(text1: str, text2: str) -> str:
    if get_number_of_vowels_in(text1) > get_number_of_vowels_in(text2):
        return text1
    return text2


def main():
    TEXT1: Final = "babbba"
    TEXT2: Final =  "asdfasdfasdf"
    print(find_string_with_more_vowels(TEXT1, TEXT2))


if __name__ == '__main__':
    main()
