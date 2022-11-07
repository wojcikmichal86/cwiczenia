def find_max_of_three(num1: float, num2: float, num3: float) -> float:
    result = num1
    if num2 > result:
        result = num2
    if num3 > result:
        result = num3
    return result


def main():
    a, b, c = 15.6, 3.7, 15.6
    print(find_max_of_three(a, b, c))


main()
