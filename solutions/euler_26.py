"""euler_26.py Problem 26

Reciprocal cycles

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10
are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring
cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""

from __future__ import annotations, division


def calculate_sequence_length(number: int) -> int:
    remainders_found: dict[int, int] = {}
    value: int = 1
    sequence_length: int = 0

    for _, position in enumerate(range(1, number)):
        value *= 10
        quotient, remainder = divmod(value, number)

        # No Recurring Remainder.
        if remainder == 0:
            break

        # Recurring digit found in remainder.
        elif (found_position := remainders_found.get(quotient, None)) is not None:
            sequence_length = position - found_position
            break

        # Still processing.
        else:
            value = remainder
            remainders_found[quotient] = position

    return sequence_length


def main() -> None:
    _start: int = 9
    _target: int = 1000
    sequence_lengths: dict[int, int] = {}

    for _, denominator in enumerate(range(_start, _target)):
        sequence_lengths[denominator] = calculate_sequence_length(denominator)  # Add to container Data Structure.

    max_value = max(sequence_lengths, key=sequence_lengths.get)  # Find the maximum

    # Print the results.
    print(f"The value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part is "
          f"{max_value} with a recurring cycle of {sequence_lengths.get(max_value)} digits.")


if __name__ == "__main__":
    main()
