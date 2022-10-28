import re
import typing


def get_three_texts(message1: str, message2: str, message3: str) -> tuple[str, str, str]:
    while True:
        text1 = input(f'{message1}:\n')
        text2 = input(f'{message2}:\n')
        text3 = input(f'{message3}:\n')
        if ((fits_regex(text1, r'^[a-z]+$')
             and fits_regex(text2, r'^[A-Z]+$')
             and len(text3) % 2 == 0
             and equal_number_of_consonants_and_vowels_in(text3))):
            return text1, text2, text3


def get_vowels_only(text: str) -> list[..., str]:
    return [c for c in text if c in 'aeiouyAEIOUY']


def get_consonants_only(text: str) -> list[..., str]:
    return [c for c in text if c.isalpha() and c not in 'aeiouyAEIOUY']


def equal_number_of_consonants_and_vowels_in(text: str) -> bool:
    return len(get_consonants_only(text)) == len(get_vowels_only(text))


def fits_regex(text: str, regex: str) -> bool:
    return bool(re.match(regex, text))


def transform_texts(text1: str, text2: str, text3: str) -> tuple[..., str]:
    text1 = text1 + ''.join(get_vowels_only(text3))
    text2 = ''.join(get_consonants_only(text3)) + text2
    return text1, text2


def find_text_with_most_vowels(text1: str, text2: str, text3: str) -> str:
    winner = text1
    if len(get_vowels_only(text2)) > len(get_vowels_only(text1)):
        winner = text2
    elif len(get_vowels_only(text3)) > len(get_vowels_only(winner)):
        winner = text3
    return winner


def find_text_with_most(criteria: typing.Callable[[str], list[..., str]], text1: str, text2: str, text3: str) -> str:
    winner = text1
    if len(criteria(text2)) > len(criteria(text1)):
        winner = text2
    elif len(criteria(text3)) > len(criteria(winner)):
        winner = text3
    return winner


def main():
    text1, text2, text3 = get_three_texts("Provide lowercase only text",
                                          "Provide uppercase only text",
                                          "Provide text with equal number "
                                          "of vowels and consonants and even number of characters")
    mod_text1, mod_text2 = transform_texts(text1, text2, text3)
    print(mod_text1, mod_text2, text3)
    most_vowels = find_text_with_most(get_vowels_only, mod_text1, mod_text2, text3)
    most_consonants = find_text_with_most(get_consonants_only, mod_text1, mod_text2, text3)
    print(f'Most vowels: {most_vowels}, most consonants: {most_consonants}')


main()
