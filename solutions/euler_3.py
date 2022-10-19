"""euler_3.py Problem 3

Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from math import sqrt

def is_prime_number(num: int) -> bool:
    for i in range(2, int(sqrt(num)) + 1):
        if (num % i) == 0:
            return False
    return True
    
def main():
    target: int = 231950000 # 600851475143
    
    for i in reversed(range(2,target//2)):
        if target % i == 0:
            if is_prime_number(i):
                print(f"Largest Prime Factor of the number {target} is {i}")
                break
    

if __name__ == "__main__":
    main()
                