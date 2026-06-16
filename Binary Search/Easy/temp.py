from typing import List

# Brute-force
def first_occurence(arr: List[int], target: int) -> int:
    n = len(arr)
    low = 0
    high = n-1
    first_occurence = -1

    while low <= high:
        mid = (low+high) // 2
        
        if target == arr[mid]:
            first_occurence = mid
            high = mid - 1
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return first_occurence    

def last_occurence(arr: List[int], target: int) -> int:
    n = len(arr)
    low = 0
    high = n-1
    last_occurence = -1

    while low <= high:
        mid = (low+high) // 2
        
        if target == arr[mid]:
            last_occurence = mid
            low = mid + 1
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return last_occurence
    

# Better
# def func(arr: List[int], target: int) -> int:
#     n = len(arr)
#     low = 0
#     high = n-1



# Optimal
def func(arr: List[int], target: int) -> int:
   
    first_occurence_of_target = first_occurence(arr, target)
    last_occurence_of_target = last_occurence(arr, target)

    return last_occurence_of_target - first_occurence_of_target + 1


if __name__ == "__main__":
    print(func([2,2,3,3,3,3,4], 3))
    print(func([1,1,2,2,2,2,2,3], 2))