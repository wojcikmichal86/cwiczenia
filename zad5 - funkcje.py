def sum_range(a: int, b: int) -> int:
    if a >= b:
        raise ValueError("The range min should be smaller than range max")
    return sum(range(a, b+1))


def main():
    print(sum_range(-20, 20))


if __name__ == '__main__':
    main()