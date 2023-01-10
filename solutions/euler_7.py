"""euler_7.py Problem 7

10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from common import is_prime_number

from math import sqrt


def main():
    
    limit: int = 10001
    count, number = 0, 1
    primes: list = []
    prime: int
    
    while count < limit:
        if number in [1, 2, 3]:
            primes.append(number)
            count += 1
        elif is_prime_number(num=number):
            primes.append(number)
            count += 1
        
        number += 1
        
    else:
        prime = primes[-1]
        
        print (f"The 10001st prime number is {prime}")


if __name__ == "__main__":
    main()