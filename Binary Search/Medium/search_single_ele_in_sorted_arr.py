from typing import List


# TC: O(logn)
# SC: O(1)
def search_single_ele_in_sorted_arr(arr: List[int]) -> int:
    n = len(arr)
    
    # For case where array contains only single element.
    if n == 1:
        return arr[0]
    
    # Since we will start our low from 1 and high from n-2,
    # we need to check for 0 and n-1 index.
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n-1] != arr[n-2]:
        return arr[n-1]
    
    low = 1
    high = n-2

    while low <= high:
        mid = (low+high)//2

        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]
        
        # Eliminating left half
        if (mid%2 == 1 and arr[mid] == arr[mid-1]) or (mid%2 == 0 and arr[mid] == arr[mid+1]): 
            low = mid+1
        # Eliminating right half
        else:
            high = mid-1

    return -1          


        
        

if __name__ == "__main__":
    print(search_single_ele_in_sorted_arr([1,1,2,2,3,3,4,5,5,6,6]))
    print(search_single_ele_in_sorted_arr([1,1,3,5,5]))