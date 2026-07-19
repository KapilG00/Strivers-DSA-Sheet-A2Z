from typing import List


def merge(arr: List[int], low: int, mid: int, high: int) -> None:
    left = low
    right = mid+1
    temp_arr = []

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp_arr.append(arr[left])
            left += 1
        else:
            temp_arr.append(arr[right])
            right += 1

    # Add remaining elements of left array, if any.
    while left <= mid:
        temp_arr.append(arr[left])
        left += 1
        
    # Add remaining element of right array, if any.               
    while right <= high:
        temp_arr.append(arr[right])
        right += 1
    
    # Putting the elements in sorted order in original array.
    for i in range(low, high+1):
        arr[i] = temp_arr[i-low]    

# TC: O(nlogn)
# SC: O(n)
def merge_sort(arr: List[int], low: int, high: int) -> List[int]:
    """
    Divide & Merge
    """

    if low >= high:
        return 

    mid = (low+high) // 2
    
    # solve left part of the array.
    merge_sort(arr, low, mid)

    # solve right part of the array.
    merge_sort(arr, mid+1, high)

    # merge
    merge(arr, low, mid, high)

    return arr



if __name__ == "__main__":
    arr = [3,1,2,4,1,5,2,6,4]
    n = len(arr)
    low = 0
    high = n-1
    print(merge_sort(arr, low, high))