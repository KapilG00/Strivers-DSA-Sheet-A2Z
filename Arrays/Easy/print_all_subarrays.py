from typing import List


# TC: O(n^3)
# SC: O(1)
def print_all_subarrays(arr: List[int]) -> None:
    n = len(arr)

    for start in range(n): # O(n)
        for end in range(start, n): # O(n)
            print(arr[start:end + 1]) # O(n)


if __name__ == "__main__":
    print_all_subarrays([1,2,3,4,5])