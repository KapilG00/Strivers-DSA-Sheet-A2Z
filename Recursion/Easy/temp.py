from typing import List


def count_all_subsequences_with_sum_k(arr: List[int], idx: int, subsequence_arr_sum: int, k: int) -> None:
    n = len(arr)
    
    # base case
    if idx == n:
        if subsequence_arr_sum == k:
            return True
        return False

    # take
    subsequence_arr_sum += arr[idx]
    if count_all_subsequences_with_sum_k(arr, idx+1, subsequence_arr_sum, k):
        return True

    # not take
    subsequence_arr_sum -= arr[idx]
    if count_all_subsequences_with_sum_k(arr, idx+1, subsequence_arr_sum, k):
        return True
    
    return False


if __name__ == "__main__":
    print(count_all_subsequences_with_sum_k([1,2,1], 0, 0, 2))
    print(count_all_subsequences_with_sum_k([1,2,1], 0, 0, 5))