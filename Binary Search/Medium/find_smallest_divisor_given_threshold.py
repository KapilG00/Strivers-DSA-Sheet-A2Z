from typing import List
import math


# Brute-force  
# TC: O(max(arr)) * O(n)
# SC: O(1)    
def find_smallest_divisor_given_threshold(arr: List[int], limit: int) -> int:
    n = len(arr)

    for i in range(1, max(arr)+1):
        current_smallest_divisor = 0
        for j in range(n):
            current_smallest_divisor += math.ceil(arr[j]/i)

        if current_smallest_divisor <= limit:
            return i

    return -1        

def calculate_sum_of_divisions(arr: List[int], current_divisor: int) -> int:
    current_divisor_sum = 0
    n = len(arr)

    for j in range(n):
        current_divisor_sum += math.ceil(arr[j]/current_divisor)

    return current_divisor_sum

# Optimal  
# TC: O(log(max(arr))) * O(n)
# SC: O(1)    
def find_smallest_divisor_given_threshold(arr: List[int], limit: int) -> int:
    low = 1
    high = max(arr)
    smallest_divisor = 0

    while low <= high:
        mid = (low+high)//2

        current_divisor_sum = calculate_sum_of_divisions(arr, mid)

        if current_divisor_sum <= limit:
            smallest_divisor = mid
            high = mid-1
        else:
            low = mid+1

    return smallest_divisor        



if __name__ == "__main__":
    print(find_smallest_divisor_given_threshold([1,2,3,4,5], 8))
    print(find_smallest_divisor_given_threshold([8,4,2,3], 10))