from typing import List


# TC: O(2^n)
# SC: O(n)
def print_subsequence_sum_k(arr: List[int], idx: int, sum: int, subsequence_arr_sum: List[int], target: int) -> None:
    n = len(arr)
    
    if idx == n:
        if sum == target:
            print(subsequence_arr_sum)
        return
    
    # Add the current element and add it to the sum.
    subsequence_arr_sum.append(arr[idx])
    sum += arr[idx]

    # Take.
    print_subsequence_sum_k(arr, idx+1, sum, subsequence_arr_sum, target)

    # Remove the last added element and subtract it from the sum.
    subsequence_arr_sum.remove(arr[idx])
    sum -= arr[idx]

    # Not take.
    print_subsequence_sum_k(arr, idx+1, sum, subsequence_arr_sum, target)



if __name__ == "__main__":
    print(print_subsequence_sum_k([1,2,1], 0, 0, [], 2))