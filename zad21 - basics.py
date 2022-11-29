def get_int_from_user(message: str) -> int:
    while True:
        number = input(f"{message}:\n")
        if number.isdecimal():
            return int(number)
        print("The value provided is not correct")


def iter_factorial_of(number: int) -> int:
    result = 1
    for i in range(1, number+1):
        result = result * i
    return result


def recur_factorial_of(number: int) -> int:
    if number <= 1:
        return 1
    return recur_factorial_of(number - 1) * number


def main():
    number = get_int_from_user("Please provide a positive integer")
    print(iter_factorial_of(number))
    print(recur_factorial_of(number))


if __name__ == '__main__':
    main()
