from typing import List

# TC -> O(n^2) 
# SC -> O(1)
# Brute-force
def majority_element_1(arr: List[int]) -> int:
    n = len(arr)
    majority_count = n//2
    
    for i in range(n):
        current_count = 0
        for j in range(n):
            if arr[j] == arr[i]:
                current_count += 1
        if current_count > majority_count:
            return arr[i]

    return -1

# TC -> O(n) 
# SC -> O(k); where 'k'is total unique elements
# Better (using hash map)
def majority_element_1(arr: List[int]) -> int:
    n = len(arr)
    majority_count = n//2
    hash_map = {}

    for i in range(n):
        if arr[i] not in hash_map:
            hash_map[arr[i]] = 1
        else:
            hash_map[arr[i]] += 1

    for k, v in hash_map.items():
        if v > majority_count:
            return k

    return -1               

# TC -> O(n)
# SC -> O(1)
# Optimal (using moore's voting algorithm)
def majority_element_1(arr: List[int]) -> List[int]:
    n = len(arr)
    majority = arr[0]
    votes = 1

    for i in range(1, n):
        if arr[i] == majority:
            votes += 1
        elif votes == 0:
            majority = arr[i]
            votes = 1
        else:
            votes -= 1

    return majority


if __name__ == "__main__":
    print(majority_element_1([7,0,0,1,7,7,2,7,7]))
