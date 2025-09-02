from typing import List


# TC -> O(logn)
# SC -> O(1)
def lower_bound(arr: List[int], target: int) -> int:
    n = len(arr)
    low = 0
    high = n-1
    lower_bound_idx = n

    while low <= high:
        mid = (low+high) // 2
        if arr[mid] >= target:
            lower_bound_idx = mid
            high = mid-1
        else:
            low = mid+1
    return lower_bound_idx        


if __name__ == "__main__":
    print(lower_bound([3,5,8,15,19], 9))
    print(lower_bound([1,2,2,3], 2))