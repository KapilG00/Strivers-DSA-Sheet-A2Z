from typing import List


def first_occurence(arr: List[int], target: int) -> int:
    n = len(arr)
    low, high = 0, n-1
    first_occurence_idx = -1

    while low <= high:
        mid = (low+high) // 2

        if target == arr[mid]:
            first_occurence_idx = mid
            high = mid-1
        elif target > arr[mid]:
            low = mid+1
        else:
            high = mid-1

    return first_occurence_idx
                
def last_occurence(arr: List[int], target: int) -> int:
    n = len(arr)
    low, high = 0, n-1
    last_occurence_idx = -1

    while low <= high:
        mid = (low+high) // 2

        if target == arr[mid]:
            last_occurence_idx = mid
            low = mid+1
        elif target > arr[mid]:
            low = mid+1
        else:
            high = mid-1

    return last_occurence_idx

def first_and_last_occurence_idx(arr: List[int], target: int) -> tuple[int, int]:
    first_occurence_idx = first_occurence(arr, target)
    if first_occurence_idx == -1:
        return (-1, -1)
    last_occurence_idx = last_occurence(arr, target)

    return (first_occurence_idx, last_occurence_idx)

# TC -> O(2logn)
# SC -> O(1)
def count_occurences_in_sorted_arr(arr: List[int], target: int) -> int:
    first_idx, last_idx = first_and_last_occurence_idx(arr, target)
    if first_idx == -1:
        return 0

    return last_idx - first_idx + 1


if __name__ == "__main__":
    print(count_occurences_in_sorted_arr([2,2,3,3,3,3,4], 3))
    print(count_occurences_in_sorted_arr([1,1,2,2,2,2,2,3], 2))
    print(count_occurences_in_sorted_arr([1,1,2,2,2,2,2,3], 4))