from typing import List
from itertools import permutations


# TC: O(n!) * O(n)
# SC: O(n!)
# Brute-force
def lexicographically_next_greater_permutation(arr: List[int]) -> tuple[int, int]:
    perms = sorted(set(permutations(arr)))
    print(perms)

    # Convert list to tuple for comparison
    current = tuple(arr)

    for i in range(len(perms)):
        if perms[i] == current:
            # If last permutation, return first
            if i == len(perms) - 1:
                return list(perms[0])
            # Else return next
            return list(perms[i+1])

# TC: O(n)
# SC: O(1)
# Optimal
def lexicographically_next_greater_permutation(arr: List[int]) -> List[int]:
    n = len(arr)
    idx = -1

    # Finding the break-point i.e. longest prefix
    for i in range(n-2, -1, -1):
        if arr[i] < arr[i+1]:
            idx = i
            break

    # If idx = -1 i.e. current permutation is already at max so we need to return the lexicographically smallest permutation possible by doing reverse of the array.
    if idx == -1:
        arr.reverse()
        return arr    

    # Finding the just next greater element from the variable part of the array.
    for j in range(n-1, -1, -1):
        if arr[j] > arr[idx]:
            arr[j], arr[idx] = arr[idx], arr[j]
            break

    # Reversing the variable part of the array.
    arr[idx+1:] = reversed(arr[idx+1:])

    return arr  



if __name__ == "__main__":
    print(lexicographically_next_greater_permutation([1,3,2]))
    print(lexicographically_next_greater_permutation([3,2,1]))