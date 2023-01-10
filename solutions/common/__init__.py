"""
Common Code
"""


from typing import Generator

from math import sqrt


__all__ = ['factorial',
           'get_divisors',
           'is_prime_number']


def factorial(number: int) -> int:
    result: int = 1

    for _, num in enumerate(range(1, number + 1)):
        result *= num

    return result


def get_divisors(value: int) -> Generator[int, None, None]:
    # [(yield num) for _, num in enumerate(range(1, (value // 2) + 1)) if value % num == 0]
    for _, num in enumerate(range(1, (value // 2) + 1)):
        if value % num == 0:
            yield num


def is_prime_number(num: int) -> bool:
    if num in [1, 2, 3]:
        return True

    for _, i in enumerate(range(2, int(sqrt(num)) + 1)):
        if (num % i) == 0:
            return False
    return True
