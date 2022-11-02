import re


def name_valid(name: str) -> bool:
    return bool(re.match(r"^[A-Z]*$", name))


def power_valid(engine: str) -> bool:
    return bool(re.match(r"^\d\.\d$", engine))


def mileage_valid(mileage: str) -> bool:
    if not mileage.isdecimal():
        return False
    return 0 <= int(mileage) <= 500000


def price_valid(price: str) -> bool:
    if not price.isdecimal():
        return False
    return int(price) > 50000


def is_valid(car_info: str) -> bool:
    info = car_info.split("_")
    return (len(info) == 4 and name_valid(info[0]) and power_valid(info[1])
            and mileage_valid(info[2]) and price_valid(info[3]))


def get_valid_car_info(message: str) -> str:
    while not is_valid(car_info := input(f'{message}:\n')):
        print("Car info is not valid")
    return car_info


def main():
    car_info = get_valid_car_info("Provide the car info")
    print(car_info)


main()
