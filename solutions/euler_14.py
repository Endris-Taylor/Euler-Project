"""euler_14.py Problem 14
Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
from __future__ import annotations  # For Type Hints.

from textwrap import fill


def process_even_number(num: int):
    return num // 2


def process_odd_number(num: int):
    return (3 * num) + 1


def main():
    
    num_limit: int = 1000000
    maximum: list[int] = []
    longest_chain: int = 0
    longest_chain_str: str = None
    
    for _, number in enumerate(range(num_limit, 0, -1)):
        current_number = number
        current_sequence:  list[int] = [number]
        
        while current_number != 1:
            temp: int = None
            
            if current_number % 2 == 0:
                temp = process_even_number(current_number)
            else:
                temp = process_odd_number(current_number)
            
            current_sequence.append(temp)
            current_number = temp
            
        if len(current_sequence) > len(maximum):
            maximum = current_sequence

    longest_chain = maximum[0]
    longest_chain_str = ' -> '.join([str(x) for _, x in enumerate(maximum)])
    print(f'The starting number, under one million, that produces the longest chain is {longest_chain}.')
    print('The chain is as follows: ')
    print(fill(longest_chain_str, 160))


if __name__ == "__main__":
    main()
