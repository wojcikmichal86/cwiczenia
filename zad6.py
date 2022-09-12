def get_int_from_user(message: str) -> int:
    return int(input(f'{message}:\n'))


def get_int_until_their_product_is_bigger_than(limit: int) -> tuple[int, int, int]:
    a, b, c = 0, 0, 0
    while a * b * c <= limit or not a < b < c:
        a = get_int_from_user("Provide first number")
        b = get_int_from_user("Provide second number")
        c = get_int_from_user("Provide third number")
    return a, b, c


def return_bigger_range_sum(num1, num2, num3) -> int:
    return max(sum(range(num1, num2+1)), sum(range(num2, num3+1)))


def main():
    limit = 10
    a, b, c = get_int_until_their_product_is_bigger_than(limit)
    print(return_bigger_range_sum(a, b, c))


if __name__ == '__main__':
    main()
