"""euler_15.py Problem 15
Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly
6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""


def factorial(number: int) -> int:
    result: int = 1

    for _, num in enumerate(range(1, number + 1)):
        result *= num

    return result


def main() -> None:
    grid_size: int = 20
    numerator: int = factorial(2 * grid_size)
    denominator: int = factorial(grid_size) * factorial(grid_size)
    result: int = int(numerator / denominator)

    print(f"The number of routes through {grid_size}x{grid_size} grid is {result}.")


if __name__ == "__main__":
    main()
