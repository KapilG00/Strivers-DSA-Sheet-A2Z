from typing import List


# TC: O(logn)
# SC: O(1)
def find_minimum_in_rotated_sorted_arr(arr: List[int]) -> int:
    n = len(arr)
    low = 0
    high = n-1
    min_ele = float('inf')

    while low <= high:
        mid = (low+high)//2

        # if left half is sorted take low as min element
        # and eliminate the left half.
        if arr[low] <= arr[mid]:
            min_ele = min(min_ele, arr[low])
            low = mid+1
        # if right half is sorted take mid as min element
        # and eliminate the right half.
        elif arr[mid] <= arr[high]:
            min_ele = min(min_ele, arr[mid])
            high = mid-1

    return min_ele               
        
        



if __name__ == "__main__":
    print(find_minimum_in_rotated_sorted_arr([4,5,6,7,0,1,2,3]))
    print(find_minimum_in_rotated_sorted_arr([3,4,5,1,2]))