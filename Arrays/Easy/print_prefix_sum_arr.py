from typing import List

# TC: O(nk)
# SC: O(1)
def print_prefix_sum_arr(arr: List[int]) -> int:
    n = len(arr)
    prefix_sum_arr = [0] * n
    prefix_sum_arr[0] = arr[0]

    for i in range(1, n):
        prefix_sum_arr[i] = prefix_sum_arr[i-1] + arr[i] 

    return prefix_sum_arr


if __name__ == "__main__":
    arr = print_prefix_sum_arr([2,1,5,1,3,2])
    # Formula to find prefix sum in between any two indexes of an array.
    # prefix_sum(low, high) = prefix_sum(high) - prefix_sum(low-1)
    prefix_sum_from_2nd_to_5th_index = arr[5] - arr[2-1]
    print(prefix_sum_from_2nd_to_5th_index)