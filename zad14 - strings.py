import re


def get_all_digits_in(text: str) -> list[..., int]:
    return [int(el) for el in re.findall(r'\d', text)]


def get_text_with_sum_of_digits_bigger_than(minimum: int, message: str) -> str:
    while True:
        text = input(f'{message}:\n')
        if sum(get_all_digits_in(text)) > minimum:
            return text


def check_if_max_digit_divides_by_min_digit_in(text: str) -> bool:
    digits = get_all_digits_in(text)
    return max(digits) % min(digits) == 0


def main():
    text = get_text_with_sum_of_digits_bigger_than(20, 'Provide text with digits number bigger than 20')
    print(check_if_max_digit_divides_by_min_digit_in(text))


main()

