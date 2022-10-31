import re


def control_sum_correct(pesel: str) -> bool:
    pl = [int(c) for c in pesel]
    multipliers = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    control_sum = 0
    for i in range(len(multipliers)):
        control_sum += multipliers[i] * pl[i]
    return 10 - (control_sum % 10) == int(pl[-1])


def pesel_is_valid(pesel: str) -> bool:
    if not re.match(r'^[0-9]{11}$', pesel):
        return False
    elif not control_sum_correct(pesel):
        return False
    elif not 0 < int(pesel[2:4]) < 13:
        return False
    elif not 0 < int(pesel[4:6]) < 31:
        return False
    return True


def get_valid_pesel(message: str) -> str:
    while not pesel_is_valid(pesel := input(f'{message}:\n')):
        print("The PESEL provided is not valid")
    return pesel


def main():
    print(get_valid_pesel("Please provide a valid PESEL"))


main()
