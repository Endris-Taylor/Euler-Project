"""euler_5.py Problem 5.

Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. TEST THIS FIRST

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def smallest_multiple(number: int = 0) -> bool:
    multiple: bool = True
    
    for num in range(2,20):
        if (number % num != 0):
            multiple = False
            break;
    
    return multiple

def main():
    smallest_positive: int = 21
    found: bool = False
    
    while not found:
        found = smallest_multiple(smallest_positive)
        
        if not found:
            smallest_positive += 1
    else:
        print(f"The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is {smallest_positive}")


if __name__ == "__main__":
    main()
