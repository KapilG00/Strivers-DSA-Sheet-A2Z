from typing import List

# TC -> O(n^2)
# SC -> O(1)
# Brute-force
def two_sum(arr: List[int], target: int) -> tuple[int,int]:
    n = len(arr)
    
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return (i, j)

    return (-1,-1)        

# TC -> O(n)
# SC -> O(n)
# Better (using hashmap)
def two_sum(arr: List[int], target: int) -> tuple[int,int]:
    n = len(arr)
    hash_map = {}
    
    for i in range(n):
        rem = target - arr[i]

        if rem in hash_map:
            return (i, hash_map[rem])
        hash_map[arr[i]] = i
    
# TC -> O(n)
# SC -> O(1)
# Optimal (using two-pointers)
def two_sum(arr: List[int], target: int) -> tuple[int,int]:
    n = len(arr)
    l = 0
    r = n-1

    while l < r:
        current_sum = arr[l] + arr[r]

        if current_sum > target:
            r -= 1
        elif current_sum < target:
            l += 1
        else:
            return (1,r)

    return (-1,-1)            



if __name__ == "__main__":
    print(two_sum([2,6,5,8,11], 14))
