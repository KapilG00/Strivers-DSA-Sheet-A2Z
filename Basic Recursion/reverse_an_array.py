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


if __name__ == "__main__":
    print(reverse_an_array([5,4,3,2,1]))