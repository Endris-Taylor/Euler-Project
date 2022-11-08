"""euler_16.py Problem 16

Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


from textwrap import fill


def main():
    number, power = 2, 1000
    result: int = number ** power
    result_sum: int = sum([int(num) for num in str(result)])
    equation: str = " + ".join(num for num in str(result))
    output: str = f"{number}^{power} = {result} and the sun of its digits is {equation} = {result_sum}"

    print(fill(output, 160))


if __name__ == "__main__":
    main()
