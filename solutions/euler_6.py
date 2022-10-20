"""euler_6.py Problem 6

Sum square difference

The sum of the squares of the first ten natural numbers is 1^2 + 2^2 ...  + 10^2 = 385.

The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10) ^2 = 3025.

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

natural_numbers = []
square_numbers = []

def main():
    difference = natural_sum_squared = square_sum = 0
    statement: str = ''
    
    for number in range(0,20):
        current_number: int = number + 1
        natural_numbers.append(current_number)
        square_numbers.append(current_number ** 2)
        
    else:
        natural_sum = sum(natural_numbers)
        natural_sum_squared = natural_sum ** 2
        square_sum = sum(square_numbers)

        difference =  natural_sum_squared - square_sum
        
        statement = "The difference between the sum of the squares of the first one hundred natural numbers and the " + \
            f"square of the sum ia {natural_sum_squared} - {square_sum} = {difference}."
        print(statement)
        

if __name__ == "__main__":
    main()
