from typing import List


# Time complexity: O(n)
# Space Complexity: O(k)
# Brute-force approach.
def right_rotate_arr_by_k(arr: List[int], k: int) -> List[int]:
    n = len(arr)

    # Store last k elements.
    temp_arr = arr[-k:]
    
    # Shift the remaining elements.
    for i in range(k,n):
        arr[i+k] = arr[i]
    
    # Copy stored elements to the front.
    for j in range(k):
        arr[j] = temp_arr[j]

    return arr

# Time complexity: O(n)
# Space Complexity: O(1)
# Optimal approach.
def reverse(arr: List[int], start: int, end: int) -> None:
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def right_rotate_arr_by_k(arr: List[int], k: int) -> List[int]:
    n = len(arr)
    k = k % n
                         # [1,2,3,4,5] -> 
    reverse(arr, 0, n-1) # [5,4,3,2,1] -> 
    reverse(arr, 0, k-1) # [3,4,5,2,1] ->
    reverse(arr, k, n-1) # [3,4,5,1,2]

    return arr


if __name__ == "__main__":
    print(right_rotate_arr_by_k([1,2,3,4,5], 3))