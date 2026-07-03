from typing import List


# TC: O(2^n)
# SC: O(n)
def count_all_subsequences_sum_k(arr: List[int], idx: int, sum: int, target: int) -> int:
    n = len(arr)
    
    if idx == n:
        if sum == target:
            return 1
        return 0
    
    # Add it to the sum.
    sum += arr[idx]

    # Take.
    l = count_all_subsequences_sum_k(arr, idx+1, sum, target)

    # Subtract it from the sum.
    sum -= arr[idx]

    # Not take.
    r = count_all_subsequences_sum_k(arr, idx+1, sum, target)

    return l+r



if __name__ == "__main__":
    print(count_all_subsequences_sum_k([1,2,1], 0, 0, 2))