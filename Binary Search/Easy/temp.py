from typing import List

# Brute-force
def func(arr: List[int], target: int) -> int:
    n = len(arr)
    low = 0
    high = n-1
    idx = n

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] >= target:
            idx = mid
            high = mid-1
        else:
            low = mid+1

    return idx      


    

# Better
# def func(arr: List[int], target: int) -> int:
#     n = len(arr)
#     low = 0
#     high = n-1



# Optimal
# def func(arr: List[int], target: int) -> int:
#     n = len(arr)
#     low = 0
#     high = n-1


if __name__ == "__main__":
    print(func([1,2,4,7], 6))
    print(func([1,2,4,7], 2))