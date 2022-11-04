from typing import Final


def swap_case(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("The value provided must be a string")
    return text.swapcase()


def main():
    txt: Final = "ASDFasdf      ___ 3456346 ****** )"
    print(swap_case(txt))


main()
