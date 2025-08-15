from typing import Iterable, Union

def average(nums: Iterable[Union[int, float]]) -> float:
    """
    Calculate the average of a list of numbers.

    :param nums: An iterable of numbers (integers or floats)
    :return: The average of the numbers. If the list is empty, returns 0.
    """
    num_list = list(nums)
    n = len(num_list)
    if n == 0:
        return 0.0  # Gracefully handle empty lists by returning 0
    return sum(num_list) / n

if __name__ == "__main__":
    print(average([2, 4]))  # Corrected: should give 3.0 now