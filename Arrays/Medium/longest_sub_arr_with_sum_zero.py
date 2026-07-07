from typing import List


# TC -> O(n^2)
# SC -> O(1)
# Brute-force
def longest_sub_arr_with_sum_zero(arr: List[int], k: int) -> int:
    n = len(arr)
    max_sub_arr_length = 0

    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]

            if sum == k:
                if j-i+1 > max_sub_arr_length:
                    max_sub_arr_length = j-i+1

    return max_sub_arr_length

# TC -> O(nlogn)
# SC -> O(n)
# Optimal
def longest_sub_arr_with_sum_zero(arr: List[int], k: int) -> int:
    n = len(arr)
    prefix_sum_map = {}
    max_length = 0
    prefix_sum = 0

    for i in range(n):
        prefix_sum += arr[i]

        if prefix_sum == k:
            max_length = max(max_length, i+1)

        rem = prefix_sum - k

        if rem in prefix_sum_map:
            length = i - prefix_sum_map[rem]
            max_length = max(max_length, length)

        if rem not in prefix_sum_map:
            prefix_sum_map[prefix_sum] = i    

    return max_length        



if __name__ == "__main__":
    print(longest_sub_arr_with_sum_zero([9,-3,3,-1,6,-5], 0))
    print(longest_sub_arr_with_sum_zero([6,-2,2,-8,1,7,4,-10], 0))