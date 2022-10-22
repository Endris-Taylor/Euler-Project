"""euler_10.py Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from math import sqrt

def is_prime_number(num: int) -> bool:
    
    if num in [1,2,3]:
        return True
    
    for _, i in enumerate(range(2, int(sqrt(num)) + 1)):
        if (num % i) == 0:
            return False
    return True


def main():
    _limit: int = 2000000
    primes: list[int] = []
    prime_sum: int = None
    
    for _, number in enumerate(range(1,_limit)):
        if is_prime_number(num=number):
            primes.append(number)

    else:
        prime_sum = sum(primes)
        print(f"The sum of all the primes below two million is {prime_sum}.")
        
        # equation = " + ".join(map(str,primes))
        # print(f"The sum of all the primes below two million is {equation} = {prime_sum}.")


if __name__ == "__main__":
    main()
