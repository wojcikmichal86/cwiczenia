from typing import Final


def get_slice_of_(text: str, a: int, b: int) -> str:
    while True:
        if len(text) == 0:
            raise ValueError("The string is empty")
        if a not in range(0, len(text)) or b not in range(0, len(text)):
            raise ValueError("Numbers outside of text length")
        if a >= b:
            raise ValueError("Range min should be lower than range max")
        return text[a:b]


def main():
    TEXT: Final = "Wpłynąłem na suchego przestwór oceanu"
    print(get_slice_of_(TEXT, 5, 20))


if __name__ == '__main__':
    main()
