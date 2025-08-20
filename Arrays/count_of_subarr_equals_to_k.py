from typing import List


# TC -> O(n^3)
# SC -> O(1)
def count_of_sub_arr_equals_k(arr: List[int], k: int) -> int:
    n = len(arr)
    count_of_sub_arr = 0

    for i in range(n):
        for j in range(i, n):
            current_sum = 0
            for l in range(i, j+1):
                current_sum += arr[l]
            if current_sum == k:
                count_of_sub_arr += 1
    return count_of_sub_arr            

# TC -> O(n^2)
# SC -> O(1)
def count_of_sub_arr_equals_k(arr: List[int], k: int) -> int:
    n = len(arr)
    count_of_sub_arr = 0

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum == k:
                count_of_sub_arr += 1
    return count_of_sub_arr

# TC -> O(n)
# SC -> O(n)
def count_of_sub_arr_equals_k(arr: List[int], k: int) -> int:
    n = len(arr)
    count_of_sub_arr = 0
    prefix_sum = 0
    sum_map = {0: 1}

    for i in range(n):
        prefix_sum += arr[i]
        remove_sum = prefix_sum-k
        count_of_sub_arr += sum_map.get(remove_sum, 0)
        sum_map[prefix_sum] = sum_map.get(prefix_sum, 0) + 1

    return count_of_sub_arr    


if __name__ == "__main__":
    print(count_of_sub_arr_equals_k([3,1,2,4], 6))
    print(count_of_sub_arr_equals_k([1,2,3], 3))
    print(count_of_sub_arr_equals_k([2,3,5,1,9], 10))