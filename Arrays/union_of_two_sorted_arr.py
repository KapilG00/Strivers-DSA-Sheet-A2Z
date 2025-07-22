from typing import List


# TC -> O(n² + m(n + m))
# SC -> O(n + m)
def union_of_two_sorted_arr(arr1: List[int], arr2: List[int]) -> List[int]:
    n, m = len(arr1), len(arr2)
    union_arr = []

    for i in range(n): # O(n)
        if arr1[i] not in union_arr: # here "in" will take O(len(union_arr))
            union_arr.append(arr1[i])

    for j in range(m): # O(m)
        if arr2[j] not in union_arr: # here "in" will take O(len(union_arr))
            union_arr.append(arr2[j])

    return union_arr                

# TC -> O((n+m)log(n+m))
# SC -> O(n+m)
def union_of_two_sorted_arr(arr1: List[int], arr2: List[int]) -> List[int]:
    n, m = len(arr1), len(arr2)
    nums_freq_hash_map = {}
    union_arr = []

    for i in range(n):
        if arr1[i] not in nums_freq_hash_map:
            nums_freq_hash_map[arr1[i]] = 1
        else:
            nums_freq_hash_map[arr1[i]] += 1

    for j in range(m):
        if arr2[j] not in nums_freq_hash_map:
            nums_freq_hash_map[arr2[j]] = 1
        else:
            nums_freq_hash_map[arr2[j]] += 1
    

    for k in nums_freq_hash_map.keys():
        union_arr.append(k)

    return union_arr     

# TC -> O((n+m)log(n+m))
# SC -> O(n+m)
def union_of_two_sorted_arr(arr1: List[int], arr2: List[int]) -> List[int]:
    n, m = len(arr1), len(arr2)
    s = set()
    union_arr = []

    for i in arr1:
        s.add(i)

    for j in arr2:
        s.add(j)

    for k in s:
        union_arr.append(k)

    return union_arr    

# TC -> O(n+m)
# SC -> O(n+m)
def union_of_two_sorted_arr(arr1: List[int], arr2: List[int]) -> List[int]:
    n, m = len(arr1), len(arr2)
    i, j = 0,0
    union_arr = []

    while i < n and j < m:
        if arr1[i] == arr2[j]:
            if union_arr[-1] != arr1[i]:
                union_arr.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if len(union_arr) == 0 or union_arr[-1] != arr2[j]:
                union_arr.append(arr2[j])
            j += 1
        elif arr1[i] < arr2[j]:
            if len(union_arr) == 0 or union_arr[-1] != arr1[i]:
                union_arr.append(arr1[i])
            i += 1
    
    # For remaining elements of arr1 if any.
    while i < len(arr1):
        if union_arr[-1] != arr1[i]:
            union_arr.append(arr1[i])
        i += 1

    # For remaining elements of arr2 if any.
    while j < len(arr2):
        if union_arr[-1] != arr2[j]:
            union_arr.append(arr2[j])
        j += 1

    return union_arr    


if __name__ == "__main__":
    print(union_of_two_sorted_arr([1,2,3,4,5], [2,3,4,4,5]))
    print(union_of_two_sorted_arr([1,2,3,4,5,6,7,8,9,10], [2,3,4,4,5,11,12]))