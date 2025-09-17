from typing import List


# Brute-force approach
# TC -> O(n)
# SC -> O(1)
def search_single_ele_in_sorted_arr(arr: List[int]) -> int:
    n = len(arr)
    
    # Edge case
    if n == 1:
        return arr[0]
    
    for i in range(n):
        if i == 0:
            if arr[i] != arr[i+1]:
                return arr[i]
        elif i == n-1:
            if arr[i] != arr[i-1]:
                return arr[i]
        else:
            if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
                return arr[i]

    return -1                


# TC -> O(logn)
# SC -> O(1)
def search_single_ele_in_sorted_arr(arr: List[int]) -> int:
    n = len(arr)
    low, high = 1, n-2
    
    # Edge cases
    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]
        # For left half of the array.
        if (mid % 2 == 0 and arr[mid] == arr[mid+1]) or (mid % 2 == 1 and arr[mid] == arr[mid-1]):
            low = mid+1
        # For right half of the array.
        if (mid % 2 == 0 and arr[mid] == arr[mid-1] or (mid % 2 == 1 and arr[mid] == arr[mid+1])):
            high = mid-1

    return -1            
        


if __name__ == "__main__":
    print(search_single_ele_in_sorted_arr([1,1,2,2,3,3,4,5,5,6,6]))
    print(search_single_ele_in_sorted_arr([1,1,2,3,3,4,4,5,5,6,6]))
    print(search_single_ele_in_sorted_arr([1,2,2,3,3,4,4,5,5,6,6]))
    print(search_single_ele_in_sorted_arr([1,1,2,2,3,3,4,4,5,5,6]))
    print(search_single_ele_in_sorted_arr([1,1,2,2,3,3,4,4,5,5]))