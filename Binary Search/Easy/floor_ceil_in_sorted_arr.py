from typing import List


def find_floor(arr: List[int], target: int) -> int:
    n = len(arr)
    low = 0
    high = n-1
    floor = 0

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] <= target:
            floor = arr[mid]
            low = mid+1
        else:
            high = mid-1

    return floor        

def find_ceil(arr: List[int], target: int) -> int:
    n = len(arr)
    low = 0
    high = n-1
    ceil = 0

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] >= target:
            ceil = arr[mid]
            high = mid-1
        else:
            low = mid+1

    return ceil        


# TC -> O(logn)
# SC -> O(1)
def func(arr: List[int], target: int) -> tuple[int, int]:
    floor = 0
    ceil = 0

    floor = find_floor(arr, target)
    ceil = find_ceil(arr, target)

    return floor, ceil



if __name__ == "__main__":
    print(func([3,4,4,7,8,10], 5))
    print(func([3,4,4,7,8,10], 8))