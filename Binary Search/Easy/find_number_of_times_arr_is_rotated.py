from typing import List


# TC: O(logn)
# SC: O(1)
def find_number_of_times_sorted_arr_is_rotated(arr: List[int]) -> int:
    n = len(arr)
    low = 0
    high = n-1
    idx = -1
    min_ele = float('inf')

    while low <= high:
        mid = (low+high)//2

        # if left half is sorted take low as min element
        # and eliminate the left half.
        if arr[low] <= arr[mid]:
            if arr[low] < min_ele:
                idx = low
                min_ele = arr[low]
            low = mid+1
            
        # if right half is sorted take mid as min element
        # and eliminate the right half.
        elif arr[mid] <= arr[high]:
            if arr[low] < min_ele:
                idx = mid
                min_ele = arr[mid]
            high = mid-1

    return idx    
        
        



if __name__ == "__main__":
    print(find_number_of_times_sorted_arr_is_rotated([4,5,6,7,0,1,2,3]))
    print(find_number_of_times_sorted_arr_is_rotated([3,4,5,1,2]))