from typing import List


# Brute-force approach
# TC -> O(n)
# SC -> O(1)
def kth_missing_positive_number(arr: List[int], k: int) -> int:
    n = len(arr)

    for i in range(n):
        if arr[i] <= k:
            k += 1
        else:
            return k
    return -1

# Optimal approach
# TC -> O(logn)
# SC -> O(1)
def kth_missing_positive_number(arr: List[int], k: int) -> int:
    n = len(arr)
    low, high = 0, n-1

    while low <= high:
        mid = (low+high) // 2
        count_of_missing_numbers = arr[mid] - (mid+1)

        if count_of_missing_numbers < k:
            low = mid+1
        else:
            high = mid-1
    return low+k             


"""
Derivation of the formula when 'low' crosses 'high' because at that point 'high' and 'mid' will be at same location.

answer = arr[high] + more
more = k - count_of_missing_numbers

answer = arr[high] + (k - count_of_missing_numbers)
answer = arr[high] + (k - (arr[high] - (high + 1)))
answer = arr[high] + k - arr[high] + high + 1
answer = k + high + 1
answer = k + low
"""


if __name__ == "__main__":
    print(kth_missing_positive_number([4,7,9,10], 1))
    print(kth_missing_positive_number([4,7,9,10], 4))
    print(kth_missing_positive_number([4,7,9,10], 5))