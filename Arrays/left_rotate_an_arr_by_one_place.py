from typing import List


# Brute-force approach
# TC - O(n)
# SC - O(n)
def left_rotate_arr_by_one(arr: List[int], k: int) -> List[int]:
    n = len(arr)
    first_part_arr = arr[:k] # List Slicing
    second_part_arr = arr[k:n] # List Slicing
    
    return second_part_arr + first_part_arr

# Brute-force approach
# TC - O(n)
# SC - O(n)
def left_rotate_arr_by_one(arr: List[int]) -> List[int]:
    n = len(arr)
    temp = [0] * n

    for i in range(1, n):
        temp[i-1] = arr[i]
    temp[n-1] = arr[0]
    
    return temp

# Optimal Approach
# TC - O(n)
# SC - O(1)
def left_rotate_arr_by_one(arr: List[int]) -> List[int]:
    n = len(arr)
    first_ele = arr[0]

    for i in range(n-1):
        arr[i] = arr[i+1]

    arr[n-1] = first_ele

    return arr    


if __name__ == "__main__":
    print(left_rotate_arr_by_one([1,2,3,4,5])) # [2,3,4,5,1]    