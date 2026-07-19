from typing import List


# Brute-force
# TC: O(n^2)
# SC: O(1)
def count_inversions_in_array(arr: List[int]) -> int:
    n = len(arr)
    inversions_count = 0

    for i in range(n):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                inversions_count += 1
    return inversions_count            

def merge(arr: List[int], low: int, mid: int, high: int) -> int:
    left = low
    right = mid+1
    temp_arr = []
    inversions_count = 0

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp_arr.append(arr[left])
            left += 1
        else:
            temp_arr.append(arr[right])
            inversions_count += (mid-left+1) # Count inversions
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

    return inversions_count    

def merge_sort(arr: List[int], low: int, high: int) -> int:
    """
    Divide & Merge
    """
    inversions_count = 0

    if low >= high:
        return inversions_count

    mid = (low+high) // 2
    
    # solve left part of the array.
    inversions_count += merge_sort(arr, low, mid)

    # solve right part of the array.
    inversions_count += merge_sort(arr, mid+1, high)

    # merge
    inversions_count += merge(arr, low, mid, high)

    return inversions_count

# Optimal
# TC: O(nlogn)
# SC: O(n)
def count_inversions_in_array(arr: List[int]) -> int:
    n = len(arr)
    low = 0
    high = n-1
    inversions_count = merge_sort(arr, low, high)
    return inversions_count


if __name__ == "__main__":
    print(count_inversions_in_array([1,2,3,4,5]))
    print(count_inversions_in_array([5,4,3,2,1]))
    print(count_inversions_in_array([5,3,2,1,4]))