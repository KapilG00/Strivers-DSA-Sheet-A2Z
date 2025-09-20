from typing import List
import math


# Brute-force approach
# TC -> O(max(arr)*n)
# SC -> O(1)
def smallest_divisor_given_threshold(arr: List[int], threshold: int) -> int:
    n = len(arr)

    for i in range(1, max(arr)+1):
        sum = 0
        for j in range(n):
            current_value_after_division = math.ceil(arr[j]/i)
            sum += current_value_after_division
        if sum <= threshold:
            return i
    return -1        

# Optimal approach
# TC -> O(log(max(arr))*n)
# SC -> O(1)
def sum_of_divisors(arr: List[int], current_divisor: int) -> int:
    n = len(arr)
    sum = 0

    for i in range(n):
        current_value_after_division = math.ceil(arr[i]/current_divisor)
        sum += current_value_after_division
    return sum

def smallest_divisor_given_threshold(arr: List[int], threshold: int) -> int:
    low, high = 1, max(arr)

    while low <= high:
        mid = (low+high) // 2
        if sum_of_divisors(arr, mid) <= threshold:
            high = mid-1
        else:
            low = mid+1
    return low            


if __name__ == "__main__":
    print(smallest_divisor_given_threshold([1,2,3,4,5], 8))
    print(smallest_divisor_given_threshold([8,4,2,3], 10))
    print(smallest_divisor_given_threshold([1,2,5,9], 7))