from math import sqrt
from random import randint
from typing import Final
import json
import os


def is_prime_erastho(r_max: int) -> dict[int, bool]:
    results = {0: False, 1: False}
    for k in range(2, r_max+1):
        results[k] = True
    for i in range(2, int(sqrt(r_max)) + 1):
        square = i ** 2
        if square > r_max:
            break
        if results[i]:
            for ii in range(square, r_max + 1, i):
                results[ii] = False
    return results


def save_dict_to_file(prime_results: dict[int, bool]) -> None:
    with open('primes.txt', 'w') as file:
        file.write(json.dumps(prime_results))
    print("The file has been saved in primes.txt")


def load_primes(filename: str, r_max: int) -> dict[int, bool]:
    if not os.path.isfile(filename):
        primes = is_prime_erastho(r_max)
        save_dict_to_file(primes)
    with open(filename) as file:
        data = file.read()
    return json.loads(data)


def draw_random_int(r_min: int, r_max: int) -> int:
    if r_min >= r_max:
        raise ValueError("Range min should be lower than range max")
    return randint(r_min, r_max)


def main():
    R_MIN: Final = 10000
    R_MAX: Final = 1000000
    number = draw_random_int(R_MIN, R_MAX)
    primes = load_primes('primes.txt', R_MAX)
    print(number)
    print(primes[str(number)])


if __name__ == '__main__':
    main()