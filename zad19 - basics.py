def get_int_from_user(message: str) -> int:
    while True:
        number = input(f"{message}:\n")
        if number.isdecimal():
            return int(number)
        print("The value provided is not correct")


def iter_fibo_of_length(n: int) -> list[int]:
    result = [0, 1]
    for i in range(2, n):
        result.append(result[-2] + result[-1])
    return result[:n]


def recur_fibo_of_length(n: int) -> list[int]:
    result = [0, 1]
    while n > 2:
        base = recur_fibo_of_length(n-1)
        return base + [(base[-2] + base[-1])]
    return result[:n]


def main():
    number = get_int_from_user("Please provide a not negative integer")
    print(iter_fibo_of_length(number))
    print(recur_fibo_of_length(number))


if __name__ == '__main__':
    main()
