from typing import List

# Time complexity: O(n)
# Space Complexity: O(k)
# Brute-force approach.
def left_rotate_arr_by_k(arr: List[int], k: int) -> List[int]:
    n = len(arr)
    k = k % n

    # Store first k elements
    temp_arr = arr[:k]
    
    # Shift remaining elements.
    for i in range(k,n):
        arr[i-k] = arr[i]
    
    # Copy stored elements to the end.
    for j in range(k):
        arr[n-k+j] = temp_arr[j]

    return arr

# Time complexity: O(n)
# Space Complexity: O(1)
# Optimal approach.
def reverse(arr: List[int], start: int, end: int) -> None:
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def left_rotate_arr_by_k(arr: List[int], k: int) -> List[int]:
    n = len(arr)
    k = k % n

    reverse(arr, 0, k-1) # Here, starting from 0 hence k-1 i.e. first k elements.
    reverse(arr, k, n-1)
    reverse(arr, 0, n-1)

    return arr


if __name__ == "__main__":
    print(left_rotate_arr_by_k([1,2,3,4,5], 3))