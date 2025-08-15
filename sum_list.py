
from typing import Iterable

def sum_list(nums: Iterable[float]) -> float:
    return sum(nums)

if __name__ == "__main__":
    print(sum_list([1, 2, 3]))       
    print(sum_list([]))              
    print(sum_list([0.5, 0.5, 1]))   
