def get_texts(message1: str, message2: str) -> tuple[str, str]:
    while (len(get_consonants_only(text1 := input(f'{message1}:\n'))) !=
           len(get_vowels_only(text2 := input(f'{message2}:\n')))):
        print("The number of consonants in the first text is not"
              "equal to the number of vowels in the second text")
    return text1, text2


def get_vowels_only(text: str) -> list[..., str]:
    return [c for c in text if c in 'aeiouyAEIOUY']


def get_consonants_only(text: str) -> list[..., str]:
    return [c for c in text if c.isalpha() and c not in 'aeiouyAEIOUY']


def replace_text_vowels_with_(replacers: list[..., str], text: str) -> str:
    for c in text:
        if c in "aeiouyAEIOUY":
            text = text.replace(c, replacers.pop(0))
    return text


def main():
    text1, text2 = get_texts("Provide first text",
                             "Provide second text with the number of vowels "
                             "equal to the number of consonants in the first text")
    result = replace_text_vowels_with_(get_consonants_only(text1), text2)
    print(result)


main()
