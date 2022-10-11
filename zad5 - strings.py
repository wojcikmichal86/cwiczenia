import re


def get_vowels_from(text: str) -> str:
    return ''.join((re.findall(r'[aeiouyAEIOUY]', text)))


def get_consonants_from(text: str) -> str:
    chars = []
    for c in text:
        chars.append(c if c.isalpha() and c not in 'aeyuioAEYUIO' else '')
    return ''.join(chars)


def get_text_from_user(message: str) -> str:
    return input(f'{message}:\n')


def main():
    text1 = get_text_from_user("Provide the first text")
    text2 = get_text_from_user("Provide the second text")
    vowels = get_vowels_from(text1)
    consonants = get_consonants_from(text2)
    print(vowels+consonants)


main()