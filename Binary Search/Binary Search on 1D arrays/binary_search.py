from typing import List


# TC -> O(logn)
# SC -> O(1)
# Iterative approach
def binary_search(arr: List[int], target: int) -> int:
    n = len(arr)
    low = 0
    high = n-1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            high = mid-1
        elif arr[mid] < target:
            low = mid+1
        else:
            return mid
    return -1     

# TC -> O(logn)
# SC -> O(1)
# Recursive approach
def binary_search(arr: List[int], low: int, high: int, target: int) -> int:
    if low > high:
        return -1
    
    mid = (low+high) // 2
    if arr[mid] > target:
        return binary_search(arr, low, mid-1, target)
    elif arr[mid] < target:
        return binary_search(arr, mid+1, high, target)
    else:
        return mid

def search(arr: List[int], target: int) -> int:
    return binary_search(arr, 0, len(arr)-1, target)


if __name__ == "__main__":
    print(binary_search([3,4,6,7,9,12,16,17], 6))   # for iterative solution
    print(search([3,4,6,7,9,12,16,17], 6))   # for recursive solution