from typing import List



# TC: O(logn)
# SC: O(1)
def search_in_rotated_sorted_arr(arr: List[int], target: int) -> int:
    n = len(arr)
    low = 0
    high = n-1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == target:
            return mid
        # Check if left half is sorted.
        if arr[low] <= arr[mid]:
            # If target lies in left half.
            if target >= arr[low] and target <= arr[mid]:
                high = mid-1
            else:
                low = mid+1    
        # Right half is sorted.      
        elif arr[mid] <= arr[high]:
            if target >= arr[mid] and target <= arr[high]:
                low = mid+1
            else:
                high = mid=1    

    return -1            



if __name__ == "__main__":
    print(search_in_rotated_sorted_arr([4,5,6,7,0,1,2], 0))