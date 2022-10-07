import re


def get_uppercase_only_input(message: str) -> str:
    while not re.match('^[A-Z]+$', text := input(f'{message}: \n')):
        pass
    return text


def count_odd_ascii_code_for(text: str):
    counter = 0
    for char in text:
        if ord(char) % 2 != 0:
            counter += 1
    return counter


def sum_ascii_of_even_indexes_in(text : str) -> int:
    ascii_sum = 0
    for i in range(len(text)):
        if i % 2 == 0:
            ascii_sum += ord(text[i])
    return ascii_sum


def find_first_divisor_from(int_range: tuple[int, int], number) -> int:
    r_min, r_max = int_range
    for i in range(r_min, r_max):
        if number % i == 0:
            return i
    return 65


def count_chars_bigger_than_(ascii_code: int, text: str) -> int:
    counter = 0
    for ch in text:
        if ch > chr(ascii_code):
            counter += 1
    return counter


def main():
    text = get_uppercase_only_input("Please provide uppercase only text")
    odd_ascii_count = count_odd_ascii_code_for(text)
    print(f'Number of odd ascii chars: {odd_ascii_count}')
    ascii_sum = sum_ascii_of_even_indexes_in(text)
    print(f'The sum of ascii codes of chars with even indexes is: {ascii_sum}')
    first_div = find_first_divisor_from((65, 91), ascii_sum)
    chars_bigger_than = count_chars_bigger_than_(first_div, text)
    print(f'Number of chars bigger than first divisor ({first_div}) is: {chars_bigger_than}')


main()



