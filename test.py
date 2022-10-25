# 1. Napisz funkcję, która przyjmie wiek osoby, a następnie zwróci informację o tym, czy jest pełnoletnia czy nie.
def check_adult(age):
    if age >= 18:
        return "Pełnoletni"
    return "Niepełnoletni"


print(check_adult(34)) # Pełnoletni
print(check_adult(17)) # Niepełnoletni


# 2. Napisz funkcję, która zwraca listę wszystkich podzielnych przez n liczb z zakresu [1, 100].
def divisible(n):
    return [i for i in range(n, 101, n)]


print(divisible(3)) # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
print(divisible(5)) # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
print(divisible(8)) # [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]


# 3. Napisz funkcję, która przyjmuje kwotę (value) i jej walutę (currency), a następnie zwróci ile wart jest dana kwota w danej walucie w złotówkach.
rates = [
    {
        "currency": "USD",
        "value": 4.56
    },{
        "currency": "CHF",
        "value": 5.03
    },{
        "currency": "EUR",
        "value": 4.9
    }
]

def check_currency(value, currency):
    for rate in rates:
        if rate['currency'] == currency:
            result = round(rate['value'] * value, 2)
            return f'{result} zł'


print(check_currency(745, "CHF")) # 3747,35 zł
print(check_currency(812.5, "USD")) # 3705 zł
print(check_currency(18, "EUR")) # 88,2 zł