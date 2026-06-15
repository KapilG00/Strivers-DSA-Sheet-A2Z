from typing import List

# Brute-force
# def func(arr: List[int], target: int) -> int:
#     n = len(arr)
#     low = 0
#     high = n-1
   
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] > target:
#             high = mid - 1
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             return mid
#     return -1            

# Better
def func(arr: List[int], target: int, low: int, high: int) -> int:
    if low > high:
        return -1 

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    
    if arr[mid] > target:
        return func(arr, target, low, high-1)
    elif arr[mid] < target:
        return func(arr, target, low+1, high)



# Optimal
# def func(arr: List[int], target: int) -> int:
#     n = len(arr)
#     low = 0
#     high = n-1


if __name__ == "__main__":
    arr = [3,4,6,7,9,12,16,17]
    n = len(arr)
    print(func(arr, 13, 0, n-1))