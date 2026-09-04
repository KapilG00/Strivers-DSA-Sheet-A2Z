from typing import List


# TC: O(2^n * average length of combinations)
# SC: O(average length of combinations * number of combinations)
def combination_sum_2(arr: List[int], idx: int, current_combination: List[List[int]], combinations_arr: List[int], target: int) -> List[List[int]]:
    # base case
    if target == 0:
        combinations_arr.append(current_combination.copy())
        return

    for i in range(idx, len(arr)):
        # Case to ignore/skip the recursion calls for idx where the current and previous elements are same.
        if i > idx and arr[i] == arr[i-1]:
            continue

        # Case to ignore/skip where the current element is greater than the current target,
        # which means we cannot subtract current element from current target,
        # so we cannot consider current element as part of our current combination.
        if arr[i] > target:
            break

        current_combination.append(arr[i])
        combination_sum_2(arr, i+1, current_combination, combinations_arr, target-arr[i])
        current_combination.pop()

    return combinations_arr



if __name__ == "__main__":
    arr = [10,1,2,7,6,1,5]
    arr.sort()
    print(combination_sum_2(arr, 0, [], [], 8))

