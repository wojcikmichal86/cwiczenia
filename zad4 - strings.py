def get_text_with_even_number_of_chars(message: str) -> str:
    while len(text := input(f'{message}:\n')) % 2:
        print('The number of characters should be even')
    return text


def swap_chars_in(text: str) -> str:
    s = []
    even_chars = text[0::2]
    odd_chars = text[1::2]
    for i in range(len(even_chars)):
        s.append(odd_chars[i])
        s.append(even_chars[i])
    return ''.join(s)


def main():
    text = get_text_with_even_number_of_chars("Please provide a text with an even number of characters")
    print(swap_chars_in(text))


main()
