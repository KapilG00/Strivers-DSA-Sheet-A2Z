from typing import List

# This is not using recursion.
def reverse_an_array(arr: List[int]) -> List[int]:
    n = len(arr)
    left_ptr = 0
    right_ptr = n-1

    while left_ptr < right_ptr:
        arr[left_ptr], arr[right_ptr] = arr[right_ptr], arr[left_ptr]

        left_ptr += 1
        right_ptr -= 1

    return arr

# Using two pointers (left and right)
def reverse_an_array(arr: List[int], left: int, right: int) -> List[int]:
    if left >= right:
        return
    
    arr[left], arr[right] = arr[right], arr[left]
    reverse_an_array(arr, left+1, right-1)

    return arr  

# Using single pointer
def reverse_an_array(arr: List[int], idx: int) -> List[int]:
    n = len(arr)
    if idx >= n//2: 
        return
    
    arr[idx], arr[n-idx-1] = arr[n-idx-1], arr[idx]
    reverse_an_array(arr, idx+1)

    return arr  


if __name__ == "__main__":
    print(reverse_an_array([5,4,3,2,1]))
    print(reverse_an_array([5,4,3,2,1], 0, 4)) # 4 is len(arr)-1
    print(reverse_an_array([5,4,3,2,1], 0))
    print(reverse_an_array([6,5,4,3,2,1], 0))