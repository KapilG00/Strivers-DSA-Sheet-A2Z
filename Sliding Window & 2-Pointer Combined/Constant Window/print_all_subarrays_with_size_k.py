from typing import List


# TC: O(n^2)
# SC: O(1)
def print_all_subarrays_with_size_k(arr: List[int], k: int) -> List[int]:
    n = len(arr)

    for i in range(n):
        for j in range(i, n):
            if (j-i+1) == k:
                print(arr[i:j+1])


# TC: O(k) + O(n-k)
# SC: O(1)
def print_all_subarrays_with_size_k(arr: List[int], k: int) -> List[int]:
    n = len(arr)
    low = 0
    high = k-1

    while high < n:
        print(arr[low:high+1])
        low += 1
        high += 1


if __name__ == "__main__":
    print(print_all_subarrays_with_size_k([1,2,1,3,4,2,3], 3))