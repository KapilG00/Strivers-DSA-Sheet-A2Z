from typing import List


# Brute-force
# TC: O(n^2)
# SC: O(1)
def func(arr: List[int]) -> int:
    n = len(arr)
    
    for i in range(n):
        appearance = 0

        for j in range(n):
            if arr[i] == arr[j]:
                appearance += 1

        if appearance == 1:
            return arr[i]

    return -1            

# Better
# TC: O(n) + O(k); where k is number of distinct elements in array.
# SC: O(k)
def func(arr: List[int]) -> int:
    n = len(arr)
    hash_map = {}

    for i in range(n):
        if arr[i] in hash_map:
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1

    for key, value in hash_map.items():
        if value == 1:
            return key

    return -1                

# Optimal
# TC: O(n)
# SC: O(1)
def func(arr: List[int]) -> int:
    xorr = 0

    # XOR all elements — duplicates cancel out
    for num in arr:
        xorr ^= num

    return xorr



if __name__ == "__main__":
    print(func([4,1,2,1,2]))