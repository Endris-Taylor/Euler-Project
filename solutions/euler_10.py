"""euler_10.py Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from common import is_prime_number
from __future__ import annotations  # For Type Hints.
from math import sqrt


def main():
    _limit: int = 2000000
    primes: list[int] = []

    for _, number in enumerate(range(1, _limit)):
        if is_prime_number(num=number):
            primes.append(number)

    else:
        prime_sum: int = sum(primes)
        print(f"The sum of all the primes below two million is {prime_sum}.")
        
        # equation = " + ".join(map(str,primes))
        # print(f"The sum of all the primes below two million is {equation} = {prime_sum}.")


if __name__ == "__main__":
    main()
