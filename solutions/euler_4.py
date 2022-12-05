"""euler_4.py Problem 4

Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def reverse_number(number: int) -> int:
    return int("".join(reversed(str(number))))


def main():
    left: int = 999
    right: int = 999
    found: bool = False
    product: int = 0
    
    for _, left_cnt in enumerate(range(left, 1, -1)):
        for _, right_cnt in enumerate(range(right, 1, -1)):
            product = left_cnt * right_cnt
            if product == reverse_number(product):
                print(f"The largest palindrome made from the product of two 3-digit numbers is {product} = {left_cnt} * {right_cnt}.")
                found = True
                break
            
        if found:
            break


if __name__ == "__main__":
    main()
