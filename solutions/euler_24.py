"""euler_24.py Problem 24

Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3
and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""

from __future__ import annotations
from itertools import permutations


def main() -> None:
    digits: list[str] = [str(x) for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    lexicographic_permutation: list[str] = [x for _, x in enumerate(permutations(''.join(digits)))]
    target: int = 1000000
    millionth: str = ', '.join(lexicographic_permutation[target])

    print(f"The millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9 is {millionth},")


if __name__ == "__main__":
    main()
