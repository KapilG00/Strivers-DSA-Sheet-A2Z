from typing import List


# TC: O(2^n)
# SC: O(n)
def print_all_subsequences(arr: List[int], idx: int, a: List[int]) -> None:
    n = len(arr)
    
    if idx >= n:
        print(a)
        return 0
    
    # Add the current element in the output array.
    a.append(arr[idx])

    # Take.
    print_all_subsequences(arr, idx+1, a)

    # Remove the last added element.
    a.remove(arr[idx])

    # Not take.
    print_all_subsequences(arr, idx+1, a)




if __name__ == "__main__":
    print(print_all_subsequences([3,1,2], 0, []))

