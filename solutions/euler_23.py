"""euler_23.py Problem 23

Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if
this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
hough it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less
than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""


from typing import Generator

from common import get_divisors


def is_abundant(number: int) -> bool:
    # divisors = [x for x in get_divisors(number)]
    divisors: list[int] = list(get_divisors(number))
    sum_of_divisors: int = sum(divisors)
    return True if sum_of_divisors > number else False


def main() -> None:
    lower_limit: int = 12
    upper_limit: int = 28123
    abundant_number_list: list[int] = [number for _, number in
                                       enumerate(range(lower_limit, upper_limit)) if is_abundant(number)]
    non_abundant_numbers: list[int] = []
    abundant_sums: set = set([])
    non_abundant_sum: int = 0

    for index, left in enumerate(abundant_number_list):
        for _, right in enumerate(abundant_number_list[index + 1:]):
            if (temp_sum := left + right) <= upper_limit:
                abundant_sums.add(temp_sum)

    non_abundant_numbers = [num for _, num in enumerate(range(lower_limit, upper_limit)) if num not in abundant_sums]
    non_abundant_sum = sum(non_abundant_numbers)

    print(f"The sum of all the positive integers which cannot be written as the sum of two abundant numbers is"
          f" {non_abundant_sum}")


if __name__ == "__main__":
    main()
