from typing import List


# TC: O(1)
# SC: O(1)
def count_all_subarrays(arr: List[int]) -> None:
    n = len(arr)
    return (n*(n+1))/2


if __name__ == "__main__":
    print(count_all_subarrays([1,2,3,4,5]))