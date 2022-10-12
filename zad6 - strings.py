import re


def count_letters_in(text: str) -> int:
    return re.subn(r'[a-zA-Z]', '', text)[1]


def modify_codes_in(text: str) -> str:
    result = []
    for i in range(0, len(text), 2):
        result.append(chr(ord(text[i])+10))
    for j in range(1, len(text), 2):
        result.append(chr(ord(text[j])-5))
    return ''.join(result)


def get_text_from_user(message: str) -> str:
    return input(f'{message}:\n')


def main():
    text = get_text_from_user("Provide a text")
    modified_text = modify_codes_in(text)
    print(count_letters_in(modified_text))


main()
