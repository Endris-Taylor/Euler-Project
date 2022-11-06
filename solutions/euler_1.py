"""euler_1.py Problem 1

Multiples of 3 or 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""


def main():
    multiples: list(int) = []
    sum_of_integers: int = None
    
    for integer in range(1,1000):
        if (integer%3 == 0) or (integer%5 == 0):
            multiples.append(integer)
    else:
        sum_of_integers = sum(multiples)
        print(f"The sum of all the multiples of 3 or 5 below 1000 is {sum_of_integers}")


if __name__ == "__main__":
    main()
    