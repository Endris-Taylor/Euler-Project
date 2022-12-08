"""euler_21.py Problem 21

Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""


from __future__ import annotations  # For Type Hints.

from common import get_divisors


def get_sum_of_divisors(number: int) -> int:
    divisors: list[int] = list(get_divisors(number))
    sum_of_divisors: int = 0

    """ Test ... 
    for _, potential in enumerate(range(1, number)):
        if number % potential == 0:
            divisors.append(potential)"""

    if len(divisors) > 0:
        sum_of_divisors = sum(divisors)
        # get_sum_of_divisors.divisors = divisors

    return sum_of_divisors


def main() -> None:
    target_number: int = 10000
    amicable_numbers: list[int] = []
    sum_of_amicable_numbers: int = 0

    for _, num in enumerate(range(1, target_number)):
        if num not in amicable_numbers:  # No double calculations.
            potential_pair_num = get_sum_of_divisors(number=num)

            if potential_pair_num != 0 and num == get_sum_of_divisors(potential_pair_num) and num != potential_pair_num:
                amicable_numbers.append(num)
                amicable_numbers.append(potential_pair_num)

    sum_of_amicable_numbers = sum(amicable_numbers)
    print(f"The sum of all the amicable numbers under 10000 is {sum_of_amicable_numbers}")


if __name__ == "__main__":
    main()
