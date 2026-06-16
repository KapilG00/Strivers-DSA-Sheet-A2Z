from typing import List


# TC -> O(logn)
# SC -> O(1)
def last_occurence_in_sorted_arr(arr: List[int], target: int) -> int:
    n = len(arr)
    low, high = 0, n-1
    idx = -1
    # axaxaxaxaaxaxax

    while low <= high:
        mid = (low+high) // 2
        
        if target == arr[mid]:
            idx = mid
            low = mid + 1
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return idx                




if __name__ == "__main__":
    print(last_occurence_in_sorted_arr([3,4,13,13,13,20,40], 13))
    print(last_occurence_in_sorted_arr([3,4,13,13,13,20,40], 60))