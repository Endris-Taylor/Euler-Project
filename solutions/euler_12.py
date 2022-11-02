"""euler_12.py Problem 12
Highly divisible triangular number

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

def get_factors(num: int) -> list:
    factors: list[int] = []

    for _, i in enumerate(range(num,0,-1)):
        if (num % i) == 0:
            factors.insert(0,i)

    return factors


# dictionary with a list as value(s). The n value in the values list is also the key of that value in the resulting dictionary


def main():
    results: dict[int, list[int]] = {}
    divisor_limit: int = 500
    num_limit: int = 1000000
    number_found: int = None
    triangle_total: int = 0
    
    # TODO: Tracking triangles?
    for _, number in enumerate(range(1,num_limit)):
        triangle_total += number
        temp = get_factors(num=number)
        # results.update({number: temp})
        results[number] = temp
        
        if len(temp) >= divisor_limit or number == num_limit:
            number_found = number
            break
        else:
            print(f"Not {number}")
    else:
        print(f"The first triangle number to have over five hundred divisors is {number_found}.\n")
        # print(f"{number_found}: {results[number_found]}")


if __name__ == "__main__":
    main()
