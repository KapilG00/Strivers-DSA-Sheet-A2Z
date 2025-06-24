from typing import List


# Brute-force approach
# Time Complexity: O(N^2)
# Space Complexity: O(1)
def is_array_sorted(arr: List[int]) -> bool:
    n = len(arr)

    if n == 1 or n == 0:
        return True

    for i in range(n):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                return False

    return True


# Optimal approach
# Time Complexity: O(N)
# Space Complexity: O(1)
def is_array_sorted(arr: List[int]) -> bool:
    n = len(arr)

    if n == 1 or n == 0:
        return True

    for i in range(n-1):
        if arr[i+1] < arr[i]:
            return False
        i += 1    

    return True


if __name__ == "__main__":
    print(is_array_sorted([1,2,3,4,5]))
    print(is_array_sorted([5,4,6,7,8]))
    print(is_array_sorted([322]))
    print(is_array_sorted([]))