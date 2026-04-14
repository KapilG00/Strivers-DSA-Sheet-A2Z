from typing import List


# Time complexity: O(n^2)
# Space Complexity: O(n)
def remove_duplicates_from_sorted_arr(arr: List[int]) -> List[int]:
    n = len(arr)
    non_duplicate_arr = []

    for i in range(n):
        if arr[i] not in non_duplicate_arr:
            non_duplicate_arr.append(arr[i])
    
    m = len(non_duplicate_arr)

    for _ in range(n-m):
        non_duplicate_arr.append("_")

    return non_duplicate_arr

# Time complexity: O(n)
# Space Complexity: O(n)
# Brute-force approach. (not in-place)
def temp(arr: List[int]) -> int:
    n = len(arr)
    new_arr = [arr[0]]

    for i in range(1, n):
        if arr[i] > arr[i-1]:
            new_arr.append(arr[i])

    return len(new_arr) 

# Time complexity: O(n)
# Space Complexity: O(n)
# Brute-force approach. (in-place)
def temp(arr: List[int]) -> int:
    index = 0
    s = set()

    for num in arr:
        if num not in s:
            s.add(num)
            arr[index] = num
            index += 1
    return index

# Time complexity: O(n)
# Space Complexity: O(n)
def remove_duplicates_from_sorted_arr(arr: List[int]) -> List[int]:
    n = len(arr)
    non_duplicate_arr = [arr[0]]

    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            non_duplicate_arr.append(arr[i])
    
    m = len(non_duplicate_arr)

    for _ in range(n-m):
        non_duplicate_arr.append("_")        

    return non_duplicate_arr

# Time complexity: O(n)
# Space Complexity: O(1)
# Optimal approach. (in-place)
def temp(arr: List[int]) -> int:
    n = len(arr)
    i = 0

    for j in range(1, n):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i+1  
     

if __name__ == "__main__":
    print(remove_duplicates_from_sorted_arr([1,1,2,2,2,3,3]))