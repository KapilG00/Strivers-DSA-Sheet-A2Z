from typing import List


# TC -> O(logn)
# SC -> O(1)
def search_insert_position(arr: List[int], target: int) -> int:
    n = len(arr)
    low = 0
    high = n-1
    idx = n

    while low <= high:
        mid = (low+high)//2

        if arr[mid] >= target:
            high = mid-1
            idx = mid
        else:
            low = mid+1
    return idx


if __name__ == "__main__":
    print(search_insert_position([1,2,4,7], 6))
    print(search_insert_position([1,2,4,7], 2))
    print(search_insert_position([1,2,4,7], 8))