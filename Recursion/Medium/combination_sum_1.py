from typing import List


def combination_sum_1(arr: List[int], idx: int, current_combination: List[List[int]], combinations_arr: List[int], current_combination_sum: int, target: int) -> List[List[int]]:

    if current_combination_sum > target:
        return combinations_arr
    
    # base case
    if idx == len(arr):
        if current_combination_sum == target:
            combinations_arr.append(current_combination.copy())
        return combinations_arr

    # take
    current_combination.append(arr[idx])
    current_combination_sum += arr[idx]

    combination_sum_1(arr, idx, current_combination, combinations_arr, current_combination_sum, target)

    # not take
    current_combination.pop()
    current_combination_sum -= arr[idx]

    combination_sum_1(arr, idx+1, current_combination, combinations_arr, current_combination_sum, target)

    return combinations_arr

# Recommended solution
# TC: O(2^t * average length of combinations); where "t" is unknown.
# SC: O(average length of combinations * number of combinations)
def combination_sum_1(arr: List[int], idx: int, current_combination: List[List[int]], combinations_arr: List[int], target: int) -> List[List[int]]:
    
    # base case
    if idx == len(arr):
        if target == 0:
            combinations_arr.append(current_combination.copy())
        return

    # take
    if arr[idx] <= target:
        current_combination.append(arr[idx])
        combination_sum_1(arr, idx, current_combination, combinations_arr, target-arr[idx])
        current_combination.pop()

    # not take
    combination_sum_1(arr, idx+1, current_combination, combinations_arr, target)

    return combinations_arr



if __name__ == "__main__":
    print(combination_sum_1([2,3,6,7], 0, [], [], 0, 7))
    print(combination_sum_1([2,3,6,7], 0, [], [], 7))

