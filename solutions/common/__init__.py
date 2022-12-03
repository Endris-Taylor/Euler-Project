"""
Common Code
"""

__all__ = ['factorial']


def factorial(number: int) -> int:
    result: int = 1

    for _, num in enumerate(range(1, number + 1)):
        result *= num

    return result
