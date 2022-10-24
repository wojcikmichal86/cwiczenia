def is_code_sum_even_in(text: str) -> bool:
    code_sum = 0
    for c in text:
        code_sum += ord(c)
    return code_sum % 2 == 0


def is_palindrome(text: str) -> bool:
    return text == text[::-1]


def get_palindrome_with_even_code_sum(message: str) -> str:
    while True:
        text = input(f"{message}:\n")
        if is_code_sum_even_in(text) and is_palindrome(text):
            return text


def replace_vowels_with_consonant(text: str) -> str:
    result = []
    for c in text:
        if c in "aeiouyAEIOUY":
            c = chr(ord(c)+1)
        result.append(c)
    return ''.join(result)


def main():
    text = get_palindrome_with_even_code_sum("Provide a palindrome with even sum of codes")
    print(replace_vowels_with_consonant(text))


main()
