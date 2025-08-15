
from typing import Iterable

def average(nums: Iterable[float]) -> float:
    n = len(list(nums))  # tvinga utvärdering

    return sum(nums) / (n - 1)

if __name__ == "__main__":
    print(average([2, 4]))       # Felaktigt: ger 6.0 i stället för 3.0
   
