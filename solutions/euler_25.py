"""euler_25.py Problem 25

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?"""


from __future__ import annotations


def main() -> None:
    fibonacci: list[int] = [1, 1]
    _target_digits: int = 1000
    index: int = None

    while len(str(fibonacci[-1])) < _target_digits:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    index = len(fibonacci)
    print(f"The index of the first term in the Fibonacci sequence to contain 1000 digits is {index}")


if __name__ == "__main__":
    main()
