def get_text(message) -> str:
    return input(f'{message}:\n')


def split_(text: str) -> list:
    return text.split(' ')


def count_capital_and_lower_in(split_string: list) -> tuple[int, int]:
    lower_count = 0
    capital_count = 0
    for word in split_string:
        if len(word) == 0:
            pass
        elif word[0].isupper():
            capital_count += 1
        elif word[0].islower():
            lower_count += 1
    return lower_count, capital_count


def main():
    text = get_text("Provide text")
    split_string = split_(text)
    lower, capital = count_capital_and_lower_in(split_string)
    print(f'Number of lowercase words: {lower}, capitalcase: {capital}')


main()
