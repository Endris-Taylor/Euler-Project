"""
Common Code
"""


from typing import Generator


__all__ = ['factorial',
           'get_divisors']


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
