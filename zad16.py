def fizzbuzz(number: int) -> str:
    match number % 3 == 0, number % 5 == 0:
        case True, True: return "FizzBuzz"
        case True, False: return "Fizz"
        case False, True: return "Buzz"
        case False, False: return str(number)


def main() -> None:
    for i in range(1, 101):
        print(fizzbuzz(i))


main()
