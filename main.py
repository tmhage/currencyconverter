from typing import Callable, Union
import requests
import json


class InvalidInputException(Exception):
    """Raised for invalid input"""
    pass


class InvalidCoinException(InvalidInputException):
    """Raised if the number input is invalid"""
    pass


class InvalidRateException(InvalidInputException):
    pass


def validate_number(number: float) -> None:
    if number < 0.10:
        raise InvalidCoinException("Amount of coins has to be at least 0.10")


def validate_rate_amount(number: float) -> None:
    if number < 0.01:
        raise InvalidRateException("Exchange rate has to be at least 0.01")


def get_validated_input(prompt: str, validation_func: Callable[[str], any]) -> any:
    while True:
        user_input = input(prompt)
        try:
            value = validation_func(user_input)
            return value
        except InvalidInputException as e:
            print(e)


def get_coin_amount() -> float:
    def validate_coin_amount(input_str: str) -> float:
        try:
            value = float(input_str)
            validate_number(value)
            return value
        except ValueError:
            raise InvalidCoinException("This is not a number")

    prompt_msg = ''
    return get_validated_input(prompt_msg, validate_coin_amount)


def get_exchange_rate() -> float:
    def validate_exchange_rate(input_str: str) -> float:
        try:
            value = float(input_str)
            validate_rate_amount(value)
            return value
        except ValueError:
            raise InvalidRateException("This is not a number")
    prompt_msg = 'Please, enter the exchange rate: '
    return get_validated_input(prompt_msg, validate_exchange_rate)


def calculated_amount(coins: float, rate: float) -> float:
    return round(coins * rate, 2)


def request_exchange_rates(currency: str) -> dict:
    url = 'http://www.floatrates.com/daily/{}.json'.format(currency)
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as error:
        print(error)


def main():
    cached = {}
    currency = input().lower()
    rates = request_exchange_rates(currency)

    for initial_currency in ['usd', 'eur']:
        if currency not in cached and initial_currency in rates:
            cached.update({initial_currency: rates[initial_currency]['rate']})

    while True:
        convert_to = input().lower()
        if convert_to == "":
            break
        amount = float(input())
        print("Checking the cache...")
        if convert_to in cached:
            print('Oh! It is in the cache!')
            calc = calculated_amount(amount, cached[convert_to])
            print('You received {} {}'.format(calc, convert_to.upper()))
        else:
            print('Sorry, but it is not in the cache!')
            rate_dict = request_exchange_rates(currency)
            cached.update({convert_to: rate_dict[convert_to]['rate']})
            calc = calculated_amount(amount, cached[convert_to])
            print('You received {} {}'.format(calc, convert_to.upper()))


if __name__ == "__main__":
    main()


