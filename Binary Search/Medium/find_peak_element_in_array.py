from typing import List


# TC: O(logn)
# SC: O(1)
def find_peak_ele_in_arr(arr: List[int]) -> int:
    n = len(arr)
    
    if n == 1:
        return arr[0]
    
    if arr[0] > arr[1]:
        return 1
    if arr[n-1] > arr[n-2]:
        return n-1
    
    low = 1
    high = n-2

    while low <= high:
        mid = (low+high)//2

        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return mid
        
        # Left half is increasing so our peak would be right of the current mid,
        # hence eliminate it.
        if arr[mid] > arr[mid-1]:
            low = mid+1
        # Right half is decreasing so our peak would be left of the current mid,
        # hence eliminate it.
        elif arr[mid] > arr[mid+1]:
            high = mid-1
        # This "else" is to handle the edge case in multiple peak's present    
        else:
            low = mid+1 

    return -1            

        

if __name__ == "__main__":
    print(find_peak_ele_in_arr([1,2,3,4,5,6,7,8,5,1]))
    print(find_peak_ele_in_arr([1,2,1,3,5,6,4]))
    print(find_peak_ele_in_arr([1,5,1,2,1])) # else condition will handle this case (multiple peaks)