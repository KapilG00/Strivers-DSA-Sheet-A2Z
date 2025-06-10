from typing import List

# Time Complexity: O(N)
# Space Complexity: O(1)
def find_largest_ele_arr(arr: List) -> int:
    n = len(arr)
    largest_ele = float('-inf')

    for i in range(n):
        if arr[i] > largest_ele:
            largest_ele = arr[i]

    return largest_ele        


if __name__ == "__main__":
    print(find_largest_ele_arr([2, 5, 1, 3, 0]))
    print(find_largest_ele_arr([8, 10, 5, 7, 9]))