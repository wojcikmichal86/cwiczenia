import re


def replace_consonant_with(char: str, text: str) -> str:
    for c in text:
        if re.match('^[b-z]$', c) and not re.match('^[aeiouy]$', c):
            text = text.replace(c, char)
    return text


def find_first_vowel_in(text: str) -> str:
    for c in text:
        if re.match('^[aeiouy]$', c):
            return c
    return "NIEPRAWIDŁOWE DANE WEJŚCIOWE"


def main():
    text1 = input('Provide first string:\n')
    text2 = input('Provide second string:\n')
    first_vowel = find_first_vowel_in(text2)
    if len(first_vowel) != 1:
        print(first_vowel)
    else:
        modified_text = replace_consonant_with(first_vowel, text1)
        print(modified_text)


main()
