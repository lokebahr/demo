from typing import Iterable

def average(nums: Iterable[float]) -> float:
    n = len(list(nums))  # Force evaluation of any lazy iterables
    if n == 0:
        raise ZeroDivisionError('Cannot compute average of empty iterable')
    return sum(nums) / n

if __name__ == "__main__":
    print(average([2, 4]))  # Correct: gives 3.0