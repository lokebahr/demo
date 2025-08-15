from typing import Union


def factorial(n: Union[int, float, str, None]) -> int:
    """Calculate the factorial of a positive integer n."""
    if not isinstance(n, int) or n < 0:
        raise TypeError("Input must be a non-negative integer.")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(5))